'''
    Algo: Bubble Sort
    Type: Sorting

    Time-Complexity: O(n^2)
    Space-Complexity: O(1)
'''
from typing import List


def bubbleSort(arr: List[int]) -> List[int]:
    for itr in range(0, len(arr)):
        for idx in range(0,len(arr)-itr-1):
            if(arr[idx]>arr[idx+1]):
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
                
    return arr


arr = [64, 25, 12, 22, 11]
# 11 12 22 25 64
print(bubbleSort(arr))
