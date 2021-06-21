def solution(lottos, win_nums):
    answer = []
    zero = lottos.count(0)
    count = 0
    
    for i in lottos:
        if i in win_nums:
            count += 1

    answer = [7-count-zero, 7-count]       

    if (7-count) > 6 :
        answer[1] = 6
        
    if (7-count-zero) > 6 :
        answer[0] = 6

    return answer

lottos = [44, 1, 0, 0, 31, 25]	
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))