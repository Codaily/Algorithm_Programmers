#첫번째 시도 : 단순 배열 사용 -> for문 너무 많이써서 효율성이 떨어진다!
def solution(clothes):
    answer = 0
    clothes_sort = []
    
    for x, y in clothes:
        clothes_sort.append(y)

    clothes_sort = list(set(clothes_sort))
    clothes_cnt = [0] * len(clothes_sort)

    for i in range (len(clothes_sort)):
        for j in range (len(clothes)):
            if clothes_sort[i] == clothes[j][1]:
                clothes_cnt[i] += 1
    answer = 1
    for k in range(len(clothes_cnt)):
         answer *= (clothes_cnt[k] + 1)

    print(answer-1)    
      
    return answer - 1
