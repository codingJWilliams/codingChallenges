import random 
tries, continueLoop, generatedValues, userValues = (0, True, [random.choice([0,1,2,3,4,5,6,7,8,9]),random.choice([0,1,2,3,4,5,6,7,8,9]),random.choice([0,1,2,3,4,5,6,7,8,9]),random.choice([0,1,2,3,4,5,6,7,8,9])], [0,0,0,0])
while continueLoop:
    userGuessString = input("Guess>")
    try: userGuess = int(userGuessString)
    except ValueError: continue
    if len(userGuessString) != 4: continue
    tries += 1
    for key,digit in enumerate(userGuessString): userValues[key] = int(digit)
    correctCounter = 0
    for key,entry in enumerate(userValues): if entry == generatedValues[key]: correctCounter += 1
    if correctCounter <= 3: print("You got {} correct.".format(correctCounter))
    elif correctCounter == 4: continueLoop = False
print(" Tries: {}".format(tries))
