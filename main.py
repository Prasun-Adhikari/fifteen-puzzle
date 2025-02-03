import pyautogui as pag
from solve_fifteen import solve_fast, solve_optimal
from idle_tools import mouse_position, color_to_pos


def positions(n):
    for i in range(n**2):
        x, y = i%n, i//n
        yield mouse_position(x, y, n)


def detect_board(n, blank=(0,0)):
    board = [[0]*n for _ in range(n)]

    for i, position in enumerate(positions(n)):
        color = pag.pixel(*position)[0]
        num = color_to_pos(color, n)

        # for n = 4, 8 has same color as blank
        if n == 4 and num == 0:
            if blank != (i//4, i%4):
                num = 8

        board[i//n][i%n] = num

    return board


def main():
    n = int(input("Enter n: "))

    # for n = 4, 8 has same color as blank
    if n == 4:
        bx, by = map(int, input("Enter pos of blank: ").split(' '))
        board = detect_board(n, (bx, by))
    else:
        board = detect_board(n)

    print("\nDetected Board: ")
    print(board)

    print("Searching...")
    if n <= 3:
        steps, moved_nums = solve_optimal(board)
    else:
        steps, moved_nums = solve_fast(board)

    print("\nSteps to solve are: ")
    print(moved_nums)

    input("Press Enter to start moving...")
    for y, x in steps:
        mx, my = mouse_position(x, y, n)
        pag.click(mx, my)

    print("Complete")


if __name__ == "__main__":
    main()
