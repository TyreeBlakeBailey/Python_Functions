# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number
# For the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”."'''

import random  # imports teh random libary done for a bit of extra fun


class FizzBuzz:  # declared the calss with the name FizzBuzz
    @staticmethod
    def Fizz_Check(Num):  # function that checks if the current number is a multiple of 3
        if Num % 3 == 0:  # if it is it will return True
            return True
        else:  # else it will return false
            return False

    def Buzz_Check(Num):  # function that checks if the current number is a multiple of 5
        if Num % 5 == 0:  # if it is it will return True
            return True
        else:  # else it will return false
            return False

    def FizzBuzz(Amount):  # main function that prints the numbers and text, takes a user input to tell it what number to
        # run to
        y = random.randint(1,Amount)
        # used for the extra sections on line 28 will generate a random number between 1
        # and user input
        x = 1
        while x <= Amount:  # runs a loops up until the inputted number while also incrementing x
            if x == y:  # random number will have a little surprise (Easter Egg)
                print(
                    "༼つ ◕_◕ ༽つ")  # What ever the random number is will be replaced with this face instead of the number
            elif FizzBuzz.Fizz_Check(x) and FizzBuzz.Buzz_Check(x):
                # checks if the current value of x is multiple of 3 and 5
                print("FizzBuzz")  # if the number is both a multiple of 3 and 5 it will print this line
            elif FizzBuzz.Fizz_Check(x):  # checks if the current value of x is multiple of 3
                print("Fizz")
            elif FizzBuzz.Buzz_Check(x):  # checks if the current value of x is multiple of 5
                print("Buzz")
            else:
                print(x)  # if the value of x doesnt match any of the condition it will prints the number
            x += 1  # incrementation of x at the end of the loop


Amount = input("How much would you like to go to? ")  # allows the user to input

if Amount.isdigit() and Amount != "0":  # checks that the user has entered a nnumber and nothing else
    FizzBuzz.FizzBuzz(int(Amount))  # if it is a number then run the main function in the FizzBuzz class
else:
    print("Please only enter numbers")  # if the user enters anything that isnt a number that it will close and print
    # this line
