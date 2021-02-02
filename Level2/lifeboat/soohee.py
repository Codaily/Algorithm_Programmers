def solution(people, limit):
    cnt = 0
    people.sort()
    min = 0
    max = len(people)-1

    while min <= max :
        cnt += 1       
        if people[min] + people[max] <=limit: #둘이 나가게 됨
            min += 1
            max -= 1
        else : # max 혼자만 나가게 됨
            max -=1  
    return cnt

solution([30,40,50,60,70,230],100)
# cnt = 4