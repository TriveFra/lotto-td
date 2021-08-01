import random

d_targets = {1: 'Estratto', 2: 'Ambo', 3: 'Terno', 4: 'Quaterna', 5: 'Cinquina'}
d_ruote = {0: 'Tutte', 1: 'Bari', 2: 'Cagliari', 3: 'Firenze', 4: 'Genova', 5: 'Milano', 6: 'Napoli', 7: 'Palermo', 8: 'Roma', 9: 'Torino', 10: 'Venezia'}

class Ticket:
    """
    Represents a valid ticket for Italian Lotto.
    """
    def __init__(self, target, n_numbers, ruota):
        self.target = target
        self.numbers = []   # generates the actual numbers
        while len(self.numbers) < n_numbers:
            new = random.randrange(1, 91)
            if new not in self.numbers:
                self.numbers.append(new)
        self.numbers.sort()
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

    def win(self, extracted):
        count = 0
        for n in extracted:
            if n in self.numbers:
                count += 1
                if d_targets[count] == self.target:
                    return True
        return False

class Extraction:
    """
    Simulates a Lotto extraction.
    """
    def __init__(self):
        d_ext = {}
        d_ext['Tutte'] = set()
        for r in d_ruote.values():
            if r != 'Tutte':
                d_ext[r] = []
                while len(d_ext[r]) < 5:
                    new = random.randrange(1, 91)
                    if new not in d_ext[r]:
                        d_ext[r].append(new)
                d_ext[r].sort()
                d_ext['Tutte'] = d_ext['Tutte'].union(set(d_ext[r]))
        d_ext['Tutte'] = list(d_ext['Tutte'])
        self.results = d_ext

    def __str__(self):
        extraction = "Here are the results of the extraction:\n"
        for r in self.results:
            extraction += str(r) + ": " + str(self.results[r]) + "\n"
        return extraction
