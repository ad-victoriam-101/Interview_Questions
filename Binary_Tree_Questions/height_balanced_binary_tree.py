#given a binary tree, determin whether or not its a height - balanced. 
#this can be defined as one in which the heights of the two subtrees of any node never differ by more than one.

#step one: make binary tree with N nodes.
#step two: count the number of nodes/branches on each side. 
#step three: if this number is the same return true.else return false. 
#create a step binary tree node.
class Node:
        def __init__(self,data):
            self.data = data
            self.left = None
            self.right = None
    #this is an empty node and will fill out as time goes on. 
    def height(root):
        #check if the tree is empty.
        if root is None:
            return 0 
        return max(height(root.left),height(root.right))+1
    #now we have to make a function to check if height-balanced or not.
    def is_balanced(root):
        if root is None:
            return True
        left_height = height(root.left)
        right_height = height(root.right)

        if (abs(left_height - right_height) <= 1) and is_balanced(
            root.left) is True and is_balanced(root.right) is True:
            return True
        return False
    #Driver Functions
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
if is_balanced(root):
    print("The Tree is Balanced.")
else:
    print("Not balanced.")

