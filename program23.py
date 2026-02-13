#  Plot a line graph showing moving average of temperature data

import matplotlib.pyplot as plt 
temperature = [28, 30, 29, 31, 33, 34, 32, 31] 
days = list(range(1, len(temperature) + 1)) 

moving_avg = [] 
for i in range(len(temperature)): 
    if i == 0: 
        moving_avg.append(temperature[i]) 
    else: 
        avg = (temperature[i] + temperature[i-1]) / 2 
        moving_avg.append(avg) 
 
plt.plot(days, temperature, label="Actual Temperature") 
plt.plot(days, moving_avg, label="Moving Average") 
plt.xlabel("Days") 
plt.ylabel("Temperature") 
plt.title("Temperature Trend Analysis") 
plt.legend() 
plt.show()

# i used loop because we can't calculate the moving avg directly

