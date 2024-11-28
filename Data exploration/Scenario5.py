import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'Data exploration/Data Excel.xlsx'  
data = pd.read_excel(file_path, engine='openpyxl')

first_sem_grades = data['Curricular units 1st sem (grade)']
second_sem_grades = data['Curricular units 2nd sem (grade)']

plt.figure(figsize=(12, 6))
sns.kdeplot(first_sem_grades, shade=True, label='1st Semester Grades', color='blue')
sns.kdeplot(second_sem_grades, shade=True, label='2nd Semester Grades', color='green')

plt.title('Distribution of Grades (First vs. Second Semester)', fontsize=16)
plt.xlabel('Grades', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.legend(title='Semester')
plt.tight_layout()
plt.show()
