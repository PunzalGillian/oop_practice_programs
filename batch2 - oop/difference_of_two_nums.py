# Prog03: Create a program that ask user to input 2 numbers.
# Print the difference of the two numbers.

class DifferenceCalculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.difference = 0

    def get_input(self):
        self.num1 = float(input("Enter a number: "))
        self.num2 = float(input("Enter a number: "))

    def calculate_difference(self):
        self.difference = self.num1 - self.num2

    def display_result(self):
        print(
            f"Difference of {self.num1} and {self.num2} is {self.difference}")


# Create object and run program
calculator = DifferenceCalculator()
calculator.get_input()
calculator.calculate_difference()
calculator.display_result()
