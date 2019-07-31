#given n'th nodes in a Binary search tree. 
#find all unique itterations of the tree. 
#remember each node can only have two offsprings. 
#the solution for now many nodes you can have is a corelation formula called Catalan formula, 

def Catalan_formula(number_nodes):
    if number_nodes <= 1:
        return 1
    res = 0
    for i in range(number_nodes):
        res += Catalan_formula(i) * Catalan_formula(number_nodes - i -1)
    return res

for i in range(10):
    print(Catalan_formula(i))
