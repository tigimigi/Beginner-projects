import time
lose=False
win=False
print("You've been driving for 4 hours to get to your in-laws' house for Thanksgiving, and you finally arrive. ")


q0=input("You're about to pull to their house. Continue driving or go back? (Continue/Go back) ").lower()
if q0== "go back":
    while True:
        q1=input("Aww, c'mon man, that was a 4 hour drive. Are you sure u wanna go back? (Yes/Never mind) ").lower()
        if q1=="never mind":
            print("Alright! Your adventure continues.")
            break
        elif q1=="yes":
            while True:
                q2=input("Okay. You're really low on fuel. Would you like to go to the gas station? (Yes/No) ").lower()
                if q2=="no":
                    print("🤣🤣🤣🫵🫵🫵 YOU RAN OUT OF GAS AND DIED 🤣🤣🤣🤣")
                    print("You lost :(. Better luck next time.")
                    quit()
                elif q2=="yes":
                    print("You arrive home, safe and sound.")
                    time.sleep(1)
                    print("and then your spouse beats you to death.")
                    time.sleep(0.7)
                    print("You lost :(. Better luck next time.")
                    quit()
                else:
                    print("🙄🤦‍♀️ FOLLOW INSTRUCTIONS")

        else:
            print("🙄🤦‍♀️ FOLLOW INSTRUCTIONS")


print("You arrive, and your in-laws start sizing you up.")
print("You feel uncomfortable, and the second you sit down, they ask you who you're voting for. ")
while True:
    q1=input("You know it's Harris, but they're Trump supporters. What do you say? (Harris/Trump) ").lower()
    if q1=="harris":
        print("Your in-laws kick you out of the house immediately.")
        lose=True
        break
    elif q1=="trump":
        print("Good choice! Your in-laws are starting to like you.")
        q2=input("Now, you sit at the dinner table, and your really hungry. How much food do you eat? (2 servings/1 serving) ").lower()
        if q2=="2 servings":
            print("Your mother in law notices. She calls you an ungrateful turd and kicks you out.")
            lose=True
            break
        elif q2=="1 serving":
            print("You continue to have a great day at your in-laws' house. They accept you into the family and wish you a good night.")
            break
        else:
            print("🙄🤦‍♀️ FOLLOW INSTRUCTIONS! Either input '1 serving' or '2 servings'!!!")


timea.sleep(1)
if lose==True:
    print("You lost :(. Better luck next time.")
elif win:=True:
    print("You won!")
else:
    print("Something went wrong 🤔")
