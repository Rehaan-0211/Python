# Plot two line graphs on the same axes showing sales of two products.

import matplotlib.pyplot as plt 

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']

product1 = [100, 150, 200, 250, 300]
product2 = [80, 120, 160, 200, 240]

plt.plot(months, product1, label='Product A')
plt.plot(months, product2, label='Product B')
plt.title("Sales of Product A and Product B")

plt.xlabel("Months")
plt.ylabel("Sales")

plt.legend()
plt.show()