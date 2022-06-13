"""Given a non-negative integer, reverse its digits without converting it to string.

Input: 
N = 14503

Output:
out = 30541
"""

def reverse_int(N: int) -> int:
    out = 0
    while N > 0:
        N, remainder = divmod(N, 10)    #divmod returns quotient and remainder pair as a tuple
        out = out * 10 + remainder
    return out

N = 14503
print(reverse_int(N))