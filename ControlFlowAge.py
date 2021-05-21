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
