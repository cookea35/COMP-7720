def rle(sequence):
    tempList = []
    currBit = sequence[0]
    prevBit = sequence[0]
    tracker = 1

    for i in range(1, len(sequence)):
        currBit = sequence[i]
        if(prevBit != currBit):
            tempList.append(tracker)
            format(tempList[len(tempList)-1], 'b')
            tempList.append(prevBit)
            prevBit = currBit
            tracker = 0
        tracker+=1
    return tempList

def rld(sequence):
    tempList = []
    currBits = []
    index = 0

    while index < len(sequence):
        currBits.append(sequence[index])
        currBits.append(sequence[index+1])

        for j in range(0, int(currBits[index])):
            tempList.append(currBits[index+1])
        index+=2
    return tempList
