import os
from instance.problem import StudentPA
from instance.ref_problem import RefPA
from checker.example_checker import ExampleChecker
from checker.my_checker import MyChecker
from reporter.default_reporter import DefaultReporter


base_path = os.path.dirname(os.path.realpath(__file__))
hw_base = "data/ai_judge_dist/1B"
student_id = "1"
model = "chatglm-4-air" #['wenxin', 'chatglm-4-air', 'claude-3-sonnet', 'gpt-3.5-turbo', 'gpt-4o-mini', 'gpt-4', 'deepseek-chat']

ref_path = os.path.join(hw_base, "ref_answers/Chap1B.json")
student_path = os.path.join(hw_base, f"testcases/Ch1-1B-{student_id}.json")
ref_path = os.path.join(base_path, ref_path)
student_path = os.path.join(base_path, student_path)

ref_pa = RefPA.from_json(ref_path)
student_pa = StudentPA.load_raw(student_path)

checker = ExampleChecker()
#checker = MyChecker(sample_size=3)
student_pa = checker.check(model, ref_pa, student_pa)

# reporter
reporter = DefaultReporter(os.path.join(base_path, hw_base, "results"))
reporter.generate_reports(student_pa, f"{student_id}_glm.json", f"{student_id}_glm.md")
