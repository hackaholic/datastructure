"""Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the 
           adjacent elements if they are in wrong order.
"""


arr = [4, 2, 9, 5, 3, 0, 6]

def bubbleSort(arr):
  for i in range(len(arr)):
    for j in range(0, len(arr) -1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
 
print(arr)

bubbleSort(arr)
print(arr)
