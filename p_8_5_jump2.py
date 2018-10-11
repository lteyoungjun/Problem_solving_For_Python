import numpy as np

cache = -1*np.ones((100,100))

sample_board_1 = np.array([[2,5,1,6,1,4,1],
                  [6,1,1,2,2,9,3],
                  [7,2,3,2,1,3,1],
                  [1,1,3,1,7,1,2],
                  [4,1,2,3,4,1,2],
                  [3,3,1,2,3,4,1],
                  [1,5,2,9,4,7,0]])

n = sample_board_1.shape[0]

def jump2(y, x, board):
    if y >= n or x >= n:
        return False
    if y == n-1 and x == n-1:
        return True

    if cache[y][x] != -1:
        return cache[y][x]

    jumpsize = board[y][x]

    cache[y][x] = jump2(y+jumpsize, x, board) or jump2(y,x+jumpsize, board)

    return cache[y][x]

ret = jump2(0,0,sample_board_1)
print(ret)

