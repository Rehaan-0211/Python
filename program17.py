#  Plot a line graph with markers showing the performance of a company over 8 quarters

import matplotlib.pyplot as plt

quarters = ["Q1","Q2","Q3","Q4","Q5","Q6","Q7","Q8"] 
profit = [12, 15, 14, 18, 20, 22, 21, 25] 
plt.plot(quarters, profit, marker='o')  
plt.xlabel("Quarters") 
plt.ylabel("Profit (in lakhs)") 
plt.title("Company Performance Over Quarters") 
plt.show()