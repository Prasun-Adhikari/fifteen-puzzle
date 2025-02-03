import time
import pyautogui as pag
from idle_tools import mouse_position, color_to_pos


def print_cur_pos():
    while True:
        x, y = pag.position()
        print((x, y), pag.pixel(x, y)[0])
        time.sleep(1)


def print_colors(n):
    colors = []
    for i in range(n*n):
        x, y = mouse_position(i%n, i//n, n)
        pag.moveTo(x, y)
        # print(i, pag.pixel(x, y)[0])
        colors.append(pag.pixel(x, y)[0])
        time.sleep(0.1)

    for c in colors:
        print(c, color_to_pos(c, n))


def move_n(n):
    for i in range(n*n):
        x, y = mouse_position(i%n, i//n, n)
        pag.moveTo(x, y)
        time.sleep(0.5)


if __name__ == '__main__':
    # print_cur_pos()
    n = int(input("Enter n: "))
    print_colors(n)
    move_n(n)
