import matplotlib.pyplot as plt

domain = range(0, 1000)
results = [x**2 for x in domain]

# A gradient is possible using cmap + c optional arguments
plt.scatter(domain, results, c=results, cmap=plt.cm.Blues, s=10, edgecolor='none')

# Label your axes!
plt.title("Square numbers", fontsize=14)
plt.xlabel("X", fontsize=14)
plt.ylabel("X^2", fontsize=14)

# Since our scale is massive, we can specify what range to display
# so we don't get (0.0 to 1.0 * 1e6) as a range
plt.axis([0, 1100, 0, 1100000])

# I don't really know what this does
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
