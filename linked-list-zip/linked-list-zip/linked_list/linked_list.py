
class Node:
    """
    A class representing a Node
    """
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

class LinkedList:
    """
      A class for creating instances of a Linked List.
    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        """"
        Adds a new node with that value to the head of the list with an O(1) Time performance.
        """
        # create new node


        node = Node(value)
        self.head = Node(value, self.head)


    def includes(self, data):
        """Indicates whether that value exists as a Node’s value somewhere within the list.
        """
        value=self.head
        while value :
          if value.data==data:
              value= value.next
              return True
          else:
              return False

        """ Returns: a string representing all the values in the Linked List, formatted as:
        "{ a } -> { b } -> { c } -> NULL" """
    def __str__(self):
        output = ""
        current = self.head
        while current:
            value = current.data
            if current.next is None:
                output += f"( {value} ) -> None"
                break
            output = output + f"( {value} ) -> "
            current = current.next
        return output
    def append(self, value='null'):

          node = Node(value)
          if not self.head:
              self.head = node

          else:
              crrval = self.head
              while crrval.next != None:
                  crrval = crrval.next
              crrval.next = node
    """
    Code Challenge: Class 06
    """
    """
    insert before adds a new node with the given new value
    immediately before the first node that has the value specified
    """
    def insert_before(self, value, new):
        current = self.head
        if current.data == value:
            self.insert(new)
        else:
          while current:
             if current.next.data == value:
                value = current.next
                current.next = Node(new)
                current.next.next = value
                break
             current = current.next
    """
    insert after adds a new node with the given new value
    immediately after the first node that has the value specified
    """
    def insert_after(self, value, new):
        current = self.head
        while current:
            if current.data == value:
                value = current.next
                current.next = Node(new)
                current.next.next = value
                break
            current = current.next

    """
    Code Challenge: Class 07
    """
    def kthFromEnd(self, k):
        if k < 0:
            return "K is negative"
        node_num = 0
        current = self.head
        while current: # count the nodes
            current = current.next
            node_num = node_num + 1

        if node_num >= k:
            current = self.head # reset the current value to start the count from the beggining node
            for i in range(node_num - k-1): #k-1 to remove null
                current = current.next
        else:
            return "Number of K is bigger than the number of Nodes !!!"
        return current

    """
    Code Challenge: Class 08
    """
    def zip_list(self,list1=None, list2=None):
        """
        zip two linked list together
        """
        if list1.head and list2.head:
            temp1=list1.head.next
            temp2=list2.head.next
            list1.head.next=list2.head
            current = list1.head.next

            while(current.next and temp1 and temp2):
                current.next = temp1
                current = current.next
                temp1= current.next
                current.next = temp2
                current=current.next
                temp2= current.next

            while temp1:
                current.next = temp1
                current = current.next
                temp1 = current.next

            while temp2:
                current.next = temp2
                current = current.next
                temp2 = current.next

            return list1

        else:
            if list1.head:
                return list1
            elif list2.head:
                return list2
            else:
                return None