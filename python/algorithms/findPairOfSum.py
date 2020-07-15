"""
Given an unsorted array of integers, find a pair with given sum in it.
For example,
Input:
arr = [8, 7, 2, 5, 3, 1]
sum = 10

Output:
Pair found at index 0 and 2 (8 + 2)
or
Pair found at index 1 and 4 (7 + 3)
"""

# Using hashing to solve in O(n) 

def findPair(arr, value):
  my_dict = {}
  for i,x in enumerate(arr):
    if my_dict.get(value-x):
        print("Pair found at index {}  and {}".format(my_dict.get(value-x)-1, i))
    my_dict[x] = i+1


arr = [8, 7, 2, 5, 3, 1]
value = 9
print(arr)
findPair(arr, value)
