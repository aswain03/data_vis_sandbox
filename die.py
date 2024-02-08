from random import randint


class Die:
    """represents a single dice"""

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """returns a random value between 1 and number of sides"""
        return randint(1, self.num_sides)
