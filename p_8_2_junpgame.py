import numpy as np

sample_board_1 = np.array([[2,5,1,6,1,4,1],
                  [6,1,1,2,2,9,3],
                  [7,2,3,2,1,3,1],
                  [1,1,3,1,7,1,2],
                  [4,1,2,3,4,1,2],
                  [3,3,1,2,3,4,1],
                  [1,5,2,9,4,7,0]])

sample_board_2 = np.array([[1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,2],
                         [1,1,1,1,1,2,0]])


n = 7

def jump(y,x, board):
    if y >= n or x >= n:
        return False
    if y == n-1 and x == n-1:
        return True

    jumpsize = board[y][x]
    result = jump(y + jumpsize, x, board) or jump(y, x + jumpsize, board)
    return result

print(jump(0,0, sample_board_1))

