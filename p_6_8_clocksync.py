import numpy as np

INF = 9999; SWITCHES = 10; CLOCKS = 16

linked = np.array([[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1],
                   [1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,1,1,1,0,1,0,1,0,0,0],
                   [1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1],
                   [0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1],
                   [0,0,0,0,1,1,0,1,0,0,0,0,0,0,1,1],
                   [0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,1,1,1,0,0,0,1,0,0,0,1,0,0]])

clocks = [12, 6, 6, 6, 6, 6, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]

def areAligned(clocks):
    for clock in range(CLOCKS):
        if clocks[clock] != 12:
            return False

    return True

def push(clocks, swtch):
    for clock in range(CLOCKS):
        if linked[swtch][clock] == 1:
            clocks[clock] += 3
            if clocks[clock] == 15:
                clocks[clock] = 3

def solve(clocks, swtch):
    if swtch == SWITCHES:
        if areAligned(clocks):
            return 0
        else:
            return INF

    ret = INF
    for cnt in range(4):
        ret = min(ret, cnt + solve(clocks, swtch+1))
        push(clocks, swtch)

    return ret

print(solve(clocks, 0))