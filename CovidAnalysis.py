import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

covid = pd.read_csv("C:\\Users\\Biju\\Desktop\\Jetlearn\\Data Science\\Resources\\covid_data.csv")

print(covid.info())
covid = covid[['Province_State', 'Country_Region', 'Confirmed', 'Recovered', 'Deaths']]
print(covid)
print(covid.isnull().sum())
covid.fillna(value = "", inplace = True)
print(covid.isnull().sum())

#Scatter plot for top ten most affected countries:

bob = covid.groupby('Country_Region')
harry = bob.sum()
ttc = harry.sort_values("Confirmed", ascending = False).head(10)
print(ttc)

x = ttc.index
y = ttc['Confirmed']
plt.scatter(x, y, marker = "*", s = 20, color = "darkred")
plt.show()