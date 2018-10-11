import numpy as np

def bruteforce(height):
    ret = 0
    size = height.shape[0]
    for left in range(size):
        minHeight = height[left]
        for right in range(left, size):
            minHeight = min(minHeight, height[right])
            ret = max(ret, minHeight*(right - left + 1))

    return ret

height = np.array([7,1,5,9,6,7,3])
print(height[2])
size = bruteforce(height)
print(size)
