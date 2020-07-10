class Queue:
  def __init__(self, size=10):
    self.size = 10
    self.front, self.rear = -1, -1
    self.queue = [None] * size

  def isEmpty(self):
    return self.front == -1

  def isFull(self):
    return self.size == self.rear+1

  def enqueue(self, e):
    if self.isFull():
      print("Queue Full")
      return 
    elif self.front == -1 and self.rear == -1:
      self.front += 1
      self.rear += 1
      self.queue[self.rear] = e
    else:
      self.rear += 1
      self.queue[self.rear] = e
    print("Added element {} to queue".format(e))

  def peek(self):
    if not self.isEmpty():
      return self.queue[self.front]

  def dequeue(self):
    if self.isEmpty():
      print("Queue is Empty")
    else:
      if self.rear == 0:
        e = self.queue[self.front]
        self.front, self.rear = -1, -1
        return e
      e = self.queue[self.front]
      for i in range(1, self.rear+1):
          self.queue[i-1] = self.queue[i]
      self.rear -= 1
      return e

queue = Queue()
print("Queue Empty: {}".format(queue.isEmpty()))
print("Enqueing element")
for x in range(20):
  if queue.isFull():
    break
  queue.enqueue(x)

print("Queue Full: {}".format(queue.isFull()))
print("Peeking element: {}".format(queue.peek()))
print("Deque elements")
for x in range(20):
  if queue.isEmpty():
    break
  print("Removing Element: {}".format(queue.dequeue()))

