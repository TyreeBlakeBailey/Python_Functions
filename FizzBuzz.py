#Write a program that prints the numbers from 1 to 100.
#But for multiples of three print “Fizz” instead of the number
#For the multiples of five print “Buzz”.
#For numbers which are multiples of both three and five print “FizzBuzz”."'''

x = 0
while x <= 100:
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
    x += 1

