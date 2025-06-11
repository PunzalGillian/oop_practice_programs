# Prog05: Create a program that ask user to input 2 numbers.
# Print the remainder when the first number is divided by the second number.

class RemainderCalculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.remainder = 0

    def get_input(self):
        self.num1 = float(input("Enter a number: "))
        self.num2 = float(input("Enter a number: "))

    def calculate_remainder(self):
        self.remainder = self.num1 % self.num2

    def display_result(self):
        print(f"Remainder of two numbers is: {self.remainder:.0f}")


# Create object and run program
calculator = RemainderCalculator()
calculator.get_input()
calculator.calculate_remainder()
calculator.display_result()
