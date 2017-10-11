""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    if not root:
        return True
    
    v = root.data
        
    max_l = root.left and getMax(root.left)
    min_r = root.right and getMin(root.right)
    
    if root.left and v <= max_l:
            return False
    if root.right and v >= min_r:
            return False
 
    return checkBST(root.left) and checkBST(root.right)

def max(a,b):
    if a > b:
        return a
    return b

def min(a,b):
    if a < b:
        return a
    return b


def getMax(root):
    if root and not root.left and not root.right:
        return root.data
    
    return max(root.data, max(getMax(root.left), getMax(root.right)))
        
def getMin(root):
    if root and not root.left and not root.right:
        return root.data
    
    return min(root.data, min(getMin(root.left), getMin(root.right)))
    
      
            
        
  
