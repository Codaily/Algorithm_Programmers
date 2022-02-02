def solution(dirs):
    x = 0
    y = 0
    visited = set() # 이동경로 저장 : 이전 < 현재

    for i in dirs:
        if i == "U" and y < 5:
            visited.add(((x, y), (x, y+1)))
            y += 1
        elif i == "D" and y > -5:
            visited.add(((x, y-1), (x, y)))
            y -= 1
        if i == "L" and x < 5:
            visited.add(((x, y), (x+1, y)))
            x += 1
        if i == "R" and x > -5:
            visited.add(((x-1, y), (x, y)))
            x -= 1

    return len(visited)

dirs = "ULURRDLLU"
print(solution(dirs))