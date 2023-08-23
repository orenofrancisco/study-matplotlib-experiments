import matplotlib.pyplot as plt

domain = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
codomain = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
plt.scatter(domain, codomain, s=100)

# Label your axes!
plt.title("Square numbers", fontsize=14)
plt.xlabel("Domain", fontsize=14)
plt.ylabel("Codomain", fontsize=14)

# I don't really know what this does
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
