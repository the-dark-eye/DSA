"""Given a string, count the recurrences of alphabets. Count shall not be case-sensitive.

Input: 
string = 'I have typed 200 such strings so far!!!'

Output:
out = {'u': 1, 'c': 1, 'n': 1, 'g': 1, 'e': 2, 'h': 2, 'f': 1, 't': 2, 'y': 1, 'r': 2, 's': 4, 'a': 2, 'd': 1, 'v': 1, 'p': 1, 'i': 1, 'o': 1}

Explanation: The input string contains both alphanumeric and special characters, hence we need to ignore numeric and special characters.
Finally, cases are ignored when counting.
"""

def count_alphabets(string: str) -> dict:
    out = {i:string.count(i) for i in set(string.lower()) if i.isalpha()}
    return out

string = 'I have typed 200 such strings so far!!!'
print(count_alphabets(string))