def solution(cap, n, deliveries, pickups):
    distance = 0
    sum_del = sum(deliveries)
    sum_pic = sum(pickups)
    p_n = d_n = n-1
    while sum_del != 0 or sum_pic != 0:
        d_box = 0
        d_flag = 0
        d_dist = 0   
        for d in range(d_n, -1, -1):
            # 더 담을 수 있는 상태.
            if d_box < cap:
                if deliveries[d] == 0:
                    continue

                if deliveries[d] + d_box > cap:
                    sum_del -= (cap-d_box)
                    deliveries[d] -= (cap-d_box)
                    d_box = cap             
                else:
                    sum_del -= deliveries[d]
                    d_box += deliveries[d]  
                    deliveries[d] = 0
                      
                if d_flag == 0:
                    d_dist += d+1
                    d_flag = 1
            else:
                d_n = d+1
                break
        
        p_box = 0
        p_flag = 0
        p_dist = 0
        for d in range(p_n, -1, -1):
            if p_box < cap:
                if pickups[d] == 0:
                    continue
                
                if pickups[d] + p_box > cap:
                    sum_pic -= (cap-p_box)
                    pickups[d] -= (cap-p_box)
                    p_box = cap             
                else:
                    sum_pic -= pickups[d]
                    p_box += pickups[d]  
                    pickups[d] = 0  
                
                if p_flag == 0:
                    p_dist += d+1
                    p_flag = 1
            else:
                p_n = d+1
                break
        
        if d_dist > p_dist:
            distance += d_dist * 2
        else:
            distance += p_dist * 2

    return distance

print(solution(4,5,	[1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
