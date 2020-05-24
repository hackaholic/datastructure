import timeit

import sys

n = sys.argv[1]

def methodone(n):
    arr = range(n)
    count = 0
    for x in arr:
        count +=1

# len built in function
print("len inbuilt function execution time ->", end= " ")
print(timeit.timeit("arr=range({});k=len(arr)".format(n), number=1))

print("Methodone Execution time -> ", timeit.timeit('methodone({})'.format(n), setup="from __main__ import methodone", number=1))
