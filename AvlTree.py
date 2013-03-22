class AvlNode:
    """
    An interface for an sorted binary tree.

    Implementation notes:
    Implemented as Balanced BST (AVL tree)
    Sorted from left/min to right/max
    Works by default for any objects with defined comparison operators
    
    You can use IBinNode directly, but need to resave root after ever insertion
    ie: "b = b.insert(5)" instead of "b.insert(5)", as b may no longer be the root
    Use the IBinTree wrapper class (below) if you don't want to deal with this
    
    Duplicates are handled by keeping an internal "dups" count at each node
    and incrementing w/e a duplicate value is added
    
    This can easily be extended to store key,value pairs
    """

    def __init__(self, value=None):
        """ Init a node
            value is value assigned to node, defaults to "None" (leaf node)
        """
        self.value = value
        self.dups = 1
        if self.value is not None:
            self.height = 0
            self.left = AvlNode(None)
            self.right = AvlNode(None)
        else:
            self.height = -1
            self.left = None
            self.right = None

    def __iter__(self):
        """ Return generator
        """
        return self.gen()

    def gen(self):
        """ Iterator object implemented as Python generator
        """
        if self.value is not None:
            # iterate over left subtree
            for x in self.left.gen():
                yield x
        
            # yield selfb
            for i in range(0,self.dups):
                yield self.value
    
            # iterate over right subtree
            for x in self.right.gen():
                yield x
    

    def insert(self, value): 
    	"""
    	Insert an object into the binary tree. 
    	Note: The tree should be sorted, inserting the same object 
    	twice is allowed but the insert is expected to be stable.
        
        Returns new root.
    	"""
        # examine current node
        if self.value is None:
            # leaf node - insert here
            self.value = value
            self.height = 0
            self.left = AvlNode()
            self.right = AvlNode()
            return self
        else:
            # keep searching
            if value == self.value:
                # add to dup count
                self.dups = self.dups+1
                
            elif value < self.value:
                # search left
                self.left = self.left.insert(value)
                self.height = max(self.left.height+1, self.height)
                
            else:
                # search right
                self.right = self.right.insert(value)
                self.height = max(self.right.height+1, self.height)
            
            # check and correct balance
            return self.correctBalance()
    
    def correctBalance(self):
        """ Subroutine to correct balance of tree
            Returns new root
        """
        balance = self.balanceDiff()
        
        if balance < -1:
            # rebalance right
            rbalance = self.right.balanceDiff()
            if rbalance == -1:
                return self.rotateLeft()
            if rbalance == 1:
                self.right = self.right.rotateRight()
                return self.rotateLeft()
                
        elif balance > 1:
            # rebalance left
            lbalance = self.left.balanceDiff()
            if lbalance == 1:
                return self.rotateRight()
            elif lbalance == -1:
                self.left = self.left.rotateLeft()
                return self.rotateRight()
        
        else:
            # no change to root
            return self
    
    def rotateRight(self):
        """ Right tree rotation
            Returns new root
        """
        temp = self.left
        self.left = temp.right
        temp.right = self
        self.height = max(self.left.height+1, self.right.height+1)
        temp.height = max(temp.left.height+1, temp.right.height+1)
        return temp
    
    def rotateLeft(self):
        """ Left tree rotation
            Returns new root
        """
        temp = self.right
        self.right = temp.left
        temp.left = self
        self.height = max(self.left.height+1, self.right.height+1)
        temp.height = max(temp.left.height+1, temp.right.height+1)
        return temp
    
    def balanceDiff(self):
        """ Returns balance of node
        """
        return self.left.height - self.right.height
            
    def insertAll(self, values): 
    	"""
    	Batch-insert multiple elements.
        Ryan: I changed the var name, as list conflicts with a keyword
    	"""
        root = self
        for x in values:
            root = root.insert(x)
        return root
    
    def delete(self, value):
        """ Deletes node containing value
            maintains balance
        """
        if self.value is None:
            # base case
            # don't delete anything
			return self
        else:
            if self.value == value:
                # delete something
                if self.dups > 1:
                    self.dups = self.dups - 1
                    return self
                else:
                    # replace root w/ max from left subtree
                    # and rebalance
                    newRoot = findMax(self.left)[0]
                    newRoot.left = self.left
                    newRoot.right = self.right
                    newRoot.height = max(newRoot.left.height+1, newRoot.right.height+1)
                    return newRoot.checkBalance()
            else:
                # keep searching
                if value < self.value:
                    self.left = self.left.delete(value)
                else:
                    self.right = self.right.delete(value)
                
                self.height = max(self.left.height+1, self.right.height+1)
                return self.checkBalance()

    def findMax(self):
        """ Helper for delete routine
            Finds max node in subtree
            return it and delete it
            Returns tuple, element 0 is the max node you'll want
        """
        if self.value is None:
            return (None, false, self)
        else:
            maxtup = findMax(self.right)
            if maxtup[0] is None:
                # return self and set second entry in tuple to true
                # to signal parent to remove max node
                return (self, true, None)
            elif maxtup[1]:
                # delete the max node
                # set to max node's left
                # (so we don't accidentally delete something)
                self.right = maxtup[0].left
                self.height = max(self.height, self.right.height+1)
                newRoot = self.correctBalance()
                return (maxtup[0], false, newRoot)
            else:
                # set new right and correct balance
                self.right = maxtup[3]
                self.height = max(self.height, self.right.height+1)
                maxtup[2] = self.correctBalance()
                return maxtup
    
    def contains(self, value): 
    	"""
    	Check if the object is already in the tree. 
    	Return true if it is, false otherwise.
    	"""
        if self.value is None:
            return False
    	elif value == self.value:
            return True
        elif value < self.value:
            return self.left.contains(value)
        else:
            return self.right.contains(value)
    
    def printOut(self):
        """ Used for quick visual debugging
        """
        if self.left is not None:
            print 'left: '
            self.left.printOut()
            
        for i in range(0,self.dups):
            print str(self.value)
        
        if self.right is not None:
            print 'right: '
            self.right.printOut()

class AvlTree:
    """ Wrapper for IBinNode
        All calls to API automatically run on root node of tree
    """
    
    def __init__(self, val=None):
        self.root = AvlNode()
    
    def __iter__(self):
        """ return root's iterator
        """
        return self.root.__iter__()
    
    def insert(self, value):
    	"""
    	Insert an object into the binary tree. 
    	Note: The tree should be sorted, inserting the same object 
    	twice is allowed but the insert is expected to be stable.
        
        Returns new root.
    	"""
        self.root = self.root.insert(value)
    
    def insertAll(self, values):
    	"""
    	Batch-insert multiple elements.
        Ryan: I changed the var name, as list conflicts with a keyword
    	"""
        self.root = self.root.insertAll(values)
    
    def delete(self, value):
        self.root = self.root.delete(value)
    
    def contains(self, value):
    	"""
    	Check if the object is already in the tree. 
    	Return true if it is, false otherwise.
    	"""
        return self.root.contains(value)
    
    def printOut(self):
        """ Debug utility
        """
        self.root.printOut()