
arr = [1,2,3,4,5,6,7,8,9]

def binSearch(arr, low, high, key):
  if high >= low:
    mid = int((low+high)/2)
    if key == arr[mid]:
      return mid
    if key > arr[mid]: return binSearch(arr, mid+1, high, key)
    if key < arr[mid]: return binSearch(arr, low, mid-1, key)
  else: return -1

print(arr)
print(binSearch(arr, 0, len(arr)-1, 0))
