import heapq
def solution(jobs):
    jobs = sorted(jobs, key=lambda x: x[1])  # 소요시간 우선 정렬
    length = len(jobs)
    
    average = 0
    start = 0
    while len(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= start:
                start += jobs[i][1]
                average += start - jobs[i][0]
                jobs.pop(i)
                break
            # 해당시점에 아직 작업이 들어오지 않았으면 시간 ++
            if i == len(jobs) - 1:
                start += 1
        


    return average // length

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))
