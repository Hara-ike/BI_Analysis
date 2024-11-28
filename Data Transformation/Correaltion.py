import pandas as pd

# Load the dataset
file_path = 'Data Transformation/Distributed Data.xlsx' 
data = pd.read_excel(file_path, engine='openpyxl')

numeric_data = data.select_dtypes(include=['int64', 'float64'])
correlation_matrix = numeric_data.corr()

correlation_file_path = 'Data Transformation/Correlation_Matrix_Distributed.xlsx'
correlation_matrix.to_excel(correlation_file_path, index=True)

