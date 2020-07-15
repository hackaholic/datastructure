"""
Given an array of integers, print all sub-arrays with 0 sum.

For example,
Input: { 4, 2, -3, -1, 0, 4 }
Sub-arrays with 0 sum are
{ -3, -1, 0, 4 }
{ 0 }

Input: { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }
Sub-arrays with 0 sum are
{ 3, 4, -7 }
{ 4, -7, 3 }
{ -7, 3, 1, 3 }
{ 3, 1, -4 }
{ 3, 1, 3, 1, -4, -2, -2 }
{ 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }

"""

def printSubArray(arr, value):
  for k in range(len(arr)):
    total = 0
    for i, x in enumerate(arr[k:]):
      total += x
      if total == value:
        print("subarray: {}".format(arr[k:k+i+1]))

#arr = [4, 2, -3, -1, 0, 4]
arr = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
value = 0
printSubArray(arr, value)
