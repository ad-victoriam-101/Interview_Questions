#given a linked list remove all consecutive nodes that sum to zero. 
#you can re think of this problem as just checking if the sum of the two nodes is = 0. 
class Node:
    def __init__(self,x):
        self.value = x
        self.next = None
        self.cumulative = 0

    def __str__(self):
        string = "["
        node = self
        while node:
            string += "{},{}->".format(node.value,node.cumulative)
            node = node.next
        string +="None]"
        return string
        #end of class definition 
def get_nodes(values):
    next_node = None
    for value in values[::-1]:
        node = Node(value)
        node.next = next_node
        next_node = node
    return next_node

def get_list(head):
    node = head 
    nodes = list()
    while node:
        nodes.append(node.value)
        node = node.next
    return nodes

def add_cumulative_sum(head):
    node = head
    cumulative_sum = 0
    while node:
        node.cumulative = node.value + cumulative_sum
        cumulative_sum = node.cumulative
        node = node.next

def remove_zero_sum(head):
    add_cumulative_sum(head)
    dummy_head = Node(None)
    dummy_head.next = head

    seen_totals = dict()
    node = dummy_head
    index = 0
    while node:
        if node.cumulative in seen_totals:
            seen_totals[node.cumulative].next = node.next
        seen_totals[node.cumulative] = node
        index += 1 
        node = node.next
    return dummy_head.next

    
llist = get_nodes([3,4,-7,5,6,-6])

print(get_list(remove_zero_sum(llist)) == [5])
#replace this with a assertion test. 
