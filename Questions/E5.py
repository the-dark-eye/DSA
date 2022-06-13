"""Given a list of integers, in which ith element is the price of a given stock on ith day, 
design an algorithm to find the maximum profit if you were only permitted to complete at most 
one transaction. 

Note that you cannot sell a stock before you buy one.

Input: 
data = [7, 1, 5, 3, 6, 4]

Output:
out = 5 

Input: 
data = [7, 6, 4, 3, 0]

Output:
out = 0

Explanation: The stock price is continuously decreasing, so no profit can be obtained.
"""

def max_profit(data: list) -> int:
    
    if len(data) != 0:
        max_price, min_price  = max(data), min(data)
        max_price_ind = data.index(max_price)
        min_price_ind = data.index(min_price)

        if max_price_ind > min_price_ind:
            return max_price - min_price
        else:
            data.pop(max_price_ind)
            return max_profit(data)
    return 0

data = [7, 1, 5, 3, 6, 4]
print(max_profit(data))

data = [7, 6, 4, 3, 0]
print(max_profit(data))