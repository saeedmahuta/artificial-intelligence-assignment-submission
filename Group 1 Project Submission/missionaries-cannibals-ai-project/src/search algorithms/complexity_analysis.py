# complexity_analysis.py

import timeit
import sys
from memory_profiler import memory_usage

from bfs import bfs
from dfs import dfs

def run_bfs():
    return bfs()

def run_dfs():
    return dfs((3,3,1), [], set())


if __name__ == "__main__":           # ← Add this!
    print("=== Complexity Comparison (Missionaries & Cannibals) ===\n")

    N = 20  # or 50, whatever you prefer
    
    print(f"Measuring time over {N} runs each...")
    
    time_bfs = timeit.timeit(run_bfs, number=N) / N
    time_dfs = timeit.timeit(run_dfs, number=N) / N

    print(f"BFS average time:  {time_bfs:.6f} seconds")
    print(f"DFS average time:  {time_dfs:.6f} seconds\n")

    # If using memory_profiler:
    try:
        from memory_profiler import memory_usage
        mem_bfs = max(memory_usage(run_bfs))
        mem_dfs = max(memory_usage(run_dfs))
        print(f"BFS peak memory:   {mem_bfs:.1f} MiB")
        print(f"DFS peak memory:   {mem_dfs:.1f} MiB")
    except ImportError:
        print("memory_profiler not installed → skipping memory stats")