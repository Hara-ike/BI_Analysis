import pandas as pd

file_path = 'Data Transformation/Data Excel.xlsx'
data = pd.read_excel(file_path, engine='openpyxl')

nominal_columns = [
    "Marital status", "Application mode", "Application order", "Course", 
    "Daytime/evening attendance", "Previous qualification", "Nacionality", 
    "Mother's qualification", "Father's qualification", "Mother's occupation", 
    "Father's occupation", "Displaced", "Educational special needs", "Debtor", 
    "Tuition fees up to date", "Gender", "Scholarship holder", "International"
]

missing_summary = data.isnull().sum() / len(data) * 100  
print("Percentage of Missing Values in Each Column:\n")
print(missing_summary[missing_summary > 0]) 

for col in nominal_columns:
    if col in data.columns:  
        data[col] = data[col].fillna(data[col].mode()[0])

numeric_columns = [col for col in data.columns if col not in nominal_columns]
for col in numeric_columns:
    if col in data.columns: 
        if data[col].dtype in ['int64', 'float64']:  
            data[col] = data[col].fillna(data[col].median())

data.to_excel("Data Transformation/Missing_Values.xlsx", index=False)