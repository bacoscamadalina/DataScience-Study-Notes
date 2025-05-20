# CORRELATION VS CAUSALITY EXAMPLE

import pandas as pd
import matplotlib.pyplot as plt

month = list(range(1,13))
movies = [20,40,60,80,100,120,140,160,180,200,220,240]
coffee_consumption = [20,40,60,80,100,120,140,160,180,200,220,240]

data = pd.DataFrame({
    'Month': month,
    'Released_Movies':movies,
    'Coffee_Consumption': coffee_consumption
})

data.plot(x='Released_Movies',y='Coffee_Consumption',kind='scatter')
plt.title('Released Movies vs Coffe Consumption')
plt.show()

print(data[['Released_Movies', 'Coffee_Consumption']].corr())

'''
We can see that there is a perfect correlation between 'Released Movies' and 'Coffee Consumption' but in reality they are 
accidentally correlated. 
Coffee consumption does not actually affect the number of movies released.
'''
