## Problem 1.25
### Subproblem (1)
#### Status
graded
#### Answer
由题意得： \begin{align*} \sum_{A\in S} \operatorname{min} A &= 1\cdot C^{r-1}_{n-1} + 2\cdot C^{r-1}_{n-2} + \cdots + (n-r+1)\cdot C^{r-1}_{r-1} \end{align*} 注意到$1\cdot C^{r-1}_{n-1}$是多项式$(1+x)^{n-1}$中$x^{r-1}$的系数，$2\cdot C^{r-1}_{n-2}$是多项式$2(1+x)^{n-2}$中$x^{r-1}$的系数，以此类推，考虑多项式: \begin{align*} & (1+x)^{n-1} + 2(1+x)^{n-2} + \cdots + (n-r+1)(1+x)^{r-1} \\ = & \{(1+x)^{n-1} + \cdots + (1+x)^{r-1}\} + \{(1+x)^{n-2} + \cdots + (1+x)^{r-1} \} + \cdots + (1+x)^{r-1}\\ = & (1+x)^{r-1}\cdot \frac{(1+x)^{n-r+1} - 1}{x} + \cdots + (1+x)^{r-1}\cdot \frac{(1+x)^1 - 1}{x} \\ = & (1+x)^{r-1}\cdot \sum_{k=1}^{n-r+1} \frac{(1+x)^k - 1}{x} \\ = & -(n-r+1)\frac{(1+x)^{r-1}}{x} + \frac{(1+x)^{r-1}}{x} \cdot \sum_{k=1}^{n-r+1} (1+x)^k \\ = & -(n-r+1)\frac{(1+x)^{r-1}}{x} + \frac{(1+x)^{r-1}}{x} \cdot (1+x)\cdot \frac{(1+x)^{n-r+1}-1}{x} \\ = & -(n-r+1)\frac{(1+x)^{r-1}}{x} + \frac{(1+x)^{n+1} - (1+x)^{r}}{x^2} \end{align*} 注意到在求和后的结果中，$x^{r-1}$的系数仅在$\frac{(1+x)^{n+1}}{x^2}$中存在，易得结果为$\binom{n+1}{r+1}$。
#### Matched solution ID
0
#### Correct solution
考虑选择$\left\{ 0, 1, 2, \cdots, n \right\}$的$r + 1$元子集，然后去掉其中的最小元后得到$A$。 $A$显然是$\left\{ 1, 2, \cdots, n \right\}$的$r$元子集，并且共有$\min A$个集合在去掉最小元后都能得到$A$。 因此，和式的值即为$\binom{n + 1}{r + 1}$。
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 说明每个$r$元子集最小值与$r+1$元子集有映射关系 | 10 | 7 | 学生的答案尝试通过多项式展开和生成函数的方式求解，而标准答案通过直接建立$r$元子集与$r+1$元子集之间的映射关系来证明。学生给出了多项式展开的过程，并推导出最终结果$\binom{n+1}{r+1}$，但是没有明确提到通过映射关系来解释最小值与$r+1$元子集的关系，因此未能完全符合评分标准。虽然结果是正确的，但缺乏直接的映射关系说明。 |


## Problem 1.26
### Subproblem (1)
#### Status
graded
#### Answer
考虑``dog''为一个元素，首先不考虑p,dog,q的顺序问题，则原问题等价于24个元素全排列，共有$A^{24}_{24}$种方案，根据题目要求最终排列中必须满足p,dog,q的顺序，故总共有$A^{24}_{24}/3$种方案。
#### Matched solution ID
0
#### Correct solution
将dog视作一个整体与其他$23$个字母一起参与排列，其中p, dog, q只能按顺序出现，方案数即为$\frac{24!}{3!}$。
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| dog视作整体，得到24! | 4 | 4 | 学生答案考虑将 'dog' 看作一个整体，但在后续的计算中存在问题。学生认为全排列的总数为24!，这个部分是正确的，符合标准答案的第一步，即将 'dog' 视为一个整体。但学生错误地使用了 'A^{24}_{24}' 来表示排列数，实际上应该是 24!（这两个符号在排列中是不同的）。另外，学生在考虑顺序约束时，使用了除以 3 的做法，这并不符合题目要求，应该是通过在整体中保留 'dog' 和其他字母的顺序来得出正确的方案数。标准答案应该是 24! / 3! 而不是除以 3。因此，学生正确完成了将 'dog' 视作整体的部分，但在接下来的步骤中犯了错误。 |
| p, dog, q按顺序出现，需要/3! | 4 | 0 | 学生答案在理解题意时考虑了dog作为一个整体，并且没有错误地推导出排列的基础数量（$24!$）。然而，在考虑p, dog, q的顺序时，学生错误地将除以3而不是3!，即缺少了对3个元素（p, dog, q）顺序的完整排列数。标准答案是将p, dog, q作为3个固定顺序的元素，得出除以3!，而学生的答案是除以3，未准确处理排列的方式，因此得分不全。 |
| 答案正确 | 2 | 1 | 学生的解答中首先考虑了将' dog'作为一个整体，这一部分与标准答案一致。然后学生提到了24个元素的全排列，即$A^{24}_{24}$，这个做法正确。但学生在处理p、dog、q顺序问题时，使用了错误的表达。标准答案中是通过将p、dog、q按顺序排列的限制来得出$\frac{24!}{3!}$，而学生的解答则错误地表示为$A^{24}_{24}/3$，这种方式不正确，因为涉及到的排列方式应该是$\frac{24!}{3!}$，而不是除以3。因此，学生的答案在最终方案数的计算上是错误的，未能达到标准答案的要求。 |


## Problem 1.27
### Subproblem (1)
#### Status
graded
#### Answer
假设$a$之前有$x_1$个字母，$a,b$之前有$x_2$个，$b,c$之前有$x_3$个，$c,d$之前有$x_4$个,$d,e$之前有$x_5$个,$e$之后有$x_6$个，于是： \[ x_1 + x_2 + x_3 + x_4 + x_5 + x_6 + 5 = 100 \] 其中$x_2\ge 3, x_3\ge 5, x_4\ge 7, x_5\ge 9$， 令$y_1=x_1, y_2 = x_2 - 3, y_3 = x_3 - 5, y_4 = x_4 - 7, y_5 = x_5-9, y_6=x_6$, 得: \[ y_1 + y_2 + y_3 + y_4 + y_5 + y_6 = 100 - 5 - 3 - 5 - 7 - 9 = 71 \] 问题转化为求上述非负整数解，共有$C^{71}_{76}$组。最后对剩下95个字母进行多重全排列，得到最终排列方案数目为： \[ \binom{76}{71} \cdot \frac{95!}{19!\cdot 19! \cdot 19! \cdot 19! \cdot 19!} \]
#### Matched solution ID
0
#### Correct solution
先为除$a, b, c, d, e$以外的字母安排位置，相当于求$x_1 + x_2 + \cdots + x_6 = 71$的非负整数解数目，方案数为$\binom{76}{5}$； 然后排列这些字母，方案数为$\frac{95!}{(19)^5}$。 相乘即得总的方案数为$\binom{76}{5}\frac{95!}{(19)^5}$。
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 列出不定方程 | 3 | 3 | 学生答案正确列出了不定方程，并且通过变量替换的方式将问题转化为求解非负整数解数目。具体的方程式为 y_1 + y_2 + y_3 + y_4 + y_5 + y_6 = 71，且给出了 x_2 >= 3, x_3 >= 5, x_4 >= 7, x_5 >= 9 的约束条件。此过程符合题目要求，因此能够得到满分。 |
| 化为标准形式，即任意变量的限制都是$x\ge0$ | 1 | 1 | 学生在解答中提出了一个变量变换的想法，设定了新的变量 $y_1, y_2, ..., y_6$，并将约束条件转化为相应的非负整数解问题。对于原题中的约束条件，学生准确地进行了变换，得到了新的方程 $y_1 + y_2 + y_3 + y_4 + y_5 + y_6 = 71$，并保证了所有变量的非负性。与标准答案的变换方法一致，因此能够得到这一得分点。 |
| 插板法得到解的正确数目 | 3 | 2 | 学生在使用插板法求解问题时，首先设定了 $x_1$ 到 $x_6$ 的关系，这与标准解法的设定相符。学生在转换变量后，得到了正确的方程 $y_1 + y_2 + y_3 + y_4 + y_5 + y_6 = 71$，并正确地列出了约束条件 $x_2 \geq 3$, $x_3 \geq 5$, $x_4 \geq 7$, $x_5 \geq 9$。但在标准答案中，最后得出的组合数应是 $\binom{76}{5}$，而学生将其写成了 $\binom{76}{71}$，这是一个错误。这个错误使得学生的组合数计算公式与标准答案有所偏差，因此评分规则中的“插板法得到解的正确数目”部分应该未能完全符合要求。 |
| 由多重排列得到95个位置的排列数 | 2 | 1 | 学生答案对题目的理解和步骤基本正确，但在多重排列的部分存在错误。学生正确地计算了非负整数解的部分，并且设定了适当的变量转换，得到了正确的方程 y_1 + y_2 + y_3 + y_4 + y_5 + y_6 = 71。然后，学生正确地使用组合数 C(71, 76) 来计算非负整数解的数量。关键错误在于最后的多重排列部分，学生使用了错误的排列公式。正确的排列公式应该是 95! / (19!)^5，而学生错误地使用了 95! / (19! * 19! * 19! * 19! * 19!)，虽然这个表达式形式看似相似，但本质上没有体现出分母中有五个19!，这一点导致了分数上的细微偏差。 |
| 乘法原理得到正确答案 | 1 | 1 | 学生答案正确地应用了乘法原理，首先通过转换变量的方式，将字母a, b, c, d, e的位置间隔问题转化为求非负整数解的形式，并且正确得出总和为71，最后根据公式 $\binom{76}{5}$ 和 $95!$ 的全排列计算得到总方案数。但学生在计算组合数时，写作了 $C^{71}_{76}$，实际应写为 $\binom{76}{5}$，这仅仅是符号上的错误，不影响解答的正确性。最后，排列部分的形式 $\frac{95!}{19! \cdot 19! \cdot 19! \cdot 19! \cdot 19!}$ 是正确的，完全符合标准答案的要求。 |


## Problem 1.28
### Subproblem (1)
#### Status
graded
#### Answer
考虑以下不定方程的所有非负整数解： \[ x_1 + x_2 + \cdots + x_n + x_{n+1} = m \] 利用隔板法考虑$m$个1和$n$个板的全排列，得到等式左侧$C^{m}_{n+m}$。接着首先考虑$x_{n+1}\ge 1$时解的个数，此时: \[ x_1 + x_2 + \cdots + x_n + (x_{n+1} - 1) = m - 1 \] 解的个数为$C^{m-1}_{n+m-1}$, 接着考虑$x_{n+1}=0, x_n\ge 1$的解的个数： \[ x_1 + x_2 + \cdots + x_{n-1} + (x_{n} - 1) = m - 1 \] 解的个数为$C^{m-1}_{n+m-2}$, 以此类推，可知当考虑$x_{k+1}=\cdots=x_{n+1}=0, x_k\ge 1$时解的个数为$C^{m-1}_{k+m-2}$。由于每种情况下的解一定不会出现重复，故所有方程的解为： \[ \sum_{k=1}^{n+1} C^{m-1}_{k+m-2} = \sum_{k=0}^{n} C^{m-1}_{k+m-1} = C^{m}_{n+m} \]
#### Matched solution ID
0
#### Correct solution
等式左侧为$\sum_{i = 1}^{m+1} x_i = n$的非负整数解数目，等式右侧和式中的第$k$项表示$\sum_{i = 1}^m x_i = k$且$x_{m+1} = n - k$的非负整数解数目，可知右侧和式与左侧相等。 证明方法不只这一种，其他方法只要满足题意亦可。
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 构造左侧对应的不定方程 | 3 | 3 | 学生答案构造了不定方程并试图通过隔板法进行求解。学生写出了方程形式为$x_1 + x_2 + \cdots + x_{n+1} = m$，这是一个典型的隔板法应用，符合左侧对应的不定方程的要求。然而，学生对于方程中的各个约束条件进行了进一步的细化，并详细推导了不同情况下的解数目，最终推导出答案为$\sum_{k=0}^{n} C^{m-1}_{k+m-1}$。这个过程虽然涉及更多的步骤，但总体上是合理的，并且与标准答案中的不定方程对应，符合评分标准的要求。因此，可以认为学生在这一评分规则下得分。 |
| 求解左侧不定方程解个数 | 2 | 2 | 学生答案中的左侧不定方程是 $x_1 + x_2 + \cdots + x_{n+1} = m$，并且利用隔板法正确地得出了此方程的解个数为 $C^{m}_{n+m}$，这与标准答案中提到的左侧不定方程的解数目一致。因此，学生在此部分正确地解决了左侧的不定方程解个数问题。 |
| 构造右侧对应的不定方程 | 3 | 1 | 学生答案尝试通过不定方程和隔板法来证明给定的等式。首先，学生设立了一个和式表示方程的所有非负整数解，最终归结为求解一些组合数的和。虽然学生使用了隔板法来列举解法，并且推导出了一些部分正确的组合数，但在细节上存在错误。例如，学生在设立不定方程时没有正确匹配左侧和右侧的方程形式，且对方程中的索引及组合数的表达不完全准确。此外，学生推导中的$k$范围也不一致。总体来看，学生的思路接近正确，但存在重要的推导错误，因此没有完全构造出右侧的不定方程。由于存在明显的推导问题，学生没有完全实现题目要求的构造，因此无法完全得分。 |
| 求解右侧不定方程解个数 | 2 | 2 | 学生答案中的思路和方法基本正确，使用了隔板法来处理不定方程的解，明确了等式右侧每一项的含义，并逐步推导出了求解解个数的过程。学生通过考虑不同条件下的解个数，最终得到了和标准答案相符的求和表达式。虽然学生解法的符号和排列顺序与标准答案稍有不同，但逻辑正确，因此可以获得满分。 |


## Problem 1.29
### Subproblem (1)
#### Status
graded
#### Answer
\subsection{(1)} $C^4_5 + C^2_5\cdot C^2_4 + C^4_4 = 66$.
#### Matched solution ID
0
#### Correct solution
\item 四个正数$1$种方案，两正两负$\binom{4}{2}\binom{5}{2} = 60$种方案，四个负数$\binom{5}{4} = 5$种方案，合计$66$种；
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 4正情况正确 | 1 | 0 | 学生答案中的 'C^4_5' 部分看似是想表示选择4个正数的情况，但这并不是正确的表达方式。标准答案中提到选择四个正数应该只有 1 种方案，而学生的表达式是 'C^4_5'，这显然不符合正确的计算方法。因此，学生在四个正数的情况中没有正确理解和表达。根据评分规则，学生未能正确处理四个正数的情况，得分为 0。 |
| 2正2负情况正确 | 2 | 2 | 学生在计算'两正两负'的情况时，表达式C^2_5·C^2_4应当为正确的'选2个正数'和'选2个负数'的组合数。学生的表达式C^2_5·C^2_4表示组合数的选择方式正确，因此在这一部分得分。标准答案也提出了类似的公式计算，因此在这一规则下，学生得到了2分。 |
| 4负情况正确 | 1 | 1 | 学生答案中提到了 'C^4_4' 这个组合公式，实际上是指四个负数的选法，符合标准答案中的 '四个负数' 方案。标准答案中正确地使用了组合公式 $\binom{5}{4} = 5$，而学生答案 'C^4_4' 对应的含义是正确的。因此，学生对于 '四个负数' 的情况是正确的，符合评分规则，得分1分。 |
| 求和正确 | 1 | 0 | 学生答案中出现了组合符号 $C^4_5 + C^2_5\cdot C^2_4 + C^4_4$，但是这些组合的具体含义与标准答案中的情况不完全对应。标准答案中计算了三种情况：四个正数、两正两负、四个负数。学生答案没有明确区分这些情况，且组合项的选择与标准答案中的情况不一致。尤其是 $C^4_5$ 这种组合不符合题意，因此不能算作正确的求和过程。尽管最终结果 $66$ 是正确的，但中间的步骤并未正确描述，导致评分为0。 |


### Subproblem (2)
#### Status
graded
#### Answer
\subsection{(2)} $5^4 + 5^2\cdot 4^2 + 4^4 = 1281$.
#### Matched solution ID
0
#### Correct solution
\item 若四个正数，设第$i$个正整数选择$x_i$次，则就相当于求$x_1 + x_2 + x_3 + x_4 = 4$的非负整数解数目，为$\binom{7}{3} = 35$种方案； 类似地，两正两负$\binom{6}{4}\binom{5}{3} = 150$种方案，四个负数$\binom{8}{4} = 5$种方案，合计$255$种。
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 4正情况正确 | 1 | 0 | 学生答案中给出的表达式$5^4 + 5^2\cdot 4^2 + 4^4 = 1281$并没有体现出标准答案中提到的正确的求解方法。标准答案中列出了不同组合的计算方法，例如四个正数的组合数$\binom{7}{3}$等，然而学生答案并没有正确地按照标准解法进行。学生的答案和评分规则中的正确方法完全不一致，因此无法获得分数。 |
| 2正2负情况正确 | 2 | 0 | 学生答案没有正确计算2正2负的情况。标准答案中，2正2负的方案数应为$\binom{6}{4} \binom{5}{3} = 150$，而学生的答案未进行相应的组合计算。学生答案中提到的$5^4 + 5^2\cdot 4^2 + 4^4 = 1281$并没有直接体现2正2负的正确计算。因为学生没有正确处理2正2负的情况，所以没有得分。 |
| 4负情况正确 | 1 | 0 | 根据评分规则，要求检查学生是否正确处理了4个负数的情况。标准答案中指出4个负数的情况是$\binom{8}{4} = 5$种方案，而学生在答案中给出的计算方式为$5^4$，这明显是错误的计算方式。$5^4$是一个乘积，而不是组合数计算的结果，因此学生在这一部分的答案是错误的，未能正确处理4个负数的情况。 |
| 求和正确 | 1 | 0 | 学生答案给出的计算表达式为 $5^4 + 5^2 \cdot 4^2 + 4^4 = 1281$，而标准答案则通过组合数学方法计算方案数，得出的是 255 种方案。学生的计算方法和答案明显不符合标准答案，且没有遵循正确的组合公式，也没有体现求和的正确步骤，因此无法获得求和正确的分值。 |


## Problem 1.30
### Subproblem (1)
#### Status
graded
#### Answer
由于： \[ xyz = 2^6 \cdot 5^6 \] 令： \[ x = 2^{a_1}\cdot 5^{b_1}, y = 2^{a_2}\cdot 5^{b_2}, z = 2^{a_3}\cdot 5^{b_3}. \] 于是问题转化为求下列不定方程的非负整数解： \[ a_1+a_2+a_3 = 6, b_1 + b_2 + b_3 = 6 \] 可得$(a_1, a_2, a_3)$共有$C^6_{8}=28$组解， 同理$(b_1, b_2, b_3)$也有28组解。最后考虑$x,y,z$中任意两数为负数或全为正数的情况，最终共有$28\times 28 \times (1 + C^2_3) = 3136$组整数解。
#### Matched solution ID
0
#### Correct solution
$10^6 = 2^6 \times 5^6$，$2, 5$这两个因子在$x, y, z$中的分配均等价于$x_1 + x_2 + x_3 = 6$的非负整数解，为$\binom{8}{2}$。 由于要求整数解而不是非负整数解，因此需再乘以$4$种符号分配方式，总方案数为$\binom{8}{2}^2 \dotp 4 = 3136$。
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 分解$10^6$ | 1 | 1 | 学生在答案中已经正确地将$10^6$分解为$2^6 \times 5^6$，这一部分符合评分规则。标准答案和学生的分解一致，因此可以得1分。 |
| 列出不定方程 | 4 | 4 | 学生答案中已经列出了方程 $xyz = 2^6 \times 5^6$，并正确地通过 $x = 2^{a_1} \cdot 5^{b_1}, y = 2^{a_2} \cdot 5^{b_2}, z = 2^{a_3} \cdot 5^{b_3}$ 转化为两个不定方程 $a_1 + a_2 + a_3 = 6$ 和 $b_1 + b_2 + b_3 = 6$。这与标准解法一致，因此符合列出不定方程的要求。 |
| 得到不定方程解个数 | 2 | 2 | 学生答案正确地将方程$xyz = 1,000,000$转化为$xyz = 2^6 \times 5^6$，并将$x, y, z$表示为$2^{a_1} \cdot 5^{b_1}$等形式。然后正确地设定了两个方程$a_1 + a_2 + a_3 = 6$和$b_1 + b_2 + b_3 = 6$的非负整数解，并使用组合公式$C^6_8 = 28$计算了解的数量。最后，学生正确考虑了符号分配的情况，并得到了最终答案$28 \times 28 \times (1 + C^2_3) = 3136$，与标准答案一致。因此，学生得分。 |
| 考虑负数情况 | 2 | 2 | 学生答案正确地考虑了负数情况，即在最后一部分提到需要考虑$x, y, z$中任意两数为负数或全为正数的情况，并正确地使用了$C^2_3$来计算符号分配的方式。因此，学生在这一部分考虑了负数的情况，并且计算方法与标准答案一致。 |
| 答案正确 | 1 | 1 | 标准答案中，首先通过因式分解 $10^6 = 2^6 \times 5^6$，然后将 $x, y, z$ 分解为 $x = 2^{a_1} \cdot 5^{b_1}$, $y = 2^{a_2} \cdot 5^{b_2}$, $z = 2^{a_3} \cdot 5^{b_3}$，转换为求解 $a_1 + a_2 + a_3 = 6$ 和 $b_1 + b_2 + b_3 = 6$ 的非负整数解，这两部分分别有 $\binom{8}{2} = 28$ 种解法。然后考虑符号分配问题，学生答案正确地给出了符号分配的情况（通过 $(1 + \binom{3}{2})$ 来表示符号选择），并且得到了最终的整数解数目 $3136$。学生答案和标准答案一致，且推理过程完全正确，因此得分为 1 分。 |


## Problem 1.31
### Subproblem (1)
#### Status
graded
#### Answer
考虑如下游戏：开始有一个盒子和$n$个不同的白球，第一次在这$n$个球中取出一个放入盒子中（不放回），每次取到一个白球放入盒子后补充一个的红球。每个红球不同，下一次在再这$n$个球中取一个球放入盒子中，取到红球时就终止。第$k$次操作后这$n$个球中有$n-k$个不同的白球和$k$个不同的红球，第$k+1$次终止的概率为： \[ \frac{P_n^{k}\cdot P_{k}^1}{n^{k+1}} = \frac{k\cdot P_n^k}{n^{k+1}} \] 由于到第$n+1$次时一定会终止（只剩红球），即这个游戏最终一定会终止，而另一方面这个游戏终止的概率等于在每一轮终止的概率之和，于是对$k$从1到$n$进行求和可得： \[ \sum_{k=1}^n \frac{k\cdot P_n^k}{n^{k+1}} = 1 \]
#### Matched solution ID
0
#### Correct solution
考虑由$1, 2, \cdots, n$组成长度为$n + 1$的序列，方案数为$n^{n + 1}$。 现在讨论此排列各元素互异的最长前缀的长度。 若此前缀长度为$k$，则此前缀有$P(n, k)$种构造方式； 第$k + 1$个元素必须和前面重复，因此有$k$种选择； 后续的元素可以任意，有$n^{n - k}$种选择。 由此即有 % \begin{equation*} \sum_{k = 1}^n P(n, k) \dotp k \dotp n^{n - k} = n^{n + 1} \end{equation*} % 两侧同除以$n^{n + 1}$即得所要证的等式。
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 找到$n^{n+1}$的组合含义 | 2 | 2 | 学生答案中描述的游戏过程与标准答案中的排列思路不完全一致，但学生使用的概率模型实际上是在讨论一种与标准答案类似的过程。学生的解释虽然不同，但本质上描述了一个包含组合和排列选择的过程。通过概率的方式推导出终止概率的和，也正是通过组合计算排列数，最终得出求和结果为1。因此，学生的理解和推导大致是合理的，虽然表述方式不完全吻合，但思路上是相似的。 |
| 找到$k\dotp P(n,k)的组合含义 | 2 | 2 | 学生答案中通过描述一个与题目相关的游戏场景来解释问题，并且明确提出了$k\cdot P_n^k$的组合含义。通过对每次操作过程的描述，学生成功地阐明了$k \dotp P_n^k$代表在第$k$次操作中，发生某一特定事件的概率，并与问题中的数学表达式相符。虽然表述中有些模糊的部分（如$P_n^k$的具体定义不清楚），但总体来说，学生是通过合理的推理展示了组合的含义。 |
| 找到$\frac{1}{n^{k+1}}$的组合含义 | 2 | 2 | 学生答案中有关于游戏的解释，描述了每一轮的终止概率，并且正确地列出了概率公式 \(\frac{k \cdot P_n^k}{n^{k+1}}\)。这个公式中有 \(\frac{1}{n^{k+1}}\)，说明学生正确理解了这个部分的组合含义，表明他们理解了游戏模型中的概率与排列的关系。与标准答案中提到的类似，学生将 \(\frac{1}{n^{k+1}}\) 的含义与概率计算相结合，因此符合评分规则。 |
| 鸽巢原理得到前$k+1$个元素必重复 | 3 | 3 | 学生答案中使用了一个不同的模型来解释问题，描述了一个游戏过程来进行推导。该过程中的关键部分是计算每个步骤中的概率，并结合概率求和来证明最终结果。尽管思路不同，但学生在推导过程中成功地使用了鸽巢原理，特别是在每次操作后，$k+1$次操作时必定出现重复的球，确保游戏最终终止。学生的推导形式虽然不完全相同，但核心思想和鸽巢原理的应用是正确的。因此，学生在这部分评分规则下是合格的。 |
| 得到正确和式 | 1 | 1 | 学生在解答过程中给出了一个与标准答案不同的情境模型，描述了一个关于盒子、白球和红球的过程，最终得到了与题目给出的和式相同的结论。学生的答案通过不同的思路重新推导了标准答案中的和式，并且给出了正确的最终等式。因此，学生的解答通过了题目要求，得出了正确的和式，尽管用的模型不同。 |


## Problem 1.32
### Subproblem (1)
#### Status
graded
#### Answer
根据题意可知，$a_4 = 7, a_6 = 8$，$5$仅可在$a_2,a_3$的位置，故共有$C^1_2\cdot A^4_4=48$组解。
#### Matched solution ID
0
#### Correct solution
$8$后面有$2$个比它小的元素，因此它只能在第$6$个位置； $7$后面有$3$个比它小的元素，因此它只能在第$4$个位置，如下所示： % \begin{equation*} \begin{array}{cccccccc} \underline{\quad} & \underline{\quad} & \underline{\quad} & 7 & \underline{\quad} & 8 & \underline{\quad} & \underline{\quad} \end{array} \end{equation*} % $5$后面有$3$个比它小的元素，因此它只能在第$2$或$3$个位置。 无论哪种情况下，$5$前面都必须恰有一个比它小的元素。 % \begin{itemize} \item 若$5$在第$2$个位置，方案数为$4 \dotp 4! = 96$； \item 若$5$在第$3$个位置，方案数为$2 \dotp \binom{4}{1} \dotp 3! = 48$。 \end{itemize} % 共计$144$种方案。
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 证明5,7,8顺序 | 3 | 2 | 学生答案正确地识别出了7和8的位置要求，给出了$a_4 = 7$和$a_6 = 8$，并且明确了5的位置只能在$a_2$或$a_3$。然而，学生没有详细展开如何从排列中进一步推导出5的具体可能位置以及方案数。学生也忽略了详细的排列计数方式，尤其是对于5的排放方式和之后的计数。 |
| 得到7和8位置 | 3 | 3 | 学生答案中已经正确指出$7$的中介数要求它必须在第4个位置，$8$的中介数要求它必须在第6个位置。并且学生正确给出了$7$和$8$的位置安排（$a_4 = 7$，$a_6 = 8$）。这个步骤符合标准答案的要求，因此得到3分。 |
| 分类讨论得到正确结果 | 4 | 2 | 学生的答案首先正确确定了$7$和$8$的位置，$a_4 = 7, a_6 = 8$，这一点是符合标准答案的。然而，学生在后续的计算部分出现了问题。标准答案在讨论$5$的位置时提到，若$5$在第$2$个位置，方案数应为$4 \cdot 4! = 96$，若$5$在第$3$个位置，方案数应为$2 \cdot \binom{4}{1} \cdot 3! = 48$。而学生在答案中直接写了$C^1_2 \cdot A^4_4 = 48$，没有正确考虑两种情况，也没有明确使用$96$的计算。由于缺少分类讨论和准确的计算过程，最终得出的结果不完全正确。 |


## Problem 1.33
### Subproblem (1)
#### Status
graded
#### Answer
首先考虑抽取$n$个不相邻的盒子，利用插空法，去掉$n$个盒子后还剩余$m-n$个盒子，有$m-n+1$个空可插入，故选法共有$C_{m-n+1}^n$种。 其次考虑这$n$个盒子每个包含$x_1,\dots,x_n$个小球，故问题转化为： \[ x_1 + x_2 +\cdots+x_n = r, \forall i\in [n] \quad x_i \ge k \] 令$y_i = x_i -r$，得： \[ y_1 + y_2 +\cdots+y_n = r - nk, \forall i\in [n] \quad y_i \ge 0 \] 可知$(y_1,\dots,y_n)$共有$C^{r-nk}_{n+r-nk-1}$组解。由于这$n$个盒子互不相同，于是最终结果为: \[ A^n_n\cdot C_{m-n+1}^n\cdot C^{r-nk}_{n+r-nk-1}. \]
#### Matched solution ID
0
#### Correct solution
先选择放球的盒子，不相邻组合方案数为$\binom{m - n + 1}{n}$； 再决定盒子中小球数量，相当于$x_1 + x_2 + \cdots + x_n = r - nk$的非负整数解，方案数为$\binom{r - nk + n - 1}{n - 1}$。 因此总的方案数即为$\binom{m - n + 1}{n} \binom{r - nk + n - 1}{n - 1}$。
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 得到不相邻组合方案数 | 5 | 5 | 学生的答案中，选择不相邻盒子的方案是用插空法解决的，表达式中写为 $C_{m-n+1}^n$，与标准答案中的 $\binom{m - n + 1}{n}$ 是一致的。虽然学生在写法上使用了 $C$ 和 $A$ 符号，但是核心思路和计算结果是正确的，得到了相同的组合数。因此，在该评分规则下，学生可以得到满分。 |
| 得到小球数量分配的方案数 | 4 | 2 | 学生在解答中将问题分为两部分处理。第一部分是选择放球的盒子，即选择$n$个不相邻的盒子，学生正确使用了插空法，得到选择盒子的方案数为$C_{m-n+1}^n$，这一部分没有问题。第二部分是分配小球的问题。学生给出$ x_1 + x_2 + \cdots + x_n = r $且$x_i \ge k$的条件后，通过令$y_i = x_i - k$转化为$y_1 + y_2 + \cdots + y_n = r - nk$，这一步也正确，且正确地应用了非负整数解公式，即$C^{r - nk}_{n + r - nk - 1}$，但在后面的步骤中，学生错误地给出了组合数公式中的两个参数，且没有符合标准答案中正确的形式$ \binom{r - nk + n - 1}{n - 1}$，而是给出了错误的$C^{r - nk}_{n + r - nk - 1}$。此外，学生答案中的$A^n_n$部分并不合适，似乎是理解上的混淆。总体来说，学生在第二部分关于小球数量的分配上虽然有部分思路正确，但表达和公式上存在明显错误。 |
| 乘法原理得到答案 | 1 | 1 | 学生的解答首先考虑选择不相邻的盒子，利用插空法得到选法是 $C_{m-n+1}^n$，这一部分是正确的。接着，学生使用了变量替换法，将 $x_i \geq k$ 转化为 $y_i \geq 0$，并推导出非负整数解的数目为 $C^{r-nk}_{n+r-nk-1}$，这一部分虽然推导有误，但结果的形式是正确的，只是学生误用了 $C$ 代替了正确的二项式符号 $\binom{}{}$。最终结果中的公式形式与标准答案有差异，并且学生多用了一个无关的 $A^n_n$ 项，这部分不影响方案数的正确性，但公式表示不完全正确。总体来说，学生虽然有一些符号和表达上的错误，但基本思路符合标准解法，因此可以部分得分。 |


## Problem 1.34
### Subproblem (1)
#### Status
graded
#### Answer
首先考虑这$n$个字母的多重全排列为: \[ \frac{n!}{\Pi_{k=1}^{26}(a_k!)} \] 当存在超过1个$k\in[26]$, $a_k$为奇数时，此时一定无法出现回文串，此时所有合法字符串为: \[ \frac{n!}{\Pi_{k=1}^{26}(a_k!)} \] 当有且仅有1个$k\in[26]$, $a_{k}$为奇数时，不失一般性，考虑$a_1$为奇数，此时回文串的数量为$(a_1-1)/2$个a以及$a_k/2$个第$k$个字母的多重全排列($k\neq 1$), 为： \[ \frac{((n-1)/2)!}{((a_1-1)/2)!\cdot \Pi_{k=2}^{26}(a_k/2)!} \] 合法的数量即为： \[ \frac{n!}{\Pi_{k=1}^{26}a_k!} - \frac{((n-1)/2)!}{((a_1-1)/2)!\cdot \Pi_{k=2}^{26}(a_k/2)!} \] 最后考虑所有$a_k$均为偶数，此时回文串的数量为： \[ \frac{(n/2)!}{\Pi_{k=1}^{26} (a_k/2)!} \] 剩余合法数量为： \[ \frac{n!}{\Pi_{k=1}^{26}a_k!} - \frac{(n/2)!}{\Pi_{k=1}^{26} (a_k/2)!} \]
#### Matched solution ID
0
#### Correct solution
分类讨论： % \begin{itemize} \item 若有两个或以上$a_i$为奇数，则无论如何不可能构造出回文串，答案为$\binom{n}{a_1 \; a_2 \; \cdots a_{26}}$； \item 若仅$a_k$为奇数，则要构成回文串必须是字母$k$位于中央，其两侧字符串互为逆序； 去除这种情况后，答案为$\binom{n}{a_1 \; a_2 \; \cdots a_k} - \binom{(n-1)/2}{a_1/2 \; a_2/2 \; \cdots \; (a_k-1)/2 \; \cdots a_{26}/2}$； \item 若全为偶数，则要构成回文串必须是前一半、后一半字符串互为逆序； 去除这种情况后，答案为$\binom{n}{a_1 \; a_2 \; \cdots a_k} - \binom{n/2}{a_1/2 \; a_2/2 \; \cdots a_{26}/2}$。 \end{itemize}
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 得到总回文串数量 | 1 | 1 | 学生答案中给出的回文串数量计算公式与标准答案类似。学生正确地推导了回文串的计算方法，并在三种情况（多个奇数、一个奇数、全偶数）下分别给出了回文串的数量公式。尽管具体的数学表达式与标准答案略有差异，但本质上是正确的，能够得出回文串数量并通过减去得到非回文串数量。尤其是，对于每种情况，学生都考虑了合理的排列公式并给出了相应的处理方式。根据评分标准，学生在这部分的计算是正确的，因此得分。 |
| 多余一个奇数的情况正确 | 3 | 3 | 学生在处理多余一个奇数的情况时，给出的结论是：'当存在超过1个k∈[26], a_k为奇数时，此时一定无法出现回文串，此时所有合法字符串为: \[ \frac{n!}{\Pi_{k=1}^{26}(a_k!)} \]'。这与标准答案中的说法相符，标准答案中指出，若有两个或以上a_i为奇数，则无论如何不可能构造出回文串，答案为 \[ \binom{n}{a_1 \; a_2 \; \cdots a_{26}} \]。因此，学生在这部分的处理是正确的。 |
| 恰好一个奇数的情况正确 | 3 | 3 | 学生在答案中正确描述了当有且仅有1个奇数的情况时的回文串构造方式，并给出了合法字符串的数量公式。特别地，学生的公式中正确地考虑了回文串的排列数和剩余合法字符串数目： \n 1. 回文串的数量计算为 $(a_1-1)/2$个字母的排列和其他字母的多重全排列。\n 2. 合法字符串的数量为总的排列数减去回文串的数量。\n 因此，学生在这一部分的解答符合评分规则要求，得分为3分。 |
| 全为偶数的情况正确 | 3 | 3 | 学生答案中提到，如果所有$a_k$均为偶数，则回文串的数量为$\frac{(n/2)!}{\Pi_{k=1}^{26} (a_k/2)!}$，这个公式是正确的。并且学生也提到，剩余合法数量为$\frac{n!}{\Pi_{k=1}^{26} a_k!} - \frac{(n/2)!}{\Pi_{k=1}^{26} (a_k/2)!}$，这个表达式也符合标准答案中的要求。由于学生正确地处理了全为偶数的情况，因此得分3分。 |


## Problem 1.35
### Subproblem (1)
#### Status
graded
#### Answer
考虑8个角的全排列，并且每个角可以旋转3次，共有$8!\cdot 3^8$种组合。考虑12个棱的全排列，每个棱可以转2次，共有$12!\cdot 2^{12}$种组合，故合法状态共有： \[ \frac{8!\cdot 12!\cdot 2^{12}\cdot 3^8}{12}. \]
#### Matched solution ID
0
#### Correct solution
固定魔方，拆下其所有角块（$8$个）与棱块（$12$个），然后逐个拼回。 角块和棱块的位置有$8! \dotp 12!$种情况，每个角块有$3$个角度，每个棱块有$2$个角度，因此共计$8! \dotp 12! \dotp 3^8 \dotp 2^{12}$。 除以$12$即得$12! \dotp 8! \dotp 3^7 \dotp 2^{10}$。
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 注意到一个三阶魔方共有8个角块和12个棱块 | 2 | 2 | 学生答案提到三阶魔方的角块有8个和棱块有12个，这与标准答案一致。因此，在这一评分规则下，学生正确地注意到了魔方的角块和棱块数量。 |
| 每个棱块有2个方向 | 1 | 1 | 标准答案中指出每个棱块有2个方向，因此在计算中应有$2^{12}$。学生答案中也正确地提到每个棱块有2个方向，并将其考虑在内，即$12! \cdot 2^{12}$，这一部分完全符合要求。 |
| 每个角块有3个方向 | 1 | 1 | 学生在答案中正确考虑了每个角块有3个方向（旋转方式），即将每个角块有3个旋转状态（$3^8$）的因素包含在内，符合评分标准中要求的每个角块有3个方向，因此可以获得此分值。 |
| 得到有重总状态数 | 4 | 4 | 学生在答案中提到考虑了角块和棱块的位置及旋转状态，分别有8!·3^8和12!·2^12种组合，这是正确的。学生最终将这两部分的组合数相乘，并且给出了最终除以12的结果（与标准答案一致）。学生的答案表达了正确的计算过程，虽然排列次序不同，但没有影响最终结果的正确性。因此，符合规则要求，得分为4。 |
| 除以12得到答案 | 2 | 2 | 学生答案中提到的计算公式与标准答案非常相似，但缺少了标准答案中的部分内容。标准答案明确提到角块和棱块位置的计算分别为$8! \cdot 12!$，角块有$3^8$个旋转状态，棱块有$2^{12}$个旋转状态。学生答案确实使用了角块和棱块的位置排列（$8!$和$12!$）以及旋转方式（$3^8$和$2^{12}$），并且在最后正确地进行了除以12的操作。因此，学生答案的计算过程符合标准答案的结构，最终公式也符合，但缺少了标准答案中的详细步骤和解释。 |


## Problem 1.36
### Subproblem (1)
#### Status
graded
#### Answer
\subsection{(1)} 设$A,B,C,D$每个选项各有$x_1,x_2,x_3,x_4$个人选，则： \[ x_1 + x_2 + x_3 + x_4 = 147 \] 此时共可能有$C^{147}_{150}=551300$种结果。
#### Matched solution ID
0
#### Correct solution
\item $A + B + C + D = 147$的非负整数解数目，为$\binom{150}{3}$；
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 正确 | 3 | 0 | 学生答案中表示每个选项的选择人数为 $x_1, x_2, x_3, x_4$，并列出了方程 $x_1 + x_2 + x_3 + x_4 = 147$，这与标准答案中的方程是相符的。然而，学生计算结果时使用了组合数 $C^{147}_{150}$，这个形式不符合题目要求。正确的公式应该是计算组合数 $\binom{150}{3}$，而学生使用了错误的组合数表示形式 $C^{147}_{150}$，并给出了错误的数值结果 551300。由于学生公式错误，得分为 0。 |


### Subproblem (2)
#### Status
graded
#### Answer
\subsection{(2)} 假设有$k$位同学作答，结合题1.28证明的公式，结果为： \[ \sum_{k=0}^{147} C^{k}_{k+3} = \sum_{k=0}^{147} C^{3}_{k+3} = C_{151}^4 = 20811575 \]
#### Matched solution ID
0
#### Correct solution
\item 让没有回答的同学都去选$E$选项，相当于$A + B + C + D + E = 147$的非负整数解数目，为$\binom{151}{4}$；
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 正确 | 3 | 0 | 学生的解答涉及到了求解一个非负整数解的问题，但在公式应用和表达上有误。标准答案中提到的问题是要求解$A + B + C + D + E = 147$的非负整数解数目，应该使用组合数公式$\binom{151}{4}$。而学生使用了一个不同的形式，$\sum_{k=0}^{147} C^{k}_{k+3}$，并最终得出一个结果$20811575$，这个结果与标准答案不符。学生的推导过程存在错误，因此没有满足评分规则中的正确性要求。 |


### Subproblem (3)
#### Status
graded
#### Answer
\subsection{(3)} 由题意得，若此题算分,则$k$为奇数时$x_3 \ge (k+1)/2$, $k$为偶数时$x_3\ge k/2$, 最终结果为： \[ C^3_3 + C^3_4 + C^3_4 + \cdots + C^3_{76} + C^3_{76} = 1 + 2\cdot \sum_{k'=1}^{76} C^3_{k'+3} = 1 + 2\cdot C_{80}^4 = 3163161 \]
#### Matched solution ID
0
#### Correct solution
\item $74$位同学必须选$C$，相当于$A + B + C + D + E = 73$的非负整数解数目，为$\binom{77}{4}$。
#### Grading rules
| 评分规则 | 分值 | 得分 | 评分过程 |
| --- | --- | --- | --- |
| 正确 | 3 | 0 | 学生的答案中，使用了复杂的符号表达和不正确的计数方法。标准答案要求通过计算非负整数解数目，即通过组合数 \(\binom{77}{4}\) 来解决问题，而学生采用了不相关的组合数公式和不准确的计算，导致得出的答案和标准答案完全不一致。学生的计算过程中，使用了符号和组合数形式不符合题目要求，且最终结果3163161显然与正确答案（\(\binom{77}{4} = 76076\)）相差甚远。因此，学生在这个评分标准下并未得分。 |


## PA Report
### Problem 1.25
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 7 | 10 |
| | | **7** | **10** |
### Problem 1.26
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 5 | 10 |
| | | **5** | **10** |
### Problem 1.27
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 8 | 10 |
| | | **8** | **10** |
### Problem 1.28
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 8 | 10 |
| | | **8** | **10** |
### Problem 1.29
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 3 | 5 |
| (2) | graded | 0 | 5 |
| | | **3** | **10** |
### Problem 1.30
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 10 | 10 |
| | | **10** | **10** |
### Problem 1.31
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 10 | 10 |
| | | **10** | **10** |
### Problem 1.32
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 7 | 10 |
| | | **7** | **10** |
### Problem 1.33
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 8 | 10 |
| | | **8** | **10** |
### Problem 1.34
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 10 | 10 |
| | | **10** | **10** |
### Problem 1.35
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 10 | 10 |
| | | **10** | **10** |
### Problem 1.36
| Subproblem | Status | Score | Total |
| --- | --- | --- | --- |
| (1) | graded | 0 | 3 |
| (2) | graded | 0 | 3 |
| (3) | graded | 0 | 3 |
| | | **0** | **9** |
## Total
| Score | Total |
| --- | --- |
| 86 | 119 |
