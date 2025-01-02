# 基于可学习权重的联合AI批改助手

本工作通过先后考虑答案步骤、多次采样取最大值、构建Pairwise获取联合权重等方式，融合了多个大模型的不同能力，从而实现了对不同大模型的合理利用，提升了最后的预测准确度。

## 文件目录说明
除原始项目文件外，

/checker/final_checker.py 为我们实现的checker

/data/results 会保存AI系统评阅时生成的报告

/files 为冗余的中间文件

/LLM 保存了相关大模型的调用方法

/pointwise 保存了不同大模型对于所有同学的所有题目的评分结果。

/utils/wrappers/final_grading.py 包含评分时所用到的prompt

/utils/wrappers/pointwise_grading.py 包含生成pointwise数据的prompt

main.py 是启动时的主函数

Pearson.py 是通过网格搜索方式枚举相关权重的代码

PICO.py 为使用PICO一文中提出的方式，计算Pairwise下模型对其他模型评分能力的评分的代码。

run.sh 包含了启动时的bash命令。

## 安装方式

~~~
pip install -r requirements.txt
~~~


## 运行方式

可以参考代码根目录中的run.sh文件。可以直接运行main.py来进行评测，需要传入的参数由以下几个：

--ref_path 参考答案文件的路径

--student_path 学生作答文件的路径

--report_path 批改报告的保存路径，默认保存到data/results目录下

--run_name 当前运行的名称，建议设置为“<章节id>_<学生id>”，例如“1B_1”

--n_samples 采样的次数，默认为3
