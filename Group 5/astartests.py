import heapq
import time

# Goal state
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)

def manhattan(board):
    """Calculates the sum of distances of tiles from their goal positions."""
    distance = 0
    for i in range(16):
        if board[i] == 0:
            continue
        # The value 'val' should be at index 'val-1'
        correct_pos = board[i] - 1
        x1, y1 = divmod(i, 4)
        x2, y2 = divmod(correct_pos, 4)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def get_neighbors(board):
    """Finds all legal moves (Up, Down, Left, Right)."""
    neighbors = []
    zero = board.index(0)
    x, y = divmod(zero, 4)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            new_zero = nx * 4 + ny
            new_board = list(board)
            new_board[zero], new_board[new_zero] = new_board[new_zero], new_board[zero]
            neighbors.append(tuple(new_board))
    return neighbors

def solve_a_star(start, test_name):
    """A* algorithm with node counting and performance tracking."""
    # pq stores: (f_score, g_score, current_board, path)
    # f(n) = g(n) + h(n)
    pq = []
    heapq.heappush(pq, (manhattan(start), 0, start))
    visited = {} # Use a dict to store the best g_score found for a state
    nodes_expanded = 0
    start_time = time.time()

    while pq:
        f, g, board = heapq.heappop(pq)
        nodes_expanded += 1

        if board == GOAL:
            elapsed = time.time() - start_time
            print(f"{test_name} SUCCESS")
            print(f"Nodes Expanded: {nodes_expanded}")
            print(f"Moves (Depth): {g}")
            print(f"Time Taken: {elapsed:.4f}s")
            print("-" * 30)
            return nodes_expanded, g, elapsed

        if board in visited and visited[board] <= g:
            continue
        visited[board] = g

        for neighbor in get_neighbors(board):
            # Cost to move to neighbor is always g + 1
            new_g = g + 1
            if neighbor not in visited or visited[neighbor] > new_g:
                f_neighbor = new_g + manhattan(neighbor)
                heapq.heappush(pq, (f_neighbor, new_g, neighbor))

    return None

# --- RUNNING THE TEST CASES ---

# Test A: 1 Move away
test_a_state = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 15)
solve_a_star(test_a_state, "A* TEST A")

# Test B: 4 Moves away
test_b_state = (1, 2, 3, 4, 5, 6, 7, 8, 0, 10, 11, 12, 9, 13, 14, 15)
solve_a_star(test_b_state, "A* TEST B")

# Test C: 14 Moves away (The one that was hard for BFS)
test_c_state = (5, 1, 2, 3, 9, 6, 7, 4, 13, 10, 11, 8, 0, 14, 15, 12)
solve_a_star(test_c_state, "A* TEST C")
