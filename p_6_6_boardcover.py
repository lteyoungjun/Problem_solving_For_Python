import numpy as np

def mapping(i,j):

    board[i,j] = 1

board = np.zeros((3,7))
board[0,0] = 1;board[0,6] = 1;board[1,0] = 1;board[1,6] = 1;board[2,0] = 1;board[2,1] = 1;board[2,4] = 1;board[2,5] = 1;board[2,6] = 1
print(board)

coverType = np.array([[[0,0],[1,0],[0,1]],
                      [[0,0],[0,1],[1,1]],
                      [[0,0],[1,0],[1,1]],
                      [[0,0],[1,0],[1,-1]]])

def set(board, y, x, type, delta):
    ok = True
    for i in range(3):
        newY = y + coverType[type][i][0]
        newX = x + coverType[type][i][1]
        board[newY][newX] += delta
        if newY < 0 or newY >= board.shape[0] or newX < 0 or newX >= board.shape[1]:
            ok = False
        elif board[newY][newX] > 1:
            ok = False

    return ok


def cover(board):
    x = -1;y = -1
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if board[i][j] == 0:
                y = i
                x = j
                break
        if (y != -1):
            break

    if y == -1:
        return 1

    ret = 0

    for type in range(coverType.shape[0]):
        if set(board,y,x,type,1):
            ret += cover(board)
        set(board,y,x,type,-1)

    return ret

print(cover(board))