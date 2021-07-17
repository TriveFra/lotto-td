import random

def gen_ran_num(n_numbers):
	numbers = []
	while len(numbers) < n_numbers:
		new = random.randrange(1, 91)
		if new not in numbers:
			numbers.append(new)
	numbers.sort()
	return numbers
