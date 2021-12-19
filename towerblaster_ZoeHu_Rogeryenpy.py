import random

def main():
	viking_tower = []
	player_tower = []
	block_list = [None] * 2

####generate player tower
	while len(player_tower) < 10:
		number = random.randint(1, 50)
		if number not in player_tower:
			player_tower.append(number)

###generate viking tower
	while len(viking_tower) < 10:
		number = random.randint(1, 50)
		if number not in player_tower and number not in viking_tower:
			viking_tower.append(number)

####game starts
	print('Your goal is to blast vikings\' tower！')
	print('You have a tower made up with 10 blocks, and the blocks are numbered from 1 to 50.')
	print('Try to replace the blocks with what is provided and make the block ranging from smallest to biggest.')
	print('Each round, you can choose between a \'clear\' block and a mysterious block.')
	print('If you choose the clear block, you must use it. If you chose the mysterious block, you can choose whether to use it or not.')
	print('The block that is replaced is passed on to the Vikings.')
	print('They are trying to build their own tower too!')
	print('If you want to blast their tower, build it before they do!\n')
	print('*********GAME STARTS HERE***********\n')

####random block
	block_list[0] = random_block(player_tower)
	block_list[1] = random_block(player_tower)

	while(check(player_tower) and check(viking_tower)):

		print_tower(player_tower)

		#block_list[0] = random_block(player_tower)
		#block_list[1] = random_block(player_tower)
		while block_list[1] == block_list[0]:
			block_list[1] = random_block(player_tower)

		block_yes = input("Here's your block: " + str(block_list[0]) + '. \nDo you want the block? (Enter no to get the mysterious block.)\nEnter Yes or No: ')

		while 'no' not in block_yes and 'No' not in block_yes and 'yes' not in block_yes and 'Yes' not in block_yes:
			print('You must enter yes or no!!')
			block_yes = input("Here's your block: " + str(block_list[0]) + '. \nDo you want the block?\nEnter Yes or No: ')

		if 'No' in block_yes or 'no' in block_yes:
			block_list[1] = random_block(player_tower)

			want_yes  = input("Here's your block: " + str(block_list[1]) + ". \nDO you want the block?\nEnter Yes or No: ")
			while 'no' not in want_yes and 'No' not in want_yes and 'yes' not in want_yes and 'Yes' not in want_yes:
				print('You must enter yes or no!!')
				want_yes  = input("Here's your block: " + str(block_list[1]) + ". \nDO you want the block?\nEnter Yes or No: ")
			if 'No' in want_yes or 'no' in want_yes:
				block_chosed = 0
			else:
				block_chosed = block_list[1]
			
		elif 'Yes' in block_yes or 'yes' in block_yes:
			block_chosed = block_list[0]
		

####问player换哪个，输入
		if block_chosed != 0:
			index = int(input('Which block do you want to change?\nEnter 1 to 10: '))
			block_discarded = player_tower[index - 1]
			player_tower[index - 1] = block_chosed
		else:
			block_discarded = block_list[1]

###把换下来的block pass to vikings
		if block_discarded not in viking_tower:
			if block_discarded <= 5:
				nextnumber = viking_tower[0]
				viking_tower[0] = block_discarded
			elif block_discarded <= 10:
				nextnumber = viking_tower[1]
				viking_tower[1] = block_discarded
			elif block_discarded <= 15 : 
				nextnumber = viking_tower[2]
				viking_tower[2] = block_discarded
			elif block_discarded <= 20 : 
				nextnumber = viking_tower[3]
				viking_tower[3] = block_discarded
			elif block_discarded <= 25 : 
				nextnumber = viking_tower[4]
				viking_tower[4] = block_discarded
			elif block_discarded <= 30 : 
				nextnumber = viking_tower[5]
				viking_tower[5] = block_discarded
			elif block_discarded <= 35 : 
				nextnumber = viking_tower[6]
				viking_tower[6] = block_discarded
			elif block_discarded <= 40 :
				nextnumber = viking_tower[7] 
				viking_tower[7] = block_discarded
			elif block_discarded <= 45 : 
				nextnumber = viking_tower[8]
				viking_tower[8] = block_discarded
			elif block_discarded <= 50 : 
				nextnumber = viking_tower[9]
				viking_tower[9] = block_discarded
		block_list[0] = nextnumber
		#print('viking_tower is: ', viking_tower)
		print('\n')

####循环结束之后，确认输赢
	if check(player_tower):
		print('YOU LOSE! Your tower is blasted!')
	elif check(viking_tower) and not check(player_tower):
		print_tower(player_tower)
		print('YOU WIN! You blast Vikings\' tower!')
	elif not check(viking_tower) and not check(player_tower):
		print('GOOD AS VIKINGS......NO ONE WIN......')


####检查tower是否符合条件
def check(list):
	for i in range(0, len(list) - 1):
		if list[i] >= list[i + 1]:
			return True
	return False

def random_block(ls):
	block = random.randint(1, 50)
	while block in ls:
		block = random.randint(1, 50)
	return block

def print_tower(tower):
	print('Here is your tower: ')
	for i in range(0, len(tower)):
		if tower[i] >= 10:
			print(" "*(25 - int(tower[i]) // 2) + '|' * (int(tower[i]) // 2) + str(tower[i]) + "|" * (int(tower[i]) //2))
		else:
			print(" "*(25 - int(tower[i]) // 2) + '|' * (int(tower[i]) // 2) + '0' + str(tower[i]) + "|" * (int(tower[i]) // 2))

main()





