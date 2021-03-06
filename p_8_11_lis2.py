import numpy as np

S = np.random.randint(1,100,(100,))
#S = np.array([1,3,4,2,4])
n = S.shape[0]

cache = -1*np.ones((100,))

def lis(start):
    ret = cache[start]
    if ret != -1:
        return ret

    ret = 1
    for next in range(start+1, n):
        if S[start] < S[next]:
            ret = max(ret, lis(next) + 1)
            cache[start] = ret

    return ret

maxlen = 0

for i in range(len(S)):
    maxlen = max(maxlen, lis(i))

print(maxlen)

print(lis(0))

