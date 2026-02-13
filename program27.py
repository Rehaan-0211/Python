# Cumulative Marks Analysis

import matplotlib.pyplot as plt
 
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
marks = [85, 78, 92, 88, 95]

plt.figure(figsize=(10, 6))
plt.bar(students, marks, color='skyblue')

plt.title('Cumulative Marks of Students')
plt.xlabel('Students')
plt.ylabel('Marks')

plt.grid(axis='y', alpha=0.75)
plt.show()