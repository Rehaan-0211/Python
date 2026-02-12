# Plot a simple line graph showing the marks of a student in 5 subjects.
import matplotlib.pyplot as plt 

subjects = ['Math', 'Science', 'English', 'History', 'Art']
marks = [85, 90, 78, 92, 88]    

plt.plot(subjects, marks)
plt.title("Student's Marks in 5 Subjects")
[plt.xlabel("Subjects"), plt.ylabel("Marks")]   

plt.show()