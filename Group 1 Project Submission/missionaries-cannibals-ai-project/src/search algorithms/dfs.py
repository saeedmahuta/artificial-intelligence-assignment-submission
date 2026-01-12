def is_valid(state):
    ml, cl, boat = state
    mr, cr = 3 - ml, 3 - cl
    if ml < 0 or cl < 0 or mr < 0 or cr < 0:
        return False
    if (ml > 0 and cl > ml) or (mr > 0 and cr > mr):
        return False
    return True

def dfs(state, path, visited):
    if state in visited:
        return None
    visited.add(state)
    
    if state == (0, 0, 0):
        return path + [state]
    
    ml, cl, boat = state
    direction = -1 if boat == 1 else 1
    
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    
    for m, c in moves:
        new_ml = ml + direction * m
        new_cl = cl + direction * c
        new_state = (new_ml, new_cl, 1 - boat)
        
        if is_valid(new_state):
            result = dfs(new_state, path + [state], visited.copy())
            if result:
                return result
    
    return None

if __name__ == "__main__":
    start = (3, 3, 1)
    solution = dfs(start, [], set())
    if solution:
        print("DFS found a solution:")
        for i, s in enumerate(solution):
            print(f"{i:2d}: {s}")
    else:
        print("No solution found")