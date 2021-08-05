def solution(s):
    s = s.split(" ")
    for i in range(len(s)):
        if s[i] != "":
            if  s[i][0].isalpha():
                s[i] = s[i][0].upper() + s[i][1:].lower()
    return " ".join(s)

print(solution("2v 3hello m y friend 23HIz"))