def solution(numbers):
    isZero = []
    number = []
    numbers = list(map(str,numbers))
    numbers = sorted(numbers,key =lambda x:x*4 , reverse= True)
    isZero = sum(list(map(int,numbers)))
    return "".join(numbers) if isZero != 0 else '0'

print(solution([0,0,0,0]))