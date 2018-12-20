
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

questionCounter = 0
scoreCounter = 0

for x in range(0, 10): #question loop, outer
    randNum = int(random.randint(0, 10))

    questionCounter = questionCounter + 1
    print("Question " + str(questionCounter))
    
    song = open("songs.txt", "r")
    songName = song.readlines()[randNum]
    print(songName[0])
    song.close()

    artist = open("artists.txt", "r")
    artistName = artist.readlines()[randNum]
    print(artistName)
    artist.close()

    guessCounter = 0

    print()
    songGuess = input("What is the name of the song?\n> ")
    while(guessCounter <= 2):
        if songGuess == songName:
            print("Answer correct!")
            scoreCounter = scoreCounter + 1
            break
        else:
            guessCounter = guessCounter + 1
            print("Answer incorrect, try again.")
        if guessCounter == 2:
            print("GAME OVER")
            break

print()
print("Your score was:  " + str(scoreCounter))

#store externally
file = open("user.txt", "a")
file.write("Username: " + uName + ", Password: " + pWord + ", Score: " + str(scoreCounter) + "\n")
file.close()

# ISSUES: "Game over" displays after 1st incorrect guess.
#          Second incorrect guess doesn't end game.
#          Doesn't read more than the 1st line out of external file.


# FURTHER IMPLEMENTATIONS: Randomize order for reading lines from external file.
#                          Store User data in external "scoreboard" file in a numerically ordered "Top 5" by score.
