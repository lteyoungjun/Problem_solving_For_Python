import numpy as np

triangle = np.array([[9,0,0,0],
                     [5,7,0,0],
                     [1,3,2,0],
                     [3,5,5,6]])

cache = -1*np.ones((100,100))

n = triangle.shape[0]

def path(y,x):

    if y == n-1:
        return triangle[y][x]

    ret = cache[y][x]

    if ret != -1:
        return ret

    cache[y][x] = max((triangle[y][x] + path(y+1,x)),(triangle[y][x] + path(y+1, x+1)))

    return cache[y][x]

print(path(0,0))

