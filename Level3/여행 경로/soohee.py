from collections import defaultdict
def solution(tickets):

    answer = []
    path = defaultdict(list)
    
    for ticket in tickets:
        path[ticket[0]].append(ticket[1])
    
    for i in path.keys():
        path[i].sort(reverse=True)
    
    stack = ["ICN"]
    while stack:
        top = stack[-1]
        if not path[top]:
            answer.append(stack.pop())
        else:
            stack.append(path[top].pop())
    
    answer.reverse()
    return answer

print(solution( [["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]]))
