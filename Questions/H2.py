"""Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but
"[)", "({[)]" and "{{{" are invalid.

Input: parenthese_str = "(){}[]"
Output: out = True

Input: parenthese_str = "({}[])"
Output: out = True

Input: parenthese_str = "({)}"
Output: out = False
"""

def is_valid_parenthese(parenthese_str):
    
    stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
    
    for parenthese in parenthese_str:
        if parenthese in pchar:
            stack.append(parenthese)
        elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
            return False
    return len(stack) == 0

parenthese_str = "(){}[]"
print(is_valid_parenthese(parenthese_str))

parenthese_str = "({)}"
print(is_valid_parenthese(parenthese_str))
