pyavl

An implementation of AVL trees in Python.
Handles duplicate items.
Works on any datatype for which comparison operators are defined (tested on strings and numbers)

To run tests:

    python path/to/pyavlTests.py

To use:

    from pyavl import AvlTree

    b = AvlTree()

    b.insert(5)
    b.insertAll([5,3,4])
    b.contains(10)
    b.delete(3)

    for x in b:
        # iterator yields items in ascending sorted order
