string = input("문자열을 입력하세요 : ")
w_pattern = input("패턴을 입력하세요 : ")

def match(string, wildcard):
    pos = 0
    s_size = len(string)
    w_size = len(wildcard)
    while(pos < s_size and pos < w_size) and (wildcard[pos] == "?" or string[pos]==wildcard[pos]):
        pos += 1

    if(pos == w_size):
        if(w_size == s_size):
            return True
        else:
            return False

    if(wildcard[pos] == "*"):
        for skip in range(0,s_size-pos+1):
            if match(string[pos+skip:],wildcard[pos+1:]):
                return True

    return False

print(match(string,w_pattern))

