import numpy as np

board = np.array(([['w','o','r','s','k'],
                   ['k','s','w','w','o'],
                   ['a','b','c','o','e'],
                   ['w','b','c','r','d'],
                   ['a','b','c','d','d']]))


dx = [-1,-1,-1,1,1,1,0,0]
dy = [-1,0,1,-1,0,1,-1,1]

def inRange(x, y):
    if(x < 0 or x >= 5 or y < 0 or y >= 5):
        return False
    else:
        True

def hasWord(x, y, word):

    if inRange(x, y) == False:
        return False

    if board[x][y] != word[0]:
        return False

    if len(word) == 1:
        return True

    for direction in range(0, 8):
        newX = x + dx[direction]
        newY = y + dy[direction]
        if hasWord(newX, newY, word[1:]):

            return True
    return False

print(hasWord(3,"word"))

