

Cat = []
Dog = []

class AnimalShelter:
    def __init__(self):

        self.cats = Cat()

        self.dogs = Dog()

    def enqueue(self, animal):

        if animal.name == 'cats':

            self.cats.enqueue(animal)

        elif animal.name == 'dogs':

            self.dogs.enqueue(animal)
        else:

            return 'NOT Cat, NOT Dog'

    def dequeue(self, pref=None):
        if pref == 'cats':

            return self.cats.dequeue().name

        elif pref == 'dogs':

            return self.dogs.dequeue().name

        else:

            return None
