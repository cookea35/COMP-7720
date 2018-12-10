''' This implementation of timeStamp is based on my reference in MoveToFront.py '''

def timeStamp_encode(string, symboltable):
    sequence, pad = [], symboltable[::]

    tally = []

    for char in string:
        index = pad.index(char)
        tally.append(char)

        if (tally.count(char) == 2):
            pad = [pad.pop(index)] + pad 
            tally.remove(char)
            tally.remove(char)
        sequence.append(index)
    return sequence


def timeStamp_decode(sequence, symboltable):
    chars, pad = [], symboltable[::]
    
    tally = []

    for index in sequence:
        char = pad[index]
        tally.append(char)

        if (tally.count(char) == 2):
            pad = [pad.pop(index)] + pad
            tally.remove(char)
            tally.remove(char)
        chars.append(char)
    return chars
