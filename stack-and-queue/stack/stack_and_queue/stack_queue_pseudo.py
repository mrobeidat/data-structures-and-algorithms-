from stack_and_queue.stack_and_queue import Stack, Node


class Pseudo_queue():

    def __init__(self):

        self.front = None
        self.rear = None
        self.stack_1 = Stack()
        self.stack_2 = Stack()

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

    def is_empty(self):
        return self.front == None

