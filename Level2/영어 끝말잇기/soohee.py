def solution(n, words):
    turn = [1] * n
    for idx, w in enumerate(words):
        if words[idx] in words[:idx]:
            return [idx%n+1, turn[idx%n]]
        
        try:
            if w[-1] == (words[idx+1])[0]:
                turn[idx%n] += 1
            else:
                return [(idx+1)%n+1, turn[(idx+1)%n]]
        except IndexError:
            return [0,0]
    
    return [0,0]

#print(solution(3,	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(2,	["hello", "one", "even", "never", "now", "world", "draw"]))
# 끝말잇기 조건
# 1. 앞사람의 끝단어와 다르면 실패
# 2. 나왔던 단어가 또 나와도 실패
# 3. 모두 다 없으면 성공.