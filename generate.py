import json, argparse
from tqdm import tqdm
from LLM import APILLM
from utils.wrappers.pointwise_grading import *

parser = argparse.ArgumentParser()
parser.add_argument("--chapter", type=str, default="0X", help="Chapter to grade")
parser.add_argument("--n_samples", type=int, default=3, help="Number of samples to grade")
parser.add_argument("--model", type=str, default="deepseek-chat", choices=['chatglm-4-air', 'claude-3-sonnet', 'gpt-3.5-turbo', 'gpt-4o-mini', 'gpt-4', 'deepseek-chat'], help="Model to use for grading")
args = parser.parse_args()

chapter = args.chapter
n_samples = args.n_samples
model = args.model

llm = APILLM(model=model)
base_path=f"data/ai_judge_dist/{chapter}/"
answer_file = f"{base_path}/ref_answers/Chap{chapter}.json"
homework_base_path = f"data/ai_judge_dist/{chapter}/testcases/"

chapter_2_uids = {
    '0X': [1,2,3,4,7,8,9,10,12,14,15,17],
    '1A': [1,3,4,5,6,8,9,10,11,13,14,15,17,18,20,21,22,24,25],
    '1B': [1,2,4,5,6,7,11,13,14,15,16],
    '1X': [2,5,7,10,12,13,14],
    '2A': [1,2,4,6,7,9,10],
    '2B': [1,2],
    '2X': [7,8,9,14],
    '3X': [6,7,10,11,12],
    '4X': [6,7,9,10],
    '6X': [1,2,3,4,5]
}
uids = chapter_2_uids[chapter]

with open(answer_file, "r") as f:
    answers = json.load(f)
    qids = list(answers.keys())

def parse_correctness_response(response):
    try:
        response = response.split("```json")[-1]
        response = response.split("```")[0]
        response = response.replace("\\", "\\\\").replace("\\\\\\\\", "\\\\").replace('\n', ' ').replace('\t', ' ')
        response = json.loads(response)
        judge = response["response"]
        correctness = int(response["correct"])
    except:
        try:
            idx = response.lower().find("correct")
            judge = response
            correctness = 1 if "1" in response[idx:] else 0
        except:
            judge = "###JSON Format Error"
            correctness = -1
            
    return judge, correctness

def parse_grading_response(response):
    try:
        response = response.split("```json")[-1]
        response = response.split("```")[0]
        response = response.replace("\\", "\\\\").replace("\\\\\\\\", "\\\\").replace('\n', ' ').replace('\t', ' ')
        response = json.loads(response)
        process = response["process"]
        score = float(response["score"])
    except:
        print("Format Error Response: ", response)
        try:
            idx = response.lower().find("score")
            process = response
            score = float(response[idx+7:].split('\n')[0])
        except:
            process = "###JSON Format Error"
            score = 0
            
    return process, score

for i, uid in tqdm(enumerate(uids), desc="Users"):
    user_homework_file = f"{homework_base_path}/Ch{chapter[0]}-{chapter}-{uid}.json"
    with open(user_homework_file, "r") as f:
        user_homework = json.load(f)
    
    for qid in tqdm(qids, desc=f"User {i+1} of {len(uids)} users: "):
        problem_solution, problem_text, problem_answer = user_homework[qid], answers[qid]['problem'], answers[qid]['answers']
        sub_problems = list(problem_answer.keys())
        output = {"uid":uid, "model": model}
        
        for sub_problem in sub_problems:
            sub_problem_output = {"scores": [], "responses": [], "correctness": []}
            
            for sample_id in range(n_samples):
                if sub_problem in problem_solution:
                    sub_problem_solution = problem_solution[sub_problem]
                    sub_problem_overall_answer, sub_problem_rules = problem_answer[sub_problem][0]['answer'], problem_answer[sub_problem][0]['rules']
                    
                    correct_check_inputs = correct_check_input(
                        problem=problem_text,
                        subproblem=sub_problem,
                        answer=sub_problem_overall_answer,
                        student_answer=sub_problem_solution
                    )

                    correctness_response = llm.generate(
                        instruction=correct_check_inputs["system_prompt"],
                        prompt=correct_check_inputs["user_prompt"],
                        history=correct_check_inputs['history'],
                        temperature=correct_check_inputs['temperature'],
                        max_tokens=correct_check_inputs['max_tokens']
                    )
                    
                    judge, correctness = parse_correctness_response(correctness_response)

                    cur_sample_responses, cur_sample_scores = [], []
                    for rule in sub_problem_rules:
                        if correctness < 1:
                            check_rule_inputs = rule_based_input(
                                problem=problem_text,
                                subproblem=sub_problem,
                                answer=sub_problem_overall_answer,
                                student_answer=sub_problem_solution,
                                rule=rule
                            )
                        else:
                            check_rule_inputs = positive_rule_based_input(
                                problem=problem_text,
                                subproblem=sub_problem,
                                answer=sub_problem_overall_answer,
                                student_answer=sub_problem_solution,
                                rule=rule
                            )
                        
                        response = llm.generate(
                            instruction=check_rule_inputs["system_prompt"],
                            prompt=check_rule_inputs["user_prompt"],
                            history=check_rule_inputs['history'],
                            temperature=check_rule_inputs['temperature'],
                            max_tokens=check_rule_inputs['max_tokens']
                        )
                        
                        
                        process, score = parse_grading_response(response)
                        cur_sample_responses.append(process)
                        cur_sample_scores.append(score)
                
                    sub_problem_output["correctness"].append((correctness, judge))
                    sub_problem_output["responses"].append(cur_sample_responses)
                    sub_problem_output["scores"].append(cur_sample_scores)

                else:
                    sub_problem_output["correctness"].append((0, "没有做这道题"))
                    sub_problem_output["responses"].append(["没有做这道题"])
                    sub_problem_output["scores"].append([0])
                
            output[sub_problem] = sub_problem_output
        
        with open(f"pointwise/{qid}.json", 'a') as fw:
            fw.write(json.dumps(output, ensure_ascii=False) + '\n')

                
        