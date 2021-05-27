def solution(record):
    answer = []
    print(record[1][1])
    for i in range(len(record)):
        array = record[i].split(' ')
        answer.append(array)
    
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))