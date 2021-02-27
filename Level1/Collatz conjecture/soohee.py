def solution(num):
    cnt = 0 

    while num != 1 :
        cnt += 1
        num = int (num / 2) if num % 2 == 0 else  (num * 3 + 1)
        if cnt >= 500:
            cnt = -1
            break

    
    return cnt

solution(6)