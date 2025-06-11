# Prog01: Create a program that ask user to input 2 numbers.
# Print the smaller number.

class NumberComparer:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def get_input(self):
        self.num1 = float(input("Enter a number: "))
        self.num2 = float(input("Enter a number: "))

    def find_smaller_number(self):
        if self.num1 < self.num2:
            return self.num1
        else:
            return self.num2

    def display_result(self):
        print(self.find_smaller_number())


# Create object and run program
comparer = NumberComparer()
comparer.get_input()
comparer.display_result()
