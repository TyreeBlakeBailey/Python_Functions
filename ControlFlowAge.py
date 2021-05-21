
# - You can vote and drivre
# - You can vote
# - You can driver
# - you can't legally drink but your mates/uncles might have your back (bigger 16)
# - Your too young, go back to school!


 #  as a user I should be able to keep being prompted for input until I say 'exit'

#Starter code

age = 17
driver_lisence = True


if age >= 18 and driver_lisence:
    print("You can vote and drive ")
elif age >= 18 and driver_lisence == False:
    print("You can vote")
if age > 16 and age < 18:
    print("You can't legally drink but your mates/uncles might have your back")
elif age < 16:
    driver_lisence = False
    print("Your too young go back to school")
elif driver_lisence and age < 18:
    print("You can drive")

