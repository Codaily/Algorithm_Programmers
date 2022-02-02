# def solution(s):
#     s = list(s)
#     i = 0
#     while s:
#         if i == len(s) -1:
#             break
#         elif (s[i] == s[i+1]):
#             s.pop(i)
#             s.pop(i)
#             i = 0
#         else:
#             i += 1
#     if len(s) == 0:
#         return 1
#     else:
#         return 0

def solution(s):
    stack = []
    for i in s:
        if stack:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    if stack:
        return 0
    else:
        return 1

print(solution("baabaa"))