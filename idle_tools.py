def mouse_position(x, y, n):
    '''Maps array position to actual x,y coordinates'''

    # top left corner of board
    x0, y0 = (2010, 650)

    # size of cell depending on number of cells
    square_size = 625 // n
    return (x0 + x * square_size, y0 + y * square_size)


def color_to_pos(color, n):
    '''Find corresponding number according to pixel colour'''

    if color == 51:
        return 0

    # regression to fit color to corresponding number
    m = (85-17)/(n**2-2)
    return int((color - 15) / m) + 1
