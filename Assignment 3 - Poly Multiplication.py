"""
Given two polynomials represented by two lists, write a function that efficiently multiplies given two polynomials.

Inputs: [2, 0, 5, 7], [3, 4, 2]
Outputs: [6, 8, 19, 41, 38, 14]
"""

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