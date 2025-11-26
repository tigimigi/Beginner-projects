import random

userwins=0
computerwins=0
draws=0

options=["rock", "paper", "scissors"]

while True:
    userinput=input("Type rock/paper/scissors or q to quit: ").lower()
    if userinput=="q":
        break

    if userinput not in options:
        continue

    randomnumber = random.randint(0, 2)
    # rock-0, paper-1, scissors-2
    computerpick = options[randomnumber]
    print("Computer picked", computerpick + ".")

    if userinput == "rock" and computerpick== "scissors":
        print("You won!")
        userwins+=1
    elif userinput == computerpick:
        print("Oh, that was a draw!")
        draws+=1
    elif userinput == "paper" and computerpick== "rock":
        print("You won!")
        userwins+=1
    elif userinput == "scissors" and computerpick== "paper":
        print("You won!")
        userwins+=1
        continue
    else:
        print("You lost! :(")
        computerwins +=1
print ("You won", userwins, "times. The computer won", computerwins, "times. You and the computer drew", draws, "times.")

print("Goodbye!")