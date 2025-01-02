def pearson_correlation(x, y):
    print(x,y)
    """
    计算两个变量的皮尔逊相关系数
    :param x: 第一个变量的列表或数组
    :param y: 第二个变量的列表或数组
    :return: 皮尔逊相关系数
    """
    # 检查输入长度是否一致
    if len(x) != len(y):
        raise ValueError("两个输入数组长度必须相等")

    # 计算均值
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)

    # 计算分子和分母
    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denominator_x = sum((xi - mean_x) ** 2 for xi in x)
    denominator_y = sum((yi - mean_y) ** 2 for yi in y)

    # 避免分母为零
    denominator = (denominator_x * denominator_y) ** 0.5
    if denominator == 0:
        raise ValueError("分母为零，无法计算相关系数")

    res=numerator / denominator
    print(res)
    return numerator / denominator




concern=['gpt-4o-mini','chatglm-4-air','deepseek-chat']
score=[[116, 14, 85], [115, 23, 94], [130, 36, 127]]

mx=-99999999
res=[]
for w1 in range(0,100,1):
    for w2 in range(0,100,1):
        w3=100-w1-w2
        if w3<0:
            continue
        w=[w1/100,w2/100,w3/100]
        G=[0,0,0]
        for i in range(3):
            for j in range(3):
                G[i]+=score[i][j]*w[j]
        pearson=pearson_correlation(w,G)
        if pearson>mx:
            mx=pearson
            res=w

print("max pearson ",mx)
for id,model in enumerate(concern):
    print(model,res[id])