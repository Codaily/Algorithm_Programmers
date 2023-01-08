def solution(score):
    dict = {}
    avgs = [sum(s) / 2 for s in score]
    avgss = sorted(avgs, reverse=True)
    for i, avg in enumerate(avgss, start=1):
        if avg not in dict:
            dict[avg] = i
        
    return [dict[a] for a in avgs]
