#  Plot a stacked bar chart showing expenditure distribution over five years.

import matplotlib.pyplot as plt

years = [2015, 2016, 2017, 2018, 2019]
rent = [5000, 5200, 5400, 5600, 5800]
utilities = [1500, 1600, 1700, 1800, 1900]
groceries = [3000, 3200, 3400, 3600, 3800]  
plt.bar(years, rent, label='Rent')
plt.bar(years, utilities, bottom=rent, label='Utilities')
plt.bar(years, groceries, bottom=[i+j for i,j in zip(rent, utilities)], label='Groceries')
plt.xlabel("Years")
plt.ylabel("Expenditure (in dollars)")
plt.title("Expenditure Distribution Over Five Years")
plt.legend()
plt.show()