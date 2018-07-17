from p_7_3_multiply import *
from copy import copy

def addTo(a, b, k):
    a = copy(a)
    bn = b.shape[0]
    a.resize(max(10*a.shape[0], 10*bn + k), refcheck=False)
    for i in range(bn):
        a[i+k] += b[i]
        if(a[i+k] > 10):
            a[i+k] -= 10
            a[i+k+1] += 1
    while a[-1] == 0 and a.shape[0] > 1:
        a = a[:-1]
    return a

def subFrom(a, b):
    a = copy(a)
    bn = b.shape[0]
    a.resize(max(a.shape[0], bn + 1), refcheck=False)
    for i in range(bn):
        a[i] -= b[i]
        if a[i] < 0:
            a[i] += 10
            a[i+1] -= 1

    return a

def karatsuba(a, b):
    an = a.shape[0]; bn = b.shape[0]
    if an < bn:
        return karatsuba(b, a)
    if an == 0 or bn == 0:
        return []
    if an <= 3:
        return multiply(a,b)

    half = an//2

    a0 = a[0:half]
    a1 = a[0+half:]
    b0 = b[0:min(half,bn)]
    b1 = b[0+min(half,bn):]

    z2 = karatsuba(a1, b1)
    z0 = karatsuba(a0, b0)

    a0 = addTo(a0, a1, 0); b0 = addTo(b0, b1, 0)
    z1 = karatsuba(a0, b0)

    z1 = subFrom(z1, z0)
    z1 = subFrom(z1, z2)

    ret = np.array([])

    ret = addTo(ret, z0, 0)
    ret = addTo(ret, z1, half)
    ret = addTo(ret, z2, half + half)

    return ret

if __name__ == "__main__":


    a = input("곱하고 싶은 수를 입력하세요 : ")
    b = input("곱하고 싶은 수를 입력하세요 : ")

    a_array = mul_array(a)
    b_array = mul_array(b)

    print(num_array(karatsuba(a_array, b_array)))