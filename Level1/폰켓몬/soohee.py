def solution(nums):
    dict = {}
    for i in nums :
        if i not in dict:
            dict[i] = 1
        else :
            dict[i] += 1

    return min(len(list(dict.keys())),len(nums)//2)

print(solution([3,3,3,2,2,4])) 