from stack_and_queue.animal_shelter import AnimalSheltr


def test_enqueue():
    expected = 'animal'
    actual = 'Cats, Dogs'
    assert expected == actual, "animal : Cats, Dogs"

def test_dequeue():
    expected = 'name'
    actual = 'pref'
    assert expected == actual, "name : pref"