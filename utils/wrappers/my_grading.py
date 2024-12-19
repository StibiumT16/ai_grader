"""
    Wrapper for the example grading API
"""
from instance.ref_problem import Solution
from instance.problem import StudentSolution

CHECK_PATTERN="""
### 题目文本
{problem}

### 当前题目编号
{subproblem_id}

### 当前题目分值
{score}

### 参考答案
{rule_str}

### 学生答案
{student_answer}
"""


SYSTEM="""
你是一个辅助批改数学题目的助教。你的任务是根据输入的一个题目和其参考答案，对学生的答案进行批改。

输入格式：
1. 题目文本：在“### 题目文本”后以文本形式给出，包括题目本身的文本，注意题目可能有多个小题，这里给出的是完整的题目
2. 当前题目：在“### 当前题目编号”后指定当前批改的小题编号，如果没有小题则批改整道题目
3. 当前题目分值：在“### 当前题目分值”后指定当前批改小题的总分值。注意：学生在当前小题中的得分不能超过给定的总分值
4. 参考答案：在“### 参考答案”后给出当前题目的参考答案，其中提供了可以参考的解题步骤和该步骤对应的得分。注意：学生可能给出与参考答案不完全一致解题思路，只要思路合理且答案正确，则学生的答案也应该视为正确
5. 学生答案：在“### 学生答案”后给出，是学生给出的解答，可能有错误

你的任务是检查评分规则，判断学生答案是否正确，并根据解题步骤给出当前小题学生应当获得的分值。要求返回格式为JSON Dict，包括两个字段：
- process: 一段文本，描述你的评判依据，即给分的过程。比如，对于有多个数值的比较部分（如表格），请逐个列出标准答案中的值和学生答案中的值，并进行比较。评分过程应该足够细致，防止有错误没有发现。
- score：一个整数值
"""

def my_format_openai_inputs(
    problem: str,   # whole problem text
    solution: Solution, # ref solution
    score: int,
    student_solution: StudentSolution,  # student answer
    rule_str: str,   # index of the grading rule    
):
    subproblem_id = solution.subproblem_id
    answer = solution.answer
    student_answer = student_solution.answer

    return {
        "model": "deepseek-chat",
        "system_prompt": SYSTEM,
        "user_prompt": CHECK_PATTERN.format(
            problem=problem,
            subproblem_id=subproblem_id,
            score=score,
            rule_str=rule_str,
            student_answer=student_answer,
        ),
        "history": [],
        "temperature": 0.0,
        "max_tokens": 2048,
    }