# def solution(s):
#     changeCnt = 0
#     zeroCnt = 0
#     while s != "1":
#         changeCnt += 1
#         tmp = ""
#         for i in s:
#             if i == "1" : 
#                 tmp += i
#             else :
#                 zeroCnt += 1
#         s = format(len(tmp),'b') 
        
#     return [changeCnt, zeroCnt]

def solution(s):
    changeCnt = 0
    zeroCnt = 0
    while s != "1":
        changeCnt += 1 
        zeroCnt +=  s.count('0')
        s = format (len(s) - s.count('0'), 'b')
        
    return [changeCnt, zeroCnt]

print(solution("110010101001"))