# Prog07: Create a program that ask user to input 10 numbers.
# Print the sum of all the numbers.

class NumberSummer:
    def __init__(self):
        self.numbers = []
        self.sum = 0

    def get_numbers(self, count=10):
        for i in range(count):
            num = float(input("Enter a number: "))
            self.numbers.append(num)
            self.sum += num

    def display_sum(self):
        print(self.sum)


# Create object and run program
summer = NumberSummer()
summer.get_numbers()
summer.display_sum()
