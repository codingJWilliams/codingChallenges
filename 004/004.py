incorrect=True                                                      # So we can stop while loop
while incorrect:                                                    # While the user's password hasn't been accepted:
    containsOneUpper, containsOneLower = (False, False)             # Set both of our trackers to false
    password = input("Password>")                                   # Get user's try
    if len(password) >= 8:                                          # Make sure it's at least 8 chars long
        for letter in password:                                     # Iterate through characters
            if letter.isupper() == True: containsOneUpper = True    # Make sure at least one is upper. If so, containsOneUpper is set to true
            elif letter.islower() == True: containsOneLower = True  # Make sure at least one is lower. If so, containsOneLower is set to true
        if containsOneUpper and containsOneLower: incorrect = False # If both are true, break out of loop
    else: print("Try again.")                                       # If password length isn't 8, print try again
passwordRepeat = input("Verification>")                             # Ask user to repeat password
if password == passwordRepeat: print("Great! Your password is {}".format(passwordRepeat))# Make sure they're both the same
else: print("sIncorrect. Try again.")                                                     # If not, stop prog
