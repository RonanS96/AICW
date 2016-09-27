/*
 * F29AI - Artificial Intelligence and Intelligent Agents
 *
 * Coursework - Part I - A* Search
 *
 * A* search code, adapted from http://www.redblobgames.com/pathfinding/
 * Copyright 2014 Red Blob Games <redblobgames@gmail.com>
 * License: Apache v2.0 <http://www.apache.org/licenses/LICENSE-2.0.html>
 */

#include <map>
#include <set>
#include <array>
#include <vector>
#include <utility>
#include <queue>
#include <algorithm>

using std::map;
using std::set;
using std::array;
using std::vector;
using std::queue;
using std::priority_queue;
using std::pair;
using std::tie;


/*
 * A priority queue implementation
 */
template<typename T, typename priority_t>
struct PriorityQueue {
    typedef pair<priority_t, T> PQElement;
    priority_queue<PQElement, vector<PQElement>, 
                   std::greater<PQElement>> elements;

    inline bool empty() const { return elements.empty(); }

    inline void put(T item, priority_t priority) { elements.emplace(priority, item); }

    inline T get() {
        T best_item = elements.top().second;
        elements.pop();
        return best_item;
    }
};


/*
 * Extract the path from the traversal graph
 */
template<typename State>
vector<State> reconstruct_path(
    State start,
    State goal,
    map<State, State>& came_from
)
{
    vector<State> path;
    State current = goal;
    path.push_back(current);
    while (current != start) {
        current = came_from[current];
        path.push_back(current);
    }

    path.push_back(start); // optional
    std::reverse(path.begin(), path.end());
    
    return path;
}


/* 
 * An implementation of the A* algorithm
 */
template<typename G>
void a_star_search (
    G& graph,
    typename G::State start,
    typename G::State goal,
    double (*h)(typename G::State, typename G::State),
    vector<typename G::State> &path
)
{
    typedef typename G::State State;
    map<typename G::State, typename G::State> came_from;
    map<typename G::State, double> cost_so_far;
    PriorityQueue<State, double> frontier;
    frontier.put(start, 0);

    came_from[start] = start;
    cost_so_far[start] = 0;
  
    while (!frontier.empty()) {
        auto current = frontier.get();

        if (current == goal)
            break;

        for (auto next : graph.neighbours(current)) {
            double new_cost = cost_so_far[current] + graph.cost(current, next);
            if (!cost_so_far.count(next) || new_cost < cost_so_far[next]) {
                cost_so_far[next] = new_cost;
                double priority = new_cost + h(next, goal);
                frontier.put(next, priority);
                came_from[next] = current;
            }
        }
    }

    path = reconstruct_path(start, goal, came_from);
}

