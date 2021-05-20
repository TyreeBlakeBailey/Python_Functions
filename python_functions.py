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