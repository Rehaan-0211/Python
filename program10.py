#  Plot a scatter graph to show the relationship between hours studied and marks obtained.
import matplotlib.pyplot as plt
hours_studied = [1, 2, 3, 4, 5]
marks_obtained = [50, 60, 70, 80, 90]
plt.scatter(hours_studied, marks_obtained)
plt.title("Relationship between Hours Studied and Marks Obtained")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Obtained")
plt.show()