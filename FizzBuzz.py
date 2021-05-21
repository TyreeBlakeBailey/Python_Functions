# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number
# For the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”."'''


import random


class FizzBuzz:
    @staticmethod
    def Fizz_Check(Num):
        if Num % 3 == 0:
            return True
        else:
            return False

    def Buzz_Check(Num):
        if Num % 5 == 0:
            return True
        else:
            return False

    def FizzBuzz(Amount):
        y = random.randint(1, Amount)
        x = 0
        while x <= Amount:
            if x == y:  # random number will have a little suprise (Easter Egg)
                print("༼つ ◕_◕ ༽つ")
            elif FizzBuzz.Fizz_Check(x) and FizzBuzz.Buzz_Check(x):
                print("FizzBuzz")
            elif FizzBuzz.Fizz_Check(x):
                print("Fizz")
            elif FizzBuzz.Buzz_Check(x):
                print("Buzz")
            else:
                print(x)
            x += 1


Amount = input("How much would you like to go to? ")

if Amount.isdigit():
    FizzBuzz.FizzBuzz(int(Amount))
else:
    print("Please only enter numbers")
