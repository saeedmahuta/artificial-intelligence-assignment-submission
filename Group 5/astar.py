import heapq

# Goal state
GOAL = (1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12,
        13, 14, 15, 0)

# Manhattan distance heuristic
def manhattan(board):
    distance = 0
    for i in range(16):
        if board[i] == 0:
            continue
        correct_pos = board[i] - 1
        x1, y1 = divmod(i, 4)
        x2, y2 = divmod(correct_pos, 4)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

# Find possible moves
def get_neighbors(board):
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

# A* algorithm
def a_star(start):
    pq = []
    heapq.heappush(pq, (manhattan(start), 0, start, []))
    visited = set()

    while pq:
        f, g, board, path = heapq.heappop(pq)
        print("Exploring board:", board)


        if board == GOAL:
            return path + [board]

        if board in visited:
            continue
        visited.add(board)

        for neighbor in get_neighbors(board):
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (g + 1 + manhattan(neighbor), g + 1, neighbor, path + [board])
                )

    return None

# Example board (easy one)
start_board = (1, 2, 3, 4,
               5, 6, 7, 8,
               9, 10, 11, 12,
               13, 14, 0, 15)

solution = a_star(start_board)

# Print solution
for step in solution:
    print(step[0:4])
    print(step[4:8])
    print(step[8:12])
    print(step[12:16])
    print("-----")
