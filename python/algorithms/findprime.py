import sys
n = int(sys.argv[1])

print("generating numbers. ..")
numbers = list(range(n+1))

print("Prime Lookup Started ...")

p = 2
while p*p <= n:
  if numbers[p] !=  None:
    for i in range(p*p, n+1, p):
        numbers[i] = None
  p += 1

print([x for x in numbers if x])
