"""
	F29AI - Artificial Intelligence and Intelligent Agents
	Coursework - Part I - A* Search

	A* search code, adapted from http://www.redblobgames.com/pathfinding/a-star/introduction.html
	Copyright 2014 Red Blob Games <redblobgames@gmail.com>
    License: Apache v2.0 <http://www.apache.org/licenses/LICENSE-2.0.html>

    Edited by Ronan Smith and Jamie McCulloch
    Last edited: 26/09/2016, 14:08

"""
from Python import * # to import the queue implementation


"""	
	An implementation of the A* algorithm
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


