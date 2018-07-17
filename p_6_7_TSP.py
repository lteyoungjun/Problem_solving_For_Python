import numpy as np

n = int(input("도시의 수를 입력하세요:"))

dist = np.random.randint(1,10,(n,n))

for i in range(n):
    for j in range(n):
        if i == j:
            dist[i][j] = 0

print(dist)
visited = np.zeros((n,),dtype=bool)

def shortest_path(path, visited, currentLength):

    if len(path) == n:
        print(path)
        return currentLength + dist[path[n-1]][path[0]]

    ret = 1000000

    for next in range(n):
        if visited[next] == True:
            continue
        here = path[len(path)-1]
        path.append(next)
        visited[next] = True

        cand = shortest_path(path, visited, currentLength + dist[here][next])

        ret = min(cand, ret)
        visited[next] = False
        path.pop()

    return ret

path = [0]
print(shortest_path(path, visited, 0))
