from lotto import functions

class Extraction:
    """
    Simulates a Lotto extraction.
    """
    def __init__(self):
        results = {}
        results[0] = set()
        for r in range(1, 11):
            results[r] = functions.generate_random_numbers(5)
            results[r].sort()
        results[0] = results[0].union(set(results[r]))
        results[0] = list(results[0])
        results[0].sort()
        self.results = results

    def __str__(self):
        extraction_display = "Here are the results of the extraction:\n"
        for r in self.results:
            extraction_display += str(r) + ": " + str(self.results[r]) + "\n"
        return extraction_display
