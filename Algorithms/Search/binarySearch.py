'''
    Algo: Binary Search
    Type: Searching

    Time-Complexity: 
        - Best: O(1)
        - Worst: O(logn)
    Space-Complexity: O(1)
'''
from typing import List

''' Recursive Approach ''' 
def binarySearch(arr: List[int], ele: int, l: int, r: int) -> int:
    if l <= r:
        mid = l + (r-l)//2
        if(arr[mid] == ele):
            return ele
        elif(arr[mid] < ele):
            return binarySearch(arr, ele, l+1, r)
        else:
            return binarySearch(arr, ele, l, r-1)
    else:
        return -1


arr = [2, 3, 4, 10, 40]
ele = 10
# 3
print(binarySearch(arr, ele, 0, len(arr)-1))
