#  Plot cumulative rainfall over 10 days using a line graph.

import matplotlib.pyplot as plt

days = list(range(1, 11))
cumulative_rainfall = [0, 5, 12, 20, 30, 45, 60, 80, 100, 120]

plt.figure(figsize=(10, 6))
plt.plot(days, cumulative_rainfall, marker='o', color='blue', linestyle='-', linewidth=2)

plt.title('Cumulative Rainfall Over 10 Days')
plt.xlabel('Day', fontsize=14)
plt.ylabel('Cumulative Rainfall (mm)')
plt.xticks(days)
plt.grid(True)

plt.show()