"""
Rubik's Cube Simulation Code
Executes simple moves to demonstrate sub-problem solving
"""

# Simplified cube state
cube_state = {
    "U": "Mixed",
    "D": "Mixed",
    "F": "Mixed",
    "B": "Mixed",
    "L": "Mixed",
    "R": "Mixed",
}

def apply_move(face, result_color):
    """
    Simulates applying a move to a face
    """
    cube_state[face] = result_color
    print(f"Applied move on {face}, new state: {result_color}")

def print_cube_state():
    print("\nCurrent Cube State:")
    for face, state in cube_state.items():
        print(face, ":", state)

if __name__ == "__main__":
    print_cube_state()

    # Simulating sub-problem solving
    apply_move("U", "White Cross Solved")
    apply_move("F", "First Layer Solved")
    apply_move("L", "Middle Layer Solved")
    apply_move("D", "Final Layer Oriented")

    print_cube_state()