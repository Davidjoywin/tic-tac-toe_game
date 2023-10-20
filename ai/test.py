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
'''
for i in range(3):
    for j in range(3):
        print(board[i][j], end=' ')
    print()
agent.buildWeight(board, 'x', ('x', 'o'))
'''
# print(agent.getBestMove())

board[2][2] = 'x'
agent.buildWeight(board, 'x', ('x', 'o'))
# print(agent.getBestMove())

agent.buildWeight(board, 'x', ('x', 'o'))
# print(agent.getBestMove())

"""
for _ in range(10):
    agent.buildWeight(board, 'x', ('x', 'o'))
    best_move = agent.getBestMove()
    print(best_move)
"""


import time
from lib import winPos, circular_list

def drawBoard(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=' ')
        print()

win_pos = winPos()
players = circular_list.run('X', 'O')

board = [['-' for _ in range(3)] for _ in range(3)]
agent = Agent()

def isWin(board, cur_player):
    is_win = []
    for win_pos in winPos():
        for pos in win_pos:
            x, y = pos
            is_win.append(board[x][y] == cur_player)
        return all(is_win)

def isTie(board, players):
    is_tie = False
    
    for i in range(3):
        for j in range(3):
            is_tie = board[i][j] in players
    return is_tie
    
            
while True:
    drawBoard(board)

    print()
    cur_player = players.data
    time.sleep(1)
    agent.buildWeight(board, cur_player, ('X', 'O'))
    best_move = agent.getBestMove()
    if best_move:
        x, y = best_move
        board[x][y] = cur_player
    if isWin(board, cur_player):
        print("congrats you won!!")
        break

    players = players.next
    time.sleep(1)

"""
from lib import winPos

board = [['-' for _ in range(3)] for _ in range(3)]

agent = Agent()

# pot_moves = Agent.getPotMove(board, (2,2), 'x')

weight = agent.buildWeight(board, 'X', ('X', 'O'))
print(agent.weight)
"""