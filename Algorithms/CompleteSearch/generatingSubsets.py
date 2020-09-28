'''
Complete search is a good technique if there is enough time to go through
all the solutions, because the search is usually easy to implement and it always
gives the correct answer. If complete search is too slow, other techniques, such as
greedy algorithms or dynamic programming, may be needed.


The subsets of {0,1,2} are {0}, {1}, {2}, {0,1}, {0,2}, {1,2} and {0,1,2}.
'''

# Method 1 (Recursion)

from typing import List


def generateSubsetsMethodOne(arr: List[int], idx: int, subset: List[int]):
    if(idx == len(arr)):
        print(subset)
    else:
        generateSubsetsMethodOne(arr, idx+1, subset)
        subset.append(arr[idx])
        generateSubsetsMethodOne(arr, idx+1, subset)
        subset.pop()


# Method 2
'''
Another way to generate subsets is based on the bit representation of integers.
Each subset of a set of n elements can be represented as a sequence of n bits,
which corresponds to an integer between 0...2
n −1. The ones in the bit sequence
indicate which elements are included in the subset
'''


def generateSubsetsMethodTwo(arr: List[int]):
    for x in range(0, 1 << len(arr)):
        subset = []
        for y in range(0, len(arr)):
            if(x & (1 << y)):
                subset.append(arr[y])
        
        print(subset)


arr = [1,2,3,4,5,6]
generateSubsetsMethodOne(arr, 0, [])
# generateSubsetsMethodTwo(arr)
