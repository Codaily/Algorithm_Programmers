import heapq
def solution(n, k, enemy):
    answer = 0
    sum = 0
    fight = []
    if k >= len(enemy):
        return len(enemy)
    
    for i in enemy:
        heapq.heappush(fight, -i)
        print(fight)
        sum += i
        if n < sum:
            if k <= 0: 
                break
            sum += heapq.heappop(fight)
            k -= 1            

        answer += 1
    
    return answer
