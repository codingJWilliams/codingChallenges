wordList, userLetter, endList=(["asparagus", "apples", "avacado", "alfalfa", "broccoli", "celery", "donuts"], input("Select a letter>"), [])   #Define wordlist, ask for input and define endlList as emptyfor i in wordList:   # Iterate wordList    if userLetter == i[0]: endList += [i] # if firstLetter and the word's first letter match, add word to listfor i in endList: print(i, end=', ') #Print list
