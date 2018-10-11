import numpy as np

triangle = np.array([[100,0,0,0,0],
                  [100,2,0,0,0],
                  [100,7,4,0,0],
                  [100,4,1,7,0],
                  [100,7,5,9,4]])

board = -1*np.ones((100,100,100*100+1))

n = triangle.shape[0]

def path(y,x,sum):

    if y == n-1:
        return triangle[y][x] + sum

    ret = board[y][x][sum]

    if ret != -1:
        return ret

    sum += triangle[y][x]

    board[y][x][sum] = max(path(y+1,x,sum), path(y+1,x+1,sum))

    return board[y][x][sum]


a = path(0,0,0)
print(a)
