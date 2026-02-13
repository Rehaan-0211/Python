#  Plot sales data of a shop for weekdays and weekends on the same graph.

import matplotlib.pyplot as plt
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend = ['Saturday', 'Sunday']
sales_weekdays = [200, 220, 250, 270, 300]
sales_weekend = [400, 450]
plt.plot(weekdays, sales_weekdays, label='Weekdays', marker='o')
plt.plot(weekend, sales_weekend, label='Weekend', marker='o')
plt.title("Sales Data of a Shop for Weekdays and Weekends")
plt.xlabel("Days")
plt.ylabel("Sales") 
plt.show()

# import matplotlib.pyplot as plt

# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] 
# weekday_sales = [200, 220, 210, 230, 250, 0, 0] 
# weekend_sales = [0, 0, 0, 0, 0, 300, 350] 
 
# plt.plot(days, weekday_sales, label="Weekdays") 
# plt.plot(days, weekend_sales, label="Weekends") 
# plt.xlabel("Days") 
# plt.ylabel("Sales") 
# plt.title("Weekly Sales Report") 
# plt.legend() 
# plt.show() solution in the question pdf
