def solution(n):
    answer = ''
    while n > 0:
        n, rest = divmod(n-1, 3)
        answer += str(rest+1)
    answer = (''.join(reversed(answer))).replace('3','4')
    return answer

#list를 reversed 하면 list로 str을 reversed히먄 객체로
print(solution(9))