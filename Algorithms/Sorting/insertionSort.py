'''
    Algo: Insertion Sort
    Type: Sorting

    Time-Complexity: 
        - Worst: O(n^2)
        - Best : O(n)s
    Space-Complexity: O(1)
'''
from typing import List


def insertionSort(arr: List[int]) -> List[int]:
    for itr in range(1, len(arr)):
        key = arr[itr]
        idx = itr - 1
        while(idx >= 0 and arr[idx] > key):
            arr[idx + 1] = arr[idx]
            idx = idx - 1
        arr[idx + 1] = key 

    return arr


arr = [64, 25, 12, 22, 11]
# 11 12 22 25 64
print(insertionSort(arr))
