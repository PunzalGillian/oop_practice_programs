# Prog10: Create a program that ask user to input 2 numbers.
# Print all the numbers between the two numbers.

class NumberRangePrinter:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def get_input(self):
        self.num1 = int(input("Enter a number: "))
        self.num2 = int(input("Enter a number: "))

    def print_numbers_between(self):
        # Make sure we handle the case where num1 > num2
        start, end = min(self.num1, self.num2), max(self.num1, self.num2)
        for number in range(start + 1, end):
            print(number)


# Create object and run program
printer = NumberRangePrinter()
printer.get_input()
printer.print_numbers_between()
