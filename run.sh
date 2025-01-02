chapter=6X
student="1"

run_name=${chapter}_${student}

base_path=data/ai_judge_dist/${chapter}/
report_path=data/results/

ref_path=$base_path/ref_answers/Chap${chapter}.json
student_path=$base_path/testcases/Ch${chapter:0:-1}-${chapter}-${student}.json


python main.py \
    --ref_path $ref_path \
    --student_path $student_path \
    --report_path $report_path \
    --run_name $run_name
