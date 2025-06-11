# Prog08: Create a program that print all the odd numbers
# starting from 0 to 100. (Use while loop)

class OddNumberGenerator:
    def __init__(self):
        self.odd_nums = []

    def generate_odd_numbers(self, start=0, end=100):
        count = start
        while count <= end:
            if count % 2 != 0:
                self.odd_nums.append(count)
            count += 1
        return self.odd_nums

    def display_numbers(self):
        print(self.odd_nums)


# Create object and run program
generator = OddNumberGenerator()
generator.generate_odd_numbers()
generator.display_numbers()
