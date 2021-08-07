class BetType:
    """
    Represents the number of matches a single Ticket is targeting.
    """
    bet_types_dict = {1: 'Estratto', 2: 'Ambo', 3: 'Terno', 4: 'Quaterna', 5: 'Cinquina'}
    def __init__(self, code):
        self.code = code
        self.type = self.bet_types_dict[code]

    def __str__(self):
        return self.type
