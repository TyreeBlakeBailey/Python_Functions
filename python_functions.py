# Let's create a basic functions to greet
# syntax def name()


#first iteration

def greeting():
    return "Welcome to Cyber Security! " # last line in function should be a return statment

print(greeting())#function has to be called in order to run


##Second iteration

def greeting_user(name):
    return f"Welcome to the team {name}"

print(greeting_user(input("What is your name? ").capitalize()))