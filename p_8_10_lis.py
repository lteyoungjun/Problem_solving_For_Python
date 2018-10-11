import numpy as np

def lis(A):

    if len(A) == 0:
        return 0
    ret = 0

    for i in range(len(A)):
        B = np.array([])
        for j in range(i,len(A)):
            if A[i] < A[j]:
                B = np.append(B, A[j])
        ret = max(ret, 1 + lis(B))

    return ret

A = [1,3,4,2,4]

print(lis(A))
