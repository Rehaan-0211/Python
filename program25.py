#  Scatter Plot of Study Time vs Score

import matplotlib.pyplot as plt

study_time = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 55, 60, 65, 70, 75, 80, 85]

plt.figure(figsize=(10, 6))
plt.scatter(study_time, scores, color='blue')

plt.title('Study Time vs Score')
plt.xlabel('Study Time (hours)')
plt.ylabel('Score')

plt.grid(True)
plt.show()