/*
 * F29AI - Artificial Intelligence and Intelligent Agents
 *
 * Coursework - Part I - A* Search
 *
 * Starter code
 */

#include "astar.cpp"


/*
 * You should define an appropriate Graph structure for the problem.
 * This should include a definition of State and the neighbours()
 * and cost() functions. The neighbours() and cost() functions must
 * be defined as listed below, however, you may add new variables,
 * functions, etc. to the struct as needed.
 */
struct Graph {
    typedef int State;   // Redefine State as needed.

    // This function should return a vector containing the neighbouring
    // States for a given State.
    vector<State> neighbours(State s) {
        vector<State> neighbour_v;

        // Fill in your implementation here.

        return(neighbour_v);
    }

    // This function should return the cost of moving from State a
    // to State b.
    double cost(State a, State b) {
        return(0);       // Fill in your implementation here.
    }
};


/*
 * You should define appropriate heuristic functions for the problem.
 * The function should return the heuristic value of transitioning
 * from State a to State b as a double.
 */
double heuristic(Graph::State a, Graph::State b) {
    return(0);           // Fill in your implementation here.
}


/*
 * You should define a function to display your solution path.
 * Feel free to design this function as appropriate.
 */
void display_solution(Graph g, vector<Graph::State> path) {
    ;
}


/*
 * Make changes to main() as needed.
 */
int main() {
  // Remember to define an appropriate graph, initial state, and goal state
  Graph g;
  Graph::State init_state;
  Graph::State goal_state;

  // Call the search
  vector<Graph::State> path;
  a_star_search(g, init_state, goal_state, heuristic, path);

  // Display the result
  display_solution(g, path);
}

