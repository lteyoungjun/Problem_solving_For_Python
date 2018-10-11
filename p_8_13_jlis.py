import numpy as np

NEGINF = -10**3

#A = np.random.randint(1,100,(100,))
#B = np.random.randint(1,100,(100,))

#A = np.array([1,2,3])
#B = np.array([3,4,7])

A = np.array([10,20,30,1,2])
B = np.array([10,20,30])

n = A.shape[0]
m = B.shape[0]
cache = -1*np.ones((101,101))

def jlis(indexA, indexB):
    ret = cache[indexA+1][indexB+1]
    if ret != -1:
        return ret

    ret = 2
    if indexA == -1:
        a = NEGINF
    else:
        a = A[indexA]

    if indexB == -1:
        b = NEGINF
    else:
        b = B[indexB]

    maxElement = max(a,b)

    for nextA in range(indexA+1,n):
        if(maxElement < A[nextA]):
            ret = max(ret, jlis(nextA, indexB)+1)


    for nextB in range(indexB+1,m):
        if(maxElement < B[nextB]):
            ret = max(ret, jlis(indexA, nextB)+1)

    return ret

print(jlis(-1,-1)-2)