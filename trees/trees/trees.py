
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Queue:
  def __init__(self, collection=[]):
    self.data = collection

  def peek(self):
    if len(self.data):
      return True
    return False

  def enqueue(self,item):
    self.data.append(item)

  def dequeue(self):
    return self.data.pop(0)
    
class BinaryTree:

    def __init__(self):
        self.root = None
    def breadth_first(self):
       
        breadth = Queue()
        breadth.enqueue(self.root)

        list_of_items = []

        while breadth.peek():
         front = breadth.dequeue()
         list_of_items += [front.data]

         if front.left is not None:
            breadth.enqueue(front.left)

         if front.right is not None:
            breadth.enqueue(front.right)

        return list_of_items

    def pre_order(self):
      
        list_of_items = []

        def walk(node):
            if node:
                list_of_items.append(node.data)
                if node.left:
                    walk(node.left)
                if node.right:
                    walk(node.right)

        walk(self.root)
        return list_of_items

    def in_order(self):
       
        list_of_items = []

        def walk(node):
            if node:
                if node.left:
                    walk(node.left)
                list_of_items.append(node.data)

                if node.right:
                    walk(node.right)

        walk(self.root)

        return list_of_items

    def post_order(self):
   
        list_of_items = []

        def walk(node):
            
            if node:
                if node.left:
                    walk(node.left)
                if node.right:
                    walk(node.right)
                list_of_items.append(node.data)

        walk(self.root)

        return list_of_items

    def get_max(self):

        self.max = self.root.data

        def max_num(node):
            if node.data > self.max:
              self.max = node.data
            if node.left:
                max_num(node.left)
            if node.right:
                max_num(node.right)
            return self.max
            
        if not self.root:
            raise Exception("The Tree is empty !!!")

        return max_num(self.root)

    
class BinarySearchTree(BinaryTree):
   

    def add(self, value):


        if not self.root:
            self.root = Node(value)

        else:
            temp = self.root
            while temp:

                if value < temp.data:
                    if not temp.left:
                        temp.left = Node(value)
                        break
                    temp = temp.left

                else:
                    if not temp.right:
                        temp.right = Node(value)
                        break
                    temp = temp.right

    def __contains__(self, value):
       
        if not self.root:
            raise Exception("Empty Tree !!!")

        else:
            temp = self.root
            while temp:
                if temp.data == value:
                    return True
                elif temp.data > value:
                    if not temp.left:
                        return False
                    temp = temp.left
                else:
                    if not temp.right:
                        return False
                    temp = temp.right

def breadth_first(self):
    """
    A binary tree method which returns a list of items that it contains
    input: None
    output: tree items
    """
    breadth = Queue()
    breadth.enqueue(self.root)

    list_of_items = []

    while breadth.peek():
      front = breadth.dequeue()
      list_of_items += [front.data]

      if front.left:
        breadth.enqueue(front.left)

      if front.right:
        breadth.enqueue(front.right)

    return list_of_items