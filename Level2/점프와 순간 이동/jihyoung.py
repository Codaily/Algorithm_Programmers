def solution(n):
    ans = 0
    while n > 0:
        mok, left = divmod(n, 2)
        n = mok
        if left != 0:
            ans += 1
        print(mok, left)

    return ans

print(solution(5000))