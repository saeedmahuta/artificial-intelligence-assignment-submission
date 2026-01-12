import collections
import time

# 1. Define the Goal State
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)

def get_neighbors(state):
    """Generates all possible legal moves from the current state."""
    neighbors = []
    idx = state.index(0)  # Locate the empty tile
    row, col = divmod(idx, 4)
    
    # Define possible moves for the empty space (Up, Down, Left, Right)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < 4 and 0 <= c < 4:
            new_idx = r * 4 + c
            new_state = list(state)
            # Swap the empty tile with the adjacent tile
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(tuple(new_state))
    return neighbors

def solve_bfs(start_state):
    """Performs Breadth-First Search to find the shortest path."""
    # Frontier: FIFO Queue (stores states and the path taken to reach them)
    frontier = collections.deque([(start_state, [])])
    # Explored: Set to keep track of visited states (prevents cycles)
    explored = {start_state}
    
    nodes_expanded = 0
    start_time = time.time()
    
    while frontier:
        current_state, path = frontier.popleft()
        nodes_expanded += 1
        
        # Goal Test
        if current_state == GOAL_STATE:
            duration = time.time() - start_time
            return path, nodes_expanded, duration
        
        # Expand neighbors
        for neighbor in get_neighbors(current_state):
            if neighbor not in explored:
                explored.add(neighbor)
                # Add neighbor to the back of the queue (Layer-by-layer)
                frontier.append((neighbor, path + [neighbor]))
                
    return None  # No solution found

# --- Example Usage for Presentation ---
# A puzzle solvable in 4 moves
initial_state = (1, 2, 3, 4, 5, 6, 7, 8, 0, 10, 11, 12, 9, 13, 14, 15)

path, nodes, exec_time = solve_bfs(initial_state)

if path:
    print(f"Solution Found in {len(path)} moves!")
    print(f"Nodes Expanded: {nodes}")
    print(f"Execution Time: {exec_time:.4f}s")
