import numpy as np

def pick(n, picked, toPick):

    if toPick == 0:
        print(picked)
        return

    if len(picked) != 0:
        smallest = picked[len(picked)-1] + 1
    else:
        smallest = 0

    for i in range(smallest, n):
        picked.append(i)
        pick(n, picked, toPick - 1)
        picked.pop()


pick(10, [], 4)