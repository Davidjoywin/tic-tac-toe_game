pos = []
def winPos():
	for i in range(3):
		win = []
		for j in range(3):
			cell = (i, j)
			win.append(cell)
		pos.append(win)

	for i in range(3):
		win = []
		for j in range(3):
			cell = (j, i)
			win.append(cell)
		pos.append(win)

	win = []
	for i in range(3):
		cell = (i,i)
		win.append(cell)
	pos.append(win)
	
	win = []
	for i in reversed(range(3)):
		cell = (i, i)
		win.append(cell)
	pos.append(win)
	
	return pos
