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

def Nums():
    try:
        Num1 = int(input("Number 1 = "))
        Num2 = int(input("Number 2 = "))
        return Num1,Num2
    except ValueError:
        print("Closing.... \n Please try again and Enter valid numbers")

while True:
    Input_Choice = input("Please choose from the following....\nAdd, Subtract, Multiply, Divide, Percentage\n").capitalize()
    Num1, Num2 = Nums()
    if Input_Choice == "Add":
        print(Calculator.add(Num1, Num2))
    elif Input_Choice == "Subtract":
        print(Calculator.subtract(Num1, Num2))
    elif Input_Choice == "Multiply":
        print(Calculator.multiply(Num1, Num2))
    elif Input_Choice == "Divide":
        print(Calculator.divide(Num1, Num2))
    elif Input_Choice == "Percentage":
        print(Calculator.percentage(Num1, Num2))
    else:
        print("Please enter valid method")
