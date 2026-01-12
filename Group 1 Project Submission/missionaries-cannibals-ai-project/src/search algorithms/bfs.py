from collections import deque

def is_valid(state):
    ml, cl, boat = state
    mr, cr = 3 - ml, 3 - cl
    if ml < 0 or cl < 0 or mr < 0 or cr < 0:
        return False
    if (ml > 0 and cl > ml) or (mr > 0 and cr > mr):
        return False
    return True

def bfs():
    start = (3, 3, 1)  # left_m, left_c, boat_on_left
    goal = (0, 0, 0)
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        
        ml, cl, boat = state
        direction = -1 if boat == 1 else 1
        
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:  # boat capacity 1-2
                    new_ml = ml + direction * m
                    new_cl = cl + direction * c
                    new_boat = 1 - boat
                    new_state = (new_ml, new_cl, new_boat)
                    
                    if is_valid(new_state) and new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, path + [new_state]))
    
    return None

if __name__ == "__main__":
    solution = bfs()
    if solution:
        print("BFS Solution found (optimal):")
        for i, s in enumerate(solution):
            print(f"{i:2d}: {s}")
    else:
        print("No solution found")