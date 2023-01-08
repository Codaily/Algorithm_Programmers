def solution(files):
    dict = {}
    for file in files:
        dict[file] = divideName(file)
    
    dict = sorted(dict.items(), key = lambda x:(x[1][0], int(x[1][1])))
    return [k for k, _ in dict]

def divideName(file):
    head = ''
    number = ''
    flag = 0
    for f in file:
        if f.isdigit():
            number += f
            flag = 1
        elif flag == 0:
            head += f.lower()
        else:
            break 
    return [head , number]
