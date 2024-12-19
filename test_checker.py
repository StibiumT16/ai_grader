from instance.problem import StudentPA
from instance.ref_problem import RefPA

import os
base_path = os.path.dirname(os.path.realpath(__file__))
hw_base = "data/ai_judge_dist/1A"
student_id = "17"

ref_path = os.path.join(hw_base, "ref_answers/chap1A.json")
student_path = os.path.join(hw_base, f"testcases/Ch1-1A-{student_id}.json")
ref_path = os.path.join(base_path, ref_path)
student_path = os.path.join(base_path, student_path)

ref_pa = RefPA.from_json(ref_path)
student_pa = StudentPA.load_raw(student_path)

# local deepseek api key
import json, os
api_configs = json.load(open("api_config.json", "r"))
os.environ["OPENAI_API_KEY"] = api_configs["api_key"]
os.environ["OPENAI_BASE_URL"] = api_configs["base_url"]

#from checker.example_checker import ExampleChecker
#checker = ExampleChecker()
from checker.my_checker import MyChecker
checker = MyChecker(sample_size=3)

student_pa = checker.check(ref_pa, student_pa)

# reporter
from reporter.default_reporter import DefaultReporter
reporter = DefaultReporter(os.path.join(base_path, hw_base, "results"))
reporter.generate_reports(student_pa, f"{student_id}_mix.json", f"{student_id}_mix.md")
