nameList = []                                                            # Init list to hold names
def ifReplacement(u): return {"o": nameList, "r": reversed(nameList)}[u] # Basically look up user input in dictionary, errors if not found and prints results if found.
while True:                                                                 # ^- I could have used an if elif etc but that takes up too many lines.
    userInput = input(">")
    try: print(list(ifReplacement(userInput)))
    except: nameList += [userInput]
