# Prog09: Create a program that print all the numbers starting
# from 0 to 100 except numbers ending in zero or ending five.

class NumberFilter:
    def __init__(self):
        self.filtered_numbers = []

    def filter_numbers(self, start=0, end=100):
        for count in range(start, end + 1):
            if count % 10 != 0 and count % 10 != 5:
                self.filtered_numbers.append(count)
        return self.filtered_numbers

    def display_numbers(self):
        print(self.filtered_numbers)


# Create object and run program
filter = NumberFilter()
filter.filter_numbers()
filter.display_numbers()
