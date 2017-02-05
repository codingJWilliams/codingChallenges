userValues = []
while True:
    currentInput = input(">")
    if currentInput == "a": print(sum(userValues) / len(userValues))
    elif currentInput == "q": break
    userValues += [int(currentInput)]
