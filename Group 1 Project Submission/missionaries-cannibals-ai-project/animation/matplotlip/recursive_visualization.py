import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import networkx as nx
from typing import Tuple, List

# ──── Global tracking ────────────────────────────────────────────────
visited = set()
solution_path: List[Tuple[int, int, int]] = []
exploration_tree = nx.DiGraph()

def is_valid(state: Tuple[int, int, int]) -> bool:
    lm, lc, boat = state
    rm, rc = 3 - lm, 3 - lc
    if lm < 0 or lc < 0 or rm < 0 or rc < 0:
        return False
    return not ((lm > 0 and lc > lm) or (rm > 0 and rc > rm))

def recursive_dfs(current: Tuple[int, int, int], parent=None) -> bool:
    if current in visited:
        return False
    visited.add(current)
    
    if parent is not None:
        exploration_tree.add_edge(parent, current)
    
    if current == (0, 0, 0):
        solution_path.append(current)
        return True
    
    lm, lc, boat = current
    direction = -1 if boat == 1 else 1
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    
    for dm, dc in moves:
        new_lm = lm + direction * dm
        new_lc = lc + direction * dc
        new_state = (new_lm, new_lc, 1 - boat)
        
        if is_valid(new_state):
            if recursive_dfs(new_state, current):
                solution_path.append(current)
                return True
    
    return False

# Run the recursive search once
start = (3, 3, 1)
recursive_dfs(start)
solution_path = solution_path[::-1]  # reverse to get start → goal

# ──── Visualization ──────────────────────────────────────────────────
fig, (ax_tree, ax_anim) = plt.subplots(1, 2, figsize=(14, 7))
fig.suptitle("Recursive DFS - Missionaries & Cannibals", fontsize=14)

# Left: Exploration tree
pos = nx.spring_layout(exploration_tree, seed=42)
nx.draw(exploration_tree, pos, ax=ax_tree, with_labels=True,
        node_color="lightblue", node_size=1200, font_size=8,
        arrowsize=12)
ax_tree.set_title(f"Exploration Tree ({len(exploration_tree.nodes)} nodes)")

# Right: Animation area
ax_anim.set_xlim(-1.5, 3.5)
ax_anim.set_ylim(-0.5, 2.5)
ax_anim.axis('off')

# Static background
ax_anim.fill_between([-1.5, -0.2], -0.5, 2.5, color="#8B4513", alpha=0.6)  # left bank
ax_anim.fill_between([2.2, 3.5], -0.5, 2.5, color="#8B4513", alpha=0.6)   # right bank
ax_anim.fill_between([-0.2, 2.2], -0.5, 2.5, color="#4682B4", alpha=0.4)  # river

missionaries = ax_anim.scatter([], [], s=400, c='navy', label='Missionaries')
cannibals    = ax_anim.scatter([], [], s=400, c='darkred', marker='s', label='Cannibals')
boat_marker  = ax_anim.scatter([], [], s=800, c='black', marker='>', label='Boat')
step_text    = ax_anim.text(1, 2.7, "", ha='center', fontsize=12, fontweight='bold')

ax_anim.legend(loc='upper right')

def update(frame):
    lm, lc, b = solution_path[frame]
    rm, rc = 3 - lm, 3 - lc
    
    # Positions
    m_pos = [(-1.0 + i*0.4, 1.6) for i in range(lm)] + [(2.5 + i*0.4, 1.6) for i in range(rm)]
    c_pos = [(-1.0 + i*0.4, 0.6) for i in range(lc)] + [(2.5 + i*0.4, 0.6) for i in range(rc)]
    boat_x = 0.8 if b == 1 else 2.0
    
    missionaries.set_offsets(m_pos)
    cannibals.set_offsets(c_pos)
    boat_marker.set_offsets([(boat_x, 1.2)])
    step_text.set_text(f"Step {frame+1} / {len(solution_path)}   →   {lm}M {lc}C | Boat {'Left' if b==1 else 'Right'}")
    
    return missionaries, cannibals, boat_marker, step_text

ani = FuncAnimation(fig, update, frames=len(solution_path),
                    interval=1800, blit=True, repeat=True)

plt.tight_layout()
plt.show()


