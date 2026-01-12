def is_valid(state):
    ml, cl, boat = state
    mr, cr = 3 - ml, 3 - cl
    if ml < 0 or cl < 0 or mr < 0 or cr < 0:
        return False
    if (ml > 0 and cl > ml) or (mr > 0 and cr > mr):
        return False
    return True