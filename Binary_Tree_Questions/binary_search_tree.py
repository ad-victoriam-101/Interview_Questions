class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
#this creates the first line of the tree. It also sets up the values to be added wherever they fall. 
# A utility function to insert a new node with the given key 
def insert(root,node): 
    if root is None: 
        root = node 
        #If there is no root yet this will add the first value given as the new root.
    else: 
        #nodes are seperated down, if the root val is less than the new node its added to the right. 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            #since the value is either < or > we don't have to compare the node to the root as all options(aside form one) have be tried.
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 
# A utility function to search a given key in BST 
def search(root,key): 
      
    # Base Cases: root is null or key is present at root 
    if root is None or root.val == key: 
        return root 
  
    # Key is greater than root's key 
    if root.val < key: 
        return search(root.right,key) 
    
    # Key is smaller than root's key 
    return search(root.left,key)

def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right) 
