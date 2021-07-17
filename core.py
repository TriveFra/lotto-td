"""
Generates 1-5 Italian Lotto tickets and prints them.
"""

from objects import *
from functions import *

def main():
	print('This program randomly generates 1-5 Italian Lotto tickets of the chosen type and prints them.')
	valid = False
	while not valid:
		try:
			n_tickets = int(input('How many tickets would you like to generate? (0 to quit) '))
		except:
			n_tickets = 6
		if n_tickets in (0, 1, 2, 3, 4, 5):
			valid = True
		else:
			print('Invalid data. Please try again.')

	if n_tickets == 0:
		print('A nice day to you, sir.')
	else:
		ticket_data = []
		# ask the user for data about the tickets
		for i in range(0, n_tickets):
			print ('As for ticket number ' + str(i + 1) + '...')

			valid = False
			while not valid:
				try:
					i_target = int(input('  ...what kind of bet would you like to place? (1: Estratto, 2: Ambo, 3: Terno, 4: Quaterna, 5: Cinquina) '))
				except:
					i_target = 6
				if i_target in d_targets:
					valid = True
					target = d_targets[i_target]
					print(target)
				else:
					print('Invalid data. Please try again.')

			valid = False
			while not valid:
				try:
					n_numbers = int(input('  ...how many numbers would you like to generate? (1 to 10) '))
				except:
					n_numbers = 0
				if n_numbers in range(1, 11):
					valid = True
					numbers = gen_ran_num(n_numbers)
				else:
					print('Invalid data. Please try again.')

			valid = False
			while not valid:
				try:
					i_ruota = int(input('  ...which "ruota" would you like your ticket to refer to? (1: Bari, 2: Cagliari, 3: Firenze, 4: Genova, 5: Milano, 6: Napoli, 7: Palermo, 8: Roma, 9: Torino, 10: Venezia, 0: Tutte) '))
				except:
					i_ruota = 11
				if i_ruota in d_ruote:
					valid = True
					ruota = d_ruote[i_ruota]
					print(ruota)
				else:
					print('Invalid data. Please try again.')
			# collect user preferences for each ticket in a list
			ticket_data.append([target, numbers, ruota])
		# generate and print the tickets
		tickets = []
		for t in ticket_data:
			ticket = Ticket(t[0], t[1], t[2])
			print(ticket)
			tickets.append(ticket)

if __name__ == "__main__":
	main()
