import numpy as np

cache = np.ones((101,101))*(-1)

wildcard = input("패턴을 입력하세요 : ")
string = input("문자열을 입력하세요 : ")

w_size = len(wildcard)
s_size = len(string)

def match_memoized(w, s):

    if cache[w][s] != -1:
        return cache[w][s]

    if(w < w_size and s < s_size) and (wildcard[w] == "?" or wildcard[w] == string[s]):
        cache[w][s] = match_memoized(w+1,s+1)
        return cache[w][s]


    if(w_size == w):
        cache[w][s] = int((s == s_size))
        return cache[w][s]

    if(s_size == s):
        for i in range(w,w_size):
            if wildcard[i] != "*":
                cache[w][s] = 0
                return cache[w][s]
        cache[w][s] = 1
        return cache[w][s]

    if(wildcard[w] == "*"):
        if match_memoized(w+1,s) or (s < s_size and match_memoized(w, s+1)):
            cache[w][s] = 1
            return cache[w][s]

    return 0

print(match_memoized(0, 0))
