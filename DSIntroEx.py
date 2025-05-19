import pandas as pd
import numpy as np

'''
Requirements: 
1. Read the file students.csv into a DataFrame.
2. Display the first 5 rows to check data types and null values.
3. Clean the data: remove any rows that contain missing values (NaN).
4. Print out the following:
    a.The maximum math score.
    b.The minimum English score.
    c.The average science score.
5. Use .describe() to display a statistical summary of the DataFrame.
6. Create a new column called Total_Score that sums the 3 subjects for each student.
7. Create another column called Performance_Level:
    'High' if Total_Score >= 270
    'Medium' if between 240 and 269 
    'Low' if below 240
8. Group the data by Performance_Level and calculate:
    Average Study_Hours per group
    Average Sleep_Hours per group
9. Sort the DataFrame by Total_Score in descending order and print the top 5 students.
'''

#1.
stud_info=pd.read_csv("students.csv",header=0,sep=',')
print(stud_info)
#2.
print(stud_info.head())
#3.
stud_info.dropna(axis=0,inplace=True)
print(stud_info)
#4.
print(stud_info.info())
max_score = np.max(stud_info['Math_Score'])
min_score = np.min(stud_info['English_Score'])
mean_score = np.mean(stud_info['Science_Score'])
#5.
print(stud_info.describe())
#6.
total_score = stud_info['Math_Score']+stud_info['English_Score']+stud_info['Science_Score']
stud_info['Total_Score'] = total_score
print(stud_info)
#7.
for i in stud_info.index:
    if total_score[i] >= 270:
        stud_info.loc[i,'Performance_Level'] = 'High'
    elif 240<total_score[i]<269:
        stud_info.loc[i,'Performance_Level'] = 'Medium'
    else:
        stud_info.loc[i,'Performance_Level'] = 'Low'

print(stud_info)
#8.
grouped_data = stud_info.groupby('Performance_Level')[['Study_Hours', 'Sleep_Hours']].mean()
print(grouped_data)
#9.
sorted_data = stud_info.sort_values(by=['Total_Score'], ascending=False)
print(sorted_data.head())
