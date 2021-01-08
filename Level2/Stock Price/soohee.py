def solution(prices):

    answer = []
    stack = [0]
    length = len(prices)

    for i in range(1, length):
        cnt = 0
        while stack:
            
            index = stack[-1]

            if prices[index] > prices[i]: # 떨어질때 
                answer.append(i - index)
                stack.pop()
                cnt += 1

            else:
                answer.append(length-i-cnt) # 떨어지지 않을때, 
                if i ==length -1:
                   answer.append(0)
                break

        stack.append(i)
    return answer

solution([1,2,3,2,3])
solution([4,3,2,1,2,3])
# [1, 1, 1, 2, 1, 0]
# [1, 1, 1, 2, 0]