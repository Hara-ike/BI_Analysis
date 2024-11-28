import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'Data exploration/Data Excel.xlsx'  
data = pd.read_excel(file_path, engine='openpyxl')

numeric_data = data.select_dtypes(include=['int64', 'float64'])

correlation_matrix = numeric_data.corr()

plt.figure(figsize=(14, 10))
sns.heatmap(correlation_matrix, annot=False, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap (Numeric Data)', fontsize=16)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout() 
plt.show()
