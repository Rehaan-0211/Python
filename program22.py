#  Draw a histogram and explain peak distribution using student marks.

import matplotlib.pyplot as plt

marks = [55, 67, 45, 80, 90, 72, 60, 85, 78, 92, 88, 70, 65, 82, 95]
plt.figure(figsize=(10, 6))
plt.hist(marks, bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Student Marks')
plt.xlabel('Marks')
plt.ylabel('Number of Students')
plt.grid(axis='y', alpha=0.75)
plt.show()