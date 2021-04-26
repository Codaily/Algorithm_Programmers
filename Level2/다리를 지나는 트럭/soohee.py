def solution(bridge_length, weight, truck_weights):
    seconds = 0
    cnt = [0] * bridge_length
    Cross_truck = []
    Passed_truck = []
    n = len(truck_weights)
    while len(Passed_truck) < n :
        seconds += 1
        if len(truck_weights) > 0 and truck_weights[0] + sum(Cross_truck) <= weight :
            Cross_truck.append(truck_weights.pop(0))
            cnt.append(0)

        if cnt[0] == bridge_length:
            Passed_truck.append(Cross_truck.pop(0))
            cnt.pop(0)
        cnt = [i+1  for i in cnt]

    return seconds



#print(solution(3,100,[10,20,30,40,50]))  #10
print(solution(2,10,[7,4,5,6])) #10
#print(solution(100,100,[10]))