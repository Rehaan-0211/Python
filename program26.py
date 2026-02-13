# Stacked Bar Chart of Monthly Expenses

import matplotlib.pyplot as plt

categories = ['Rent', 'Food', 'Transport', 'Entertainment', 'Utilities']
expenses = [1000, 300, 150, 200, 250]

plt.figure(figsize=(10, 6))
plt.bar(categories, expenses, color=['blue', 'orange', 'green', 'red', 'purple'])

plt.title('Monthly Expenses')
plt.xlabel('Expense Categories')
plt.ylabel('Amount ($)')
plt.grid(axis='y', alpha=0.75)

plt.show()