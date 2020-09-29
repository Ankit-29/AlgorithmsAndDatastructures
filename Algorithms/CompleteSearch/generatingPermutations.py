'''
The problem of generating all permutations of a set of n elements.
For example, the permutations of {0,1,2} are (0,1,2), (0,2,1), (1,0,2), (1,2,0),
(2,0,1) and (2,1,0). Again, there are two approaches: we can either use recursion
or go through the permutations iteratively.

'''

from typing import List


def generatingPermutations(arr: List[int], perm: List[int], chosen: List[bool]):
    if(len(perm) == len(arr)):
        print(perm)
    else:
        for x in range(0, len(arr)):
            if(chosen[x]):
                continue
            chosen[x] = True
            perm.append(arr[x])
            generatingPermutations(arr, perm,chosen)
            chosen[x] = False
            perm.pop()


arr = [1,2,3]
chosen = [False]*len(arr)
generatingPermutations(arr, [], chosen)
