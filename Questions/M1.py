"""Print the following inverted staircase pattern based on input size:

Input:
N = 9

Output:
9 8 7 6 5 4 3 2 1
8 7 6 5 4 3 2 1
6 5 4 3 2 1
3 2 1
0

Input:
N = 10

Output:
10 9 8 7 6 5 4 3 2 1
9 8 7 6 5 4 3 2 1
7 6 5 4 3 2 1
4 3 2 1
0
"""

def print_pattern(N: int, n=1):
    if N - n + 1 < 0:
        print(0)
    else:
        print(*list(range(N, 0, -1)))
        print_pattern(N - n, n+1)
        
print_pattern(6)