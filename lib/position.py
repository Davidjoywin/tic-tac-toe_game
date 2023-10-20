def positioning():
    """
    map the equivalent position on the board to a number
    for a easy input in the cells of the tic-tac game 
    game board

    map n => (x, y)
    """
    pos = {}
    tmp = 1
    for i in range(3):
        for j in range(3):
            pos[f"{tmp}"] = (i,j)
            tmp += 1
    return pos