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


x = 0
while x <= 100:
    if x == random.randint(1, 100): #random number will have a little suprise (Easter Egg)
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
