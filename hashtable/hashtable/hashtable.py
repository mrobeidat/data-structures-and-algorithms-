class Node:
    def __init__(self, value=None, next_=None):
    
        self.value = value
        self.next = next_

class LinkedList:
    def __init__(self):
     
        self.head = None

    def insert(self, value):
      
        self.head = Node(value, self.head)

class HashTable:
    def __init__(self, size=1024):
      
        self.__size = size
        self.__buckets = [None] * size

    def add(self, key, value):
      
        index = self.__hash(key)

        if not self.__buckets[index]:
          self.__buckets[index] = LinkedList()

        my_value = [key,value]
        self.__buckets[index].insert(my_value)

    def get(self, key):
      index = self.__hash(key)

      if self.__buckets[index]:

        linked_list = self.__buckets[index]
        current = linked_list.head

        while current:
          if current.value[0] == key:
            return current.value[1]
            
          current = current.next

      return None


    def contains(self,key):

        index = self.__hash(key)

        if not self.__buckets[index]:
            return False

        linked_list = self.__buckets[index]
        current = linked_list.head
        while current:

          if current.value[0] == key:

            return True
          current = current.next
    def __hash(self, key):
 
        return sum([ord(char) for char in key]) * 7 % self.__size


    def repeated_word(self,str):
        
        if str == "":
         return str
        arr1 = str.split(',')
        arr2 = ' '.join(arr1)
        arr = arr2.split()
        for value in arr:
            repeted_word = value.lower()
            if self.contains(repeted_word):
                return value
            else:
                self.add(repeted_word,value)


if __name__ == "__main__":
    table = HashTable()
    table.add('Yousef' , 25)
    print(table.get('Yousef'))
    hash = HashTable()
    str="Once upon a time, there was a brave princess who..."
    actual = hash.repeated_word(str)
    print(actual)