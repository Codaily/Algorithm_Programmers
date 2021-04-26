def solution(genres, plays):
    BestAlbum = []
    dict = {}
    PlaysNum = sorted([[i,j] for i, j in enumerate(plays)],key = lambda x : x[1] , reverse =True)
    for g, p in zip(genres, plays):
        if g not in dict:
            dict[g] = [p]
        else:    
            dict[g] += [p]
    dict = sorted(dict.items(), key = lambda x : sum(x[1]) , reverse =True)
    
    
    for i in dict:
        cnt = 0
        for j in PlaysNum:
            if  j[1] in i[1] and cnt<2:
                BestAlbum.append(j[0]) 
                cnt += 1
            elif cnt >=2:
                break

    return BestAlbum

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))