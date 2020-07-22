"""QuickSort is a Divide and Conquer algorithm. It picks an element as pivot 
and partitions the given array around the picked pivot. """

arr = [7, 2, 0, -1, 5, 8, 3]

print("Input: {}".format(arr))

def partition(arr, start, end):
  pivot_index, pivot_element = start, arr[end]
  for i in range(start, end):
    if arr[i] < pivot_element:
      if i!=pivot_index: 
        arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
      pivot_index +=1
  arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
  return pivot_index

def quickSort(arr, start, end):
  if start < end:
    pivot_index = partition(arr, start, end)
    quickSort(arr, start, pivot_index-1)
    quickSort(arr, pivot_index+1, end)

quickSort(arr, 0, len(arr)-1)
print("Output: {}".format(arr))
