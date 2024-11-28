import pandas as pd

file_path = 'Data exploration/Data to manipulate.xlsx'  
data = pd.read_excel(file_path, engine='openpyxl')

numeric_data = data.select_dtypes(include=['int64', 'float64'])

Q1 = numeric_data.quantile(0.25)  # First quartile (25th percentile)
Q3 = numeric_data.quantile(0.75)  # Third quartile (75th percentile)
IQR = Q3 - Q1                     # IQR = Q3 - Q1

outliers = ((numeric_data < (Q1 - 1.5 * IQR)) | (numeric_data > (Q3 + 1.5 * IQR)))

outlier_counts = outliers.sum()

outlier_summary = pd.DataFrame({
    "Column": outlier_counts.index,
    "Outlier Count": outlier_counts.values
})

# Save the summary to an Excel file
outlier_summary.to_excel("outlier_summary.xlsx", index=False, engine='openpyxl')

