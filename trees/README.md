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
## White-Board Process

![](max_tree.jpg)

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
| tree_max | [test_trees.py](https://github.com/mrobeidat/data-structures-and-algorithms-401/blob/trees-max/trees/trees/trees.py) |
