from drawingpanel import *
import sys

filename = sys.argv[1]
width = sys.argv[2]
height = sys.argv[3]
font_size = sys.argv[4]
wpm = sys.argv[5]

def animate_text(panel, filename, width, height, font_size, wpm):
	canvas = panel.canvas
	f = open(filename, 'r')
	string = f.read()
	for ch in string:
		if ch == '\n':
			string = string[:string.find('\n')] + string[string.find('\n')+1:]
	word = string.split(' ')
	for w in word:
		if len(w)<=1:
			canvas.create_text(int(width)/2, int(height)/2, text = w[0],font = ('Courier', font_size), anchor = 'w', fill = 'Red' )
		elif len(w)<=5:
			canvas.create_text(int(width)/2, int(height)/2, text = w[:1], font = ('Courier', font_size), anchor = 'e')
			canvas.create_text(int(width)/2, int(height)/2, text = w[1],font = ('Courier', font_size), anchor = 'w', fill = 'Red' )
			canvas.create_text(int(width)/2, int(height)/2, text = ' ' + w[2:],font = ('Courier', font_size), anchor = 'w',)
		elif len(w)<=9:
			canvas.create_text(int(width)/2, int(height)/2, text = w[:2], font = ('Courier', font_size), anchor = 'e')
			canvas.create_text(int(width)/2, int(height)/2, text = w[2],font = ('Courier', font_size), anchor = 'w', fill = 'Red' )
			canvas.create_text(int(width)/2, int(height)/2, text = ' ' + w[3:],font = ('Courier', font_size), anchor = 'w',)
		elif len(w)<=13:
			canvas.create_text(int(width)/2, int(height)/2, text = w[:3], font = ('Courier', font_size), anchor = 'e')
			canvas.create_text(int(width)/2, int(height)/2, text = w[3],font = ('Courier', font_size), anchor = 'w', fill = 'Red' )
			canvas.create_text(int(width)/2, int(height)/2, text = ' ' + w[4:],font = ('Courier', font_size), anchor = 'w',)
		else:
			canvas.create_text(int(width)/2, int(height)/2, text = w[:4], font = ('Courier', font_size), anchor = 'e')
			canvas.create_text(int(width)/2, int(height)/2, text = w[4],font = ('Courier', font_size), anchor = 'w', fill = 'Red' )
			canvas.create_text(int(width)/2, int(height)/2, text = ' ' + w[5:],font = ('Courier', font_size), anchor = 'w',)
		if w[-1] == ',' or w[-1]=='.' or w[-1]==';':
			panel.sleep(120000/int(wpm))
		panel.sleep(60000/int(wpm))
		canvas.delete('all')

def main():
	panel = DrawingPanel(int(width), int(height))
	#canvas = panel.canvas
	animate_text(panel, filename, width, height, font_size, wpm)

main()