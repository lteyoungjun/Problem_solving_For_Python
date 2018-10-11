import numpy as np

INF = 987654321

N = input("문자열을 입력하세요 : ")
n = len(N)

def classify(a, b):

    M = N[a:b+1]
    if M == M[0]*(b-a+1):
        return 1

    progressive = True

    for i in range(len(M)-1):
        if(int(M[i+1])-int(M[i])) != (int(M[1])-int(M[0])):
            progressive = False

    if progressive and abs(int(M[1])-int(M[0])) == 1:
        return 2

    alternating = True

    for i in range(len(M)):
        if(int(M[i])!=int(M[i%2])):
            alternating = False

    if(progressive): return 4
    if(alternating): return 5

    return 10

cache = -1*np.ones((10002))

def memorize(begin):
    if(begin == n):
        return 0

    ret = cache[begin]
    if ret != -1:
        return ret

    ret = INF

    for i in range(3,6):
        if(begin+i <= n):
            ret = min(ret, memorize(begin + i)+classify(begin, begin+i-1))

    return ret


print(memorize(0))
