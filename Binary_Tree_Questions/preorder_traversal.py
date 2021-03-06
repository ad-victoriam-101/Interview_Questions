#given a binary tree. preform preorder traversial. 
#remember binary trees can only have 2 leaves max. 2-0 is a perfect tree. 
#for preorder the traversal is as follows (Root, Left Right.)
#algorithem preorder visit the root. traverse left side, Traverse right side. 
import random

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
# Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Inorder traversal
# Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res
#Preorder Traversal
# Root -> Left -> Right
    def preorder_traversal(self,root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorder_traversal(root.left)
            res = res + self.preorder_traversal(root.right)
        return res

root = Node(27)
for i in range(10):
    root.insert(random.randint(1,101))
print(root.inorderTraversal(root))
print(root.preorder_traversal(root))