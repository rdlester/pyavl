AvlTree

An implementation of AVL trees in Python.
Handles duplicate items.
Works on any datatype for which comparison operators are defined (tested on strings and numbers)

To run tests:

    python path/to/AvlTreeTests.py

To use:

    from AvlTree import AvlTree

    b = AvlTree()

    b.insert(5)
    b.insertAll([5,3,4])
    b.contains(10)
    b.delete(3)

    for x in b:
        # do stuff
