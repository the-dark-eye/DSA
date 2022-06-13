"""
There are n bulbs that are initially off. You first turn on all the bulbs. Then you turn off every second bulb.
On the third round, you toggle every third bulb (turning on if it's off and vice versa). For the i-th round,
you toggle every i bulb. For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Input: 3
Output: 1

Explanation: At first the three bulbs are [off, off, off]
After first round, the three bulbs are [on, on, on]
After second round, the three bulbs are [on, off, on]
After third round, the three bulbs are [on, off, off]

Therefore we return 1, because only 1 bulb is on.
"""

def find_on_bulbs(N: int) -> int:
    return int(N**0.5)

N = 5
print(find_on_bulbs(N))
