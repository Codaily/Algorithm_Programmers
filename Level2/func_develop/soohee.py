import math
def solution(progresses, speeds):
    clear = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
   
    num = clear[0]
    answer = []
    while(len(clear)>0):
        cnt = 0
        for i in range(len(clear)):
            if num >= clear[i]:
                cnt += 1
                if len(clear)==i+1:
                     answer.append(cnt)
                     del clear[:i+1]
                
            else:
                answer.append(cnt)
                num = clear[i]
                del clear[:i]
                break

    print(answer)
    return answer

#solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])
solution([93, 30, 55],[1, 30, 5])