#  Draw a line graph to show temperature changes over 7 days. 

import matplotlib.pyplot as plt

days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7']
temperatures = [25, 28, 30, 27, 29, 31, 26]

plt.plot(days, temperatures)
plt.title("Temperature Changes Over 7 Days")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.show()