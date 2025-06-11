# Prog06: Create a program that ask user to input 10 numbers.
# Print the result of the 1st number minus all of the remaining nums.

class NumberProcessor:
    def __init__(self):
        self.numbers = []
        self.result = 0

    def get_numbers(self, count=10):
        for i in range(count):
            num = float(input("Enter a number: "))
            self.numbers.append(num)

    def calculate_difference(self):
        self.result = self.numbers[0] - sum(self.numbers[1:])

    def display_result(self):
        print("Num1 minus all of the remaining nums is:", self.result)


# Create object and run program
processor = NumberProcessor()
processor.get_numbers()
processor.calculate_difference()
processor.display_result()
