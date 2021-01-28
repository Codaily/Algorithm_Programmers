import math

def divide(outstart,instart,arrlist): #outstart는 arr안의 array들에서의 순서 시작 (x) , instart는 arr 안의 array 하나 안의 순서 시작 (y)
    dlength = int(len(arrlist)/2)
    newArr = [0] * dlength * dlength
    num = 0

    for i in range(outstart,outstart+dlength):           
        for j in range(instart,instart+dlength):
            newArr[num] = arrlist[i][j]
            num += 1
            
    return newArr

def solution(arr):
    length = int(len(arr))
    cnt0,cnt1 = 0, 0
    outstart, instart = 0, 0
    arrlist= []
    arrlist.append(arr)
    step = 1
    while int(length) > 0 :

        for s in range(step):
            arrlist.append(divide(outstart,instart,arrlist[s]))
            arrlist.append(divide(outstart,int(length /2)+instart,arrlist[s]))
            arrlist.append(divide(int(length /2)+outstart,instart,arrlist[s]))
            arrlist.append(divide(int(length /2)+outstart,int(length /2)+instart,arrlist[s]))

        del arrlist[:step]
        
        for t in range(step):
            for i in range(len(arrlist)):
                if len(set(arrlist[t][i]))==1 :
                    if arrlist[t][i][0] == 1:
                        cnt1 += 1
                    elif arrlist[t][i][0] == 0:
                        cnt0 += 1

        
        print(arrlist)
        length = int(length/2)
        step *= 4

        
          
    print(cnt0, cnt1)
    answer = [cnt0,cnt1]
    return answer

#solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])
solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])