import heapq
def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville) 
    first = heapq.heappop(scoville)
    while first < K:
        if len(scoville) > 0:
            second = heapq.heappop(scoville)
            first = heapq.heappushpop(scoville, first+second*2)
            cnt += 1
        else :
            return -1
    return cnt

print(solution([1,1,100],5))