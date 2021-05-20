class Calculator:

    @staticmethod
    def add(Num1, Num2):
        return Num1 + Num2

    def subtract(Num1, Num2):
        return Num2 - Num1

    def multiply(Num1, Num2):
        return Num1 * Num2

    def divide(Num1, Num2):
        return Num1/Num2

    def percentage(Num1, Num2):
        Answer = (Num1/100) * Num2
        return f"{Num1}% of {Num2} is {Answer}"

    def divisible(Num1, Num2):
        if Num1 % Num2 == 0:
            return True
        else:
            return False

def Nums():
    try:
        Num1 = int(input("Number 1 = "))
        Num2 = int(input("Number 2 = "))
        return Num1,Num2
    except ValueError:
        print("Closing.... \n Please try again and Enter valid numbers")

#Divisible by the method that returns true or false depending on the outcome
#Work out and return the area of a triangle

while True:
    Input_Choice = input("\nPlease choose from the following....\nAdd, Subtract, Multiply, Divide, Percentage, Divisible\n").capitalize()
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
    elif Input_Choice == "Divisible":
        print("Enter bigger number first")
        Num1, Num2 = Nums()
        if Calculator.divisible(Num1, Num2):
            print(f"{Num1} is divisible by {Num2}")
        else:
            print(f"{Num1} is not divisible by {Num2}")
    else:
        print("Please enter valid method")
