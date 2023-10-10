"""
from circular_link_list import circular_list

clist = circular_list.run('X', 'O')

for _ in range(50):
	print(clist.data)
	clist = clist.next
	print("\n")
"""

"""
from datetime import datetime

from score import score

date_time = datetime.now()
score(str(date_time), {"name": "david"})
"""


"""
from check_tie import checkTie

board = [['O' for _ in range(3)] for _ in range(3)]

player_1 = 'O'
player_2 = 'X'

# when the board are contained by the players
check_tie = checkTie(board, player_1, player_2)

# True
print(check_tie)

# when the board is not contained by the players
check_tie = checkTie(board, 'o', 'x')

# False
print(check_tie)
"""


from score import score

obj = {"name": "david"}

score(obj)
