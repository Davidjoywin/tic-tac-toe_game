from lib import winPos


class Agent:
	def __init__(self):
		self.weight = {}

	def buildWeight(self, board, visited):
		win_pos = winPos()
		for i in range(3):
			for j in range(3):
				pos = (i, j)
				is_visited = pos in visited

	@staticmethod
	deg no_name():
		...	
