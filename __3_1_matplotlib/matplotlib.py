from matplotlib import pyplot as plt

'''
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300, 543, 1075, 2862, 5979, 10289, 14958]
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
plt.title("Nominal GDP")
plt.ylabel("Billions of $")
plt.show()
'''


gdp = {}
gdp[1950] = 300
gdp[1960] = 543
gdp[1970] = 1075
gdp[1980] = 2862
gdp[1990] = 5679
gdp[2000] = 10289
gdp[2010] = 14958

plt.plot( list(gdp.keys()), list(gdp.values()), color='green', marker='o', linestyle='solid')
plt.title("Nominal GDP")
plt.ylabel("Billions of $")
plt.show()

