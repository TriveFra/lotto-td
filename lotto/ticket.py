from lotto import bet_type, ruota

class Ticket:
    """
    Represents a valid ticket for Italian Lotto.
    """
    def __init__(self, bet_type_code, ruota_code, numbers):
        self.bet_type = bet_type.BetType(bet_type_code)
        self.ruota = ruota.Ruota(ruota_code)
        self.numbers = numbers

    def __str__(self):
        ticket = ""
        num_line = ""
        for n in self.numbers:
            num_line += " " + str(n)
        ticket += "+------------+-------------------------------+\n"
        ticket += "|    Numbers |{:>31}|\n".format(num_line)
        ticket += "|   Bet Type |{:>31}|\n".format(self.bet_type.type)
        ticket += "|      Ruota |{:>31}|\n".format(self.ruota.city)
        ticket += "+------------+-------------------------------+"
        return ticket
