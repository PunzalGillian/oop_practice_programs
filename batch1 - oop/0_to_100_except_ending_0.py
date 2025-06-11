# Prog10: Create a program that print all the numbers
# starting from 0 to 100 except numbers ending in zero.

class NumberFilter:
    def __init__(self):
        self.numbers = []

    def get_numbers_without_zero_ending(self):
        for num in range(101):
            if num % 10 != 0:
                self.numbers.append(num)
        return self.numbers

    def display_numbers(self):
        print(self.numbers)


# Create object and run program
filter = NumberFilter()
filter.get_numbers_without_zero_ending()
filter.display_numbers()
