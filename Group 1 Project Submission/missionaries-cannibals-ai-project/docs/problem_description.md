# Missionaries and Cannibals Problem - Implementation

## Problem Statement

The Missionaries and Cannibals problem is a classic AI puzzle:

- There are **3 missionaries** and **3 cannibals** on the left bank of a river  
- They need to cross to the right bank using a boat that can carry **at most 2 people**  
- The boat needs **at least 1 person** to row it  
- **Constraint**: Cannibals must never outnumber missionaries on either bank (unless no missionaries are present)  

**Goal**: Get everyone safely to the right bank.

**Initial state**: Left: 3M 3C, Right: 0M 0C, Boat: Left  
**Goal state**: Left: 0M 0C, Right: 3M 3C, Boat: Right

## Solution Approach

We solve this using **uninformed search** algorithms in state space:

State representation: `(left_missionaries, left_cannibals, boat_position)`  
- boat_position = 1 → boat on left  
- boat_position = 0 → boat on right  

Valid moves: 1 or 2 people (any combination of M and/or C), boat must change side.

## Implemented Algorithms

We implemented and compared two search strategies:

1. **Breadth-First Search (BFS)**  
   - Explores level by level  
   - Guarantees the **shortest** (optimal) path  
   - Uses more memory (queue stores all frontier nodes)  

2. **Depth-First Search (DFS)** – recursive version  
   - Explores as deep as possible along each branch before backtracking  
   - Uses less memory (only current path on stack)  
   - Does **not** guarantee the shortest path  

Both algorithms avoid revisiting states using a visited set.

## Optimal Solution (found by BFS)

All valid solutions require **11 crossings**. Here is one optimal sequence (BFS result):

1. 2C → right  
2. 1C ← left  
3. 2C → right  
4. 1C ← left  
5. 2M → right  
6. 1M 1C ← left  
7. 2M → right  
8. 1C ← left  
9. 2C → right  
10. 1C ← left  
11. 2C → right  

Final: Everyone on right side.

## Why BFS and DFS?

- **BFS** → demonstrates optimality and completeness  
- **DFS** → shows recursion, backtracking, and lower space usage  
- Together they allow clear time/space complexity comparison (see complexity_results.md)

This project focuses only on these two algorithms for clarity and direct comparison.