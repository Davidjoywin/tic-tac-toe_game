import os, sys

path = os.path.abspath('..')
sys.path.append(path)

from agent import Agent


agent = Agent()

board = [['-' for _ in range(3)] for _ in range(3)]

pot = Agent.getPotMove(board, (0,0), 'x', 'o')
print(pot)
