import pandas as pd

file_path = 'Data Transformation/Missing_Values.xlsx'
data = pd.read_excel(file_path, engine='openpyxl')

target_mapping = {'Dropout': 0, 'Enrolled': 1, 'Graduate': 2}
if 'Target' in data.columns:
    data['Target'] = data['Target'].map(target_mapping)

encoded_output_file_path = 'Data Transformation/Encoded_Data.xlsx'
data.to_excel(encoded_output_file_path, index=False)
