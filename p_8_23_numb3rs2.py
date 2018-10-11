import numpy as np
'''
connected = np.array([[0,1,1,1,0],
                      [1,0,0,0,1],
                      [1,0,0,0,0],
                      [1,0,0,0,0],
                      [0,1,0,0,0]])
'''
connected = np.array([[0,1,1,1,0,0,0,0],
                      [1,0,0,1,0,0,0,0],
                      [1,0,0,1,0,0,0,0],
                      [1,1,1,0,1,1,0,0],
                      [0,0,0,1,0,0,1,1],
                      [0,0,0,1,0,0,0,1],
                      [0,0,0,0,1,0,0,0],
                      [0,0,0,0,1,1,0,0]])

#deg = np.array([3,2,1,1,1])
deg = np.array([3,2,2,5,3,2,1,2])

d = int(input("지난일 수:"))
s = int(input("교도소가 있는 마을의 번호:"))
n = deg.shape[0]
q = int(input("어느 마을에 있을까:"))

path = np.array([s])

cache = -1*np.ones((51,101))

def search(here, days):

    if days == d:
        if here == q:
            return 1
        else:
            return 0

    ret = cache[here][days]

    if ret != -1:
        return ret

    ret = 0

    for there in range(n):
        if(connected[here][there]):
            ret += search(there, days+1)*(1/deg[here])
            cache[here][there] = ret

    return ret


print(search(s, 0))
