import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# LINEAR FUNCTIONS
health_data=pd.read_csv('data2.csv',header=0,sep=',')

# Create a plot
health_data.plot(x='Average_Pulse',y='Calorie_Burnage',kind='line')
plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.show()

# Find slope = how much calorie burnage increases
# Find intercept = y, where x=0

x= health_data['Average_Pulse']
y = health_data['Calorie_Burnage']
slope_interc=np.polyfit(x,y,1)
print(slope_interc)

# same graph but formatted

health_data.plot(x='Average_Pulse',y='Calorie_Burnage',kind='line')
plt.ylim(ymin=0,ymax=400)
plt.xlim(xmin=0,xmax=150)

plt.show()