import pygal
from random import randint

class Die():
    # Simple die class with optional argument for number of sides
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)

if __name__ == '__main__':
    # Prevent accidental execution of this code if this module is imported
    # It will not be, the filename I chose saw to that

    # Instance a die
    die = Die()

    # Make some rolls and store them in a list
    results = []
    for _ in range(10000):
        temp = die.roll()
        results.append(temp)

    # Now let's study these results
    frequency = []
    for instance in range(1, die.sides + 1):
        hits = results.count(instance)
        frequency.append(hits)

    # See how many times the die landed on each face
    hist = pygal.Bar()

    hist.title = "Results of rolling a D6 1000 times"
    hist.x_labels = ['1', '2', '3', '4', '5', '6']
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"

    # If you had tests from other dice, you could add them like so
    hist.add('D6', frequency)
    hist.render_to_file('images/011_pygal.svg')
