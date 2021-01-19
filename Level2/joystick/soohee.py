def solution(name):

    answer = 0
    change1 = [min(ord(i)-ord('A'), ord('Z')-ord(i)+1) for i in name]
    answer += sum(change1) # 알파벳 바꾸는 거 
    print(change1)
    # ------------------- 이동 하기 ------------------

    cut = change1.index(0)
    change2 = change1[cut:] + change1[:cut]
 
    print(change2)
    return answer


solution("BBBAAAB")
