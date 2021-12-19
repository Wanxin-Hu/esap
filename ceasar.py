#
def encode(code_to_encode, rotation):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	alphabet_rotated = alphabet +  alphabet[0:int(rotation)]
	code=''
	for i in range(0, len(code_to_encode)):
		if (code_to_encode[i] in alphabet):
			index = alphabet.find(code_to_encode[i])
			code += alphabet_rotated[index + int(rotation)]
		else:
			code += code_to_encode[i]
	return code

def decode(code_to_decode, decoded):
	alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
	rotation_0 = alphabet.find(decoded[0]) - alphabet.find(code_to_decode[0])
	for i in range (0, len(code_to_decode)):
		original = alphabet.find(code_to_decode[i])
		finalindex = alphabet.find(decoded[i])
		possible_rotation = finalindex - original
		if(rotation_0 != possible_rotation):
			return "No such rotation"
	return rotation_0

def quit():
	print("SEE YOU AGAIN")

def main():
	key = input("Encode: e; Decode: d; Quit: q ")

	if key == 'e':
		code_to_encode = input('What string do you want to encode? : ')
		rotation = input("Choose a number between 1 and 25, inclusive: ")
		print(encode(code_to_encode, rotation))

	elif key == 'd':
		code_to_decode = input("What string do you want to decode? : ")
		decoded = input("What is the decoded string? :")
		print(decode(code_to_decode, decoded))

	elif key == 'q':
		quit()

	else:
		key = input("Wrong Key! Encode: e; Decode: d; Quit: q")

main()
