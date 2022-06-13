"""Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place (do not return anything).

Input: matrix = [[1,1,1],
                 [1,0,1],
                 [1,1,1]]
Output: [[1,0,1],
         [0,0,0],
         [1,0,1]]

"""

def set_zeroes(matrix: list) -> list:
    
    R = len(matrix)
    C = len(matrix[0])
    rows, cols = set(), set()

    # Essentially, we mark the rows and columns that are to be made zero
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    # Iterate over the array once again and using the rows and cols sets, update the elements
    for i in range(R):
        for j in range(C):
            if i in rows or j in cols:
                matrix[i][j] = 0

matrix = [[1,1,1], [1,0,1], [1,1,1]]
set_zeroes(matrix)
print(matrix)
