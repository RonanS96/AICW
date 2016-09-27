"""
	F29AI - Artificial Intelligence and Intelligent Agents
	Coursework - Part I - A* Search

	Main program.

	Ronan Smith & Jamie McCulloch
	Last edited: 26/09/2016, 14:34
"""

"""
  	from starter.cpp: You should define an appropriate Graph structure for the problem.
  	This should include a definition of State and the neighbours()
  	and cost() functions. The neighbours() and cost() functions must
  	be defined as listed below, however, you may add new variables,
  	functions, etc. to the struct as needed.
"""
def graph():
	all_nodes = []
	for x in range(20):		#20x10 map.
		for y in range(10):
			all_nodes.append([x, y])

"""
	Finds the available nodes connected the current node.
	North, South, East and West (no diagonals).
"""
def neighbors(node):
	dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
	result = []
	for dir in dirs:
		neighbor = [node[0] + dir[0], node[1] + dir[1]]
		if neighbor in all_nodes:	
			result.append(neighbor)	
	return result

""" Continue from  "An alternative way is to make sure the coordinates are in range". 
	Website in favourites as Gra. """