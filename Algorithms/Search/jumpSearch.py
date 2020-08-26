'''
    Algo: Jump Search
    Type: Searching

    Time-Complexity: 
        - Best: O(1)
        - Worst: O(√n)
    Space-Complexity: O(1)
'''
import math
from typing import List


def jumpSearch(arr: List[int], ele: int) -> int:
    size = len(arr)
    jumpBlock = int(math.sqrt(size))
    step = jumpBlock
    prev = 0
    while(arr[min(step, size)-1] < ele):
        prev = step
        step += jumpBlock
        if(prev >= size):
            return -1

    while(arr[prev] < ele):
        prev += 1
        if(prev == min(step, size)):
            return -1

    if(arr[prev] == ele):
        return prev

    return -1


arr = [2, 3, 4, 10, 40]
ele = 10
# 3
print(jumpSearch(arr, ele))
