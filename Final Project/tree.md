# Tree Data Structure Tutorial
## Introduction
A Tree is a linked list, except each node in the tree can connect to multiple nodes, like how a branch in a tree can connect to multiple other smaller branches. There are multiple types of trees, including Binary Trees, Binary Search Trees (BST), and Balanced Binary Search Trees.
## Binary Tree
- A Binary Tree is a tree in which each node can connect to between 2 and 0 other nodes. The node from which all others stem is the root node. The nodes which connect to no other nodes are called leaf nodes. A node which connects to other nodes is called a parent node, and the nodes which follow it are called child nodes. The nodes to the left or to the right of any parent node is called a subtree. 

## Binary Search Tree (BST)
- A binary search tree is a tree which abides by certain rules which make it easy to find data within it. Relative to the root, all smaller values are placed to the left of it and larger ones are placed to its right. No duplicate values are permitted in a binary search tree. 

## Inserting data into a BST
- When a new value is inserted into a tree, the following process is used to find where it should go:
1. Step 1: If value is less than the root, value goes left.
2. Step 2: If no value exists going left, that’s where it should go. Otherwise, select the value to the right and go back to step one and compare it to the value.
3. Step 3: Else if value is greater than root, value goes right. 
- Step 4: If no value exists going right, that’s where it should go. Otherwise, select the value to the right and go back to step one and compare it to the value.
- Accessing data from a BST
- To access data in a BST, if you are looking for a particular value then simply iterate through the tree until you find the value you are looking for. Compare the value you want to the root. If it is smaller than the root, then traverse left. If it is larger, then traverse right. Continue this process until you find the value you want.
## Example in Python
- 
## Problem to solve
- 