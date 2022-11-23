from collections import deque
def solution(queue1, queue2):
    count = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    limit = len(q1) * 4

    if (sum1+sum2) % 2 != 0:
        return -1

    while sum1 != sum2:
        count += 1
        if sum1 > sum2:
            num = q1.popleft()
            q2.append(num)
            sum1 -= num
            sum2 += num
        elif sum1 < sum2:
            q1.append(q2.popleft())
            sum1 += num
            sum2 -= num

        if count > limit:
            return -1
    return count

print(solution([3,2,7,2],[4,6,5,1]))
    
