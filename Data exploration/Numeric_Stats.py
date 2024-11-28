import pandas as pd

file_path = 'Data Excel.xlsx' 
data = pd.read_excel(file_path, engine='openpyxl')

numeric_data = data.select_dtypes(include=['int64', 'float64'])

summary_statistics = numeric_data.agg(['mean', 'median', 'max', 'min']).T
summary_statistics.rename(columns={'mean': 'Mean', 'median': 'Median', 'max': 'Maximum', 'min': 'Minimum'}, inplace=True)

columns_to_exclude = [
    "Marital status", "Application mode", "Application order", "Course", 
    "Daytime/evening attendance", "Previous qualification", "Nacionality", 
    "Mother's qualification", "Father's qualification", "Mother's occupation", 
    "Father's occupation", "Displaced", "Educational special needs", "Debtor", 
    "Tuition fees up to date", "Gender", "Scholarship holder", "International"
]
summary_statistics = summary_statistics.loc[~summary_statistics.index.isin(columns_to_exclude)]

summary_file = "numeric_summary.xlsx"
summary_statistics.to_excel(summary_file, engine='openpyxl')
print(f"Summary statistics saved to {summary_file}")

print(summary_statistics)
