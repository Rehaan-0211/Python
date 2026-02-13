#  Percentage Growth of Attendance

import matplotlib.pyplot as plt
months = ['January', 'February', 'March', 'April', 'May', 'June']
attendance = [80, 85, 90, 95, 100, 105]

plt.figure(figsize=(10, 6))
plt.plot(months, attendance, marker='o', color='blue', linestyle='-', linewidth=2)

plt.title('Percentage Growth of Attendance Over 6 Months')
plt.xlabel('Month', fontsize=14)
plt.ylabel('Attendance (%)', fontsize=14)

plt.grid(True)
plt.show()