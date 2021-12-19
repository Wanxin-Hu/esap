from drawingpanel import *
import math

width = 1024
height = 768
panel = DrawingPanel(width, height)
canvas = panel.canvas

def sierpinski(n,  x,  y, size):

	if n == 0:	
		#画出最外层大三角形
		first_triangle(x, y, size)
	elif n ==1:
		#画出最外层大三角形
		sierpinski(n - 1, x, y, size)
		#画出中间的三角形
		draw_triangle(x, y, size / 2)
		#panel.sleep(1)
	else:
		#size /= 2
		#recursion
		x0 = x - size / 4
		y0 = y + size / (4*math.sqrt(3))
		x1 = x + size / 4
		y1 = y + size / (4*math.sqrt(3))
		x2 = x
		y2 = y - size/(2*math.sqrt(3))
		#画出左下角的三角形
		sierpinski(n-1, x0, y0, size / 2)
		#画出右下角的三角形
		sierpinski(n-1, x1, y1, size / 2)
		#画出上方的三角形
		sierpinski(n-1, x2, y2, size / 2)


def draw_triangle(x, y, size):
	canvas = panel.canvas
	canvas.create_line(x - size / 2, y - size*(math.sqrt(3)/6), x + size / 2, y - size*(math.sqrt(3)/6), fill = 'gold')
	canvas.create_line(x - size / 2, y - size*(math.sqrt(3)/6), x , y + size/math.sqrt(3),fill = 'gold')
	canvas.create_line(x + size / 2, y - size*(math.sqrt(3)/6), x, y + size/math.sqrt(3),fill = 'gold')

def first_triangle(x, y, size):
	canvas = panel.canvas
	canvas.create_line(x - size / 2, y + size*(math.sqrt(3)/6), x + size / 2, y + size*(math.sqrt(3)/6),fill = 'gold')
	canvas.create_line(x - size / 2, y + size*(math.sqrt(3)/6), x , y - size/math.sqrt(3),fill = 'gold')
	canvas.create_line(x + size / 2, y + size*(math.sqrt(3)/6), x, y - size/math.sqrt(3),fill = 'gold')


def main():
	sierpinski(5, width/2, height*0.6, width*0.75)
	

main()