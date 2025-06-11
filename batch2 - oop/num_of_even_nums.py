# Prog07: Create a program that ask user to input 10 numbers.
# Print how many are even numbers.

class EvenNumberCounter:
    def __init__(self):
        self.even_count = 0

    def get_numbers(self, count=10):
        for i in range(count):
            num = float(input("Enter a number: "))
            if num % 2 == 0:
                self.even_count += 1

    def display_result(self):
        print("The number of even numbers is:", self.even_count)


# Create object and run program
counter = EvenNumberCounter()
counter.get_numbers()
counter.display_result()
