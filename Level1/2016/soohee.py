def solution(a, b):
    sum = 0
    day = [31,29,31,30,31,30,31,31,30,31,30,31]
    date = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    for i in range(a-1):
        sum += day[i]
    return date[(sum+b)%7 -1]
