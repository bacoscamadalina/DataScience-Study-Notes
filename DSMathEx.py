import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import stats
from scipy import stats

'''
1. Create a line chart to show the relationship between Study_Hours and Total_Score. Add a title and labels for both axes.
Set axis limits if needed.
2. Display on the same chart:
    a.A scatter plot of Study_Hours vs Total_Score using plt.scatter().
    b.A regression line using np.polyfit() and plt.plot().
3. Create a bar chart showing each student’s Math_Score, with Student_ID on the x-axis.
4. Create a pie chart that displays the proportion of students in each Performance_Level category (High, Medium, Low).
5.Create a histogram of the Science_Score to analyze how science performance is distributed among students.
6.Create a box plot to compare the distributions of: Math_Score, Science_Score, English_Score
'''

stud_info=pd.read_csv("students.csv",header=0,sep=',')
total_score = stud_info['Math_Score']+stud_info['English_Score']+stud_info['Science_Score']
stud_info['Total_Score'] = total_score
stud_info.dropna(axis=0,inplace=True)
print(stud_info)

#1.
stud_info.plot(x='Study_Hours',y='Total_Score',kind='line')

plt.xlim(xmin=0)
plt.ylim(ymin=0)
plt.xlabel('Study_Hours')
plt.ylabel('Total_Score')
plt.title('Study Hours vs Total Score')
plt.show()

#2.
x=stud_info['Study_Hours']
y=stud_info['Total_Score']
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept
mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.title('Relationship between Study Hours and Total Score.')
plt.show()

#3.
x=stud_info['Math_Score']
y=stud_info['Student_ID']
plt.barh(y,x)
plt.xlabel('Math Score')
plt.ylabel('Student ID')
plt.title('Math Score')
plt.show()

#4.
for i in stud_info.index:
    if total_score[i] >= 270:
        stud_info.loc[i,'Performance_Level'] = 'High'
    elif 240<total_score[i]<269:
        stud_info.loc[i,'Performance_Level'] = 'Medium'
    else:
        stud_info.loc[i,'Performance_Level'] = 'Low'

counts= stud_info['Performance_Level'].value_counts()

labels=counts.index
sizes = counts.values

plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title('Proportion of students in Performance_Level ')
plt.axis('equal')
plt.show()

#5.Create a histogram of the Science_Score to analyze how science performance is distributed among students.
x=stud_info['Science_Score']
plt.hist(x)
plt.xlabel('Science Score')
plt.ylabel('Frequency')
plt.title('Science performance distributed among students')
plt.show()

#6.
x=stud_info['Math_Score']
y=stud_info['Science_Score']
z=stud_info['English_Score']
p=[x,y,z]

plt.boxplot(p,tick_labels=['Math Score', 'Science Score', 'English Score'])
plt.ylabel('Scores')
plt.title('Math Score VS Science Score VS English Score')
plt.show()


