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

    def parse_grading_response(self, response):
        try:
            response = response.split("```json")[-1]
            response = response.split("```")[0]
            response = response.replace("\\", "\\\\").replace("\\\\\\\\", "\\\\")
            response = json.loads(response)
            process = response["process"]
            score = int(response["score"])
        except:
            print("Format Error Response: ", response)
            idx = response.lower().find("score")
            process = "#Json Format Error"
            score = int(response[idx+8])
        return process, score