"""Given an array of elements and change the array in such a way that all the elements on the array are distinct. if you are replacing a value, then the replacing value should be great than the previous value and after modification sum of the elements should be as less as possible.

Examples:

    Input : arr = {1, 2, 2, 5, 8, 8, 8}
    Output : 1 2 3 5 8 9 10
    8 is replaced with 9 (A non-existing element greater than 8). Next duplicate occurrence of 8 is replaced with 10.


    Input : arr = {1, 2, 5, 7, 8, 8, 7}
    Output : 1 2 5 7 8 9 10

    Input : arr = {9, 9, 9, 9, 9}
    Output : 9 10 11 12 13"""


def partition(low, high, arr):
  pivot = arr[high]
  p_index = low
  for i  in range(low, high):
    if arr[i] < pivot:
      if i != p_index:
        arr[i], arr[p_index] = arr[p_index], arr[i]
      p_index +=1
  arr[high], arr[p_index] = arr[p_index], arr[high]
  return p_index

def quicksort(low, high, arr):
  if low < high:
    p_index = partition(low, high, arr)
    quicksort(low, p_index-1, arr)
    quicksort(p_index+1, high, arr)

def replacedup(arr):
  quicksort(0, len(arr)-1, arr)
  print(arr)
  temp = []
  for x in arr:
    if x in temp:
      temp.append(temp[-1]+1)
    else: temp.append(x)
  return temp

arr = [1,2,5,7,8,8,7]
print(replacedup(arr))
