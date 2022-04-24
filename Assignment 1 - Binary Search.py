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
    """Linear search function that counts how many times a list needs to be rotated to be in ascending order

    Args:
        nums (list): list of numbers in ascending order, rotated by some number
    """
    
    position = 0                 # Initialize position variable
    
    while position < len(nums):                     # Loop terminated when position is equal to length of list
        
        # Success criteria: check whether the number at the current position is smaller than the one before it
        if position > 0 and nums[position] < nums[position - 1]:  
            return position
        
        # Move to the next position
        position += 1
    
    return 0                     # return 0 if none of the positions passed the check

# Set up test cases

test1 = [27, 29, 3, 5, 6, 7, 9, 11, 14]
test2 = [0, 1]
test3 = []
test4 = [10, -1, 3, 5]
test5 = [1]

# Check brute force solution for test cases

print("Checking linear search algorithm")
print(count_rotations_linear(test1))
print(count_rotations_linear(test2))
print(count_rotations_linear(test3))
print(count_rotations_linear(test4))
print(count_rotations_linear(test5))

# Optimize algorithm using binary search

def count_rotations_binary(nums):
    """Binary search function to count how many times a list needs to be rotated for it 
    to be in ascending order

    Args:
        nums (list): List of integers, rotated by some number
    """
    
    N = len(nums)
    low = 0
    high = N
    
    if N > 1:   # If length of list is more than 1
            
        while low < high:   # Terminating condition
            
            mid = (low + high)//2
            
            if nums[mid] < nums[mid - 1]:   # Check if number at mid position is greater
                                            # than the number preceeding it
                return mid
            elif nums[mid] > nums[-1]:  # Check if number at mid is greater than number at
                                        # end of the list
                low = mid + 1
            else:
                high = mid  # else change the length of search list to first half

    return 0    # Return 0 if lenght of list is 1 or less than 1

# Check binary solution for test cases

print("Checking binary search algorithm")
print(count_rotations_binary(test1))
print(count_rotations_binary(test2))
print(count_rotations_binary(test3))
print(count_rotations_binary(test4))
print(count_rotations_binary(test5))
