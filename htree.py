from drawingpanel import *

width = 1024
height = 768
panel = DrawingPanel(width, height)
canvas = panel.canvas
 
def draw_h(x, y, size):
    #construct a panel of width 640, height = 480
    
    #get the canvas from this window/panel
    canvas = panel.canvas
    canvas.create_line(x - size / 2, y, x + size / 2, y)
    canvas.create_line(x - size / 2, y + size / 2, 
    	x - size / 2, y - size /2)
    canvas.create_line(x + size / 2, y + size / 2,
                    x + size / 2, y - size / 2)
 

def draw(n,  x,  y, size):
        if n == 0:
        	return
        draw_h(x, y, size)
        
        #now recursively make 4 smaller H trees
        x0 = x - size / 2
        y0 = y - size / 2
        x1 = x + size / 2
        y1 = y + size / 2
        #first draw the bottom left subtree
        draw(n - 1, x0, y0, size / 2)
        #then draw the top left subtree
        draw(n - 1, x0, y1, size / 2)      
        #then the bottom right subtree
        draw(n - 1, x1, y0, size / 2)
        draw(n - 1, x1, y1, size / 2)
        panel.sleep(100)


def main():
    
    draw(8, width / 2, height / 2, width / 4)


main()

