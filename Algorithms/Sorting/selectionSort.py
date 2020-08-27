'''
    Algo: Selection Sort
    Type: Sorting

    Time-Complexity: O(n^2)
    Space-Complexity: O(1)
'''
from typing import List


def selectionSort(arr: List[int]) -> List[int]:
    for itr in range(0, len(arr)):
        minIdx = itr
        for idx in range(itr, len(arr)):
            if(arr[idx] < arr[minIdx]):
                minIdx = idx

        arr[minIdx], arr[itr] = arr[itr], arr[minIdx]

    return arr


arr = [64, 25, 12, 22, 11]
# 11 12 22 25 64
print(selectionSort(arr))
