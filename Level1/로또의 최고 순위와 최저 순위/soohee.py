def solution(lottos, win_nums):
    cnt = 0
    for l in lottos:
        if l in win_nums:
            cnt += 1 
    answer = [7-lottos.count(0)-cnt, (7-cnt if cnt !=0 else 6)]
    return answer if cnt != 0 or lottos.count(0) != 0 else [6,6]
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))