import numpy as np


def mul_array(x):
    ret = []

    for i in range(len(x)):
        ret.append(int(x[len(x)-i-1]))

    return np.array(ret)

def num_array(x):
    ret = ""

    for i in range(len(x)):
        ret += str(int(x[len(x)-i-1]))

    return ret


def normalize(num):

    num = list(num)
    num.append(0)
    for i in range(len(num)):

        if(num[i] < 0):
            borrow = (abs(num[i]) + 9) // 10
            num[i+1] -= borrow
            num[i] += borrow*10

        elif(i < len(num)-1):
            num[i+1] += num[i] // 10
            num[i] %= 10
    while(len(num) > 1 and num[-1] == 0):
        num.pop()

    return np.array(num)

def multiply(a_array, b_array):
    c = np.zeros(shape=(len(a_array)+len(b_array) + 1,))

    for i in range(a_array.shape[0]):
        for j in range(b_array.shape[0]):
            c[i+j] += a_array[i]*b_array[j]
    c = normalize(c)
    return c

if __name__ == "__main__":

    a = input("곱하고 싶은 수를 입력하세요 : ")
    b = input("곱하고 싶은 수를 입력하세요 : ")

    a_array = mul_array(a)
    b_array = mul_array(b)

    print(num_array(multiply(a_array, b_array)))


