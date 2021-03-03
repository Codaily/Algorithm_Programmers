def solution(answers):
    answer = []
    num = len(answers)
    stu1 = [i%5+1 for i in range(num) ]
    stu2 = [2,1,2,3,2,4,2,5] * (num//2 )
    stu3 = [3,3,1,1,2,2,4,4,5,5] * (num//2 )
    cnt = [0] * 3
    for i in range(num):
        if answers[i] == stu1[i]:
            cnt[0] += 1
        if answers[i] == stu2[i]:
            cnt[1] += 1
        if answers[i] == stu3[i]:
            cnt[2] += 1

    cntMax = max(cnt)
    for i in range(len(cnt)):
        if cnt[i] == cntMax:
            answer.append(i+1)
    return answer

