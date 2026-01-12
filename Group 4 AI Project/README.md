#  Red Donkey Puzzle — BFS vs A* Algorithm Comparison (Browser-Based AI Project)

This project implements the **Red Donkey sliding block puzzle** and solves it using two different Artificial Intelligence search algorithms:

-  Breadth First Search (BFS)
-  A* Search (A-star)

Both algorithms solve the **same hard puzzle configuration** and are compared based on:

- Execution Time (milliseconds)
- Number of States Explored (used as space complexity approximation)

The project runs entirely in the browser using **HTML, JavaScript, and Canvas**, and is hosted using **GitHub Pages**.

---

##  Problem Description

The Red Donkey Puzzle is a sliding block puzzle where:

- Blocks can move only up, down, left, or right
- Blocks cannot overlap
- Blocks must remain inside the board
- Only one block moves at a time
- The goal is to move the **red block** to the exit at the bottom center

Each arrangement of blocks on the board is treated as a **state** in the search space.

---

##  Algorithms Implemented

### 🔹 1. Breadth First Search (BFS)
**File:** `bfs.html`

- Explores the state space level by level
- Does not use any heuristic information
- Guarantees the shortest solution path
- Requires very high memory
- Slower for large state spaces

**Time Complexity:** O(b^d)  
**Space Complexity:** O(b^d)

---

### 🔹 2. A* Search (A-star)
**File:** `astar.html`

- Uses heuristic guidance to prioritize promising states
- Heuristic used: Manhattan distance of the red block to the exit
- Explores fewer states than BFS
- Faster and more memory efficient
- Still guarantees optimal solution

**Worst-case Time Complexity:** Exponential  
**Practical performance:** Much better than BFS due to heuristic guidance

---

##  Performance Comparison

Each solver displays:

- Number of states explored during the search
- Execution time in milliseconds
- Step-by-step animation of the solution

By comparing the two solvers, it is clearly observed that:

- BFS explores many more states and consumes more memory
- A* reaches the solution faster with fewer explored states

This demonstrates the advantage of **informed search over uninformed search**.

---

##  Homepage (`index.html`) — How the Two Codes Are Connected

The project includes a homepage file named **`index.html`**, which acts as a **navigation menu**.

### 🔹 Purpose of the Homepage

- GitHub Pages automatically loads `index.html` as the main page
- Since this project contains **two separate solver programs**, the homepage allows the user to choose which algorithm to run
- It improves usability and makes the project more professional

### 🔹 How It Works

The homepage **does not execute any algorithm**.

Instead, it contains simple links (buttons):

- **Solve using BFS** → opens `bfs.html`
- **Solve using A* Search** → opens `astar.html`

When a button is clicked:
1. The browser loads the selected HTML file
2. The JavaScript code inside that file runs independently
3. The chosen algorithm solves the puzzle and displays animation

Each solver runs in its **own page**, ensuring fair and isolated comparison of algorithm performance.

---

##  Graphical Representation & Animation

- Board size: **5 × 4 grid**
- Implemented using HTML `<canvas>`
- Blocks are drawn as rectangles
- Exit area is highlighted at the bottom center
- Each move in the solution path is animated sequentially

Both BFS and A* use the **same drawing and animation logic**, ensuring that differences in performance are caused only by the algorithm.

---

##  How to Run the Project

###  Run Online (GitHub Pages)

After enabling GitHub Pages:

- Homepage:
