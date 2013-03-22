AvlTree

Had to code this up recently, thought I'd share.

An implementation of AVL trees.
Handles duplicate items.
Works on any datatype for which comparison operators are defined (tested on strings and numbers)

Note: haven't had time to test delete operator yet, use 'beta version' at own risk.

To run tests:
'python path/to/AvlTreeTests.py'

To use:
from AvlTree import AvlTree

b = AvlTree()

b.insert(5)
b.insertAll([5,3,4])
b.contains(10)

for x in b:
    # do stuff