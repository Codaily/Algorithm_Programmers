# def solution(land):
#     sum = 0
#     check = 0
#     for i, j in enumerate(land):
#         if i == 0:
#             sum += max(j)
#         else:
#             sum += max(land[i][:check]+land[i][check+1:])
#         check = j.index(max(j))

#     return sum

def solution(land):

    for i in range(0,len(land)-1):
        for j in range(4):
            land[i+1][j] += max(land[i][:j] + land[i][j+1:])

    return max(land[-1])

print(solution([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]))