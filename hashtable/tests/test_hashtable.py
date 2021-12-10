from hashtable import __version__
from hashtable.hashtable import HashTable
import pytest


def test_version():
    assert __version__ == '0.1.0'





@pytest.fixture
def hashtable():
	return HashTable()
    
def test_hash_add(hashtable):
    hashtable.add('Yousef' , 25)
    expected=25
    actual= hashtable.get('Yousef')
    assert actual == expected

def test_hash_not_exist(hashtable):
    hashtable.add('Yousef' , 25)
    expected=None
    actual= hashtable.get('march 10')
    assert actual == expected

def test_hash_handle_collision(hashtable):
    hashtable.add('Yousef' , 25)
    hashtable.add('Yousef' , 40)
    expected=40
    actual= hashtable.get('Yousef')
    assert actual == expected

def test_hash(hashtable):
	expected = 700
	actual = hashtable._HashTable__hash("d")
	assert actual == expected


def test_value_handle_collision(hashtable):
    hashtable.add('Yousef' , 25)
    hashtable.add('Yousef' , 40)
    expected=True
    actual= hashtable.contains('Yousef')
    assert actual == expected