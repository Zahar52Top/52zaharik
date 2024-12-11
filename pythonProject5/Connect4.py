import  pygame as pg
import sys
import math
import random
from config import *
from boaedd import *

pg.init()
pg.display.set_caption('Connect 4')

width = COLUMNS * DISC_SIZE
height = (ROWS + 1) * DISC_SIZE

size = (COLUMNS * DISC_SIZE, (ROWS + 1) * DISC_SIZE)
screen = pg.display.set_mode(size)

my_font = ...

def main():
    grid = new_grid()
    draw_grid(grid)
    pg.display.update()
    pick_random = random.randint(REAL_PLAYER, AI_PLAYER)
    game_over = false
    while not game_over:

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    sys.exit()
            elif event.type == pg.QUIT:
                sys.exit()
            is event.type == pg.MOUSEMOTION:
                pg.draw.rect(screen, WHITE, (0, 0, width, DISC_SIZE))

