# Create a scatter plot with different marker sizes based on population.
import matplotlib.pyplot as plt

cities = ["City A", "City B", "City C", "City D", "City E"]
population = [1000000, 500000, 2000000, 1500000, 800000]

marker_sizes = [pop/10000 for pop in population]
plt.scatter(cities, population, s=marker_sizes)

plt.xlabel("Cities")
plt.ylabel("Population")
plt.title("Population of Cities with Marker Sizes")

plt.show()