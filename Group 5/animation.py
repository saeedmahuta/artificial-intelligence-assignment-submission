import pygame
import heapq
import time

# --- Puzzle setup ---
goal_state = ((1, 2, 3, 4),
              (5, 6, 7, 8),
              (9, 10, 11, 12),
              (13, 14, 15, 0))  # 0 is empty

start_state = ((0, 2, 3, 4),
               (5, 6, 1, 8),
               (9, 10, 7, 12),
               (13, 14, 11, 15))

# --- Heuristic: Manhattan distance ---
def manhattan(state):
    distance = 0
    for i in range(4):
        for j in range(4):
            val = state[i][j]
            if val != 0:
                goal_i = (val-1)//4
                goal_j = (val-1)%4
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

# --- Generate neighbors ---
def get_neighbors(state):
    neighbors = []
    for i in range(4):
        for j in range(4):
            if state[i][j] == 0:
                x, y = i, j
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0<=nx<4 and 0<=ny<4:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))
    return neighbors

# --- A* search ---
def a_star(start, goal):
    open_set = []
    heapq.heappush(open_set, (manhattan(start), 0, start, []))
    visited = set()
    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        if current == goal:
            return path + [current]
        visited.add(current)
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                heapq.heappush(open_set, (g+1 + manhattan(neighbor), g+1, neighbor, path + [current]))
    return None

solution = a_star(start_state, goal_state)
if not solution:
    print("No solution found.")
    exit()

# --- Pygame visualization ---
pygame.init()
size = 400
tile_size = size // 4
screen = pygame.display.set_mode((size, size))
pygame.display.set_caption("15-Puzzle Solver")

font = pygame.font.SysFont(None, 50)
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (200,200,200)
BLUE = (100,149,237)

def draw_board(state):
    screen.fill(WHITE)
    for i in range(4):
        for j in range(4):
            val = state[i][j]
            rect = pygame.Rect(j*tile_size, i*tile_size, tile_size, tile_size)
            pygame.draw.rect(screen, GRAY if val==0 else BLUE, rect)
            pygame.draw.rect(screen, BLACK, rect, 2)
            if val != 0:
                text = font.render(str(val), True, WHITE)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)
    pygame.display.update()

# Animate solution
for state in solution:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    draw_board(state)
    time.sleep(1.5)  # pause for a second and half

# Keep window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
