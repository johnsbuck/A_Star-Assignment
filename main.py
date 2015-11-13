# Concepts in AI
# Author: John Bucknam
# Homework 3 (Implementing A*)
# October 20, 2015

import time
from sys import argv


# The heuristics function of the game
def h(board):
    black = True
    # 2 iterators for checking the
    # number of Bs and number of None
    i = 0
    j = 0
    # Iterates until it hits a W
    while black and ((i + j) < len(board)):
        if board[i + j] == 'w':
            black = False
        elif board[i + j] == 'b':
            i += 1
        else:
            j += 1  # Hits an empty spot
    # Returns the number of Bs
    return i


# Checks if a board is correct
def correct(board):
    white = 0
    for i in range(len(board)):
        if white == 3:
            return True
        if board[i] == 'w':
            white += 1
        elif board[i] == 'b':
            return False


# Creates future possible boards with different moves
def moves(state):
    # Gets the current board from input
    board = state[0];
    # Finds all empty spots
    nIndex = board.index('n')
    # Checks all possible moves
    moveList = []
    # index-3 and index+3 (the nIndex+4 is in realy nIndex+4-1)
    for x in range(nIndex-3, nIndex+4):
        # Empty spot can't swap with non-existing spots or self
        if(x >= 0 and x < len(board) and not x == nIndex):
            # Create new board
            newboard = list(board)
            # Board will swap with positions with empty spot
            temp = newboard[x]
            newboard[x] = newboard[nIndex]
            newboard[nIndex] = temp
            # Based on location, cost will be up to 2
            cost = 2 if abs(x - nIndex) > 2 else 1
            # Cost will take past cost (minus past heuristic function)
            cost = cost + state[1] - state[2]
            # Add new board tuple to possible moves
            # (Board, (g(x) + h(x)), h(x), previous moves)
            moveList.append((newboard, cost + h(newboard), h(newboard), list(state[3])))
    return moveList


# Actual function
def solve(board):
    #(state, g(state) + h(state), h(state), route)
    frontier = [(board, h(board), h(board), [])]
    close = []
    # Will loop until a solution is found or there is no solution
    while True:
        # If the frontier is empty
        if len(frontier) == 0:
            ret = ('NaN', False)
            return ret

        # Pop the top of frontier
        curr = frontier.pop(0)

        # If the current board is a correct answer
        if correct(curr[0]):
            ret = (curr[1] - curr[2], [])
            for i in range(len(curr[3])):
                ret[1].append(close[curr[3][i]])
            ret[1].append(curr[0])
            return ret
        # If the current board has not already been used
        if not curr[0] in close:
            # Obtain future moves
            future = moves(curr)
            # Add the last board to future options
            # (Adding length of close which will be the curr's index once appended to close)
            for i in range(len(future)):
                future[i][3].append(len(close))
            # Add future options to frontier
            frontier.extend(future)
            # Sort frontier based on (g(x) + h(x))
            frontier.sort(key=lambda x: x[1])
            # Add current to close
            close.append(curr[0])

# START
print("John Bucknam")
print("HW 3: A* Algorithm")
print('')

# Board is being defined
board = ['b', 'b', 'b', 'n', 'w', 'w', 'w']
if len(argv) == 8 and argv.count('w') == 3 and argv.count('b') == 3 and argv.count('n') == 1:
    board = argv[1:8]
else:
    print("Default: [b, b, b, n, w, w, w]")
print('Problem:' + str(board))

# Start
begin = time.clock()
complete = solve(board)
end = time.clock()

# Print results
print('')
# Time rounded to 1000th msec
print('Time: ' + str(round(((end - begin) * 1000), 3)) + ' msec')
# Total cost
print('Cost: ' + str(complete[0]))
if complete[1]:
    # Total number of moves
    print('Moves: ' + str(len(complete[1]) - 1))
    # Each move
    for i in range(len(complete[1])):
        print(str(i) + ':' + str(complete[1][i]))
else:
    print('No solution')

# The reason why values in print are surrounded by str() is because they have to be specially concatenated
# to print out correctly in terminal [i.e. 'Time: 5 msec' instead of ('Time: ', 5, 'msec')]
