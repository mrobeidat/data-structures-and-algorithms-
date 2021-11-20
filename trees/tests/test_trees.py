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

