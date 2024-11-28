import pandas as pd
from sklearn.preprocessing import MinMaxScaler

file_path = 'Data Transformation/Distributed Data.xlsx' 
data = pd.read_excel(file_path, engine='openpyxl')

column_to_normalize = 'Academic effort' 

if column_to_normalize in data.columns:
    scaler = MinMaxScaler()
    data[[column_to_normalize]] = scaler.fit_transform(data[[column_to_normalize]])

    output_file_path = 'Data Transformation/Distributed Data.xlsx'
    data.to_excel(output_file_path, index=False)

    print(f"Normalized column saved in '{output_file_path}'.")
else:
    print(f"Column '{column_to_normalize}' does not exist in the dataset.")
