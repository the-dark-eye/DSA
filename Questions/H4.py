"""Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Input: [2, 3, 1, 1, 4]
Output: True
Explanation: Jump 1 step from index 0 to index 1, then 3 steps to last index.

Input: [3, 2, 1, 0, 4]
Output: False
Explanation: No matter how many steps we jump from index 0, we always reach back to index 0.
Therefore its impossible to reach last index.
"""

def can_jump(N: list) -> bool:
    
    if len(N) == 1:
        return True
    
    minStepsRequired = 0
    previousGood = len(N)-1
    
    # work backwards and see if can reach final cell
    for i in range(len(N)-2, -1, -1):
        minStepsRequired = previousGood - i
        if N[i] >= minStepsRequired:
            previousGood = i
            
    return previousGood == 0

N = [2, 3, 1, 1, 4]
print(N, can_jump(N), sep='\n')

N = [3, 2, 1, 0, 4]
print(N, can_jump(N), sep='\n')
