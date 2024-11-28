import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Data Transformation/Encoded_Data.xlsx'
data = pd.read_excel(file_path, engine='openpyxl')

if 'Curricular units 2nd sem (without evaluations)' in data.columns:
    International = data['Curricular units 1st sem (without evaluations)'].value_counts()

    plt.figure(figsize=(10, 6))
    International.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Curricular units 2nd sem (without evaluations)', fontsize=16)
    plt.xlabel('Curricular units 2nd sem (without evaluations)', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
else:
    print("The column 'Curricular units 2nd sem (without evaluations)' does not exist in the dataset.")
