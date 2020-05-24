import sys
import timeit
from randomarray import randomarr

k, filen = int(sys.argv[1]), open(sys.argv[2])

print("Wait creating sample space for searching algorithm test ...")
arr = []
for x in filen:
    arr.append(int(x.strip()))
filen.close()

# Linear Search
def searchLinear(k):
    global flag
    for x in arr:
        if x == k:
            flag = True
            return
    flag = False

def searchBidirectional(k):
    global flag
    i,n = 0, len(arr)-1
    while i<n:
        if arr[i] == k or arr[n] == k:
            flag = True
            return
        i += 1
        n -= 1
    flag = False


flag = False
execution_time = timeit.timeit('searchLinear({})'.format(k), setup='from __main__ import searchLinear', number=1)
print("Linear Search ...")
if flag:
    print("Element found in array")
else: print("Element Not found in array")

print("Execution time ->", execution_time)


flag = False
execution_time = timeit.timeit('searchBidirectional({})'.format(k), setup='from __main__ import searchBidirectional', number=1)
print("Bidirectional Search ...")
if flag:
    print("Element found in array")
else: print("Element Not found in array")

print("Execution time ->", execution_time)

