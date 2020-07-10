class Stack:
  def __init__(self, size=10):
    self.stack = [None]*size
    self.size = 10
    self.top = -1

  def push(self, e):
    if self.isFull():
      print("StackOverflow")
    else:
      self.top += 1
      self.stack[self.top] = e

  def pop(self):
    if self.isEmpty():
       print("Stack Empty")
       return
    self.top -= 1
    return self.stack[self.top+1]

  def peek(self):
    return self.stack[self.top]

  def isEmpty(self):
      return (False, True)[self.top == -1]

  def isFull(self):
    return (False , True)[self.size == self.top+1]

stack = Stack()
print("Stack empty: {}".format(stack.isEmpty()))
for x in range(1,11):
  stack.push(x)
print("Peeking Stack: {}".format(stack.peek()))
print("Stack full: {}".format(stack.isFull()))

print("Stack Elements")
for x in range(10):
    print(stack.pop())
stack.pop()
