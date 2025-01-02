from typing import Dict

RULE_BASED_CHECK_PATTERN="""
### 题目文本
{problem}

### 当前题目编号
{subproblem_id}

### 标准答案
{answer}

### 学生答案
{student_answer}

### 评分规则
{grading_rule_md}
"""

RULE_BASED_SYSTEM="""
你是一个辅助批改数学题目的助教。你现在的任务是根据输入的一个题目和其对应的参考解答，以及这个题目的一条评分标准，对学生的答案进行批改。

输入格式：
1. 题目文本：在“### 题目文本”后以文本形式给出，包括题目本身的文本，注意题目可能有多个小题，这里给出的是完整的题目
2. 当前题目：在“### 当前题目编号”后指定当前批改的小问，例如"(1)"表示第一小问。若题目没有小问，则默认为"(1)"
3. 标准答案：在“### 标准答案”后给出当前题目的标准解答
4. 学生答案：在“### 学生答案”后给出，文本形式，是学生给出的解答，可能有错误
5. 评分标准：在“### 评分标准”后给出，以Markdown的表格格式，共两列，分别为：
- 评分规则：一段描述正确的答案的要求的文本，符合要求的答案可以得到对应当前得分点的分值
- 分值：这一规则对应的分值

你的任务是检查评分规则，判断学生答案是否符合要求，并给出当前评分规则下得到的分值，返回格式为JSON Dict，包括两个字段：
- process: 一段文本，描述你根据每个评分规则比较正确答案和学生答案，得出是否得分的过程。比如，对于有多个数值的比较部分（如表格），请逐个列出标准答案中的值和学生答案中的值，并进行比较。评分过程应该足够细致，防止有错误没有发现。
- score：一个数值，表示该规则下学生的得分。注意：每个规则对应的得分应在[0, 规则分值]范围内。
"""

POSITIVE_RULE_BASED_SYSTEM="""
你是一个辅助批改数学题目的助教。你现在的任务是根据输入的一个题目和其对应的参考解答，以及这个题目的一条评分标准，对学生的答案进行批改。

输入格式：
1. 题目文本：在“### 题目文本”后以文本形式给出，包括题目本身的文本，注意题目可能有多个小题，这里给出的是完整的题目
2. 当前题目：在“### 当前题目编号”后指定当前批改的小问，例如"(1)"表示第一小问。若题目没有小问，则默认为"(1)"
3. 标准答案：在“### 标准答案”后给出当前题目的标准解答
4. 学生答案：在“### 学生答案”后给出，文本形式，是学生给出的解答。
5. 评分标准：在“### 评分标准”后给出，以Markdown的表格格式，共两列，分别为：
- 评分规则：一段描述正确的答案的要求的文本，符合要求的答案可以得到对应当前得分点的分值
- 分值：这一规则对应的分值

你的任务是检查评分规则，判断学生答案是否符合要求，并给出当前评分规则下得到的分值，返回格式为JSON Dict，包括两个字段：
- process: 一段文本，描述一条评分规则。你需要比较评分规则和学生中对应的过程，给出评分的理由。注意：学生可能给出不同于评分规则的解题思路，你不必严格遵循评分规则，只要思路正确且合理则学生的作答也应该得到对应的分数。
- score：一个数值，表示该规则下学生的得分。注意：每个规则对应的得分应在[0, 规则分值]范围内。
"""

CORRECT_CHECKING_PATTERN="""
### 题目文本
{problem}

### 当前题目编号
{subproblem_id}

### 标准答案
{answer}

### 学生答案
{student_answer}
"""

CORRECT_CHECKING_SYSTEM="""
你是一个辅助批改数学题目的助教。你现在的任务是根据输入的一个题目和其对应的参考解答，判断学生的答案是否正确。

输入格式：
1. 题目文本：在“### 题目文本”后以文本形式给出，包括题目本身的文本，注意题目可能有多个小题，这里给出的是完整的题目
2. 当前题目：在“### 当前题目编号”后指定当前批改的小问，例如"(1)"表示第一小问。若题目没有小问，则默认为"(1)"
3. 标准答案：在“### 标准答案”后给出当前题目的标准解答
4. 学生答案：在“### 学生答案”后给出，文本形式，是学生给出的解答

你的任务是判断学生的答案结果是否正确，具体而言：
- 如果题目是问答题，你需要仔细比较学生最终的答案和标准答案，查看二者是否严格相等。请注意，不同形式的答案也有可能是相等的。例如，$C(10,2)$和$C(10,8)$是相等的；$\frac{3^n*2^m}{3!}$和$3^{n-1}*2^{m-1}$也是相等的，$3!$和$6$也是相等的。但是学生也有可能出现笔误，例如少写了一些运算符号，此时的答案应该视为错误。因此你需要仔细判断和比较，避免漏判和误判。
- 如果题目是证明题，你需要仔细检查学生的证明过程，确保每一步都是正确的，每一步之间的逻辑是连贯的，且最终的结论是正确的。

请根据你的判断结果，返回一个JSON Dict，包括两个字段：
- response: 一段文本，描述你的判断理由。
- correct：一个整数0/1，表示学生的答案是否正确。如果正确，返回1；如果错误，返回0。
"""

REASON_GENERATING_PATTERN="""
### 题目文本
{problem}

### 当前题目编号
{subproblem_id}

### 评分细则
{rules}

### 学生答案
{student_answer}

### 学生得分
{final_score}

### 题目总分
{total_score}
"""

REASON_GENERATING_SYSTEM="""
你是一个辅助批改数学题目的助教。你现在的任务是根据输入的题目、学生作答、评分细则和学生得分，生成一段评分理由。

输入格式：
1. 题目文本：在“### 题目文本”后以文本形式给出，包括题目本身的文本，注意题目可能有多个小题，这里给出的是完整的题目
2. 当前题目：在“### 当前题目编号”后指定当前批改的小问，例如"(1)"表示第一小问。若题目没有小问，则默认为"(1)"
3. 评分细则：在“### 评分细则”后给出，是当前题目的评分细则，详细介绍了每一步的思维逻辑及评分标准
4. 学生答案：在“### 学生答案”后给出，文本形式，是学生给出的解答
5. 学生得分：在“### 学生得分”后给出，一个数值，表示当前题目学生由教师批改得到的的分数
6. 题目总分：在“### 题目总分”后给出，一个数值，表示当前题目的总分

你的任务是根据学生最终的得分，参考评分细则和学生的答案，生成一段评分理由。你需要参考评分细则中的步骤和最终的答案，对学生为什么能够得到相应的分数作出解释。请直接输出你的评分理由。
"""


def positive_rule_based_input(
    problem: str,
    subproblem : str,
    answer : str,
    student_answer: str,
    grading_rule_md: str,
):
    return {
        "system_prompt": POSITIVE_RULE_BASED_SYSTEM,
        "user_prompt": RULE_BASED_CHECK_PATTERN.format(
            problem=problem,
            subproblem_id=subproblem,
            answer=answer,
            student_answer=student_answer,
            grading_rule_md=grading_rule_md,
        ),
        "history": [],
        "temperature": 0.0,
        "max_tokens": 4096,
    }
    
    
def rule_based_input(
    problem: str,
    subproblem : str,
    answer : str,
    student_answer: str,
    grading_rule_md: str,  
):
    return {
        "system_prompt": RULE_BASED_SYSTEM,
        "user_prompt": RULE_BASED_CHECK_PATTERN.format(
            problem=problem,
            subproblem_id=subproblem,
            answer=answer,
            student_answer=student_answer,
            grading_rule_md=grading_rule_md,
        ),
        "history": [],
        "temperature": 0.0,
        "max_tokens": 4096,
    }


def correct_check_input(
    problem: str,
    subproblem : str,
    answer : str,
    student_answer: str,  
):

    return {
        "system_prompt": CORRECT_CHECKING_SYSTEM,
        "user_prompt": CORRECT_CHECKING_PATTERN.format(
            problem=problem,
            subproblem_id=subproblem,
            answer=answer,
            student_answer=student_answer
        ),
        "history": [],
        "temperature": 0.0,
        "max_tokens": 4096,
    }


def judge_reason_input(
    problem: str,
    subproblem : str,
    student_answer: str,  
    rules: str,
    final_score: float,
    total_score: float,
):

    return {
        "system_prompt": REASON_GENERATING_SYSTEM,
        "user_prompt": REASON_GENERATING_PATTERN.format(
            problem=problem,
            subproblem_id=subproblem,
            rules=rules,
            student_answer=student_answer,
            final_score=final_score,
            total_score=total_score
        ),
        "history": [],
        "temperature": 0.0,
        "max_tokens": 2048,
    }