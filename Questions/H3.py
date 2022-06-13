"""Given a matrix of m x n elements, print all elements of the matrix in spiral order.

Input: 
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]  

Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
"""

def print_spiral_order(matrix: list):

    # base case
    if not matrix or not len(matrix):
        return

    top = left = 0
    bottom = len(matrix) - 1
    right = len(matrix[0]) - 1
    
    while True:
        if left > right:
            break
        
        # print top row
        for i in range(left, right + 1):
            print(matrix[top][i], end=' ')
        top = top + 1
 
        if top > bottom:
            break
 
        # print right column
        for i in range(top, bottom + 1):
            print(matrix[i][right], end=' ')
        right = right - 1
 
        if left > right:
            break
 
        # print bottom row
        for i in range(right, left - 1, -1):
            print(matrix[bottom][i], end=' ')
        bottom = bottom - 1
 
        if top > bottom:
            break
 
        # print left column
        for i in range(bottom, top - 1, -1):
            print(matrix[i][left], end=' ')
        left = left + 1

matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]

print_spiral_order(matrix)
