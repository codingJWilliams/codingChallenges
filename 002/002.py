print("Type numbers, with an enter inbetween. Type a for average or q for quit.")
userValues = []                                 # Store the values
while True:                                     # Forever loop
    currentInput = input(">")                   # Get input from user
    if currentInput == "a":                     # If the user wants average
        print(sum(userValues) / len(userValues))#     Print the values they've given, added together then divided by the amount.
        break                                   #     Completely stop program - If this was removed you could get a running average
    elif currentInput == "q":                   # If user wants program to quit
        break                                   #     Stop program
    try:
        userValues += [int(currentInput)]       # Try and add val to list - If this fails
    except:
        print(" Invalid. Try again.")           # Then print a try again message
    
