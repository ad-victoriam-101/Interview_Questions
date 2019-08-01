# Python Program to detect cycle in an undirected graph 

from collections import defaultdict 

#This class represents a undirected graph using adjacency list representation 
class Graph: 

	def __init__(self,vertices): 
		self.V= vertices #No. of vertices 
		self.graph = defaultdict(list) # default dictionary to store graph 


	# function to add an edge to graph 
	def addEdge(self,v,w): 
		self.graph[v].append(w) #Add w to v_s list 
		self.graph[w].append(v) #Add v to w_s list 

	# A recursive function that uses visited[] and parent to detect 
	# cycle in subgraph reachable from vertex v. 
	def isCyclicUtil(self,v,visited,parent): 

		#Mark the current node as visited 
		visited[v]= True

		#Recur for all the vertices adjacent to this vertex 
		for i in self.graph[v]: 
			# If the node is not visited then recurse on it 
			if visited[i]==False : 
				if(self.isCyclicUtil(i,visited,v)): 
					return True
			# If an adjacent vertex is visited and not parent of current vertex, 
			# then there is a cycle 
			elif parent!=i: 
				return True
		
		return False
		

	#Returns true if the graph contains a cycle, else false. 
	def isCyclic(self): 
		# Mark all the vertices as not visited 
		visited =[False]*(self.V) 
		# Call the recursive helper function to detect cycle in different 
		#DFS trees 
		for i in range(self.V): 
			if visited[i] ==False: #Don't recur for u if it is already visited 
				if(self.isCyclicUtil(i,visited,-1))== True: 
					return True
		
		return False

# Create a graph given in the above diagram 
g = Graph(5) 
g.addEdge(1, 0) 
g.addEdge(0, 2) 
g.addEdge(2, 0) 
g.addEdge(0, 3) 
g.addEdge(3, 4) 

if g.isCyclic(): 
	print ("Graph contains cycle")
else : 
	print ("Graph does not contain cycle ")
g1 = Graph(3) 
g1.addEdge(0,1) 
g1.addEdge(1,2) 


if g1.isCyclic(): 
	print ("Graph contains cycle")
else : 
	print ("Graph does not contain cycle ")

###########################################################################
class Node:
    def __init__(self, val):
        self.val = val
        self.adj_nodes = set()

    def __hash__(self):
        return hash(self.val)

    def __repr__(self):
        return self.val


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.unseen_nodes = None

    def has_cycle_helper(self, node, path=list()):
        if node in self.unseen_nodes:
            self.unseen_nodes.remove(node)

        for adj_node in node.adj_nodes:
            if adj_node in path and adj_node != path[-1]:
                return True

            if self.unseen_nodes:
                return self.has_cycle_helper(adj_node, path + [node])

        return False

    def has_cycle(self):
        start_node = next(iter(self.nodes))
        self.unseen_nodes = self.nodes.copy()
        return self.has_cycle_helper(start_node)


# Tests
a = Node("a")
b = Node("b")
c = Node("c")

a.adj_nodes = {b}
b.adj_nodes = {c}
c.adj_nodes = {a}

g1 = Graph({a, b, c})
assert g1.has_cycle()

a.adj_nodes = {b, c}
b.adj_nodes = set()
c.adj_nodes = set()
g2 = Graph({a, b, c})
assert not g2.has_cycle()