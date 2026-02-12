#  Create a histogram to show the distribution of marks of students
import matplotlib.pyplot as plt

marks = [56,32,56,45,15,78,59,45,68,79,99,100]

plt.figure(figsize=(8,5))

plt.hist(marks, bins=6, color="skyblue", edgecolor="black")

plt.title("Distribution of Marks of Students", fontsize=14)
plt.xlabel("Marks", fontsize=12)
plt.ylabel("Number of Students", fontsize=12)

plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()
plt.show()
