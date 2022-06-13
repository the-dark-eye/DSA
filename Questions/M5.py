"""For a given array with repeated elements, exactly one element is not repeated (single).
Find the non-repeated element. Try to find a solution with linear time complexity.

Input: 
N = [1, 2, 5, 4, 6, 8, 9, 2, 1, 4, 5, 8, 9]

Output:
out = 6

Explanation: In the given array, all elements are repeated except 6.
"""

def find_unique(N: list) -> int:
    out = 0
    for i in N:
        out ^= i
    return out

N = [1, 2, 5, 4, 6, 8, 9, 2, 1, 4, 5, 8, 9]
print(find_unique(N))

