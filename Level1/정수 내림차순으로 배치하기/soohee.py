def solution(n):
    arr = [i for i in str(n)]
    return int("".join(sorted(arr,reverse=True)))
