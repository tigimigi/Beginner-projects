import random
from http.cookiejar import user_domain_match

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please input a number larger than 0.')
        quit()
else:
    print('Please input a number.')
    quit()
random_number = random.randint(0, top_of_range)
guesses=0

while True:

    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        guesses+=1
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess>random_number:
            print("Guess a lower number!")
    else:
            print("Guess a higher number!")

print("You got it in", guesses, "guesses!")