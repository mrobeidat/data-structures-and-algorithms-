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

def test_repeted_word(hashtable):
    str="Once upon a time, there was a brave princess who..."
    actual = hashtable.repeated_word(str)
    expected = 'a'
    assert actual == expected

def test_repeted_word_2(hashtable):
    str="It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    actual = hashtable.repeated_word(str)
    expected = 'summer'
    assert actual == expected

def test_repeted_word_3(hashtable):
    str="It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actual = hashtable.repeated_word(str)
    expected = "it"
    assert actual == expected
    
def test_empty_string(hashtable):
    "test repeated_word"
    assert hashtable.repeated_word('') == ''