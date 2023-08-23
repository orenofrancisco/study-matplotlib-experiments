import matplotlib.pyplot as plt

domain = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
codomain = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
plt.plot(domain, codomain, linewidth=5)

# Label your axes!
plt.title("Squares of numbers")
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of X", fontsize=14)

plt.show()
