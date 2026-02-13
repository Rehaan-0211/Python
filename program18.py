# Draw a grouped bar chart to compare sales of three products over four years.

import matplotlib.pyplot as plt

years = [2020, 2021, 2022, 2023]
product1_sales = [100, 150, 180, 200]
product2_sales = [80, 120, 140, 160]
product3_sales = [90, 130, 160, 190]

x = range(len(years))
width = 0.25

plt.bar([i - width for i in x], product1_sales, width=width, label='Product 1')
plt.bar(x, product2_sales, width=width, label='Product 2')
plt.bar([i + width for i in x], product3_sales, width=width, label='Product 3')

plt.xlabel("Years")
plt.ylabel("Sales (in thousands)")
plt.title("Sales Comparison of Three Products Over Four Years")
plt.xticks(x, years)
plt.legend()
plt.show()