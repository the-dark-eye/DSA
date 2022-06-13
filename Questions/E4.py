"""Write a function to convert a given 10-base non-negative integer to a given base.

Input: 
N = 11
base = 3

Output:
out = 102

Explanation: In base 3, 11 is 1*(3^2) + 0*(3^1) + 2*(3^0), hence 102
"""

def convert_to_base(N: int, base: int) -> str:
    if N//base < 1:
        return str(N%base)
    else:
        return convert_to_base(N//base, base) + str(N%base)

N = 11
base = 3
print(convert_to_base(N, base))