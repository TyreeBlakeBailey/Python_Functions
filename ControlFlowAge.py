# - You can vote and drivre
# - You can vote
# - You can driver
# - you can't legally drink but your mates/uncles might have your back (bigger 16)
# - Your too young, go back to school!


#  as a user I should be able to keep being prompted for input until I say 'exit'

# Starter code


def Over_18(age):
    if age >= 18:
        return True
    else:
        return False


def Over_16(age):
    if age > 16:
        return True
    else:
        return False


def Driver(Lisence):
    if Lisence == "Y":
        return True
    else:
        return False


while True:
    try:
        print("\nType exit to leave programme.....")
        age = input("\nHow old are you?  ")
        if age.lower() == "exit":
            break
        else:
            age = int(age)
            if Over_16(age) != True:
                driver_lisence = False
            else:
                driver_lisence = input("Do you have you driving license?  Y/N   ").upper()
    except ValueError:
        print("Try again Enter a valid age")
        continue

    if Over_18(age) and Driver(driver_lisence):
        print("\nYou can vote and drive ")
    elif Over_18(age) and not Driver(driver_lisence):
        print("\nYou can vote")
    if age >= 16 and not Over_18(age):
        print("\nYou can't legally drink but your mates/uncles might have your back")
    elif not Over_16(age):
        print("\nYour too young go back to school")
    if Driver(driver_lisence) and not Over_18(age):
        print("\nYou can drive")
