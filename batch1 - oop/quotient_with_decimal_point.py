# Prog05: Create a program that ask user to input 2 numbers.
# Print the quotient of the two numbers with the decimal point

class QuotientCalculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def get_input(self):
        self.num1 = float(input("Enter a number: "))
        self.num2 = float(input("Enter a number: "))

    def calculate_and_display(self):
        print(self.num1 / self.num2)


# Create object and run program
calculator = QuotientCalculator()
calculator.get_input()
calculator.calculate_and_display()
