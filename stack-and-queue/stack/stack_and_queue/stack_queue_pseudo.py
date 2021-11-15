from stack_and_queue.stack_and_queue import Node, Stack


class PseudoQueue:
    def __init__(self):
        self.first_stack = Stack()
        self.secand_stack = Stack()
        self.rear = None
        self.front = None

    def enqueue(self, value):
        self.first_stack.push(value)
        self.rear = self.first_stack.top.value

    def dequeue(self):

        if self.first_stack.top:
            stack1 = self.first_stack

            while not stack1.isEmpty():
                self.secand_stack.push(stack1.pop())

            poped = self.secand_stack.pop()
            self.front = self.secand_stack.top
            self.first_stack = Stack()
            stack2 = self.secand_stack

            while not stack2.isEmpty():

                self.first_stack.push(stack2.pop())

            return poped

    def __str__(self):
        content = ''
        current = self.first_stack.top
        while current:
            content += f"{{{str(current.value)}}} -> "
            current = current.next
        content += " Null"
        return content


if __name__ == "__main__":
    queue = PseudoQueue()
    queue.enqueue(5)
    print(queue.__str__())
    queue.enqueue(7)
    print(queue.__str__())
    queue.enqueue(9)
    print(queue.__str__())
    queue.dequeue()
    print(queue.__str__())
    queue.dequeue()
    print(queue.__str__())
    queue.dequeue()
    print(queue.__str__())