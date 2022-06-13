"""Given a list of non-negative integers, and a target sum, find all the sub-arrays in the list 
having a sum equal to the target sum.

Input: 
lst = [1, 2, 3, 4, 5, 1]
TARGET = 6

Output:
out = [ [1, 2, 3], [5, 1] ] 

Explanation: There are only 2 sub-arrays in the given list having total sum equal to 6, (1, 2, 3) and (5, 1).
Note that (2, 4) is also a pair having sum 6 but its not a continuous pair. 
"""

def pairs_with_target_sum(lst: list, TARGET: int) -> list:
    """ Time Complexity = O(N2) """
    out = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if sum(lst[i:j+1]) == TARGET:
                out.append(lst[i:j+1])
                
    return out


lst = [1, 2, 3, 4, 5, 1]
TARGET = 6
print(pairs_with_target_sum(lst, TARGET))
