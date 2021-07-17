d_targets = {1: 'Estratto', 2: 'Ambo', 3: 'Terno', 4: 'Quaterna', 5: 'Cinquina'}
d_ruote = {0: 'Tutte', 1: 'Bari', 2: 'Cagliari', 3: 'Firenze', 4: 'Genova', 5: 'Milano', 6: 'Napoli', 7: 'Palermo', 8: 'Roma', 9: 'Torino', 10: 'Venezia'}

class Ticket:
    """
    Represents a valid ticket for Italian Lotto.
    """
    def __init__(self, target, numbers, ruota):
        self.target = target
        self.numbers = numbers
        self.ruota = ruota

    def __str__(self):
        ticket = ""
        num_line = ""
        for n in self.numbers:
            num_line += " " + str(n)
        ticket += "+------------+-------------------------------+\n"
        ticket += "|    Numbers |{:>31}|\n".format(num_line)
        ticket += "|   Bet Type |{:>31}|\n".format(self.target)
        ticket += "|      Ruota |{:>31}|\n".format(self.ruota)
        ticket += "+------------+-------------------------------+"
        return ticket
