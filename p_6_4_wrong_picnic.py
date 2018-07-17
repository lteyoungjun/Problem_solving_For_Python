import numpy as np

#areFriends = np.random.randint(0, 2, (10, 10),dtype=bool)

areFriends = np.ones((4,4), dtype = bool)

for i in range(areFriends.shape[0]):
    for j in range(areFriends.shape[1]):
        if i == j:
            areFriends[i][j] = False

n = int(input("학생 수를 입력하세요:"))

taken = np.zeros((4,), dtype=bool)

def countParing(taken):

    finished = True

    for i in range(n):
        if taken[i] == False:
            finished = False
            break

    if finished:
        return 1

    ret = 0

    for i in range(n):
        for j in range(n):
            if(not taken[i] and not taken[j] and areFriends[i][j]):
                taken[i] = True; taken[j] = True
                ret += countParing(taken)
                taken[i] = False; taken[j] = False

    return ret

print(countParing(taken))

