class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None

  def enqueue(self, data):
    if self.head == None:
      self.head = Node(data)
      self.tail = self.head
    else:
      temp = Node(data)
      self.tail.next = temp
      self.tail = temp

  def dequeue(self):
    if self.head == None:
      print('[Error] Queue Underflow')
      return None
    else:
      temp = self.head
      self.head = self.head.next
      temp.next = None
      data = temp.data
      del temp
      return data

  def isEmpty(self):
    return self.head == None
