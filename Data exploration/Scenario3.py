import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'Data exploration/Data Excel.xlsx'  
data = pd.read_excel(file_path, engine='openpyxl')

plt.figure(figsize=(10, 6))
ax = sns.scatterplot(
    x='Admission grade', 
    y='Curricular units 1st sem (grade)', 
    hue='Target', 
    data=data, 
    palette='Set1'
)

plt.title('Admission Grade vs First Semester Grade by Target')
plt.xlabel('Admission Grade')
plt.ylabel('1st Semester Grade')
plt.legend(title='Target')

plt.show()
