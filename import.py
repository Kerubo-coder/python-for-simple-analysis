import pandas as pd
import json
import os

# Read excel file
df = pd.read_excel('data/dm_clients.xlsx')
# Which age group has the highest average blood glucose level?
df['Age_Group'] = pd.cut(
    df['Age'],
    bins=[0, 18, 35, 50, 65, 100],
    labels=['<18', '18-35', '36-50', '51-65', '65+']
)

df.groupby('Age_Group')['Blood_Glucose'].mean()
# Agegroup 51-65 with 163

"""Relationship between BMI & Blood Glucose
Correlation analysis
Scatter plots
Visualization with Matplotlib/Seaborn"""

correlation = df['BMI'].corr(df['Blood_Glucose'])
print(correlation)
# Theres no scientificaly proven Rship as -0.061
#Scatter plot Visualization
import matplotlib.pyplot as plt

plt.scatter(df['BMI'], df['Blood_Glucose'])
plt.xlabel('BMI')
plt.ylabel('Blood Glucose')
plt.show()

"""Which treatment outcomes are most common?
Objective: Understand patient recovery trends.
skills:
Frequency analysis
Bar charts"""
outcomes = df['Treatment_Outcome'].value_counts()
print(outcomes)
outcomes.plot(kind='bar')
plt.title('Treatment Outcomes')
plt.show()

"""Do smokers have higher blood pressure than non-smokers?
Objective: Compare health indicators between smoking groups.
Python skills:
Filtering data
Group comparisons"""
df.groupby('Smoking_Status')[['Systolic_BP','Diastolic_BP']].mean()

"""Which facility handles the most diabetes patients and what are their outcomes?
Objective: Evaluate workload and performance by facility.
Python skills:
Grouping
Pivot tables"""

facility_patients = df.groupby('Facility')['Patient_ID'].count()
print(facility_patients)
pd.crosstab(
    df['Facility'],
    df['Treatment_Outcome']
)
