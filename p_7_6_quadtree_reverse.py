import numpy as np

string = input("문자열을 입력하세요:")

iter_string = iter(string)

def reverse():
    try:
        word = next(iter_string)
    except StopIteration as e:
        return
    if(word == "w" or word == "b"):
        return word

    upper_left = reverse()
    upper_right = reverse()
    lower_left = reverse()
    lower_right = reverse()

    return "x" + lower_left + lower_right + upper_left + upper_right

anw = reverse()

print(anw)