import os, argparse
from instance.problem import StudentPA
from instance.ref_problem import RefPA
from checker.final_checker import FinalChecker
from reporter.default_reporter import DefaultReporter


parser = argparse.ArgumentParser()
parser.add_argument("--ref_path", type=str, default="data/ai_judge_dist", help="Path to reference answer")
parser.add_argument("--student_path", type=str, default="data/ai_judge_dist", help="Path to student homework")
parser.add_argument("--report_path", type=str, default="data/results", help="Path to output report")
parser.add_argument("--run_name", type=str, default="run", help="Name of the run")
parser.add_argument("--n_samples", type=int, default=3, help="Number of samples to grade")
args = parser.parse_args()


ref_pa = RefPA.from_json(args.ref_path)
student_pa = StudentPA.load_raw(args.student_path)


checker = FinalChecker(
    models=['deepseek-chat', 'chatglm-4-air', 'gpt-4o-mini'],
    weights=[0.64, 0.24, 0.12],
    sample_size=args.n_samples
)
student_pa = checker.check(ref_pa, student_pa)

# reporter
reporter = DefaultReporter(args.report_path)
reporter.generate_reports(student_pa, f"{args.run_name}.json", f"{args.run_name}.md")
