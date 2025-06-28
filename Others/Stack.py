class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    def isEmpty(self):
        return True if self.head == None else False
    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
        self.size +=1
    def pop(self):
        if self.head == None:
            return "[ERROR] Stack Underflow!"
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            data = temp.data
            del temp
            self.size -= 1
            return data

    def print_stack(self):
        temp = self.head
        while temp:
            
            print(f"|{temp.data}|")
            temp = temp.next
        
