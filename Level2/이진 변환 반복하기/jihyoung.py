def solution(s):
    
    zero = 0
    count = 0
    
    while True:

        if  s == '1':
            return [count, zero]

        zero += s.count('0')
        s = s.replace('0', '')

        s = format((len(s)), 'b') #bin(len(s))[2:]

        count += 1


s = "01110"
print(solution(s))