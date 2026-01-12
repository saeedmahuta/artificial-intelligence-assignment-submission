### **15-Puzzle Solver — AI Search Algorithms**



##### **Project Overview**



This project demonstrates Artificial Intelligence problem solving using state-space search through the classic 15-Puzzle problem.

The goal is to show both theoretical understanding and practical implementation of:



* Problem representation in AI
* Uninformed search (Breadth-First Search)
* Informed search (A\* with Manhattan Distance heuristic)
* Performance comparison (time, space, nodes expanded)
* Visualization of AI decision-making



This project aligns directly with concepts taught in Artificial Intelligence problem-solving and search algorithms.



##### 

##### **Problem Representation**



###### ***What is the 15-Puzzle?***



The 15-Puzzle is a sliding-tile puzzle consisting of:



* A 4×4 grid
* 15 numbered tiles
* 1 empty space (0)



The objective is to rearrange the tiles from a scrambled initial state into a goal state by sliding tiles into the empty space.



###### ***How It Is Modeled in AI***



The 15-Puzzle is modeled as a state-space search problem, where:



* State - A specific arrangement of the tiles
* State Space - All possible valid configurations of the puzzle
* Initial State - The starting scrambled configuration
* Goal State - (1, 2, 3, 4,

                 5, 6, 7, 8,

                 9, 10, 11, 12,

                 13, 14, 15, 0)

* Actions (Moves) - Move the empty tile Up, Down, Left or Right (if legal)



This problem clearly demonstrates how AI agents explore large state spaces to reach a goal efficiently.



##### 

##### **Search Algorithms Implemented**



###### ***Breadth-First Search (BFS) - Uninformed Search***



Breadth-First Search explores the puzzle level by level, expanding all states at a given depth before moving deeper.



###### ***Why BFS Is an Uninformed Search***



* It uses no heuristic information
* It has no knowledge of how close a state is to the goal
* All states are treated equally



###### ***Properties of BFS***



* Guarantees the shortest path
* Uses large amounts of memory
* Becomes impractical for deeper puzzles



###### ***Complexity***



* Time Complexity: O(b^d)
* Space Complexity: O(b^d)



&nbsp; b = branching factor (≈ 2–4)

&nbsp; d = solution depth



###### 

###### ***A\* Search with Manhattan Distance - Informed Search***



A\* improves search efficiency by using a heuristic function to guide exploration.



###### ***Why A\* Is an Informed Search***



* It uses extra information (heuristics)
* It prioritizes states that appear closer to the goal



###### ***Evaluation Function***



f(n) = g(n) + h(n)



* g(n) - cost from start to current state
* h(n) - estimated cost to goal (Manhattan Distance)



###### ***Manhattan Distance Heuristic***



Manhattan Distance calculates the horizontal + vertical distance each tile is from its goal position.



***Why it works well***:

* Never overestimates the true cost (admissible)

* Matches grid movement (no diagonal moves)
* Guarantees optimal solutions with A\*





##### **Comparison and Complexity Analysis**



###### ***Theoretical Comparison***

------------------------------------------------------------
| Aspect           | BFS (Uninformed) | A\* (Informed)      |
|------------------|------------------|--------------------|
| Time Complexity  | O(b^d)           | O(b^d) worst-case  |
| Space Complexity | O(b^d)           | O(b^d) worst-case  |
| Heuristic        | None             | Manhattan Distance |
| Optimal          | Yes              | Yes                |
| Efficiency       | Low              | High               |
| Memory Usage     | Very High        | Much Lower         |
------------------------------------------------------------





###### ***Experimental Results (Python Runs)***

--------------------------------------------------------------------
| Test Case        | Algorithm | Nodes Expanded | Moves | Time (s) |
|------------------|-----------|----------------|-------|----------|
| Test A (1 move)  | BFS       | 4              | 1     | 0.0000   |
|                  | A\*        | 2              | 1     | ~0.0000  |
| Test B (4 moves) | BFS       | 39             | 4     | 0.0001   |
|                  | A\*        | 5              | 4     | ~0.0001  |
| Test C (9 moves) | BFS       | 909            | 9     | 0.0022   |
|                  | A\*        | 10             | 9     | ~0.0001  |
--------------------------------------------------------------------



###### 

###### ***Trade-Offs***



  ***BFS***



1. &nbsp;Simple and reliable
2. &nbsp;Guaranteed shortest path
3. &nbsp;Extremely memory-intensive



  ***A\****



1. &nbsp;Faster and more efficient
2. &nbsp;Uses heuristics to reduce exploration
3. &nbsp;Slightly more complex to implement



###### ***Conclusion:***

A\* clearly outperforms BFS on complex puzzles while maintaining optimality.



##### 

##### **Pseudocode**



###### ***Breadth-First Search (BFS)***



BFS(start, goal)



Create empty QUEUE

Create empty SET VISITED



Add start to QUEUE

Add start to VISITED



WHILE QUEUE not empty

&nbsp;   Remove first element → current

&nbsp;   IF current is goal

&nbsp;       RETURN solution

&nbsp;   Generate neighbors

&nbsp;   FOR each neighbor

&nbsp;       IF neighbor not in VISITED

&nbsp;           Add neighbor to VISITED

&nbsp;           Add neighbor to QUEUE

END WHILE



###### ***A\* Search Algorithm***



A\_STAR(start, goal)



Create PRIORITY QUEUE OPEN

Create SET CLOSED



Set g(start) = 0

Set f(start) = g + h



WHILE OPEN not empty

&nbsp;   Remove node with lowest f

&nbsp;   IF node is goal

&nbsp;       RETURN solution

&nbsp;   Add node to CLOSED

&nbsp;   Generate neighbors

&nbsp;   FOR each neighbor

&nbsp;       Compute new g

&nbsp;       IF better path found

&nbsp;           Update f and parent

&nbsp;           Add to OPEN

END WHILE



##### 

##### ***Animation and Visualization***



A visual animation is included to show:



* Each tile movement
* Step-by-step AI decision making
* How the puzzle transitions from start to goal



This serves as visual proof of AI problem-solving.



##### 

##### ***Requirements***



* Python 3.x
* Standard libraries (collections, heapq, time)
* pygame (for animation)
