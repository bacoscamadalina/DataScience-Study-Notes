import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

health_data=pd.read_csv('data3.csv',header=0,sep=',')
print(health_data.describe())

# STATISTICS PERCENTILE (25,50,75)
max_pulse = health_data["Max_Pulse"]
percentile25=np.percentile(max_pulse,25)
print(percentile25)

# STANDARD DEVIATION
print('----STD----')
stand = health_data.std(axis=0, ddof=1)
print(stand)

# COEFFICIENT OF VARIATION - how large std is
print('----CV----')
cv= health_data.std(axis=0, ddof=1)/ health_data.mean(axis=0)
print(cv)

# VARIATION - steps
#1. Find the mean
mean_val = health_data['Average_Pulse'].mean()

#2. Find the diff from the mean
health_data['Diff From Mean'] = health_data['Average_Pulse'] - mean_val

#3. Find the square value
health_data['Squared Diff'] = health_data['Diff From Mean']**2

#4. Variance is the average nr of sq_val
variance = health_data['Squared Diff'].mean()
print(f'Variance: {variance}')

# Second option
var = np.var(health_data['Average_Pulse'])
print(f'Variance:{var}')

#PERFECT CORRELATION
health_data.plot(x='Average_Pulse',y='Calorie_Burnage',kind='scatter')
plt.show()
