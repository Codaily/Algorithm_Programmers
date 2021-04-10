def solution(number, k):
    numberlist = []
    for i in number:
        while len(numberlist) > 0: 
            if i > numberlist[-1]:
                if k > 0 :
                    k-= 1
                    numberlist.pop()
                else:
                    break
            else : 
                break
        numberlist.append(i)
    
    if k > 0 :
        for i in range(k):
               numberlist.pop() 
    return "".join(numberlist)

print(solution("4177252841",4))