import math

TILESIZE = 32
ROWS = 10
COLS = 15

WINDOW_WIDTH = COLS * TILESIZE
WINDOW_HEIGHT = ROWS * TILESIZE

FOV = 60 * (math.pi / 180) # Radians for math functions

RES = 4
NUM_RAYS = WINDOW_WIDTH // RES
