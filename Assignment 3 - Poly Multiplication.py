"""
Given two polynomials represented by two lists, write a function that efficiently multiplies given two polynomials.

Inputs: [2, 0, 5, 7], [3, 4, 2]
Outputs: [6, 8, 19, 41, 38, 14]
"""

def multiply_basic(poly1, poly2):
    """Basic polynomial multiplication function by Brute Force method
    Time Complexity: O(k*m*n)
    Space Complexity: Linear
    
    Args:
        poly1 (list): _description_
        poly2 (list): _description_

    Returns:
        result (list): _description_
    """
    
    m = len(poly1)
    n = len(poly2)
    
    result = [0]*(m + n - 1)
    
    for k in range(len(result)):
        pair_sum = 0
        
        for i in range(m):
            for j in range(n):
                if i + j == k:
                    pair_sum += poly1[i] * poly2[j]  
        
        result[k] = pair_sum
    
    return result

# Set up Test Cases
                
test_case1 = ([2, 0, 5, 7], [3, 4, 2])
test_case2 = ([0], [3, 4, 2])
test_case3 = ([2, 0, 5, 7], [2])
test_case4 = ([2, 0, 5, 7], [])
test_case5 = ([], [])
                
# Check test cases output

print(multiply_basic(*test_case1))
print(multiply_basic(*test_case2))
print(multiply_basic(*test_case3))
print(multiply_basic(*test_case4))
print(multiply_basic(*test_case5))

# ---------------------------------------------------------------

def add(poly1, poly2):
    """Add two polynomials"""
    result = [0] * max(len(poly1), len(poly2))
    for i in range(len(result)):
        if i < len(poly1):
            result[i] += poly1[i]
        if i < len(poly2):
            result[i] += poly2[i]
    return result

def split(poly1, poly2):
    """Split each polynomial into two smaller polynomials"""
    mid = max(len(poly1), len(poly2)) // 2
    return  (poly1[:mid], poly1[mid:]), (poly2[:mid], poly2[mid:])

def increase_exponent(poly, n):
    """Multiply poly1 by x^n"""
    return [0] * n + poly

def multiply_optimized(poly1, poly2):
    """Optimized algorithm for multiplication of two polynomials with Divide and Conquer
    Time Complexity: 
    Space Complexity: 

    Args:
        poly1 (list): list containing coefficients of polynomial 1
        poly2 (list): list containing coefficients of polynomial 2

    Returns:
        list: list containing coefficients of output polynomial
    """
    
    if len(poly1) <= 1:
        return [poly1 * poly2[i] for i in range(len(poly2))]
    elif len(poly2) <= 1:
        return [poly2 * poly1[i] for i in range(len(poly1))]
    
    n = max(len(poly1), len(poly2))
    
    (A0, A1), (B0, B1) = split(poly1, poly2)
    
    Y = multiply_optimized(add(A0, A1), add(B0, B1))
    U, Z = multiply_optimized(A0, B0), multiply_optimized(A1, B1)
    Y_U_Z = add(Y, -1 * add(U, Z))
    
    return add(add(U, increase_exponent(Y_U_Z, n//2)), increase_exponent(Z, n))
    
print(multiply_optimized(*test_case1))
print(multiply_optimized(*test_case2))
print(multiply_optimized(*test_case3))
print(multiply_optimized(*test_case4))
print(multiply_optimized(*test_case5))