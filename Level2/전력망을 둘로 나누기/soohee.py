def solution(n, wires):
    answer = n
    tree = {k: set() for k in range(1, n + 1)}

    for x, y in wires:
        tree[x].add(y)
        tree[y].add(x)

    for x, y in wires:
        tree[x].remove(y)
        tree[y].remove(x)

        result = abs(n - 2 * bfs(tree, x))
        
        tree[x].add(y)
        tree[y].add(x)
        answer = min(answer, result)
    return answer

def bfs(tree, start_node):

    queue = list()
    visit = list()
    
    queue.append(start_node)
    
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(tree[node])
            
    return len(visit)

print(solution(7,	[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))