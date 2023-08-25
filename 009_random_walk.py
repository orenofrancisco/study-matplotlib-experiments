import matplotlib.pyplot as plt

from random import choice

class RandomWalk():
    # This class generates random walk data

    def __init__(self, num_points=5000):
        # With a default 5000 data points to be generated this object
        # will be populated later with the fill_walk function
        self.num_points = num_points

        # The function starts at 0
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        # For each of the numbers in num_points, we'll create a datapoint
        # That's random (with some constraints)
        while len(self.x_values) < self.num_points:
            # Define choices for x
            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            # Define choices for y
            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that are 0 * 0
            if x_step == y_step == 0:
                continue

            # If the move is valid then let's add it to the values arrays
            x_next = self.x_values[-1] + x_step
            y_next = self.y_values[-1] + y_step

            self.x_values.append(x_next)
            self.y_values.append(y_next)

if __name__ == '__main__':
    # Only run this code if this is executed explicitly
    # I did this so I could reuse the class RandomWalk later on
    # Edit: It ended up being useless because the filename starts with a number
    
    # Create and fill the walk set
    rw = RandomWalk()
    rw.fill_walk()

    # Plot it
    plt.scatter(rw.x_values, rw.y_values, s=10)
    plt.show()
