import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

health_data=pd.read_csv('data3.csv',header=0,sep=',')
health_data2=pd.read_csv('data2.csv',header=0,sep=',')

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
health_data2.plot(x='Average_Pulse',y='Calorie_Burnage',kind='scatter')
plt.title('PERFECT CORRELATION')
plt.show()

# NEGATIVE CORRELATION
negative_corr={'Hours_Work_Before_Training':[10,9,8,7,6,5,4,3,2,1],'Calorie_Burnage': [220,240,260,280,300,320,340,360,380,400]}
negative_corr=pd.DataFrame(data=negative_corr)
negative_corr.plot(x='Hours_Work_Before_Training',y='Calorie_Burnage',kind='scatter')
plt.title('NEGATIVE CORRELATION')
plt.show()

# NO LINEAR RELATIONSHIP
health_data.plot(x='Duration',y='Max_Pulse',kind='scatter')
plt.title('NO LINEAR CORRELATION')
plt.show()

# CORRELATION MATRIX
corr_matrix=round(health_data.corr(),2)
print(corr_matrix)

#HEATMAP
corr_mat=health_data.corr()

axis_corr=sns.heatmap(
    corr_mat,
    vmin=-1,vmax=1,center=0,
    cmap=sns.diverging_palette(50,500,n=500),
    square=True,
)
plt.show()