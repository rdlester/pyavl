from AvlTree import *
from random import randint
import ipdb

""" Set of tests for IBinTree implementation
"""
# test over standard tree
b = AvlTree()
lst = [5,3,8,9,1,10,2]
b.insertAll(lst)

# test that balancing is correct
root = b.root
assert root.height == 2
assert root.value == 5

assert root.left.left.value == 1
assert root.left.left.height == 0
assert root.left.right.value == 3
assert root.left.right.height == 0
assert root.left.value == 2
assert root.left.height == 1

assert root.right.left.value == 8
assert root.right.left.height == 0
assert root.right.right.value == 10
assert root.right.right.height == 0
assert root.right.value == 9
assert root.right.height == 1

# check iterator returns sorted list correctly
lst.sort()
i = 0
for x in b:
    assert x == lst[i]
    i = i+1

# check contains
assert b.contains(1)
assert b.contains(2)
assert b.contains(3)
assert b.contains(5)
assert b.contains(8)
assert b.contains(9)
assert b.contains(10)

assert not b.contains(100)
assert not b.contains(-1)

# test deletion
b.delete(2)
assert root.left.value == 1

b.delete(1)
assert root.left.value == 3
assert root.left.height == 0

b.delete(3)
newRoot = b.root
assert newRoot.value == 9
assert newRoot.height == 2
assert newRoot.left.value == 5
assert newRoot.left.height == 1
assert newRoot.left.right.value == 8
assert newRoot.left.right.height == 0
assert newRoot.right.value == 10
assert newRoot.right.height == 0

# check dups (and normal insert)
bdup = AvlTree()
for i in range(0,10):
    bdup.insert(100)

assert bdup.contains(100)

rootdup = bdup.root
assert rootdup.height == 0
assert rootdup.dups == 10

# stress test!
bs = AvlTree()
lst2 = [randint(-1000,1000) for i in range(0,10000)] # note there will be repeats
bs.insertAll(lst2)
lst2.sort()
i = 0
for xs in bs:
    assert xs == lst2[i]
    i = i+1

# test on strings
lsts = ['bbc', 'aab', 'ebe', 'ooskfof', 'hello', 'world', 'sandler', 'dave']
bss = AvlTree()
bss.insertAll(lsts)
lsts.sort()
i = 0
for xss in bss:
    assert xss == lsts[i]
    i = i+1