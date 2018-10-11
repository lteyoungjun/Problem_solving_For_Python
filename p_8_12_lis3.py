import numpy as np

#S = np.random.randint(1,100,(100))
S = np.array([1,3,4,2,4])
S = np.append(S, -999)


cache = -1*np.ones((101))
n = S.shape[0]


def lis(start):
    ret = cache[start]

    if ret != -1:
        return ret

    ret = 1
    for next in range(start+1, n):
        if(start == -1 or S[start] < S[next]):
            ret = max(ret, lis(next)+1)

    return ret

print(lis(-1)-1)