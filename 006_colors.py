import matplotlib.pyplot as plt

domain = range(0, 1000)
codomain = [x**2 for x in domain]
plt.scatter(domain, codomain, edgecolor='red', s=1)

'''
It is also possible to use colors as a tuple with ranges 0.0 to 1.0
plt.scatter(domain, codomain, edgecolor=(1.0, 0.0, 0.0), s=1)
The above function would produce the same result as the one in use now
'''

# Label your axes!
plt.title("Square numbers", fontsize=14)
plt.xlabel("Domain", fontsize=14)
plt.ylabel("Codomain", fontsize=14)

# Since our scale is massive, we can specify what range to display
# so we don't get (0.0 to 1.0 * 1e6) as a range
plt.axis([0, 1100, 0, 1100000])

# I don't really know what this does
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
