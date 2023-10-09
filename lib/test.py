"""
from circular_link_list import circular_list

clist = circular_list.run('X', 'O')

for _ in range(50):
	print(clist.data)
	clist = clist.next
	print("\n")
"""
from datetime import datetime

from score import score

date_time = datetime.now()
score(str(date_time), {"name": "david"})
