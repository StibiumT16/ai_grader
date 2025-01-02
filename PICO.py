import json
import os
import random
from LLM.apillm import APILLM

# models: ['wenxin', 'chatglm-4-air', 'claude-3-sonnet', 'gpt-3.5-turbo', 'gpt-4o-mini', 'gpt-4']



def pearson_correlation(x, y):
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

    return numerator / denominator

def load_json(path):
    with open(path,"r") as f:
        return json.load(f)

def load_jsonl(path):
    # print("load_jsonl",path)
    # if path=='ai_grader/pointwise/3.1.json':
    #     return
    cases=[]
    with open(path,'r',encoding='utf-8') as f:
        for line in f:
            case = json.loads(line)
            cases.append(case)
    return cases

def load_answer():
    id_to_answer={}
    item_id_to_homework={}
    path='./data/ai_judge_dist'
    problems=os.listdir(path)
    for p in problems:
        if os.path.isfile(os.path.join(path,p)):
            continue
        dir=os.path.join(path,p,'ref_answers')
        tmp=os.listdir(dir)
        
        if len(tmp)==1:
            jsonfile=tmp[0]
        else:
            for s in tmp:
                t=s.split(".")[-1]
                if t=='json':
                    jsonfile=s
                    break
        print(os.path.join(dir,jsonfile))
        dict=load_json(os.path.join(dir,jsonfile))
        for k,v in dict.items():
            id_to_answer.update({k:v})
            
        dir=os.path.join(path,p,'testcases')
        tmp=os.listdir(dir)
        for jf in tmp:
            type=jf.split(".")[-1]
            if type !='json':
                continue
            dict=load_json(os.path.join(dir,jf))
            uid=jf[:-5].split('-')[-1]
            
            
            for pid,v in dict.items():
                # print("pid and uid",pid,uid)
                if pid not in item_id_to_homework:    
                    item_id_to_homework.update({pid:{}})
                item_id_to_homework[pid].update({uid:v})

    print(item_id_to_homework['1.26'].keys())
    return id_to_answer,item_id_to_homework

def refine(dict):
    yes=0
    no=0
    for lst in dict['correctness']:
        correct_or_not=lst[0]
        if correct_or_not<1:
            no+=1
        else:
            yes+=1
    mx=-1
    res=None
    for corr,response,score in zip(dict['correctness'],dict['responses'],dict['scores']):
        correct_or_not=corr[0]
        if yes>=2 and correct_or_not<1:
            continue
        if no>=2 and correct_or_not==1:
            continue
        if mx<sum(score):
            mx=sum(score)
            res={"score":mx,"reason":str(response)+"\n"+corr[-1]}
    return res

def str_to_float(s):
    try:
        return float(s)
    except ValueError:
        return 0

if __name__=="__main__":
    
    random.seed(1023)
    models=[APILLM(model='gpt-4o-mini'),APILLM(model='chatglm-4-air'),APILLM(model='deepseek-chat')]
    concern=['gpt-4o-mini','chatglm-4-air','deepseek-chat']
    # print(models[1].generate("你是一个AI助手","冬至应该吃什么"))
    # respons=llm.generate("你是一个AI助手","冬至应该吃什么")
    # print(response)
    id_to_answer,item_id_to_homework=load_answer()
    root_path='./pointwise'
    files=os.listdir(root_path)
    
    item_list=[]
    item_info={}
    model_item_uid={name:{} for name in concern}
    for name in files:
        ppp=os.path.join(root_path,name)
        if ppp=='./pointwise/3.1.json' or ppp=='./pointwise/3.3.json' or ppp=='./pointwise/3.2.json':
            continue
        cases=load_jsonl(ppp)
        sub_count=0
        uid_list=[]
        # for case in cases:  
        #     if case['model'] not in concern:
        #         continue
        #     for k,v in case.items():
        #         if k=='uid' or k=='model': 
        #             continue 
        #         model_item_uid[case['model']].update({name+"#"+k:{}})
            
        for case in cases:  
            if case['model'] not in concern:
                continue
            uid_list.append(case["uid"])
            sub_count=len(case.keys())-2  
            for k,v in case.items():
                if k=='uid' or k=='model': 
                    continue
                
                if name+"#"+k not in model_item_uid[case['model']]:
                    model_item_uid[case['model']].update({name+"#"+k:{}})
                model_item_uid[case['model']][name+"#"+k].update({case['uid']:refine(v)})
        for id in range(1,sub_count+1):
            item_list.append(name+"#"+'('+str(id)+')')
        
        uid_list=list(set(uid_list))
        item_info.update({name:{"sub_count":sub_count,"uid_list":uid_list}})
    
    compare=[(0,1),(0,2),(1,2)]
    random.shuffle(item_list)
    
    tot=48
    AtoBscores=[[95, 11, 66], [93, 21, 75], [104, 31, 103]]
    for cnt,item in enumerate(item_list):
        if cnt<=72:
            continue
        with open('log.txt', 'a') as file:
            file.write("cnt "+str(cnt)+" tot "+str(tot)+" scores "+str(AtoBscores)+"\n")
        print("cnt:",cnt,"tot",tot,"scores",AtoBscores)
        tmp=item.split("#")
        problem=tmp[0]
        sub_problem=tmp[1]
        uid=random.randint(0, len(item_info[problem]['uid_list'])-1)
        uid=item_info[problem]['uid_list'][uid]
        
        model_response=[]
        for model_name in concern:
            model_response.append(model_item_uid[model_name][item][uid])
        
        problem=problem[:-5] #删掉.json后缀
        answer=id_to_answer[problem]
        ques=answer['problem']
        ans=answer['answers'][sub_problem]
        
        print(problem,sub_problem,uid)
        homework=item_id_to_homework[problem][str(uid)][sub_problem]
        
        tot_score=0
        before=AtoBscores
        
        for id,model in enumerate(models):
            for j,A in enumerate(model_response):
                for k,B in enumerate(model_response):
                    if j==k:
                        continue
                    # print(ques,ans,homework,A,bin)
                    score=model.generate(
                        "你是一个组合数学方面的专家。请根据学生的作答，标准答案，以及A老师和B老师的评阅结果，决定A老师和B老师谁判的更准确。",
                        "题目："+str(ques)+"答案："+str(ans)+"学生的答案："+str(homework)+"老师A的评阅结果："+str(A)+"老师B的评阅结果："+str(B)+"\n 如果你认为A老师评阅得好，那么返回1；否则返回0. 请直接返回0或者1，不要说多余的话。"
                    )
                    score=str_to_float(score)
                    if score==1:
                        tot_score+=1
                        AtoBscores[j][id]+=1
        if tot_score<=5: #3*6次比较，按理说有9个1分，9个0分比较理想。如果分数小于等于5，就不管这个sample了
            AtoBscores=before
            continue
        else:
            tot+=1
        
        if tot==200:
            break
    with open('pairwise_res.json', 'w') as file:
        json.dump(AtoBscores, file)
