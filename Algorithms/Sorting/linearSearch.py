'''
    Algo: Linear Search
    Type: Searching

    Time-Complexity: 
        - Best: O(1)
        - Worst: O(n)
    Space-COmplexity: O(1)
'''
from typing import List


def linearSearch(arr: List[int], ele: int) -> int:
    for idx in range(len(arr)):
        if arr[idx] == ele:
            return idx
    return -1


arr = [2, 3, 4, 10, 40]
ele = 10
# 3
print(linearSearch(arr, ele)) 
