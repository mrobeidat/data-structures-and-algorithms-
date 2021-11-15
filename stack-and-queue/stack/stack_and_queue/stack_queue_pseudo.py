class Node:
            def __init__(self, value):
                self.value = value
                self.next = None

class pseudo_queue(object):
              
                def __init__(self, size):
                    self.stack1=[]

                    self.stack2=[]

                    self.queue = []

                    self.size = size

                def enqueue(self, value):
                    if(self.isFull() != True):
                        self.queue.insert(0, value)
                    else:
                        print('Queue is Full!')



                def dequeue(self):
                    if(self.isEmpty() != True):
                        return self.queue.pop()
                    else:
                        print('Queue is Empty!')



                def peek(self):
                    if(self.isEmpty() != True):
                        return self.queue[-1]
                    else:
                        print('Queue is Empty!')



                def isEmpty(self):
                    return self.queue == []



                def isFull(self):
                    return len(self.queue) == self.size



                def __str__(self):
                    myString = ' '.join(str(i) for i in self.queue)
                    return myString



if __name__ == '__main__':
  myQueue = pseudo_queue(10)
  myQueue.enqueue(20)
  myQueue.enqueue(15)
  myQueue.enqueue(10)

  print(myQueue)

  myQueue.enqueue(5)

  print(myQueue)

  myQueue.dequeue()

  print(myQueue)