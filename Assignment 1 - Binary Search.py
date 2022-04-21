"""
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. 
Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. 
Your function should have the worst-case complexity of O(log N), where N is the length of the list. 
You can assume that all the numbers in the list are unique.

Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].
"Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7]

Inputs: A sorted list of unique numbers
Outputs: Number by which list has been rotated
"""

def count_rotations_linear(nums):
    """_summary_

    Args:
        nums (_type_): _description_
    """
    
    position = 0                 # Initialize position variable
    
    while position < len(nums):                     # Loop terminated when position is equal to length of list
        
        # Success criteria: check whether the number at the current position is smaller than the one before it
        if position > 0 and nums[position] < nums[position - 1]:  
            return position
        
        # Move to the next position
        position += 1
    
    return 0                     # return 0 if none of the positions passed the check

def count_rotations_binary(nums):
    """

    Args:
        nums (_type_): _description_
    """
    
    N = len(nums)
    low = 0
    high = N
    
    if N > 1:
            
        while low < high:
            
            mid = (low + high)//2
            
            if nums[mid] < nums[mid - 1]:
                return mid
            elif nums[mid] > nums[-1]:
                low = mid + 1
            else:
                high = mid - 1

    return 0

# print(count_rotations_linear([27, 29, 3, 5, 6, 7, 9, 11, 14]))
print(count_rotations_binary([3, 5, 6, 7, 9, 11, 14]))