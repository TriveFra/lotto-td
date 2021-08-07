import random

def generate_random_numbers(num):
	numbers = []
	while len(numbers) < num:
		new = random.randrange(1, 91)
		if new not in numbers:
			numbers.append(new)
	numbers.sort()
	return numbers
