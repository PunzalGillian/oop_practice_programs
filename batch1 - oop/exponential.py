# Prog06: Create a program that ask user to input 2 numbers.
# Print the result when the 1st number is raised to the 2nd number

class ExponentialCalculator:
    def __init__(self):
        self.base = 0
        self.exponent = 0
        self.result = 0

    def get_input(self):
        self.base = float(input("Enter a number: "))
        self.exponent = float(input("Enter a number: "))

    def calculate(self):
        self.result = self.base ** self.exponent

    def display_result(self):
        print(self.result)


# Create object and run program
calculator = ExponentialCalculator()
calculator.get_input()
calculator.calculate()
calculator.display_result()
