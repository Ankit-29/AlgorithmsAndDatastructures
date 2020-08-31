'''
    Algo: Permutation of String
    Type: Backtracking

    Time-Complexity: O(n*n!)
'''

from typing import List


def permutations(arr: List[str], l: int, r: int, res: List[str]) -> List[str]:
    if l == r:
        res.append("".join(arr))
    else:
        for x in range(l, r):
            arr[l], arr[x] = arr[x], arr[l]
            permutations(arr, l+1, r, res)
            arr[l], arr[x] = arr[x], arr[l]

    return res



string = "ABC"
print(permutations(list(string), 0, len(string), []))
