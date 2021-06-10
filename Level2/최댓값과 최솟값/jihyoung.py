def solution(s):
    s = list(map(int,s.split()))
    print(s)
    return str(min(s)) + " " + str(max(s))


# def solution(s):
#     answer = ''
#     s = s.split(' ')
#     index = 0 
#     for i in s:
#         s[index] = int(i)
#         index += 1
#     answer += str(min(s)) + ' '
#     answer += str(max(s))
#     return answer

s = "-1 -2 -3 -4"
print(solution(s))
