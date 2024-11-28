import pandas as pd

csv_file_path = 'Data exploration/data.csv'

df = pd.read_csv(csv_file_path, delimiter=';', encoding='utf-8-sig')

excel_file_path = 'final_output.xlsx'
df.to_excel(excel_file_path, index=False, engine='openpyxl')
print(f"File has been saved correctly at: {excel_file_path}")
