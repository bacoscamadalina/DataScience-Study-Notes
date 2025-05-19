# Bibliography: W3School: Data Science

import pandas as pd
import numpy as np

d= {'Duration':[30,30,45,45,45,60,60,60,75,75],'Max_Poules':[120,120,130,130,140,140,145,145,150,150],'Average_Pulse':[80,85,90,95,100,105,110,115,120,125],'Calorie_Burnage':[240,250,260,270,280,290,300,310,320,330],'Hours_Work':[10,10,8,8,0,7,7,8,0,8],"Hours_Sleep":[7,7,7,7,7,8,8,8,8,8]}

df=pd.DataFrame(data=d)

count_column=df.shape[1]  # for columns
count_row = df.shape[0]  # for rows

print(f'Nr of columns: {count_column}')
print(f'Nr of rows: {count_row}')

#max() function
Average_pulse_max=df['Average_Pulse'].max()
print(f'Average pulse max: {Average_pulse_max}')

#min() function
Average_pulese_min=df['Average_Pulse'].min()
print(f'Average pulse min: {Average_pulese_min}')

# mean() function
Average_calorie_burnage = np.mean(df['Calorie_Burnage'])
print(f'Average calorie_burnage: {Average_calorie_burnage}')

# DATA PREPARATION
health_data=pd.read_csv('data.csv',header=0,sep=',')
print(health_data)
print(health_data.head()) # first 5 rows

# DATA CLEANING
health_data.dropna(axis=0,inplace=True)
print(health_data)
print(health_data.info())

# Convert object to float64 - astype()

health_data["Average_Pulse"]=health_data["Average_Pulse"].astype(float)
health_data["Max_Pulse"] = health_data["Max_Pulse"].astype(float)

print(health_data.info())

# Analyze the data
print(health_data.describe())
'''
WHERE: 
count - countst the nr. of observations
mean - average
std - Standard Deviation 
min - Lowes value
max - Highes value
25%,50%,75% percentage 

'''