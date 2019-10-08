# A ternary search tree is a trie-like data structure where 
# each node may have up to three children. Here is an example 
# which represents the words code, cob, be, ax, war, and we.
# ************************************************************
#        c
#     /  |  \
#    b   o   w
#  / |   |   |
# a  e   d   a
# |    / |   | \ 
# x   b  e   r  e  

parent = ["code","cod","cob","bee","ax","war","we"]
# print(given_arr)

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
def createNode(parent,i,created,root):
    if created[i] is not None:
        return
    created[i] = Node(i)
    if parent[i] == -1:
        root[0] = created[i]
        return
    if created[parent[i]] is None:
        createNode(parent,parent[i])
    p = created[parent[i]]
    if p.left is None:
        p.left = created[i]
    else:
        p.right = created[i]

def createTree(parent):
    n = len(parent)
    created = [None for i in range(n+1)]
    root = [None]
    for i in range(n):
        createNode(parent,i,created,root)
    return root[0]
def inorder(root):
    if root is not None:
        inorder(root.left)
        print (root.key)
        inorder(root.right)

root = createTree(parent)

inorder(root)