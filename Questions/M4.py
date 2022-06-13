"""Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that most significant digit is at the head of the list, and each
element in the array contain a single digit. 

You may assume the integer does not contain any leading zero, except the number 0 itself.

--Converting the list to any other data type is forbidden--

Input: 
N = [1, 2, 3]

Output:
out = [1, 2, 4]

Explanation: The array represents the integer 123, adding 1 to it, we get 124.

Input: 
N = [9, 9]

Output:
out = [1, 0, 0]

Explanation: The array represents the integer 99, adding 1 to it, we get 100.
"""

def add_one(N: list) -> list:
    
    digits = len(N)
    
    for i in range(digits-1, -1, -1):
        N[i] += 1
        if N[i] == 10:
            N[i] = 0
        else:
            return N
    
    N.insert(0, 1)
    N[1:] = [0]*digits
    return N

N = [9, 9]
print(add_one(N))

