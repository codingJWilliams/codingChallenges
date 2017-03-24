import questions, random
finalText = """
Quiz v1.0!
By: Jay Williams.

"""
for i in range(1, 6):
    currentQuestion = random.choice(random.choice(questions.subjects))
    finalText += "\nQ{}: {}".format(i, currentQuestion[0])

print(finalText)
