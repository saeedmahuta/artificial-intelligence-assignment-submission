import collections
import time

# --- Global Configuration ---
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)

def get_neighbors(state):
    """Finds all legal moves for the blank tile (0)."""
    neighbors = []
    idx = state.index(0)
    row, col = divmod(idx, 4)
    
    # Possible directions: Up, Down, Left, Right
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = row + dr, col + dc
        if 0 <= r < 4 and 0 <= c < 4:
            new_idx = r * 4 + c
            new_state = list(state)
            # Swap empty tile with neighbor
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(tuple(new_state))
    return neighbors

def solve_bfs(start_state, test_name):
    """Standard BFS logic with frontier (queue) and explored (set)."""
    queue = collections.deque([(start_state, 0)])
    visited = {start_state}
    nodes = 0
    start_time = time.time()
    
    while queue:
        curr, dist = queue.popleft()
        nodes += 1
        
        if curr == GOAL_STATE:
            elapsed = time.time() - start_time
            print(f"{test_name} SUCCESS")
            print(f"Nodes Explored: {nodes}")
            print(f"Moves (Depth): {dist}")
            print(f"Time Taken: {elapsed:.4f}s")
            print("-" * 30)
            return nodes, dist, elapsed
            
        for neighbor in get_neighbors(curr):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return None

# --- Run the Test Cases ---

# Test A: 1 Move away
test_a_state = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 15)
solve_bfs(test_a_state, "TEST A")

# Test B: 4 Moves away
test_b_state = (1, 2, 3, 4, 5, 6, 7, 8, 0, 10, 11, 12, 9, 13, 14, 15)
solve_bfs(test_b_state, "TEST B")

# Test C: 14 Moves away (Stress Test)
test_c_state = (5, 1, 2, 3, 9, 6, 7, 4, 13, 10, 11, 8, 0, 14, 15, 12)
solve_bfs(test_c_state, "TEST C")
