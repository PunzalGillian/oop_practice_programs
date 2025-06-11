# Prog04: Create a program that ask user to input 2 numbers.
# Print the product of the two numbers.

class ProductCalculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.product = 0

    def get_input(self):
        self.num1 = float(input("Enter a number: "))
        self.num2 = float(input("Enter a number: "))

    def calculate_product(self):
        self.product = self.num1 * self.num2

    def display_result(self):
        print(self.product)


# Create object and run program
calculator = ProductCalculator()
calculator.get_input()
calculator.calculate_product()
calculator.display_result()
