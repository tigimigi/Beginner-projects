import random
Q1=input("Would you like to play Guess The Number? ").lower()

if Q1=="yes":
    print("Let's go!")
elif Q1=="no":
    rush=input("Are you sure? ").lower()
    if rush=="no":
        rush2=input("So do you want to play? ").lower()
        if rush2=="yes":
            print("Yay! :D")
        elif rush2=="no":
            print("idc u ur still playing")
        else:
            print("It's a yes or no question.")
            quit()
    elif rush=="yes":
        print(":(")
        quit()
    else:
        print("Please answer with either a yes or a no.")
else:
    print("Please answer with either a yes or a no.")
    quit()

usermax=input("Please tell me the range. 1-")


if usermax.isdigit():
    usermax=int(usermax)
else:
    print("Please input a number above 1.")
    quit()

if usermax <= 1:
    print("Please input a number above 1.")
    quit()

random_number=random.randint(1, usermax)
guess=0

while True:
    userguess=input("Now make a guess! ")
    if userguess.isdigit():
        userguess=int(userguess)
    else:
        userguess=input("Please provide me with a number: ")
        if userguess.isdigit():
            userguess = int(userguess)
        else:
            print("It seems you refuse to follow directions.")
            quit()

    if userguess==random_number:
        print("You got it!")
        guess+=1
        break
    elif userguess<random_number:
        print("Guess higher!")
        guess+=1
    elif userguess>random_number:
        print("Guess lower!")
        guess+=1
print("Amazing work! You successfully guessed the number after", guess, "attempt(s)!")