"""Given two strings S and T, following operations can be performed on them-
1.) Delete one character from the string T
2.) Add one character from the string S to string T

Both operation can be applied multiple times. Find the minimum number of operations required 
to convert string T so that both T and S will become anagram of each other.

Input: 
S = 'abc'
T = 'cba'

Output:
out = 0

Explanation: S and T are already anagrams of each other, so 0 operation is required

Input: 
S = 'talentpad'
T = 'pad'

Output:
out = 6

Explanation: Have to add 6 characters ('talent') from string S to string T, hence 6 operations required

Input: 
S = 'talentpad'
T = 'abc'

Output:
out = 10

Explanation: Have to add 6 characters ('talent') from string S to string T, additionally, delete 'a' and 'c'
from string T and add 'p' and 'd' from string S to string T, hence 6 + 4 = 10 operations
"""

def min_operations(str1: str, str2: str) -> int:
    
    diff = 0

    str1_count = {char:str1.count(char) for char in set(str1)}
    str2_count = {char:str2.count(char) for char in set(str2)}

    for i in str2_count.keys():
        if i in str1_count.keys():
            if str2_count[i] > str1_count[i]:
                diff += str2_count[i] - str1_count[i]
        else:
            diff += str2_count[i]

    for i in str1_count.keys():
        if i in str2_count.keys():
            if str1_count[i] > str2_count[i]:
                diff += str1_count[i] - str2_count[i]
        else:
            diff += str1_count[i]  
    
    return diff

S = 'talentpad'
T = 'pad'
print(min_operations(S, T))

S = 'talentpad'
T = 'abc'
print(min_operations(S, T))