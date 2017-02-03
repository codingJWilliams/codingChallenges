import random   #Basis of program
randomConstraints = [0,1,2,3,4,5,6,7,8,9]
continueLoop = True #for while loop
generatedValues, userValues = (
    [random.choice(randomConstraints),random.choice(randomConstraints),random.choice(randomConstraints),random.choice(randomConstraints)],         #Target Values
    [0,0,0,0])                                                                                                                                     #User's Guess
while continueLoop:  #Create while loop with continueLoop as a condition
    userGuessString = input("Guess>")
    try: userGuess = int(userGuessString)
    except ValueError:
        print("Please enter a valid number")
        continue
    if len(userGuessString) != 4:
        print("Please enter a valid 4 digit number")
        continue
    for key,digit in enumerate(userGuessString):
        userValues[key] = int(digit)
    for 
