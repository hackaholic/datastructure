"""
Find all duplicate element in an array

Input: {1, 2, 4, 2, 6, 1, 9, 3, 0, 4, 4}
output: {1, 2, 4}
"""

def findDuplicates(arr):
  dup = []
  my_dict = {}
  for x in arr:
    my_dict[x] = my_dict.get(x, 0) + 1
    if my_dict.get(x, 0) == 2:
      dup.append(x)
  print(dup)

arr = [1, 2, 4, 2, 6, 1, 9, 3, 0, 4, 4]
print("array: {}".format(arr))
print("Duplicates", end=': ')
findDuplicates(arr)
