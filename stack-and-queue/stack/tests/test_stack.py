from stack_and_queue.stack_and_queue import Stack, Queue 
import pytest


from stack_and_queue import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_push(stack):
    actual=stack.top.value
    expected="34"
    assert expected == actual

def test_pop(stack):
    actual = stack.pop()
    expected = "34"
    assert expected == actual


@pytest.fixture
def stack():
    stack=Stack()
    stack.push(2)
    stack.push("401-python")
    stack.push("34")
    return stack

def test_is_empty():
    """
    Testing is_empty method for a queue
    """
    queue=Queue()
    expected=True
    actual= queue.is_empty()
    assert expected == actual

def test_enqueue():
    """
    Testing enqueue method for a queue
    """
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue("Python")
    expected="Python"
    actual=queue.rear.value

    assert expected == actual

def test_peek(stack):
    actual=stack.peek()
    expected='34'
    assert actual == expected

def test_is_empty_stack():
    stack=Stack()
    assert stack.is_empty() == None


