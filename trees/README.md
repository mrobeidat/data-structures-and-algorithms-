# Trees


* 1- K-ary Trees :

*If Nodes are able have more than 2 child nodes, we call the tree that contains them a K-ary Tree. In this type of tree we use K to refer to the maximum number of children that each Node is able to have.* 


* 2- Binary Search Trees :

*A Binary Search Tree (BST) is a type of tree that does have some structure attached to it. In a BST, nodes are organized in a manner where all values that are smaller than the root are placed to the left, and all values that are larger than the root are placed to the right.* 

* Traversals :

***An important aspect of trees is how to traverse them. Traversing a tree allows us to search for a node, print out the contents of a tree, and much more! There are two categories of traversals when it comes to trees:***

- 1- Depth First :

*Depth first traversal is where we prioritize going through the depth (height) of the tree first. There are multiple ways to carry out depth first traversal, and each method changes the order in which we search/print the root. Here are three methods for depth first traversal:*

* Pre-order: root >> left >> right

* In-order: left >> root >> right

* Post-order: left >> right >> root

 

* 2- Breadth First :

*Breadth first traversal iterates through the tree by going through each level of the tree node-by-node.*


### Features

> Node
**Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.**

> Binary Tree
**Create a Binary Tree class**
    
*Define a method for each of the depth first traversals:*

1. pre order
2. in order
3. post order which returns an array of the values, ordered appropriately.
    
* Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

> Binary Search Tree
**Create a Binary Search Tree class** 

*This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:*

- Add
            
1. Arguments: value
2. Return: nothing
3. Adds a new node with that value in the correct location in the binary search tree.

- Contains

1. Argument: value
2. Returns: boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency

- What approach did you take ? 

**Algorithm**

- Why ?

**Because it is Binary and Binary search trees** 

- What is the Big O space/time for this approach ?

**Space : O(1), Because : not allocating any additional space.** 

**Time : O(h), Because : have to search all the way down to a leaf**


| Subject     | links |
| ----------- | ----------- |
| binary_tree | [binary_tree](trees/trees.py) |
| test_trees | [test_trees.py](tests/test_trees.py) |