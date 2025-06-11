# Prog04: Create a program that ask user to input 2 numbers.
# Print the quotient of the two numbers without the decimal point.

class QuotientCalculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.quotient = 0

    def get_input(self):
        self.num1 = float(input("Enter a number: "))
        self.num2 = float(input("Enter a number: "))

    def calculate_quotient(self):
        self.quotient = self.num1 // self.num2

    def display_result(self):
        print(f"Quotient of two numbers is: {self.quotient:.0f}")


# Create object and run program
calculator = QuotientCalculator()
calculator.get_input()
calculator.calculate_quotient()
calculator.display_result()
