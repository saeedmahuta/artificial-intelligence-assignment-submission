# Rubik's Cube – AI Problem Solving Classification

**Course:** Artificial Intelligence (300 Level)  
**Problem:** Rubik's Cube  
**Problem Type:** Subgoals, Patterns, Sub-problems  

## Overview
This project demonstrates how the Rubik's Cube can be classified as a problem-solving task in Artificial Intelligence. The solution approach focuses on decomposing the problem into smaller subgoals, recognizing patterns, and solving sub-problems incrementally.

## Problem-Solving Classification

### Subgoals
The cube is solved by achieving smaller goals such as:
- Solving the white cross
- Completing the first layer
- Solving the middle layer
- Orienting the final layer

### Patterns
Specific cube configurations (crosses, aligned faces) are recognized and used to decide the next move.

### Sub-problems
The overall problem is broken down into:
- Edge solving
- Corner solving
- Layer-by-layer completion

## Code Description

### rubiks_ai_logic.py
Implements the AI logic for identifying subgoals and determining the next action based on the cube state.

### rubiks_simulation.py
Simulates move execution and demonstrates how sub-problems are solved step-by-step.

## Note
This implementation is simplified for academic demonstration purposes and focuses on AI problem-solving concepts rather than a full Rubik's Cube solver.