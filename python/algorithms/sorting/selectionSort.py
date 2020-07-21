""" The selection sort algorithm sorts an array by repeatedly finding the minimum element 
            (considering ascending order) from unsorted part and putting it at the beginning.
"""

arr = [3,7,4,9,2,8,0]
print("Input: {}".format(arr))

def selectionSort(arr):
  for i in range(len(arr)-1):
    min_index = i 
    for j in range(i+1, len(arr)):
      if arr[min_index] > arr[j]: min_index = j
    if min_index != i:
      arr[min_index], arr[i] = arr[i], arr[min_index]

selectionSort(arr)
print("Output: {}".format(arr))
