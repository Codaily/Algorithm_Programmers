def solution(board, moves):
    boom = 0
    basket = [0]
    for m in moves:
        for b in range(len(board)):
            if board[b][m-1] != 0:
                if basket[-1] == board[b][m-1]:
                    basket.pop()
                    board[b][m-1] = 0
                    boom += 2 
                    break
                else:
                    basket.append(board[b][m-1])
                    board[b][m-1] = 0
                    break
    return boom

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))

# 순서 1,5,3,5,1,2,1,4

# 0 0 0 0 0
# 0 0 1 0 3
# 0 2 5 0 1
# 4 2 4 4 2
# 3 5 1 3 1
