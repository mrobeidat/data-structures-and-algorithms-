
from stack_and_queue.stack_queue_pseudo import PseudoQueue

import pytest

def test_enqueue_singl():
    Pseudoqueue = PseudoQueue()
    Pseudoqueue.enqueue(21)
    actual = Pseudoqueue.rear
    expected = 21
    assert expected == actual

def test_enqueue_multiple():
    Pseudoqueue = PseudoQueue()
    Pseudoqueue.enqueue(21)
    Pseudoqueue.enqueue(22)
    Pseudoqueue.enqueue(23)
    actual = Pseudoqueue.rear
    expected = 23
    assert expected == actual


def test_dequeue_ps():
    Pseudoqueue = PseudoQueue()
    Pseudoqueue.enqueue(1)
    Pseudoqueue.enqueue(2)
    Pseudoqueue.enqueue(3)
    Pseudoqueue.dequeue()
    Pseudoqueue.dequeue()
    actual = Pseudoqueue.dequeue()
    expected = 3
    assert expected == actual

def test_dequeue_empty():
    Pseudoqueue = PseudoQueue()
    actual = Pseudoqueue.dequeue()
    expected = None
    assert expected == actual 