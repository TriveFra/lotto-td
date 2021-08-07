from lotto import functions, ticket

class Lotto:
    """
    Main business logic class.
    It receives user inputs and instantiates other classes as needed.
    """
    def __init__(self):
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
                        bet_type_code = int(input('  ...what kind of bet would you like to place? (1: Estratto, 2: Ambo, 3: Terno, 4: Quaterna, 5: Cinquina) '))
                    except:
                        bet_type_code = 6
                    if bet_type_code in range(1, 6):
                        valid = True
                    else:
                        print('Invalid data. Please try again.')

                valid = False
                while not valid:
                    try:
                        ruota_code = int(input('  ...which "ruota" would you like your ticket to refer to? (1: Bari, 2: Cagliari, 3: Firenze, 4: Genova, 5: Milano, 6: Napoli, 7: Palermo, 8: Roma, 9: Torino, 10: Venezia, 0: Tutte) '))
                    except:
                        ruota_code = 11
                    if ruota_code in range(0, 10):
                        valid = True
                    else:
                        print('Invalid data. Please try again.')

                valid = False
                while not valid:
                    try:
                        num = int(input('  ...how many numbers would you like to generate? (1 to 10) '))
                    except:
                        num = 0
                    if num in range(bet_type_code, 11):
                        valid = True
                        numbers = functions.generate_random_numbers(num)
                    elif num in range(1, bet_type_code):
                        print('You must enter at least ' + str(bet_type_code) + ' numbers due to the kind of bet you chose. Please try again.')
                    else:
                        print('Invalid data. Please try again.')

                # collect user preferences for each ticket in a list
                ticket_data.append([bet_type_code, ruota_code, numbers])
            # generate and print the tickets
            tickets = []
            for t in ticket_data:
                new_ticket = ticket.Ticket(t[0], t[1], t[2])
                print(new_ticket)
                tickets.append(new_ticket)
