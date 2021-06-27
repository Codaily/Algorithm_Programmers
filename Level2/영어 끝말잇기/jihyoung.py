import math
def solution(n, words):
    used = []
    for i in range(1, len(words)):
        prev, curr = words[i-1], words[i]
                
        # 사용됐던 단어인지 확인
        if curr in used:
            return [n, math.ceil((i+1) / n)] if ((i+1)%n == 0) else [(i+1)%n, math.ceil((i+1) / n)] 

        # 이어지는 단어인지 확인
        if prev[-1] == curr[0]:
            used.append(prev)
        else:
            return [n, math.ceil((i+1) / n)] if ((i+1)%n == 0) else [(i+1)%n, math.ceil((i+1) / n)] 
        

    return [0, 0]

n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))
