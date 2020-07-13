class Queue:
  def __init__(self, size = 10):
    self.size = 10
    self.front = -1
    self.rear = -1
    self.queue = [None] * size

  def isEmpty(self):
    return self.rear == -1

  def isFull(self):
    return (self.rear+1) % self.size == self.front

  def peek(self):
    if not self.isEmpty():
      return self.queue[self.front]

  def enqueue(self, e):
    if self.isFull():
      print("Queue is Full")
    elif self.isEmpty():
      self.front += 1
      self.rear += 1
      self.queue[self.rear] = e
    else:
      self.rear = (self.rear+1)%self.size
      self.queue[self.rear] = e

  def dequeue(self):
    if not self.isEmpty():
      if self.front == self.rear:
        e = self.queue[self.front]
        self.front, self. rear = -1, -1
        return e
      else:
        e = self.queue[self.front]
        self. front = (self.front+1) % self.size
        return e

  def printQueue(self):
    x = self.front
    while x!= self.rear:
      print(self.queue[x])
      x = (x+1)%self.size
    print(self.queue[x])

print("Initilizing Circular Queue....")
queue = Queue()
print("Is queue is empty: {}".format(queue.isEmpty()))

print("Adding element to queue")
for x in range(1, 11):
  print(x)
  queue.enqueue(x)

queue.enqueue(100)
print("Removing element: {}  from queue".format(queue.dequeue()))
print("Removing element: {}  from queue".format(queue.dequeue()))
print("Removing element: {}  from queue".format(queue.dequeue()))
print("Removing element: {}  from queue".format(queue.dequeue()))
print("Adding element to the Queue")
for x in [101, 102, 103, 104, 105]:
  print("Adding element to queue: {}".format(x))
  queue.enqueue(x)
print("Queue elements")
queue.printQueue()
