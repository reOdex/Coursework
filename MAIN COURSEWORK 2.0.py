
############################################################_LOGIN CREATION_##########################################################################################################################################################

# Set up basic login detail creation with confirmation loop:
uName = input("Choose a username\n> ")
pWord = input("Choose a password\n> ")
check = input("Your username is:  " + uName + "  -  Your password is:  " + pWord + "  - Proceed?  ")
if check == "yes":
    print()
    print("Account details successfully created.")
while check != "yes":
    uName = input("Choose a username\n> ")
    pWord = input("Choose a password\n> ")
    check = input("Your username is:  " + uName + "  -  Your password is:  " + pWord + "  - Proceed?  ")
    if check == "yes":
        print()
        print("Account details successfully created.")


#################################################################_LOGIN_###################################################################################################################################################################

# Login process:
print()
print("Welcome to the music quiz, please log in")
uNameLog = input("Input username\n> ")
pWordLog = input("Input password\n> ")
if uNameLog == uName and pWordLog == pWord:
    print()
    print("Logging in...")
while uNameLog != uName or pWordLog != pWord:
    uNameLog = input("Input username\n> ")
    pWordLog = input("Input password\n> ")
    if uNameLog == uName and pWordLog == pWord:
        print()
        print("Logging in...")

###################################################################_MAIN_####################################################################################################################################################################

import random

questionNum = 10
guessNum = 2

# Load data from external file:
file = open("songs.txt", "r")
line = file.readline()
data = line.split(",")
artist = data[0]
song = data[1]
score = 0

for questionCount in range(questionNum):
    print(line)
    print(artist)
    print(song[0])

    guess = input("What is the song called?\n> ")

    guessCount = 0
    guessCorrect = False
    while True:
        if guess == song:
            guessCorrect = True
            score = score + 3
            break

        guessCount += 1
        if guessCount >= guessNum:
            score = score + 1
            break

        # Song wasn't guessed correctly and we haven't hit 
        # the max guesses yet, so try again:
        guess = input("Incorrect! Try again:\n> ")

    if guessCorrect:
        print("Answer correct!")
    else:
        print()
        print("GAME OVER")
        break
file.close()

print(score)
