def answer(food, grid):
    frontier = [(0, 0, food, [])]
    while True:
        if len(frontier) == 0:
            return -1
        curr = frontier.pop(0)
        if curr[0] == (len(grid) - 1) and curr[1] == (len(grid) - 1):
            return curr[2]

        future = []
        for x in range(0, 2):
            for y in range(0, 2):
                if (x == 0 or y == 0) and (x != 0 or y != 0):
                    newX = curr[0] + x
                    newY = curr[1] + y
                    if newX >= 0 and newY >= 0 and newX < len(grid) and newY < len(grid) and (curr[2] - grid[newX][newY]) >= 0 :
                         future.append((newX, newY, curr[2] - grid[newX][newY]))
        frontier.extend(future)
        frontier.sort(key=lambda x: x[2])

from random import randrange
N = 20
grid = [[randrange(1, 10) for _ in range(N)] for _ in range(N)]
T = 200
foodT = randrange(1, T)

print(grid, foodT, answer(foodT, grid))

print(answer(12, [[0, 2, 5], [1, 1, 3], [2, 1, 1]]))
print(answer(7, [[0, 2, 5], [1, 1, 3], [2, 1, 1]]))