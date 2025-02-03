from collections import deque
from copy import deepcopy


class Node:
    def __init__(self, board, moved=None, last=0):
        self.parent = None
        self.board = board
        self.last = last
        if moved is None:
            for i, line in enumerate(self.board):
                for j, num in enumerate(line):
                    if num == 0:
                        self.moved = (i, j)
        else:
            self.moved = moved

    def adjacents(self, limit):
        i, j = self.moved
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        for di, dj in directions:
            try:
                if i+di < 0 or j+dj < 0:
                    raise IndexError
                if i+di < limit[0] - 1:
                    raise IndexError
                if i+di < limit[0] and j+dj < limit[1]:
                    raise IndexError
                num = self.board[i+di][j+dj]

                if self.last == num:
                    continue

                new_board = deepcopy(self.board)
                new_board[i][j] = num
                new_board[i+di][j+dj] = 0
                yield Node(new_board, (i+di, j+dj), num)
            except IndexError:
                pass

    def __str__(self):
        return str(self.board)


def match(list1, list2, req):
    x, y = req
    for i in range(x):
        for j in range(y):
            if list1[i][j] != list2[i][j]:
                return False
    return True


def bfs(start, target, limit, req):
    visited = {tuple(map(tuple, start.board))}
    queue = deque()
    queue.append(start)
    while queue:
        temp = queue.popleft()
        if match(temp.board, target, req):
            return temp
        for node in temp.adjacents(limit):
            indexable_board = tuple(map(tuple, node.board))
            if indexable_board not in visited:
                visited.add(indexable_board)
                node.parent = temp
                queue.append(node)
    return None


def solve_optimal(board):
    n = len(board)
    target = [[j*n+i+1 for i in range(n)] for j in range(n)]
    target[n-1][n-1] = 0
    start = Node(board)
    goal = bfs(start, target, (0, 0), (n, n))

    temp = goal
    steps = []
    moved_numbers = []
    while temp != start:
        steps.append(temp.moved)
        moved_numbers.append(temp.last)
        temp = temp.parent

    return steps[::-1], moved_numbers[::-1]


def generate_searches(n):
    prev = (0, 0)
    for i in range(n-1):
        if i == n-2:
            yield (prev, (n, n))
            break
        for j in range(n):
            if j == n-1:
                prev = i+1, j-1
            values = (i+1, j+1)
            yield (prev, values)
            prev = values


def solve_fast(board):
    n = len(board)
    target = [[j*n+i+1 for i in range(n)] for j in range(n)]
    target[n-1][n-1] = 0

    start = Node(board)
    steps = []
    moved_numbers = []
    limit = (0, 0)
    for limit, req in generate_searches(n):
        sub_steps, sub_nums = [], []
        goal = bfs(start, target, limit, req)

        temp = goal
        while temp != start:
            sub_steps.append(temp.moved)
            sub_nums.append(temp.last)
            temp = temp.parent

        start = goal
        limit = req

        steps += sub_steps[::-1]
        moved_numbers += sub_nums[::-1]
    return steps, moved_numbers
