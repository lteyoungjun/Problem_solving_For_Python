import numpy as np

def solve(left, right, height):

    if left == right:
        return height[left]

    mid = int((left + right)//2)

    ret = max(solve(left, mid, height), solve(mid+1, right, height))

    lo = mid; hi = mid + 1

    height_mid = min(height[lo], height[hi])

    ret = max(ret, 2*height_mid)

    while(left < lo or hi < right):
        if(hi < right) and ((left == lo) or (height[lo-1] < height[hi+1])):
            hi += 1
            height_mid = min(height_mid, height[hi])
        else:
            lo -= 1
            height_mid = min(height_mid, height[lo])

        ret = max(ret, height_mid*(hi-lo+1))

    return ret

height = np.array([7,1,5,9,6,7,3])

print(solve(0, height.shape[0]-1, height))
