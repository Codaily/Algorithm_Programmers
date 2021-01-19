def solution(name):

    answer = 0
    mov = [min(ord(i)-ord('A'), ord('Z')-ord(i)+1) for i in name]
    answer += sum(mov)

    for i in range(len(name)):
        if name[i]=='A':
            answer -=1
        
    if any(mov):
        answer += len(name) -1
    elif all(mov)==0:
        answer = 0 

   
    print(answer)
    return answer


solution("AAA")
