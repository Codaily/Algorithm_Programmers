def solution(n):
    # return ('수박'*n) [:n] -> 이게 더 느림
    return ('수박'* int(n/2) ) if n % 2 == 0 else ('수박'* int(n/2) ) + '수'