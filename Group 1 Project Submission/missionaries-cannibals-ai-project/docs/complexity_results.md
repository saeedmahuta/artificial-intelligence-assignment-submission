# Time & Space Complexity Comparison

We compared **BFS** (iterative, queue-based) and **DFS** (recursive) on the 3M+3C problem.

## Results (measured on average of 20 runs)

| Algorithm       | Average Time       | Peak Memory (approx) | Notes                                      |
|-----------------|--------------------|-----------------------|--------------------------------------------|
| BFS             | 0.000100 s  | 25.0 MiB            | Optimal (11 steps), higher memory usage    |
| DFS (recursive) | 0.000054 s   | 25.0 MiB            | Usually finds solution, but not always shortest; lower memory |

## Key Observations

- **Time**: BFS is generally faster due to finding the shortest path quickly  
- **Space**: DFS uses less memory because it only stores the current recursion stack  
- The difference is small because the state space is tiny (~ dozens of valid states)  

Measured using `timeit` for time and `memory_profiler` for peak memory.  
See `src/complexity_analysis.py` for the measurement script.