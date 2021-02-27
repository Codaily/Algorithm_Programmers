def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1, arr2):
        b1 = int(format(i,"b"))
        b2 = int(format(j,"b"))
        answer.append(str(b1+b2).zfill(n))
    
    ans = []
    sharp=''
    for k in answer:
        for l in k:
            if int(l) > 0 :
                sharp += '#'
            else: 
                sharp += ' '
        ans.append(sharp)
        sharp = ''
    return ans
print(solution(5,[0 ,0, 0, 0, 0],[30, 1, 21, 17, 28]))




