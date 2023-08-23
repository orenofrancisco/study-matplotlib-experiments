import matplotlib.pyplot as plt

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
plt.plot(squares, linewidth=5) # plot() has optional arguments, read later

# One can add labels to axes like so
plt.title("Squares of numbers")
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of X", fontsize=14)

plt.show()
