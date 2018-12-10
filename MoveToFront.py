''' This mtf encode and decode methods are based on code from: https://rosettacode.org/wiki/Move-to-front_algorithm#Python '''


def mtf_encode(charList, uniqueList):
	chars, pad = [], uniqueList[::]	

	uniqueList = list(uniqueList)    

	for i in charList:
		pos = pad.index(i)
		chars.append(pos)
		pad = [pad.pop(pos)] + pad
	return chars
	

def mtf_decode(charList, uniqueList):
	chars, pad = [], uniqueList[::]
	
	uniqueList = list(uniqueList)

	for i in charList:
		char = pad[i]
		chars.append(char)
		pad = [pad.pop(i)] + pad
	return chars 


