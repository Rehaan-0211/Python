#  Plot a line graph showing the population growth of a city over 10 years

import matplotlib.pyplot as plt 

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
population = [500000, 550000, 600000, 650000, 700000, 750000, 800000, 850000, 900000, 950000]

plt.plot(years, population)

plt.title("Population Growth of a City Over 10 Years")
plt.xlabel("Years")
plt.ylabel("Population")

plt.show()