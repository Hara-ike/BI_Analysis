import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'Data exploration/Data Excel.xlsx'  
data = pd.read_excel(file_path, engine='openpyxl')

plt.figure(figsize=(10, 6))
sns.histplot(data['Unemployment rate'], kde=True, bins=15, color='blue')
plt.title('Distribution of Unemployment Rate')
plt.xlabel('Unemployment Rate')
plt.ylabel('Frequency')

plt.show()
