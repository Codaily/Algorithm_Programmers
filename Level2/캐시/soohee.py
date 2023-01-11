def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        return 5 * len(cities)
        
    for city in cities:
        c = city.lower()
        if not c in cache:
            if len(cache) < cacheSize:
                cache.append(c)
            else:
                cache.pop(0)
                cache.append(c)
            answer += 5
        else:
            cache.pop(cache.index(c))
            cache.append(c)
            answer += 1
    return answer
