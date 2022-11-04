def swap_list(inputList):
    
    #conditions for various inputs
    if (len(inputList) == 0):
        return inputList
    if (len(inputList) % 2 == 0):
        middleIndex = int(len(inputList)/2) - 1
    else:
        middleIndex = int(len(inputList)/2)
    
    #swapping part
    temp = inputList[middleIndex]
    inputList[middleIndex] = inputList[-1]
    inputList[-1] = temp
    return inputList
