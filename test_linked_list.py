from linked_list.linked_list import LinkedList,Node
import pytest
# 1-Can successfully instantiate an empty linked list
def test_node_has_int_data():
  expected = None
  ll = LinkedList()
  actual = ll.head
  assert actual == expected
## 2-Can properly insert into the linked list
def test_node_has_str_data():
    expected = "a"
    node = Node("a")
    actual = node.data
    assert actual == expected
# 3-The head property will properly point to the first node in the linked list
def test_linked_list_insert():
  # Arrange
  expected = 1
  ll = LinkedList()
  ll.insert(1)
  node = ll.head
  actual = node.data
  assert actual == expected
#4-Can properly insert multiple nodes into the linked list
def test_linked_list_insert_twice():
  # Arrange
  expected = 0
  ll = LinkedList()
  # Act
  ll.insert(1)
  ll.insert(0)
  node = ll.head
  actual = node.data
  # Assert
  assert actual == expected
  assert ll.head.next.data == 1
#5-Will return true when finding a value within the linked list that exists
def test_includes_True():
    expected = True
    ll=LinkedList()
    ll.insert(1)
    actual = ll.includes(1)
    expected = True
    assert actual == expected
#6-Will return false when searching for a value in the linked list that does not exist
def test_includes_False():
    expected = False
    ll=LinkedList()
    ll.insert(0)
    actual = ll.includes(1)
    expected = False
    assert actual == expected
#7-Can properly return a collection of all the values that exist in the linked list
def test_return_all_values():
    ll = LinkedList()
    ll.append('m')
    ll.append('o')
    ll.append('h')
    actual = ll.__str__()
    expected = '( m ) -> ( o ) -> ( h ) -> None'
    assert actual == expected
# 8- test the append value function in the linked list
def test_append_value():
  expected = 9
  ll = LinkedList()
  ll.append(9)
  node = ll.head
  actual = node.data
  assert actual == expected
#9- Can successfully add multiple nodes to the end of a linked list
def test_multi_to_the_end():
    ll = LinkedList()
    ll.append(5)
    ll.append(4)
    ll.append(3)
    ll.append(2)
    ll.append(2)
    actual = ll.__str__()
    expected = '( 5 ) -> ( 4 ) -> ( 3 ) -> ( 2 ) -> ( 2 ) -> None'
    assert actual == expected

#Can successfully insert a node after a node located i the middle of a linked list
def test_after_middle():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_after(2, 5 )
    actual = ll.__str__()
    expected = '( 1 ) -> ( 2 ) -> ( 5 ) -> ( 3 ) -> None'
    assert actual == expected
# Can successfully insert a node before the first node of a linked list
def test_before_first():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_before(1, '5')
    actual = ll.__str__()
    expected = '( 5 ) -> ( 1 ) -> ( 2 ) -> ( 3 ) -> None'
    assert actual == expected
#Can successfully insert before a node in the middle of the linked list
def test_before_middle():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_before(2, '5')
    actual = ll.__str__()
    expected = '( 1 ) -> ( 5 ) -> ( 2 ) -> ( 3 ) -> None'
    assert actual == expected
# Can successfully insert a node after the last node of the linked list
def test_after_last():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_after(3, 5 )
    actual = ll.__str__()
    expected = '( 1 ) -> ( 2 ) -> ( 3 ) -> ( 5 ) -> None'
    assert actual == expected

    #1- Where k is greater than the length of the linked list
def test_if_k_bigger_than_numo_f_node():
    ll = LinkedList()
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    ll.append(9)
    ll.append(10)
    x=ll.kthFromEnd(20)
    assert x == "Number of K is bigger than the number of Nodes !!!"

#2- Where k and the length of the list are the same
def test_if_k_and_length_of_node_same():
    ll = LinkedList()
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    ll.append(9)
    ll.append(10)
    # ll.kthFromEnd(5)
    assert str(ll.kthFromEnd(5)) == '5'

#3- Where k is not a positive integer
def test_if_k_not_positive_integer():
    ll = LinkedList()
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    ll.append(9)
    ll.append(10)
    x = ll.kthFromEnd(-12)
    assert x == "K is negative"

#4- Where the linked list is of a size 1
def test_ll_size_1():
    ll = LinkedList()
    ll.append(5)
    assert str(ll.kthFromEnd(0))=='5'