import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'Data exploration/Data Excel.xlsx'  
data = pd.read_excel(file_path, engine='openpyxl')

plt.figure(figsize=(8, 6))
ax = sns.countplot(x='Target', data=data, palette='coolwarm')
plt.title('Distribution of Students Across Target Categories')
plt.xlabel('Target (Outcome)')
plt.ylabel('Number of Students')

for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                textcoords='offset points')

plt.xticks(rotation=45)
plt.show()
