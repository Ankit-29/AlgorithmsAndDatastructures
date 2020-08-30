'''
    Algo: Quick Sort
    Type: Sorting

    Time-Complexity: 
        - Worst: O(n^2)
        - Best : O(nLogn)
    Space-Complexity: O(1)
'''
from typing import List


def quickSort(arr: List[int], low: int, high: int):
    if(low < high):
        p = partition(arr, low, high)
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)

def partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[high]
    itr = low - 1
    for itr2 in range(low, high):
        if(arr[itr2] < pivot):
            itr += 1
            arr[itr], arr[itr2] = arr[itr2], arr[itr]
    arr[itr+1], arr[high] = arr[high], arr[itr+1]
    return itr+1


arr = [64, 25, 12, 22, 11]
# 11 12 22 25 64
quickSort(arr,0,len(arr)-1)
print(arr)