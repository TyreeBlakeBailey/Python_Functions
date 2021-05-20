class Calculator:

    @staticmethod
    def add(Num1, Num2):
        return Num1 + Num2

    def subtract(Num1, Num2):
        return Num1 - Num2

    def multiply(Num1, Num2):
        return Num1 * Num2

    def divide(Num1, Num2):
        if Num2 == 0:
            print(" ¯\_( ͡° ͜ʖ ͡°)_/¯ \nYou cannot divide by zero ")
            raise Exception
        else:
            return Num1 / Num2

    def percentage(Num1, Num2):
        Answer = (Num1 / 100) * Num2
        return f"{Num1}% of {Num2} is {Answer}"

    def divisible(Num1, Num2):
        if Num2 == 0:
            print("(‡ಠ╭╮ಠ) \nYou cannot divide by zero ")
            raise Exception
        else:
            if Num1 % Num2 == 0:
                return True
            else:
                return False

    def triangle(Num1, Num2):
        return f"The area of the triangle is {(Calculator.multiply(Num1, Num2)) / 2}"

    def inch_cm(Num1):
        return Calculator.multiply(Num1, 2.54)


def Nums():
    Num1 = input("Number 1 = ")
    Num2 = input("Number 2 = ")
    if Num1.isdigit() and Num2.isdigit():
        Num1 = int(Num1)
        Num2 = int(Num2)
        return Num1, Num2
    else:
        print("Try again....\nEnter two valid Numbers")
        raise Exception

# Divisible by the method that returns true or false depending on the outcome
# Work out and return the area of a triangle
#print(Nums())
while True:
    try:
        Input_Choice = input(
            "\nPlease choose from the following....\nAdd, Subtract, Multiply, Divide, Percentage, Divisible, Triangle, Inchtocm, Exit\n").capitalize()
        if Input_Choice == "Add":
            Num1, Num2 = Nums()
            print(Calculator.add(Num1, Num2))
        elif Input_Choice == "Subtract":
            Num1, Num2 = Nums()
            print(Calculator.subtract(Num1, Num2))
        elif Input_Choice == "Multiply":
            Num1, Num2 = Nums()
            print(Calculator.multiply(Num1, Num2))
        elif Input_Choice == "Divide":
            Num1, Num2 = Nums()
            print(Calculator.divide(Num1, Num2))
        elif Input_Choice == "Percentage":
            Num1, Num2 = Nums()
            print(Calculator.percentage(Num1, Num2))
        elif Input_Choice == "Triangle":
            print("Enter base and height of the triangle")
            Num1, Num2 = Nums()
            print(Calculator.triangle(Num1, Num2))
        elif Input_Choice == "Divisible":
            print("Enter bigger number first")
            Num1, Num2 = Nums()
            if Calculator.divisible(Num1, Num2):
                print(f"{Num1} is divisible by {Num2}")
            else:
                print(f"{Num1} is not divisible by {Num2}")
        elif Input_Choice == "Inchtocm":
            Inches = input('Enter inches to convert to cm ')
            if Inches.isdigit():
                print(f"{Calculator.inch_cm(int(Inches))}cm")
            else:
                print("Invalid entry, try again")
                continue
        elif Input_Choice == "Exit":
            break
        else:
            print("Please enter valid method")

    except Exception:
        continue