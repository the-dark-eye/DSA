"""
Given two polynomials represented by two lists, write a function that efficiently multiplies given two polynomials.

Inputs: [2, 0, 5, 7], [3, 4, 2]
Outputs: [6, 8, 19, 41, 38, 14]
"""

def multiply_basic(poly1, poly2):
    """Basic polynomial multiplication function by Brute Force method
    Time Complexity: O(m2 + n2 + m*n)
    Space Complexity: Linear
    
    Args:
        poly1 (list): coefficients of polynomial 1
        poly2 (list): coefficients of polynomial 2

    Returns:
        result (list): coefficients of product of polynomial 1 and 2
    """
    
    m = len(poly1)
    n = len(poly2)
    
    result = [0]*(m + n - 1)
    
    if m == 0 or n == 0:
        result = [0]*(m + n)
    
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
test_case6 = ([2, 0, 7], [2, 0, 7])
                
# Check test cases output using multiply_basic function

print(multiply_basic(*test_case1))
print(multiply_basic(*test_case2))
print(multiply_basic(*test_case3))
print(multiply_basic(*test_case4))
print(multiply_basic(*test_case5))
print(multiply_basic(*test_case6))

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
    Time Complexity: O(log2(n))
    Space Complexity: Linear

    Args:
        poly1 (list): list containing coefficients of polynomial 1
        poly2 (list): list containing coefficients of polynomial 2

    Returns:
        list: list containing coefficients of output polynomial
    """
    
    n = max(len(poly1), len(poly2))
    
    if len(poly1) == 1:
        return [poly1[0] * i for i in poly2]
    elif len(poly2) == 1:
        return [poly2[0] * i for i in poly1]
    elif (len(poly1) == 0) or (len(poly2) == 0):
        return [0] * n
    
    (A0, A1), (B0, B1) = split(poly1, poly2)
    
    Y = multiply_optimized(add(A0, A1), add(B0, B1))
    U = multiply_optimized(A0, B0)
    Z = multiply_optimized(A1, B1)
    Y_U_Z = add(Y, [-1 * i for i in add(U, Z)])
    
    result = add(add(U, increase_exponent(Y_U_Z, n//2)), increase_exponent(Z, 2*(n//2)))
    
    return result

# Run test cases using multiply_optimized function

print(multiply_optimized(*test_case1))
print(multiply_optimized(*test_case2))
print(multiply_optimized(*test_case3))
print(multiply_optimized(*test_case4))
print(multiply_optimized(*test_case5))
print(multiply_optimized(*test_case6))