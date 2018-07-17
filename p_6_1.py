import numpy as np

def sum(n):
    ret = 0
    for i in range(1,n+1):
        ret += i
    return ret

def recursive(n):
    if n == 1:
        return 1

    return n + recursive(n-1)

