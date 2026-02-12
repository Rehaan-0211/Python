# Create a pie chart showing monthly expenses of a family. 
import matplotlib.pyplot as plt

expenses = ['Housing', 'Food', 'Transportation', 'Entertainment', 'Utilities']
amounts = [1200, 600, 300, 200, 400]

plt.pie(amounts, labels=expenses, autopct='%1.1f%%')
plt.title("Monthly Expenses of a Family")
plt.show()