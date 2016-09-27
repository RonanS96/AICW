"""
	Example code from the following URL showing how to implement the A* algorithm
	http://www.redblobgames.com/pathfinding/a-star/introduction.html
	Date: 26/09/2016
"""

""" 
	Breadth First Search
	This loop visits every possible node on the map.
	Modified to keep track of where we came from and
	visited locations.
"""
def BFS():	
	frontier = Queue()
	frontier.put(start)
	came_from = {}
	came_from[start] = None

	while not frontier.empty():
		current = frontier.get()
		for next in graph.neighbors(current):
			if next not in visited:
				frontier.put(next)
				visited[next] = True

"""
	Reconstruct the path backwards using the various
	values inside came_from.
"""
def findPath(came_from):
	current = goal
	path = [current]
	while current != start:
		current = came_from[current]
		path.append(current)
	path.append(start) # optional
	path.reverse() # optional

"""
	Early exit - stop expanding the frontier once the goal 
	is found.
"""
def earlyExit():
	frontier = Queue()
	frontier.put(start)
	came_from = {}
	came_from[start] = None

	while not frontier.empty():
		current = frontier.get()

		if current == goal:
			break

		for next in graph.neighbors(current):
			if next not in came_from:
				frontier.put(next)
				came_from[next] = current

"""
	Code extended to act as Dijksrta's Algorithm
"""
def DijkstrasAlg():
	frontier = PriorityQueue()
	frontier.put(start, 0)
	came_from = {}
	cost_so_far = {}
	came_from[start] = None
	cost_so_far[start] = 0

	while not frontier.empty():
		current = frontier.get

		if current == goal:
			break

		for next in graph.neighbors(current):
			new_cost = cost_so_far[current] + graph.cost(current, next)
			if next not in cost_so_far or new_cost < cost_so_far[next]:
				cost_so_far[next] = new_cost
				priority = new_cost
				frontier.put(next, priority)
				came_from[next] = current

"""
	Heuristic function which tells us how close we are to the goal.
"""
def heuristic(a, b):
	# Manhatton distance on a square grid
	return abs(a.x - b.x) + abs(a.y - b.y)

def greedyBestFirstSearch():
	frontier = PriorityQueue()
	frontier.put(start, 0)
	came_from = {}
	came_from[start] = None

	while not frontier.empty():
		current = frontier.get()

		if current == goal:
			break

		for next in graph.neighbors(current):
			if next not in came_from:
				priority = heuristic(goal, next)
				frontier.put(next, priority)
				came_from[next] = current

"""
	The implementation of A* which uses both the actual distance from the start point
	and the estimated distance to the goal to find the best path to the goal.
"""
def aStar(graph):
	frontier = PriorityQueue()
	frontier.put(start, 0)
	came_from = {}
	cost_so_far = {}
	came_from[start] = None
	cost_so_far[start] = 0

	while not frontier.empty():
		current = frontier.get()

		if current == goal:
			break

		for next in graph.neighbors(current):
			new_cost = cost_so_far[current] + graph.cost(current, next)
			if next not in cost_so_far or new_cost < cost_so_far[next]:
				cost_so_far[next] = new_cost
				priority = new_cost + heuristic(goal, next)
				frontier.put(next, priority)
				came_from[next] = current









