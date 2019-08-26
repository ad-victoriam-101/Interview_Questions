#given a linked list remove all consecutive nodes that sum to zero. 
#you can re think of this problem as just checking if the sum of the two nodes is = 0. 
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
node1 = Node(12)
node2 = Node(3)
node3 = Node(4)
node5 = Node(-7)
node6 = Node(-12)
node7 = Node(8)
print(Node)