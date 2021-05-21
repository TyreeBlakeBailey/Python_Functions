# Done-> User story 1 - As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.

# Done-> 2 - As a user, I should get feedback if my number is too high or too low so I can adjust my guess.

# Done-> 3 - as a user I should only be able to guess 3 times before a new number is generated

# Done-> 4 - as a user, I should be able to keep playing until I respond with exit

# Done-> 5 - as a user, I should be able to use exit in a sentence and still terminate the program

# extra 6 - as a user, when I terminate the program I should get a message thanking me for playing and the number of times I guesses and number of times I found the number.

# Extra 7 - as a user, I should be asked the highest number that can be used to generate a random number

# self five
## Acceptance Criteria
#
# * random number is generate by random library
# * all core 5 user stories should be done
# * program should **not break** when given strings
# * program should use while loop

import random


def Random_Num(Top):
    return random.randint(0, int(Top))


def First_guess(guess, Num):
    if guess == Num:
        return True
    else:
        return False


def High_Low(guess, Num):
    if int(guess) - Num < 0:
        print("Too Low")
    else:
        print("Too high")


def Exit_Not_Press(Input):
    if "exit" not in str(Input).lower():
        return True
    else:
        return False


try:
    while True:
        print("\nYou can type 'Exit' at anytime when you want to quit playing ")
        x = 0
        Ran_Num = (input("How high do you want highest number    "))
        if Exit_Not_Press(Ran_Num):
            Ran_Num = Random_Num(Ran_Num)
            print("You are given three guesses\nBEGIN......\n")
            for x in range(4):
                User_Guess = input("What is your number guess   ")
                if Exit_Not_Press(User_Guess):
                    User_Guess = int(User_Guess)
                    if First_guess(User_Guess, Ran_Num):
                        print("CORRECT")
                        print("New number will be generated\n")
                        break
                    else:
                        High_Low(User_Guess, Ran_Num)
                        print(Ran_Num)
                        print("Wrong\nTry again....")
                        print(f"You have {3 - x} guesses left")
                if x == 2:
                    print("This is your last guess")
                elif not Exit_Not_Press(User_Guess):
                    raise SystemExit

        else:
            raise SystemExit

except SystemExit:
    print("Thank you for playing")
