import random
options=["rock", "paper", "scissors", "q", "p"]
userwins=0
compwins=0
draws=0

while True:
    q1: str=input("Do you want to play rock paper scissors? Respond with either yes or no. ").lower()
    if q1=="yes":
        print("Alright!")
        break
    elif q1=="no":
        q1_1=input("Are you sure? ").lower()
        if q1_1=="no":
            print(":)")
            break
        elif q1_1=="yes":
            print(":(")
            quit()
        else:
            continue
    else:
        continue

while True:
    userpick=input("Please pick between rock, paper or scissors. If you want to stop the game, input q. If you want to pause the game, input p. ").lower()
    if userpick not in options:
        continue
    if userpick=="q":
        break
    elif userpick=="p":
        pause=input("Input anything if you want to continue playing. ")
        continue
    randomnum = random.randint(0, 2)
    # rock-0, paper-1, scissors-3

    compick = options[randomnum]

    randomnum2=random.randint(0, 2)


    damn=["Aww, you lost!", "You lost :(. Better luck next time!", "Oof! The computer won."]
    yay=["Oh, you won!", "Great job! You beat the computer!", "Sick! You won!"]
    drawlines=["Ooh, a tie!", "You both picked the same thing!", "You drew the computer! What are the chances?"]
    damn2=damn[randomnum2]
    yay2=yay[randomnum2]
    drawlines2=drawlines[randomnum2]
    print("The computer picked " + compick + ".")

    if compick==userpick:
        print(drawlines2)
        draws+=1
    elif compick=="rock" and userpick=="scissors":
        print(damn2)
        compwins+=1
    elif compick=="rock" and userpick=="paper":
        print(yay2)
        userwins+=1
    elif compick=="paper" and userpick=="scissors":
        print(yay2)
        userwins+=1
    elif compick=="paper" and userpick=="rock":
        print(damn2)
        compwins+=1
    elif compick=="scissors" and userpick=="rock":
        print(yay2)
        userwins+=1
    elif compick=="scissors" and userpick=="paper":
        print(damn2)
        compwins+=1
print("You beat the computer a total of", userwins, "times, drew", draws, "times, and lost", compwins, "times.")












