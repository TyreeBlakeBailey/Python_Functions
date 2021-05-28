# Functions
## DRY
#### Don't repeat your self

## Example of functioned being used
```python
# Let's create a basic functions to greet
# syntax def name()


# first iteration
import math

def greeting():
    return "Welcome to Cyber Security! "  # last line in function should be a return statment


print(greeting())  # function has to be called in order to run


##Second iteration

def greeting_user(name):
    return f"Welcome to the team {name}"


print(greeting_user(input("What is your name? ").capitalize()))

#create a function that takes two args as ints


def add(Num1, Num2):
    return Num1 + Num2

def multiple(Num1, Num2):
    return Num1 * Num2

def divide(Num1, Num2):
    return Num1/Num2

def percentage(Num1, Num2):
    Answer = (Num1/100) * Num2
    return f"{Num1}% of {Num2} is {Answer}"

print(add(4,6))
print(multiple(3,8))
print(divide(10,2))
print(percentage(5, 20))

print(20%5)
print(math.remainder(20,5))
```

## Magic number task
- game that generates random number and allows the user to have 3 guess to guess the right number
```python
# Done-> User story 1 - As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.

# Done-> 2 - As a user, I should get feedback if my number is too high or too low so I can adjust my guess.

# Done-> 3 - as a user I should only be able to guess 3 times before a new number is generated

# Done-> 4 - as a user, I should be able to keep playing until I respond with exit

# Done-> 5 - as a user, I should be able to use exit in a sentence and still terminate the program

# Done -> extra 6 - as a user, when I terminate the program I should get a message thanking me for playing and the number of times I guesses and number of times I found the number.

# Done -> Extra 7 - as a user, I should be asked the highest number that can be used to generate a random number

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
    y = 0
    while True:
        print("\nYou can type 'Exit' at anytime when you want to quit playing ")
        x = 0
        Ran_Num = (input("How high do you want highest number    "))
        if Exit_Not_Press(Ran_Num):
            if not Ran_Num.isdigit():
                print("Please enter valid number")
                continue
            Ran_Num = Random_Num(Ran_Num)
            print("You are given three guesses\nBEGIN......\n")
            for x in range(4):
                User_Guess = input("What is your number guess   ")
                if not User_Guess.isdigit():
                    if not Exit_Not_Press(User_Guess):
                        print(f"\nYou guessed right {y} time(s) well done")
                        raise SystemExit
                    else:
                        print("Please enter valid number")
                        continue
                if Exit_Not_Press(User_Guess):
                    User_Guess = int(User_Guess)
                    if First_guess(User_Guess, Ran_Num):
                        print("CORRECT")
                        print(f"It took you {x} guesses to get it right")
                        print("New number will be generated\n")
                        y += 1
                        break
                    else:
                        High_Low(User_Guess, Ran_Num)
                        print(Ran_Num)
                        print("Wrong\nTry again....")
                        print(f"You have {3 - x} guesses left\n")
                if x == 2:
                    print("This is your last guess")

        else:
            print(f"\nYou guessed right {y} time(s) well done")
            raise SystemExit

# except ValueError:
#     print("Please Enter valid number ")
except SystemExit:
    print("Thank you for playing")

```

## Control flow task
- checks the user of functions and while loops
```python
# - You can vote and drivre
# - You can vote
# - You can driver
# - you can't legally drink but your mates/uncles might have your back (bigger 16)
# - Your too young, go back to school!


#  as a user I should be able to keep being prompted for input until I say 'exit'

# Starter code


def Over_18(age):  # Function to check if the given value is over 18
    if age >= 18:  # will return True if the age is over 18
        return True
    else:  # if not will return False
        return False


def Over_16(age):  # Function to check if the given value is over 16
    if age > 16:
        return True
    else:
        return False


def Driver(Lisence):  # Takes the users Input of Y/N and turns it into True of False
    if Lisence == "Y":
        return True
    elif Lisence == "N":
        return False
    else:  # if they enter an incorrect answer will raise a error to be caught in the try segment
        raise ValueError


while True:  # Continous loop until break is given
    try:
        print("\nType exit to leave programme.....")
        age = input("\nHow old are you?  ")  # Takes the first users input of their age
        if age.lower() == "exit":  # if exit is type close the programme with break
            break
        else: #as long as exit is type it will run the next lines
            age = int(age) # will try to convert into an int if not will raise an error
            if Over_16(age) != True:
                driver_lisence = False
            else:
                driver_lisence = Driver(input("Do you have you driving license?  Y/N   ").upper())
    except ValueError:
        print("Try again Enter a valid input")
        continue

    if Over_18(age) and driver_lisence:
        print("\nYou can vote and drive ")
    elif Over_18(age) and not driver_lisence:
        print("\nYou can vote")
    if age >= 16 and not Over_18(age):
        print("\nYou can't legally drink but your mates/uncles might have your back")
    elif not Over_16(age):
        print("\nYour too young go back to school")
    if driver_lisence and not Over_18(age):
        print("\nYou can drive")

```