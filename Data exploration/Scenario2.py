import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'Data exploration/Data Excel.xlsx'  
data = pd.read_excel(file_path, engine='openpyxl')

data_cleaned = data.dropna(subset=['Marital status', 'Admission grade'])

Q1 = data_cleaned['Admission grade'].quantile(0.25)
Q3 = data_cleaned['Admission grade'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

data_cleaned = data_cleaned[(data_cleaned['Admission grade'] >= lower_bound) &
                            (data_cleaned['Admission grade'] <= upper_bound)]

plt.figure(figsize=(8, 6))
ax = sns.boxplot(x='Marital status', y='Admission grade', data=data_cleaned, palette='pastel')
plt.title('Admission Grade Distribution by Marital Status')
plt.xlabel('Marital Status')
plt.ylabel('Admission Grade')

medians = data_cleaned.groupby('Marital status')['Admission grade'].median()
for index, median in enumerate(medians):
    plt.text(index, median, f'{median:.2f}', ha='center', va='center', fontsize=10, color='black')

plt.xticks(rotation=45)
plt.show()
