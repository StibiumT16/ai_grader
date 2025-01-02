"""
    An example checker for the problem.
"""

import json
import numpy as np
from tqdm import tqdm, trange

from checker.base import BaseChecker
from instance.problem import *
from instance.ref_problem import *
from utils.wrappers.final_grading import *

from LLM import APILLM

# tools 
# wrapper for checker api

class FinalChecker(BaseChecker):
    def __init__(self, models, weights, sample_size=3, grading_key=None):
        self.sample_size = sample_size
        self.grading_key = grading_key
        
        self.weights = weights
        self.LLMs = [APILLM(model=model) for model in models]

    def cal_mode(self, ary: list): # 计算众数和对应的id(取第一个)
        count_list = np.bincount(ary)
        mode = np.where(count_list == count_list.max())[0][-1] # 取最大的一个众数
        id = np.where(ary == mode)[0][0]
        return int(mode), id
        
    def check(self, ref_pa, student_pa):
        
        for problem_id, ref_problem in tqdm(ref_pa.problems.items(), desc="Checking problems", total=len(ref_pa.problems)):
            student_problem = student_pa.problems[problem_id]
            
            for subproblem_id, ref_subproblem in ref_problem.answers.items():
                
                solution_id = 0
                ref_solution = ref_subproblem.solutions[solution_id]
                
                try:
                    student_solution = student_problem.answers[subproblem_id]
                except:
                    tqdm.write(f"Problem {problem_id} sub-Problem {subproblem_id}:  学生未完成")
                    for id, rule in enumerate(ref_solution.rules):
                        student_solution.add_score(rule, "## 学生没有完成这一小题", 0.)
                    student_solution.finalize(ref_solution.rules)
                    continue
                
                student_solution.set_solution(ref_solution.answer, solution_id)
                
                # For each judger LLM, seperately generate the correctness and rule-based scores:
                
                final_score = 0.
                for llm, weight in zip(self.LLMs, self.weights):
                    
                    # 1. Correctness Check   
                    correct_check_inputs = correct_check_input(
                        problem=ref_problem.problem,
                        subproblem=ref_solution.subproblem_id,
                        answer=ref_solution.answer,
                        student_answer=student_solution.answer
                    )
                    
                    correctnesses = []
                    for _ in range(self.sample_size):
                        correctness_response = llm.generate(
                            instruction=correct_check_inputs["system_prompt"],
                            prompt=correct_check_inputs["user_prompt"],
                            history=correct_check_inputs['history'],
                            temperature=correct_check_inputs['temperature'],
                            max_tokens=correct_check_inputs['max_tokens']
                        )
                    
                        judge, correctness = self.parse_correctness_response(correctness_response)
                        correctnesses.append(correctness)
                        
                    
                    positive = True if self.cal_mode(correctnesses)[0] == 1 else False
                
                    # 2. Rule-based Check
                    rule_based_scores = []
                    for _ in range(self.sample_size):
                        rule_based_scores.append([])
                                        
                        for id, rule in enumerate(ref_solution.rules):
                            
                            input_params = {
                                "problem": ref_problem.problem,
                                "subproblem": ref_solution.subproblem_id,
                                "answer": ref_solution.answer,
                                "student_answer": student_solution.answer,
                                "grading_rule_md": ref_solution.rules[id].format_md_table()
                            }
                            
                            check_rule_inputs = positive_rule_based_input(
                                **input_params
                            ) if positive else rule_based_input(
                                **input_params
                            )
                            
                            rule_score_response = llm.generate(
                                instruction=check_rule_inputs["system_prompt"],
                                prompt=check_rule_inputs["user_prompt"],
                                history=check_rule_inputs['history'],
                                temperature=check_rule_inputs['temperature'],
                                max_tokens=check_rule_inputs['max_tokens']
                            )
                            
                            response, score = self.parse_grading_response(rule_score_response)
                            rule_based_scores[-1].append(score)
                        
                    cur_model_scores = np.max(np.sum(rule_based_scores, axis=1))
                    final_score += weight * cur_model_scores
                
                final_score = round(final_score * 2) / 2 #规约到最接近的0.5
                total_score, rule_text = 0., ""
                for i, rule in enumerate(ref_solution.rules):
                    rule_text += f'第{i+1}步，分值为{rule.score}：{rule.rule}\n'
                    total_score += float(rule.score)
                
                tqdm.write(f"Problem {problem_id} sub-Problem {subproblem_id}:  Final Score {final_score} / {total_score}")
                   
                judge_reason_inputs = judge_reason_input(
                    problem=ref_problem.problem,
                    subproblem=ref_solution.subproblem_id,
                    student_answer=student_solution.answer,
                    rules=rule_text, 
                    final_score=final_score,
                    total_score=total_score
                )
                
                final_reason = self.LLMs[0].generate(
                    instruction=judge_reason_inputs["system_prompt"],
                    prompt=judge_reason_inputs["user_prompt"],
                    history=judge_reason_inputs['history'],
                    temperature=judge_reason_inputs['temperature'],
                    max_tokens=judge_reason_inputs['max_tokens']
                )                
                
                for i, rule in enumerate(ref_solution.rules):
                    if i == 0: student_solution.add_score(rule, final_reason, final_score)
                    else: student_solution.add_score(rule, "", 0.)
                    
                student_solution.finalize(ref_solution.rules)

        return student_pa