"""
at start
loop
    calcCosts
    go to lowest
    add to closed
    add neighbors to open
    when target
        return
"""
from itertools import product


class Node:
    """
    distance: direct 10, diagonal 14
    g cost: dist from start
    h cost: dist from end
    f cost: g + h
    """

    def __init__(self, traversable: bool):
        self.traversable = traversable
        self.g_cost = 0
        self.h_cost = 0
        self.parent = None

    @property
    def f_cost(self):
        return self.g_cost + self.h_cost

    def __str__(self):
        return f"{self.g_cost} {self.h_cost} {self.f_cost}"

    def should_draw(self):
        return self.f_cost != 0


def get_distance(a, b):
    dst_x = abs(a[0] - b[0])
    dst_y = abs(a[1] - b[1])
    if dst_x > dst_y:
        return 14 * dst_y + 10 * (dst_x - dst_y)
    return 14 * dst_x + 10 * (dst_y - dst_x)


def get_path(start, end, board):
    path = []
    current = end
    while current != start:
        path.append(current)
        current = board[current[0]][current[1]].parent
    return path


def neighbors(middle, board):
    nbs = []
    for offset in product(range(-1, 2), repeat=2):
        pos = middle[0] + offset[0], middle[1] + offset[1]
        if pos != middle and 0 <= pos[0] < len(board) and 0 <= pos[1] < len(board[0]):
            nbs.append(pos)
    return nbs


def astar_step(board, start, end):
    def node_at(pos):
        return board[pos[0]][pos[1]]

    open = [start]
    closed = []
    while open:
        current = open[0]
        for pos in open:
            if (
                node_at(pos).f_cost <= node_at(current).f_cost
                and node_at(pos).h_cost < node_at(current).h_cost
            ):
                current = pos

        open.remove(current)
        closed.append(current)

        if node_at(current) == node_at(end):
            yield open, closed, get_path(start, end, board)
            return

        for pos in neighbors(current, board):
            nb = node_at(pos)
            if not nb.traversable or pos in closed:
                continue

            cost_to_neighbor = nb.g_cost + get_distance(current, pos)
            if cost_to_neighbor < nb.g_cost or pos not in open:
                nb.g_cost = cost_to_neighbor
                nb.h_cost = get_distance(pos, end)
                nb.parent = current
                if pos not in open:
                    open.append(pos)
        yield open, closed, []


def astar(board, start=(0, 0), end=(-1, -1)):
    for path in astar_step(board, start, end):
        pass
    return path
