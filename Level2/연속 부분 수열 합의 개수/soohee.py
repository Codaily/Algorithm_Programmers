def solution(elements):
    answer = set()
    length = len(elements)
    elements.extend(elements)
    
    for i in range(length):
        answer.update(getSum(elements, length, i+1))
    return len(answer)

def getSum(elements, length, num):
    sets = set()
    for i in range(length):
        n = sum(elements[i:i+num])
        sets.add(n)
    return sets

print(solution([7,9,1,1,4]))
