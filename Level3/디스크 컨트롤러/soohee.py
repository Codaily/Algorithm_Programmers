import heapq
# def solution(jobs):
#     jobs = sorted(jobs, key = lambda x :x[1])
#     Now = [jobs[0][1]]  
#     for i in range(1,len(jobs)):
#         arr = -jobs[i][0] + jobs[i-1][1] + jobs[i][1]
#         for j in range(i-1):
#             arr += Now[j]
#         Now.append(arr)
#         heapq.heapify(jobs)
#     return sum(Now) // len(Now)

def solution(jobs):
    Now = 0
    cnt = 0
    answer = 0
    heap = []
    while True:
        for j in jobs:
            if j[0] <= Now:
                answer += Now - j[0]
                heapq.heappush(heap,j[1])
        heapq.heappop(jobs)
    print(heap)
    return cnt

print(solution([[0, 3], [1, 9], [2, 6]]))