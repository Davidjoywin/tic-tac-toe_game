import os, sys

path = os.path.abspath('..')
sys.path.append(path)

from agent import Agent


agent = Agent()

board = [['-' for _ in range(3)] for _ in range(3)]

board[1][1] = 'x'
board[2][2] = 'o'

# print(board)
for i in range(3):
    for j in range(3):
        pot = Agent.getPotMove(board, (i, j), ('x', 'o'))
        # print(pot)

pot = Agent.getPotMove(board, (0,1), ('x', 'o'))
sides = Agent.joinPotMovesSides(pot, (0,1))
# print(sides)

board[0][1] = 'x'
board[2][0] = 'o'
board[0][2] = 'x'
board[0][0] = 'o'
board[2][1] = 'x'

board = [['-' for _ in range(3)] for _ in range(3)]
board[1][1] = 'o'

for i in range(3):
    for j in range(3):
        print(board[i][j], end=' ')
    print()
agent.buildWeight(board, 'x', ('x', 'o'))

print(agent.weight)

print(max(agent.weight.values()))
