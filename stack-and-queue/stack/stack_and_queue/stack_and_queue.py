
# class Node:

#     def __init__(self, value=None):
#         self.next=None
#         self.value=value


# class Stack:
#     """
#     a class that implements the Stack Data structure
#     """
#     def __init__(self):
#         self.top=None

#     def push(self, value):
#         node = Node(value)
#         if self.top:
#             node.next=self.top

#         self.top=node


#     def pop(self):

#         if self.top == None:
#           raise EmptyStack("This stack is empty")
#         temp =self.top
#         self.top=self.top.next
#         temp.next=None
#         return temp.value


#     def peek(self):
#        if self.is_empty():
#         raise Exception("This stack is empty")
#        return self.top.value

#     def is_empty(self):
#         return not self.top

#     def is_empty(self):
#         pass

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None


"""Stack class and methdos"""


class Stack:

    def __init__(self):
        self.top = None


    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node


    def pop(self):
        if self.top == None:
            raise Exception("This stack is empty")
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value


    def peek(self):
        if self.is_empty():
            raise Exception("This stack is empty")
        return self.top.value


    def is_empty(self):
        return not self.top


# class Queue:
#     """
#     a class that implements the Queue Data structure
#     """
#     def __init__(self):
#         self.front = None
#         self.rear = None


#     def enqueue(self, value):
#         node=Node(value)

#         if not self.rear:
#             self.front = node
#             self.rear = node
#         else:
#             self.rear.next = node
#             self.rear = node

#     def dequeue(self):
#         pass

#     def peek(self):
#         pass

#     def is_empty(self):
#         return self.front == None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None


    def enqueue(self, value):
        node = Node(value)
        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node


    def dequeue(self):
        if self.is_empty():
            raise Exception("This stack is empty")
        if self.front is None:
            return None
        front = self.front.value
        self.front = self.front.next
        return front


    def peek(self):
        if self.is_empty():
            raise Exception("This stack is empty")
        return self.front.value


    def is_empty(self):
        return not self.front
