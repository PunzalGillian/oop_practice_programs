# Prog08: Create a program that ask user to input 10 numbers.
# Print how many are odd numbers.

class OddNumberCounter:
    def __init__(self):
        self.odd_nums = []

    def get_numbers(self, count=10):
        for i in range(count):
            num = int(input("Enter a number: "))
            if num % 2 != 0:
                self.odd_nums.append(num)

    def count_odd_numbers(self):
        return len(self.odd_nums)

    def display_result(self):
        print(f"Number of odd numbers: {self.count_odd_numbers()}")


# Create object and run program
counter = OddNumberCounter()
counter.get_numbers()
counter.display_result()
