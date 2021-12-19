from drawingpanel import *
width = 500
height = 500
panel = DrawingPanel(width, height)
canvas = panel.canvas

def circle(x0, y0, x1, y1, number, diamond):
	canvas = panel.canvas
	side = x1- x0
	#the large rectangle
	if diamond:
		canvas.create_rectangle(x0, y0, x1, y1, fill = 'cyan', outline = 'black')
	#circles
	for i in range(0, number):
		canvas.create_oval(x0 + i * side / (number * 2), y0 + i * side / (number * 2), x1 - i * side / (number * 2), y1 - i * side / (number * 2), fill = 'yellow', outline = 'black')
	#diamond
	if diamond:
		canvas.create_line((x0 + x1) / 2, y0, x0, (y0 + y1) / 2, fill = 'black')
		canvas.create_line(x0, (y0 + y1) / 2, (x0 + x1) / 2, y1, fill = 'black')
		canvas.create_line((x0 + x1) / 2, y1, x1, (y0 + y1) / 2, fill = 'black')
		canvas.create_line(x1, (y0 + y1) / 2, (x0 + x1) / 2, y0, fill = 'black')

def grid(x0, y0, x1, y1, number, a, b, diamond):
	side = x1 - x0
	for i in range(0, a):
		for j in range(0, b):
			circle(x0 + side * i, y0 + side * j, x1 + side * i, y1 + side * j, number, diamond)


def ehrenstein():
	canvas = panel.canvas
	panel.set_background("green")

	#topleft
	grid(0, 0, 75, 75, 6, 1, 1, True)
	#top
	grid(105, 15, 155, 65, 10, 7, 1, True)
	#left
	grid(10, 100, 80, 170, 3, 2, 5, True)
	#middle
	grid(175, 115, 275, 215, 8, 3, 3, True)
	#bottom
	grid(200, 430, 225, 455, 4, 10, 2, False)

def main():

	ehrenstein()

main()

