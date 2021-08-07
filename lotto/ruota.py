class Ruota:
    """
    Represents the Ruota referred to by Tickets and Extractions.
    """
    cities_dict = {0: 'Tutte', 1: 'Bari', 2: 'Cagliari', 3: 'Firenze', 4: 'Genova', 5: 'Milano', 6: 'Napoli', 7: 'Palermo', 8: 'Roma', 9: 'Torino', 10: 'Venezia'}
    def __init__(self, code):
        self.code = code
        self.city = self.cities_dict[code]

    def __str__(self):
        return self.city
