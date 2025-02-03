from solve_fifteen import solve_fast

board = [[9, 14, 8, 13], [6, 0, 1, 4], [12, 10, 7, 3], [15, 2, 11, 5]]
board = [[4, 7, 15, 12], [9, 14, 5, 11], [2, 13, 6, 0], [8, 10, 1, 3]]
# board = [[7, 6, 0], [8, 4, 3], [5, 2, 1]]
steps, nums = solve_fast(board)
print(' -> '.join(map(str, nums)))
# for t in generate_searches(4):
#    print(t)
