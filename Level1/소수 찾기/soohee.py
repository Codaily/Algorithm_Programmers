def solution(n):
    # 에라토스테네스의 체 사용
    nlist = set([num for num in range(3, n+1, 2)])
    #짝수는 이미 소수가 아니므로, 3부터 홀수만 찾아서 에라토스테네스의 체에 사용
    for i in range(3, n+1, 2): 
        if i in nlist: # 해당 값의 배수를 전체 값들을 집합에서 없앰
            nlist -= set([i for i in range(i*2, n+1, i)])
    return len(nlist) + 1