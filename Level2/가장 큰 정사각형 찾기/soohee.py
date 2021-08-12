# import math
# def solution(board):

#     maxSquare = min(len(board[0]),len(board))
#     maxSquare1 = maxSquare
#     maxSquare2 = maxSquare
#     cnt = 0
#     for i in range(len(board)):
#         for j in range(len(board)//2+1):
#             cnt += 1
#             if board[i][j] == 0 :
#                 maxSquare1 -= cnt
#                 cnt = 0
#             i += 1
#             j += 1
#         break

    
#     cnt = 0
#     for k in range(len(board)):
#         for l in range(len(board[k])-1,math.ceil(len(board)/2),-1):
#             cnt += 1
#             if board[k][l] == 0 :
#                 maxSquare2 -= cnt
#                 cnt = 0
#             k += 1
#             l -= 1
#         break
    
#     maxSquare = max(maxSquare1,maxSquare2)
#     print(maxSquare**2)
#     return maxSquare**2
def check(board, idx):
    for i in range(idx):
        for j in range(idx):
            if board[i][j] != board[i+idx][j+idx]:
                return False
    return True

def solution(board):
    answer = []
    for i in range(len(board)):
        cnt = 0
        for j in range(len(board)):
            for idx in range(5-max(i,j)):
                if check(board, idx):
                    break
                else:
                    cnt += 1
            if cnt == (5-max(i,j)) **2 :
                answer.append(cnt)
    return max(answer)

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
# #solution([[0,0,1,1],[1,1,1,1]])