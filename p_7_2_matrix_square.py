import numpy as np

def get_RdMatrix(size):
    return np.random.randint(1,10, size=(size,size))

def get_IdMatrix(size):
    return np.identity(size)

def pow_mat(Square_Matrix, m):
    if m == 0:
        return get_IdMatrix(Square_Matrix.shape[0])
    if m % 2 > 0:
        return np.matmul(pow_mat(Square_Matrix, m-1),Square_Matrix)
    half = pow_mat(Square_Matrix, m/2)

    return half*half

a = get_RdMatrix(5)
print(a)
print(pow_mat(a,3))