import numpy as np

areFriends = np.zeros((10, 10),dtype=bool)
print(areFriends)

def mapping():


    i = int(input("i를 정하세요:"))
    j = int(input("j를 정하세요:"))
    areFriends[i,j] = True
    areFriends[j,i] = True

    ex = input("계속 하시겠습니까?[Y/N]")
    if ex == 'N':
        return 0
    mapping()

mapping()
print(areFriends)

n = int(input("학생 수를 입력하세요:"))

taken = np.zeros((10,), dtype=bool)

def countPairings(taken):

    firstFree = -1

    for i in range(n):
        if not taken[i]:
            firstFree = i
            break

    if firstFree == -1:
        return 1

    ret = 0

    for i in range(firstFree + 1, n):
        if not taken[i] and areFriends[i][firstFree]:
            taken[i] = True; taken[firstFree] = True
            ret += countPairings(taken)
            taken[i] = False; taken[firstFree] = False

    return ret


print(countPairings(taken))
