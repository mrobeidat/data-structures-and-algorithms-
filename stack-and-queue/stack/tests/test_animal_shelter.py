from stack_and_queue.animal_shelter import AnimalShelter
import pytest

# @pytest.fixture
# def Can_successfully_add_an_animal(queue):
#      queue = AnimalShelter();
#      queue.enQueue('dog')
#      queue.enQueue('cat')
#      actual = queue.rear.value
#      expected= 'cat';
#      assert actual == expected


shelter = AnimalShelter()

def test_upper_case():
    # Arrange any data that you need to run your test
    shelter.enqueue("CAT")
    shelter.enqueue("DOG")
    # actual output
    actual = shelter.dequeue("CAT")
    # Assert
    expected = "cat"
    assert actual == expected

def test_animal_shelter_dequeue_cat():
    # actual output
    actual = shelter.dequeue("cat")
    # Assert
    expected = "cat"
    assert actual == expected

def test_animal_shelter_dequeue_dog():
    # actual output
    actual = shelter.dequeue("dog")
    # Assert
    expected = "dog"
    assert actual == expected

def test_animal_shelter_dequeue_other_animal():
    # actual output
    actual = shelter.dequeue()
    # Assert
    expected = 'rabbit'
    assert actual != expected

@pytest.fixture(autouse=True)
def arrange():
    for _ in range(5):
        shelter.enqueue("cat")
        shelter.enqueue("dog")

    waiting_animals = ['rabbit','parrot','goat','hamster','kaggle']
    for animal in waiting_animals:
        shelter.enqueue(animal)