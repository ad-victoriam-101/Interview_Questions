class newNode: 
    def __init__(self, item): 
        self.data = item  
        self.left = self.right = None
  
# It returns level of the node if it is  
# present in tree, otherwise returns 0. 
def getLevel(root, node, level): 
      
    # base cases  
    if (root == None): 
        return 0
    if (root == node): 
        return level  
  
    # If node is present in left subtree  
    downlevel = getLevel(root.left, node,  
                               level + 1)  
    if (downlevel != 0): 
        return downlevel  
  
    # If node is not present in left subtree  
    return getLevel(root.right, node, level + 1) 