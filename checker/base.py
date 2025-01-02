"""
    Abstract class for checkers

    Input:
        - a RefPA
        - a StudentPA

    Output:
        - a StudentPA with the scores for each subproblem
"""

import json
from abc import ABC, abstractmethod

class BaseChecker(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def check(self, model, ref_pa, student_pa):
        return student_pa

    def parse_correctness_response(self, response):
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

    def parse_grading_response(self, response):
        try:
            response = response.split("```json")[-1]
            response = response.split("```")[0]
            response = response.replace("\\", "\\\\").replace("\\\\\\\\", "\\\\").replace('\n', ' ').replace('\t', ' ')
            response = json.loads(response)
            process = response["process"]
            score = float(response["score"])
        except:
            try:
                idx = response.lower().find("score")
                process = response
                score = float(response[idx+7:].split('\n')[0])
                print(f"\nFormat Error Response: {response}\nScore:{score}")
            except:
                process = "###JSON Format Error"
                score = 0
                print(f"###JSON Format Error, No Score Found")
                
        return process, score
