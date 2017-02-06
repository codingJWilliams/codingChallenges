numList,minNumber,maxNumber = ([],0,0)                      # Init list to hold nums, min and max            
userInput = int(input(">"))
numList += [userInput]
minNumber,maxNumber = (userInput, userInput)
while True:
    userInput = int(input(">"))
    numlist += [userInput]
    for num in numlist:
        if num > maxNumber: maxNumber = num
        if num < minNumber: minNumber = num
        print("Min: {}, Max: {}".format(minNumber, maxNumber))
