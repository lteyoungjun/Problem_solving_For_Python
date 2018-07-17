def fastSum(n):

    if n == 1:
        return 1
    if n%2 == 1: return n + fastSum(n-1)

    return 2*fastSum(n/2) + (n/2)**2

print(int(fastSum(9383010239102832020202020202020103040010030302010203019)))
