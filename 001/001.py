import random   #Basis of program
randomConstraints = [0,1,2,3,4,5,6,7,8,9]  #Numbers random can choose from
tries = 0 #Count tries
continueLoop = True #for while loop
generatedValues = [random.choice(randomConstraints),random.choice(randomConstraints),random.choice(randomConstraints),random.choice(randomConstraints)]         #Target Values
userValues = [0,0,0,0]                                                                                                                                          #User's Guess
while continueLoop:  #Create while loop with continueLoop as a condition
    userGuessString = input("Guess>") #Ask user for guess
    try: userGuess = int(userGuessString)        # Makes sure that user's input is an integer
    except ValueError:                           # "
        print("Please enter a valid number")     # "
        continue                                 # Skips an iteration of loop, therefore asking for another input
    if len(userGuessString) != 4:                    # Makes sure user's input is 4 digits
        print("Please enter a valid 4 digit number") # "
        continue                                 # Skips an iteration of loop, therefore asking for another number
    tries += 1                                   # Add 1 try to counter
    for key,digit in enumerate(userGuessString): # Iterates through user's guess (which is a string), putting it in userValues list
        userValues[key] = int(digit)             # "
    correctCounter = 0                           # Counts how many correct numbers in string
    for key,entry in enumerate(userValues):      # Iterates through the dictionary of user's values
        if entry == generatedValues[key]:        # Is that digit == to the random value?
            correctCounter += 1                  #     if so, add one to correctCounter
    if correctCounter <= 3:                      # If user got less than 4 correct,
        print("You got {} correct.".format(correctCounter)) # tell user how many they got correct
    elif correctCounter == 4:                    # If user got all correct
        print(" You got it right!")              #     Notify them
        continueLoop = False                     #     Break completely out of loop, ending program
print(" Tries: {}".format(tries))
