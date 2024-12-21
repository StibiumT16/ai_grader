"""
    An example checker for the problem.
"""

import json
import numpy as np
from tqdm import tqdm, trange

from checker.base import BaseChecker
from instance.problem import *
from instance.ref_problem import *
from utils.wrappers.example_grading import format_openai_inputs
from utils.wrappers.my_grading import my_format_openai_inputs
from utils.apis.dify_api import completion_messages
from utils.apis.openai_api import openai_completion
from LLM import APILLM

# tools 
# wrapper for checker api

class MyChecker(BaseChecker):
    def __init__(self, sample_size=5, grading_key=None):
        self.sample_size = sample_size
        self.grading_key = grading_key

    def cal_mode(self, ary: list): # 计算众数和对应的id(取第一个)
        count_list = np.bincount(ary)
        mode = np.where(count_list == count_list.max())[0][-1] # 取最大的一个众数
        id = np.where(ary == mode)[0][0]
        return int(mode), id
        
    def check(self, model, ref_pa, student_pa):
        
        llm = APILLM(model=model)
        
        for problem_id, ref_problem in tqdm(ref_pa.problems.items(), desc="Checking problems", total=len(ref_pa.problems)):
            student_problem = student_pa.problems[problem_id]
            
            for subproblem_id, ref_subproblem in ref_problem.answers.items():
                student_solution = student_problem.answers[subproblem_id]
                
                # TODO: add solution matching logic here
                solution_id = 0
                ref_solution = ref_subproblem.solutions[solution_id]
                student_solution.set_solution(ref_solution.answer, solution_id)
                
                # 1. Overall Check
                rule_str, total_score = "", 0
                for i, rule in enumerate(ref_solution.rules):
                    #rule_str += rule.format_md_table(head = (i == 0))
                    rule_str += f'第{i+1}步，分值为{rule.score}：{rule.rule}\n'
                    total_score += int(rule.score)
                
                overall_check_inputs = my_format_openai_inputs(
                    problem=ref_problem.problem,
                    solution=ref_solution,
                    score=total_score,
                    student_solution=student_solution,
                    rule_str=rule_str
                )
                
                overall_processes, sample_overall_scores = [], []
                for _ in range(self.sample_size):      
                    response = llm.generate(
                        instruction=overall_check_inputs["system_prompt"],
                        prompt=overall_check_inputs["user_prompt"],
                        history=overall_check_inputs['history']
                    )
                    process, score = self.parse_grading_response(response)
                    overall_processes.append(process)
                    sample_overall_scores.append(score)                
                
                overall_check_score, id = self.cal_mode(sample_overall_scores)
                
                # 2. Rule-based Check
                rule_based_processes, rule_based_scores = [], []
                for id, rule in enumerate(ref_solution.rules):
                    rule_based_inputs = format_openai_inputs(
                        ref_problem.problem,
                        ref_solution,
                        student_solution,
                        id,
                    )
                    response = llm.generate(
                        instruction=rule_based_inputs["system_prompt"],
                        prompt=rule_based_inputs["user_prompt"],
                        history=rule_based_inputs['history']
                    )
                    process, score = self.parse_grading_response(response)

                    if not rule.check_valid_score(score):
                        student_solution.set_error(f"Invalid score {score} for rule {rule.rule} (max {rule.score})")

                    rule_based_processes.append(process)
                    rule_based_scores.append(score)                    
                
                rule_based_score = sum(rule_based_scores)
                
                tqdm.write(f"Problem {problem_id} sub-Problem {subproblem_id}:  Overall Score {overall_check_score} from {sample_overall_scores}; Rule Score{rule_based_score}")
                
                for i, rule in enumerate(ref_solution.rules):
                    if i == 0: student_solution.add_score(rule, rule_based_processes[i], (overall_check_score + rule_based_score) / 2)
                    else: student_solution.add_score(rule, rule_based_processes[i], 0)

                
                
                student_solution.finalize(ref_solution.rules)

        return student_pa