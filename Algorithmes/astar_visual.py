import pygame as pg
from random import randint
from astar import astar_step, Node

WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
YELLOW = 255, 255, 0
BLUE = 0, 0, 255
GREY = 150, 150, 150
BLACK = 0, 0, 0


def text(msg, pos):
    text_sur = font.render(str(msg), False, GREY)
    text_rect = text_sur.get_rect()
    text_rect.center = pos
    screen.blit(text_sur, text_rect)


def color(pos):
    if not board[pos[0]][pos[1]].traversable:
        return GREY
    elif pos in [start, end]:
        return YELLOW
    elif pos in path:
        return BLUE
    elif pos in open:
        return GREEN
    elif pos in closed:
        return RED
    return WHITE


pg.init()
font = pg.font.SysFont("Arial", 20)
screen = pg.display.set_mode((1000, 1000))
WIDTH, HEIGHT = screen.get_size()
size = 10, 10
tile = min(WIDTH // size[0], HEIGHT // size[1] - 0)
SIDE_MARGIN = (WIDTH - size[0] * tile) / 2
TOP_MARGIN = (HEIGHT - size[1] * tile) / 2

start = (9, 1)
end = (1, 9)
board = [[Node(randint(0, 10) != 0) for _ in range(size[1])] for _ in range(size[0])]
astar_iter = astar_step(board, start, end)
open, closed, path = next(astar_iter)

while True:
    screen.fill(BLACK)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            try:
                open, closed, path = next(astar_iter)
            except StopIteration:
                print(path)

    for x in range(size[0]):
        for y in range(size[1]):
            field = pg.Rect(
                SIDE_MARGIN + x * tile, TOP_MARGIN + y * tile, tile, tile
            ).inflate(-5, -5)
            pg.draw.rect(screen, color((x, y)), field, 0)
            if board[x][y].should_draw() != 0:
                text(board[x][y], field.center)
    pg.display.update()
