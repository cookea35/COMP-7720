import BIT
import Timestamp
import random

''' This weightedChoice method is based on code from the "Giving up the temporary list" section: https://eli.thegreenplace.net/2010/01/22/weighted-random-generation-in-python'''

def weightedChoice(weights):
	rand = random.random() * sum(weights)
	for i, w in enumerate(weights):
		rand -= w
		if rand < 0:
			return i

def combAlg_encode(string, symboltable):
    
	#probability with which timestamp and bit will be chosen respectively
	prob = [2,8]
	choice = weightedChoice(prob)
	
	if (choice == 1):
		lis = BIT.bitAlg_encode(string, symboltable)
		lis.append(choice)
		format(lis[len(lis)-1], 'b')
	if (choice == 0):
		lis = Timestamp.timeStamp_encode(string, symboltable)
		lis.append(choice)
		format(lis[len(lis)-1], 'b')
	return lis

def combAlg_decode(sequence, symboltable):
	if sequence[0] == 0b1:
		BIT.bitAlg_decode(sequence, symboltable)
	if sequence[0] == 0b0:
		Timestamp.timeStamp_decode(sequence, symboltable)
