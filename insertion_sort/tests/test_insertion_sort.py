from insertion_sort import __version__


def test_version():
    assert __version__ == '0.1.0'

from insertion_sort.insertion_sort import insertionSort

def test_version():
    assert __version__ == '0.1.0'

def test_insertionSort():
    actual = [8, 4, 23, 42, 16, 15]
    excepted = [4, 8, 15, 16, 23, 42]
    assert actual == excepted


    