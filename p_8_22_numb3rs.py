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

def search(path):
    if(len(path) == d+1):
        if(path[-1] != q):
            return 0.0

        ret = 1
        for i in range(len(path)-1):
            ret /=deg[path[i]]


        return ret

    ret = 0

    for there in range(n):
        if(connected[path[-1]][there]):
            path = np.append(path,there)
            ret += search(path)
            path = path[:-1]

    return ret

print(search(path))
