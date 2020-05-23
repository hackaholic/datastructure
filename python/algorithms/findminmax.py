""" Problem :
    Find min and max element in an array using divide and conquer algorithm
"""

import time
def findMinMax(low, high, arr):
    #print(arr[low:high+1])
    if low == high:
        return arr[low], arr[low]

    if low+1 == high:
        return  (arr[low], arr[high]) [arr[low] > arr[high]], (arr[low], arr[high]) [arr[low] < arr[high]]

    mid = int((high+low)/2)
    minL, maxL = findMinMax(low, mid, arr)
    minR, maxR = findMinMax(mid+1, high, arr)
    return (minL, minR) [minL > minR], (maxL, maxR) [maxL < maxR]

arr = [5,7,1,8,9,2,6,7,23,5,6,12,0]
print(findMinMax(0, len(arr)-1, arr)) 
