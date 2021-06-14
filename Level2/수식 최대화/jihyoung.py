def calculation (operation, index, expression):
    if expression.isdigit(): # 모두 숫자일 경우
        return str(expression)
    else:
        if operation[index] == '*':
            splitExp = expression.split('*')
            temp = []
            for i in splitExp:
                temp.append(calculation(operation, index+1, i))
            return str(eval("*".join(temp)))
        if operation[index] == '+':
            splitExp = expression.split('+')
            temp = []
            for i in splitExp:
                temp.append(calculation(operation, index+1, i))
            return str(eval("+".join(temp)))
        if operation[index] == '-':
            splitExp = expression.split('-')
            temp = []
            for i in splitExp:
                temp.append(calculation(operation, index+1, i))
            return str(eval("-".join(temp)))

def solution(expression):
    answer = 0
    # 연산 순서 정의
    operations = [('*', '+', '-'),
                  ('*', '-', '+'),
                  ('+', '-', '*'),
                  ('+', '*', '-'),
                  ('-', '*', '+'),
                  ('-', '+', '*')]
    
    for oper in operations:
        calResult = abs(int(calculation(oper, 0, expression)))
        if calResult > answer:
            answer = calResult
    
    return answer

print(solution("100-200*300-500+20"))