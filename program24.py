#  Bar Chart of Library Books

import matplotlib.pyplot as plt

categories = ['Fiction', 'Non-Fiction', 'Science', 'History', 'Biography']
book_counts = [120, 80, 60, 40, 30]
plt.figure(figsize=(10, 6))
plt.bar(categories, book_counts, color=['blue', 'orange', 'green', 'red', 'purple'])
plt.title('Number of Books in Each Category')
plt.xlabel('Book Categories')
plt.ylabel('Number of Books')
plt.grid(axis='y', alpha=0.75)
plt.show()
