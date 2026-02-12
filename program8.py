# Draw a bar chart to show the number of students present in different classes. 

import matplotlib.pyplot as plt

classes = ['Class A', 'Class B', 'Class C', 'Class D', 'Class E']
students = [30, 25, 35, 28, 32]

plt.bar(classes, students)
plt.title("Number of Students Present in Different Classes")
plt.xlabel("Classes")
plt.ylabel("Number of Students")
plt.show()