
class heap:
  def __init__(self, arr):
    self.heap = []
    self.heap_size = 0
    if arr:
      self.heap = arr
      self.heap_size = len(arr)

  def printheap(self):
    for i in range(self.heap_size -1):
      print(self.heap[i], end=", ")
    print(self.heap[i+1])

  def heapify(self, i):
    largest = i
    left_child, right_child = 2*i + 1, 2*i + 2
    if left_child < self.heap_size and self.heap[left_child] > self.heap[largest]:
      largest = left_child
    
    if right_child < self.heap_size and self.heap[right_child] > self.heap[largest]:
      largest = right_child

    if i != largest:
      self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
      self.heapify(largest)

  def buildheap(self):
    n = self.heap_size
    for i in range((n//2) -1, -1, -1):
      self.heapify(i)

  def extract_max(self):
    if self.heap_size > 0:
      self.heap[0], self.heap[self.heap_size-1] = self.heap[self.heap_size-1], self.heap[0]
      self.heap_size -= 1
      self.heapify(0)
      return self.heap[self.heap_size]

  def insert(self, k):
    self.heap.append(k)
    self.heap_size += 1
    self.heapify((self.heap_size//2)-1)

arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
myheap = heap(arr)
myheap.buildheap()
myheap.printheap()

#while myheap.heap_size > 0:
#    print(myheap.extract_max())

myheap.insert(7)
print(arr)
