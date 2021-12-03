from trees import __version__
from trees.trees import *
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_empty_tree():
    expected = None
    tree = BinaryTree()
    actual = tree.root

    assert expected == actual

def test_tree_with_single_node():
    expected = "A"
    tree = BinaryTree()
    a_node = Node('A')
    tree.root = a_node
    actual = tree.root.data

    assert actual == expected

def test_pre_order():

    tree = BinaryTree()
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    tree.root = a_node
    expected = ["1", "2", "4", "3"]
    actual = tree.pre_order()
    assert actual == expected

def test_post_order():
   
    tree = BinaryTree()
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    tree.root = a_node
    expected = ["4", "2", "3", "1"]
    actual = tree.post_order()
    assert actual == expected

def test_in_order():
    tree = BinaryTree()
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    tree.root = a_node
    expected = ["4", "2", "1", "3"]
    actual = tree.in_order()
    assert actual == expected


def test_maximum_num_in_tree():
    expected = 5
    tree = BinarySearchTree()
    tree.add(3)
    tree.add(1)
    tree.add(5)
    tree.add(2)

    actual = tree.get_max()
    assert actual == expected

def test_max_of_empty_tree():
    with pytest.raises(Exception):
        tree = BinaryTree()
        actual = tree.get_max()


def test_breadth_first_2():
   
    tree = BinaryTree()
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    tree.root = a_node
    expected = ["1", "2", "3", "4"]
    actual = tree.breadth_first()
    assert actual == expected

    
"""*********************Fizz_Buzz_Tree********************"""

def test_If_value_divisible_by_3():
    tree= KTree()
    tree.root = Node_2(3)
    excepted = 'Fizz'
    actual = fizz_buzz_tree(tree.root).value
    assert excepted == actual

def test_If_value_divisible_by_5():
    tree= KTree()
    tree.root = Node_2(3)
    tree.root.child.append(Node_2(5))
    excepted = 'Buzz'
    actual = fizz_buzz_tree(tree.root).child[0].value
    assert excepted == actual

def test_If_value_divisible_by_3_and_5_():
    tree= KTree()
    tree.root = Node_2(3)
    tree.root.child.append(Node_2(5))
    tree.root.child.append(Node_2(15))
    excepted = 'FizzBuzz'
    actual = fizz_buzz_tree(tree.root).child[1].value
    assert excepted == actual

def test_If_value_not_divisible_by_3_or_5():
    tree= KTree()
    tree.root = Node_2(3)
    tree.root.child.append(Node_2(5))
    tree.root.child.append(Node_2(2))
    excepted = '2'
    actual = fizz_buzz_tree(tree.root).child[1].value
    assert excepted == actual