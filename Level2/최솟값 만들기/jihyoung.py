# def solution(A,B):
#     answer = 0
#     small = 0
#     big = 0
#     while A:
#         small = min(A)
#         big = max(B)
#         answer += small * big
#         print(big)
#         A.pop(A.index(small))
#         B.pop(B.index(big))

#     return answer

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer


    

A = [1, 4, 2]
B = [5, 4, 4]
print(solution(A, B))