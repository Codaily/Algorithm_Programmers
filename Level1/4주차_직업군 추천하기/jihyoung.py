def solution(table, languages, preference):
    answer = {}
    for i in range (0, len(table)):

        temp = table[i].split()
        sum = 0

        for j in range(0, len(languages)):
            try :
                score = 6 - temp.index(languages[j])
            except:
                score = 0
            sum += score * preference[j]
        answer[temp[0]] = sum
        
    return sorted([k for k,v in answer.items() if max(answer.values()) == v])[0]





def solution2(table, languages, preference):
    answer = {}
    
    for i in range (0, len(table)):

        temp = table[i].split()
        length = len(temp)
        sum = 0
        for j in range(0, len(languages)):
            try :
                score = length - temp.index(languages[j])
            except:
                score = 0
            sum += score * preference[j]

        answer[temp[0]] = sum

    sortedValue = (sorted(answer.items(), key = lambda item: item[1], reverse = True))

    maxList = []
    for key, value in sortedValue:
        if value == sortedValue[0][1]:
            maxList.append(key)
        else:
            break
        
    return sorted(maxList)[0]



table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]

print(solution(table, languages, preference))