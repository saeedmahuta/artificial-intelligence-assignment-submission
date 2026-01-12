# Graphical Representation of the Missionaries and Cannibals Problem

## Recommended Representation: State Space Graph (Solution Path)

We represent the problem as a **directed graph** where:

- **Nodes** = valid states `(left_m, left_c, boat)`  
- **Edges** = legal boat moves (1 or 2 people, respecting constraints)  

### Textual Diagram – One Optimal Solution Path (BFS)

(3,3,1) ──2C→── (3,1,0) ──1C←── (3,2,1) ──2C→── (3,0,0)
   │                                                     │
   ▼                                                     ▼
(1,1,0) ←─1M1C── (2,2,1) ──2M→── (0,2,0) ──1C←── (0,3,1)
   │                                                     │
   ▼                                                     ▼
(0,0,0)  ←───────────────2C──────────────────────────────


**Legend**:
- `(M_left, C_left, boat)` where boat=1 means left, 0 means right  
- Arrows show the move (who crosses and direction)  
- This path is the **optimal 11-step solution** found by BFS

## Why this representation?

- Clearly shows state transitions  
- Highlights constraint satisfaction (no invalid states appear)  
- Easy to understand for teaching/explanation  
- Matches the search-based solution methods used (BFS/DFS)

See `presentation_slides.pdf` for visual slides showing the physical puzzle states step-by-step.