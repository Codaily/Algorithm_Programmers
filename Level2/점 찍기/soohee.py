def solution(k, d):
    answer = 0
    x = 0
    y = d if d%k== 0 else d - d%k
    while x <= d:
        if (x*x + y*y) <= d*d:
            answer += y//k+1
            x += k
        else:
            y -= k
    return answer
