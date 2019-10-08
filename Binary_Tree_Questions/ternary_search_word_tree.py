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

given_arr = ["code","cod","cob","bee","ax","war","we"]
print(given_arr)

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key