"""
Given a number check whether it is a mystery number or not. 
A mystery number is that number which can be expressed as 
sum of two numbers and those two numbers should be reverse 
of each other.

Examples:

    Input : n = 121
    Output : 29 92


    Input : n = 22
    Output : 11 11 
"""

import sys

n = int(sys.argv[1])

def magicnumber(n):
    for i in range((n//2)+1):
        rev = int(str(i)[::-1])
        if i + rev == n:
            return i, rev

print(magicnumber(n))
