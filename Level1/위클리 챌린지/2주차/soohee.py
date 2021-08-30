def solution(scores):
    answer = ''
    avg = []
    studentCount = len(scores)
    for i in range(studentCount):
        avglist = []
        for j in range(studentCount):
            avglist.append(scores[j][i])
        if ( scores[i][i] == max(avglist) or scores[i][i] == min(avglist)) and avglist.count(scores[i][i]) == 1:
            avglist[i] = 0
            avg.append(sum(avglist)/(studentCount-1))
        else:
            avg.append(sum(avglist)/studentCount)

    for i in range(len(avg)):
        if avg[i] >= 90 : answer += 'A'     
        elif  avg[i] >= 80 and avg[i] < 90 : answer += 'B'
        elif  avg[i] >= 70 and avg[i] < 80 : answer += 'C'
        elif  avg[i] >= 50 and avg[i] < 70 : answer += 'D'
        else : answer += 'F'
    return answer

print(solution([[75, 50, 100], [75, 100, 20], [100, 100, 20]]))