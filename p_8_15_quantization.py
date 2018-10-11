import numpy as np

INF = 987654321

A = np.random.randint(1,100,(101,))
#A = np.array([1,744,755,4,897,902,890,6,777])
#A = np.array([3,3,3,1,2,3,2,2,2,1])
n = len(A)


pSum = np.zeros((101))
pSqSum = np.zeros((101))

def precalc():
    A.sort()
    print(A)
    pSum[0] = A[0]
    pSqSum[0] = A[0]*A[0]

    for i in range(1, len(A)):
        pSum[i] = pSum[i-1] + A[i]
        pSqSum[i] = pSqSum[i-1] + A[i]*A[i]


def minError(lo, hi):
    if lo == 0:
        sum = pSum[hi] - 0
        sqSum = pSqSum[hi] - 0

    else:
        sum = pSum[hi] - pSum[lo-1]
        sqSum = pSqSum[hi] - pSqSum[lo-1]

    m = int(0.5 + sum/(hi-lo+1))

    ret = sqSum - 2*m*sum + m*m*(hi-lo+1)
    return ret

cache = -1*np.ones((101,11))

def quantize(here, parts):
    if here == n:
        return 0
    if parts == 0:
        return INF

    ret = cache[here][parts]

    if ret != -1:
        return ret

    ret = INF

    for partSize in range(1, n-here+1):
        ret = min(ret, minError(here, here+partSize-1) + quantize(here+partSize,parts-1))
        cache[here][parts] = ret
    return ret


precalc()

print(pSum)
print(pSqSum)
print(quantize(0,10))

