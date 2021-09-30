def solution(table, languages, preference):
    dict = {}
    for init in table:
        init = init.split() 
        dict[init[0]] = []
    for l in languages:
        for  t in table:
            t = t.split()
            if l in t:
                dict[t[0]] += [6 - t.index(l)]
            else: 
                dict[t[0]] += [0]

    for dKey, dVal in dict.items():
        sum = 0
        for p in range(len(preference)):
            sum += dVal[p] * preference[p]
        dict[dKey] = sum
    return sorted([k for k,v in dict.items() if max(dict.values()) == v])[0]


print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],["JAVA", "JAVASCRIPT"],[7, 5]))

## 뭔가 매우 깔끔하고 좋아보이는 코드..

# def solution(table, languages, preference):
#     def job(row):
#         return row.split()[0]

#     def scores(row):
#         return {lang: 5 - i for i, lang in enumerate(row.split()[1:])}

#     def total(job):
#         def score(job, lang):
#             return jobs[job][lang] if lang in jobs[job] else 0        
#         return -sum(score(job, lang) * pref for lang, pref in zip(languages, preference))

#     jobs = {job(row): scores(row) for row in table}
#     return sorted((total(job), job) for job in jobs.keys())[0][1]