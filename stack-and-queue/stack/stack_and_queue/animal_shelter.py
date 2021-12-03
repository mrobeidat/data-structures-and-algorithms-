from stack_and_queue.stack_and_queue import Queue, Stack


# class AnimalShelter(Queue):


#     def enqueue(self, value):
#         if (value == 'cat' or value == 'dog'):
#           self.enqueue(value)

#         else: return 'please add a dog or a cat'


#     def dequeue(self,pref):
#         if (pref == 'cat' or pref == 'dog'):
#             return self.dequeue(pref)

#         elif (pref != 'cat' or pref != 'dog'):
#          return None

#         else:
#             return 'please select a dog or a cat';
class AnimalShelter:
    def __init__(self):
        self.dog = Queue()
        self.cat = Queue()
        self.waiting = Stack()

    def enqueue(self, animal):
        if animal.lower() == "dog":
            self.dog.enqueue(animal.lower())
        if animal.lower() == "cat":
            self.cat.enqueue(animal.lower())
        else:
            self.waiting.push((animal.lower()))

    def dequeue(self, pref='wating'):
        if pref.lower() == "dog":
            return self.dog.dequeue()

        if pref.lower() == "cat":
            return self.cat.dequeue()

        if pref == 'wating':
            return self.waiting.pop()
        else:
            return 'Null'
