import math
def solution(fees, records):
    answer = []
    dict = {}
    for rec in records:
        info = rec.split(" ")
        carNum = info[1]
        time = info[0].split(":")

        if carNum in dict:
            dict[carNum] += [[info[2], int(time[0]), int(time[1])]]
        else:
            dict[carNum] = [[info[2], int(time[0]), int(time[1])]]
    
    dict = sorted(dict.items())
    
    for d in dict:
        time = 0
        record = d[1]
        if len(record) % 2 != 0:
            record += [['OUT', 23,59]]
        for i in range(0,len(record)-1,2):
            time += ((record[i+1][1]  - record[i][1] ) * 60 + record[i+1][2] - record[i][2])
        realTime = time-fees[0]
        if realTime <= 0:
            answer.append(fees[1])
        else:
            answer.append(fees[1]+ math.ceil(realTime/fees[2]) *fees[3])
    return answer

print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
