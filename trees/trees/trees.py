
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None

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


