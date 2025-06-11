# Prog09: Create a program that print all the
# even numbers starting from 0 to 100 (Use for loop).

class EvenNumberGenerator:
    def __init__(self):
        self.even_nums = []

    def generate_even_numbers(self, start=0, end=100):
        for count in range(start, end + 1):
            if count % 2 == 0:
                self.even_nums.append(count)
        return self.even_nums

    def display_numbers(self):
        print(self.even_nums)


# Create object and run program
generator = EvenNumberGenerator()
generator.generate_even_numbers()
generator.display_numbers()
