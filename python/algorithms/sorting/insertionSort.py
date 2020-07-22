""" Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.

Shift the element until its get ot its right position"""

arr = [6,3,0,7,1,5,2, -9]

print("Input: {}".format(arr))

def insertionSort(arr):
  for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
      arr[i], arr[i+1] = arr[i+1], arr[i]
      for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
          arr[j], arr[j-1] = arr[j-1], arr[j]

insertionSort(arr)
print("Output: {}".format(arr))
