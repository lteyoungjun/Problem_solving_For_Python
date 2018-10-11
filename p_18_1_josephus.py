


def josephus(n, k):

    survivors = []
    for i in range(1,n+1):
        survivors.append(i)
    kill = 0

    while(n > 2):

        survivors.pop(kill)
        if kill == len(survivors):
            kill = 0
        n -= 1
        print(survivors, len(survivors), kill)

        for i in range(k-1):
            if kill == len(survivors)-1:
                kill = 0
            else:
                kill += 1

    return survivors

print(josephus(6,3))