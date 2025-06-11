# Prog02: Create a program that ask user to input 2 numbers.
# Print "Not Equal" when the numbers are not the same.

class NumberComparer:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def get_input(self):
        self.num1 = float(input("Enter a number: "))
        self.num2 = float(input("Enter a number: "))

    def check_if_not_equal(self):
        if self.num1 != self.num2:
            print("Not Equal")


# Create object and run program
comparer = NumberComparer()
comparer.get_input()
comparer.check_if_not_equal()
