def draw(num):
	print("----------------")
	for i in range(0, 2 * int(num) - 2):
		print("|\/\/\/\/\/\/\/|")
	print("----------------")

def draw(num):
	for i in range(1, num + 1):
		print(" "*(num - i) + "/" + "*="*(i - 1) + "\\")
	print("-" * (2 * num))

def print_rocketship1():
	#part1
	for i in range(1, 6):
		print(" "*(6 - i) + '/' * i + "**" + "\\" * i)

	#part2
	print("+=*=*=*=*=*=*+")
	for i in range(1, 4):
		print("|" + ("." * (3 - i) + "/\\" * i + "." * (3 - i)) * 2 + "|")
	for i in range(3, 0, -1):
		print("|" + ("." * (3 - i) + "\\/" * i + "." * (3 - i)) * 2 + "|")

	#part3
	print("+=*=*=*=*=*=*+")
	for i in range(1, 4):
		print("|" + ("." * (i - 1) + "\\/" * (4 - i) + "." * (i - 1)) * 2 + "|")
	for i in range(3, 0, -1):
		print("|" + ("." * (i - 1) + "/\\" * (4 - i) + "." * (i - 1)) * 2 + "|")

	print("+=*=*=*=*=*=*+")
	for i in range(1, 6):
		print(" " * (6 - i) + '/' * i + "**" + "\\" * i)



def print_top(num):
	for i in range(1, num * 2):
		print(" " * (num * 2 - i) + '/' * i + "**" + "\\" * i)

def print_box_up(num):
	for i in range(1, num + 1):
		print("|" + ("." * (num - i) + "/\\" * i + "." * (num - i)) * 2 + "|")

def print_box_down(num):
	for i in range(1, num + 1):
		print("|" + ("." * (i - 1) + "\\/" * (num + 1 - i) + "." * (i - 1)) * 2+ "|")

def print_line(num):
	print("+" + "=*" * (2 * num) + "+")

def print_rocketship2(num):
	print_top(num)

	print_line(num)

	print_box_up(num)
	print_box_down(num)

	print_line(num)

	print_box_down(num)
	print_box_up(num)
	
	print_line(num)

	print_top(num)


def main():
	print_rocketship2(num)

num = int(input("What is the height?"))
main()
