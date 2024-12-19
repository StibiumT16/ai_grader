import re,json

questions = [str(f"1.{id + 25}") for id in range(12)]

def parse1():
    pattern = re.compile(r"\\subsection\{Solution\}.+?\\subsection\{Judgment\}")
    with open('testcases/Ch1-1B-1.tex', encoding='utf-8') as fr:
        file= "".join(fr.readlines()).replace('\n', ' ').replace('\par', '').replace('\begin{equation}', '$').replace('\end{equation}', '$')
        sols = re.findall(pattern, file)
        
    dict = {}
    assert len(questions) == len(sols)
    for qid, sol in zip(questions, sols):
        sol = sol[22:-22]
        dict[qid] = {"(1)":sol}
        
    with open('test/1.json', 'w') as fw:
        json.dump(dict, fw, indent=4,ensure_ascii=False)
    
def parse2():
    pattern = re.compile(r"   1\.[0-9][0-9].+   ")
    with open('testcases/Ch1-1B-2.md', encoding='utf-8') as fr:
        file= "".join(fr.readlines()).replace('\n', ' ').replace('\par', '').replace('\begin{equation}', '$').replace('\end{equation}', '$')
        sols = file.split('   1.')
    sols = [sol[4:] for sol in sols[1:]]

    dict = {}
    assert len(sols) == len(questions)
    for qid, sol in zip(questions, sols): 
        dict[qid] = {"(1)":sol}
    with open('test/2.json', 'w') as fw:
        json.dump(dict, fw, indent=4,ensure_ascii=False)
    
def parse3():
    with open('testcases/Ch1-1B-3.tex', encoding='utf-8') as fr:
        file= "".join(fr.readlines()).replace('\n', ' ').replace('\par', '').replace('\begin{equation}', '$').replace('\end{equation}', '$')
        sols = file.split('\section{1.')[1:]
        
    dict = {}
    assert len(questions) == len(sols)
    for qid, sol in zip(questions, sols):
        sol = sol[4:]
        dict[qid] = {"(1)":sol}
        
    with open('test/3.json', 'w') as fw:
        json.dump(dict, fw, indent=4,ensure_ascii=False)

def parse4():
    with open('testcases/Ch1-1B-4.md', encoding='utf-8') as fr:
        file= "".join(fr.readlines()).replace('\n', ' ').replace('\par', '').replace('\begin{equation}', '$').replace('\end{equation}', '$')
        sols = file.split('## 1.')[1:]
        
    dict = {}
    assert len(questions) == len(sols)
    for qid, sol in zip(questions, sols):
        tmp = {}
        sol = sol[4:].split("###")
        if(len(sol)) > 1: sol = sol[1:]
        for i, sub_sol in enumerate(sol):
            tmp[f"({i+1})"] = sub_sol
        dict[qid] = tmp
        
    with open('test/4.json', 'w') as fw:
        json.dump(dict, fw, indent=4,ensure_ascii=False)    

def parse5():
    
    pattern = re.compile(r"##### 解题过程.+?#####")
    with open('testcases/Ch1-1B-5.md', encoding='utf-8') as fr:
        file= "".join(fr.readlines()).replace('\n', ' ').replace('\par', '').replace('\begin{equation}', '$').replace('\end{equation}', '$')
        sols = re.findall(pattern, file)
        
    dict = {}
    assert len(questions) == len(sols)
    for qid, sol in zip(questions, sols):
        sol = sol[12:-6]
        dict[qid] = {"(1)":sol}
        
    with open('test/5.json', 'w') as fw:
        json.dump(dict, fw, indent=4,ensure_ascii=False)    

def parse6():
    with open('testcases/Ch1-1B-6.md', encoding='utf-8') as fr:
        file= "".join(fr.readlines()).replace('\n', ' ').replace('\par', '').replace('\begin{equation}', '$').replace('\end{equation}', '$')
        sols = file.split('   1.')[1:]
    dict = {}
    assert len(questions) == len(sols)
    for qid, sol in zip(questions, sols):
        dict[qid] = {"(1)":sol[4:]}
        
    with open('test/6.json', 'w') as fw:
        json.dump(dict, fw, indent=4,ensure_ascii=False)  

def parse7():
    with open('testcases/Ch1-1B-7.md', encoding='utf-8') as fr:
        file= "".join(fr.readlines()).replace('\n', ' ').replace('\par', '').replace('\begin{equation}', '$').replace('\end{equation}', '$')
        sols = file.split('> 1.')[1:]
    
    dict = {}
    assert len(questions) == len(sols)
    for qid, sol in zip(questions, sols):
        dict[qid] = {"(1)":sol[4:-2]}
        
    with open('test/7.json', 'w') as fw:
        json.dump(dict, fw, indent=4,ensure_ascii=False)  

def parse8():
    pattern = re.compile(r"\\subsection\{\}.+?评")
    with open('testcases/Ch1-1B-8.tex', encoding='utf-8') as fr:
        file= "".join(fr.readlines()).replace('\n', ' ').replace('\par', '').replace('\begin{equation}', '$').replace('\end{equation}', '$')
        sols = re.findall(pattern, file)
    
    
    dict = {}
    assert len(questions) == len(sols)
    for qid, sol in zip(questions, sols):
        dict[qid] = {"(1)":sol[14:-2]}
        
    with open('test/8.json', 'w') as fw:
        json.dump(dict, fw, indent=4,ensure_ascii=False) 

def parse9():
    pattern = re.compile(r"\\begin\{homeworkProblem\}(.+?)\\end\{homeworkProblem\}")
    with open('testcases/Ch1-1B-9.tex', encoding='utf-8') as fr:
        file= "".join(fr.readlines()).replace('\n', ' ').replace('\par', '').replace('\begin{equation}', '$').replace('\end{equation}', '$').replace('\t','')
        sols = re.findall(pattern, file)
    
    dict = {}
    assert len(questions) == len(sols)
    for qid, sol in zip(questions, sols):
        dict[qid] = {"(1)":sol[8:]}
        
    with open('test/9.json', 'w') as fw:
        json.dump(dict, fw, indent=4,ensure_ascii=False) 

def parse10():
    pattern = re.compile(r"\\begin\{proof\}\[\\textbf\{1\.[0-9][0-9](.+?)\\end\{proof\}")
    with open('testcases/Ch1-1B-10.tex', encoding='utf-8') as fr:
        file= "".join(fr.readlines()).replace('\n', ' ').replace('\par', '').replace('\begin{equation}', '$').replace('\end{equation}', '$').replace('\t','')
        tmps = re.findall(pattern, file)
    
    sols = []
    for it in tmps:
        if it[0] == '}': sols.append(it[7:])
        elif it[0:2] == '(1': sols.append(it)
        else: sols[-1] += it

    dict = {}

    assert len(questions) == len(sols)
    for qid, sol in zip(questions, sols):
        dict[qid] = {"(1)":sol}
        
    with open('test/10.json', 'w') as fw:
        json.dump(dict, fw, indent=4,ensure_ascii=False) 

def parse11():
    with open('testcases/Ch1-1B-11.md', encoding='utf-8') as fr:
        file= "".join(fr.readlines()).replace('\n', ' ').replace('\par', '').replace('\begin{equation}', '$').replace('\end{equation}', '$')
        sols = file.split('## 1.')[1:]
    dict = {}

    assert len(questions) == len(sols)
    for qid, sol in zip(questions, sols):
        if '###' in sol: sol = "".join(sol.split('###')[1:])
        print(sol)
        dict[qid] = {"(1)":sol}
        
    with open('test/11.json', 'w') as fw:
        json.dump(dict, fw, indent=4,ensure_ascii=False) 

def parse13():
    pattern = re.compile(r"【解答】.+?##")
    with open('testcases/Ch1-1B-13.md', encoding='utf-8') as fr:
        file= "".join(fr.readlines()).replace('\n', ' ')
        sols = re.findall(pattern, file)

    dict = {}
    assert len(questions) == len(sols)
    for qid, sol in zip(questions, sols):
        dict[qid] = {"(1)":sol[6:-5]}
        
    with open('test/13.json', 'w') as fw:
        json.dump(dict, fw, indent=4,ensure_ascii=False)
        
def parse14():
    pattern = re.compile(r"`Sol.`(.+?)`评价`")
    with open('testcases/Ch1-1B-14.md', encoding='utf-8') as fr:
        file= "".join(fr.readlines()).replace('\n', ' ')
        sols = re.findall(pattern, file)

    print(sols)
    
    dict = {}
    assert len(questions) == len(sols)
    for qid, sol in zip(questions, sols):
        dict[qid] = {"(1)":sol[1:-1]}
        
    with open('test/14.json', 'w') as fw:
        json.dump(dict, fw, indent=4,ensure_ascii=False)
    

def parse16():
    with open('testcases/Ch1-1B-16.tex', encoding='utf-8') as fr:
        file= "".join(fr.readlines()).replace('\n', ' ')
        sols = file.split('\section*{1.')[1:]

    print(sols)
    
    dict = {}
    assert len(questions) == len(sols)
    for qid, sol in zip(questions, sols):
        dict[qid] = {"(1)":sol[4:-1]}
        
    with open('test/16.json', 'w') as fw:
        json.dump(dict, fw, indent=4,ensure_ascii=False)

parse16()