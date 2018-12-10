''' This implementation of BIT is based on my reference for MoveToFront.py '''

import random

def bitAlg_encode(string, symboltable):
	sequence, pad = [], symboltable[::]
	bitTable = []
	tempTable = []

	for i in range(0, len(symboltable)):
		bitTable.append(random.randint(0,1))
        
	tempTable = bitTable

	for char in string:
		index = pad.index(char)
		if (bitTable[index] == 1):
			pad = [pad.pop(index)] + pad
			bitTable[index] = bitTable[index] ^ 1
		sequence.append(index)
	return sequence + tempTable

def bitAlg_decode(sequence, symboltable):
	chars, pad = [], symboltable[::]
	bitTable = []

	bitTable = sequence[len(sequence)-len(symboltable):len(sequence)]
	sequence = sequence[0:len(sequence)-len(symboltable)]

	for index in sequence:
		char = pad[index]
		if (bitTable[index] == 1):
			pad = [pad.pop(index)] + pad
			bitTable[index] = bitTable[index] ^ 1
		chars.append(char)
	return chars
