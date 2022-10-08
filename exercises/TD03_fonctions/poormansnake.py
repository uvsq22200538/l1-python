from random import randint
from time import sleep

grid = []

for i in range(10) :
    grid.append([])
    for o in range(10) :
        grid[i].append('-')

for o in range(5) :
    print('')
    for i in grid:
        print(' '.join([str(j) for j in i]))
    sleep(5)