import numpy as np

MAX_SIZE = 100
print(MAX_SIZE)
string = input("문자열을 입력하세요:")
decompressed = np.chararray((MAX_SIZE,MAX_SIZE))

decompressed[:] = " "

iter_string = iter(string)

def decompress(y, x, size):

    try:
        head = next(iter_string)
        print(head)
    except StopIteration as e:
        print(e)
        return

    if(head == "b" or head == "w"):
        for dy in range(size):
            for dx in range(size):
                decompressed[y + dy][x + dx] = head

    else:

        half = int(size/2)
        decompress(y, x, half)
        decompress(y, x + half, half)
        decompress(y + half, x, half)
        decompress(y + half, x + half, half)

decompress(0, 0, 4)
print(decompressed)

