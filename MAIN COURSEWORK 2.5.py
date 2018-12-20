
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

print()

import random

questionCounter = 0

for x in range(0, 10):
    randNum = int(random.randint(0, 10))

    print()

    questionCounter = questionCounter + 1
    print("Question " + str(questionCounter))

    song = open("songs.txt", "r")
    songName = str(song.readlines()[randNum])
    print("Song hint: " + songName[0])
    song.close()

    artist = open("artists.txt", "r")
    artistName = artist.readlines()[randNum]
    print("Artist name: " + artistName)
    artist.close()

    guessCounter = 0
    scoreCounter = 0

    songGuess = input("What is the song called?")
    while(guessCounter <= 0):
        if songGuess == songName:
            print("Answer correct!")
            scoreCounter = scoreCounter + 1
            break
        elif songGuess != songName:
            guessCounter = guessCounter + 1
            songGuess = input("Incorrect! Try again:")

        elif guessCounter == 2:
            print("GAME OVER")
            break

print()
print("Your score was: " + scoreCounter)
