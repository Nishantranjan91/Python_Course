import pandas as pd

# Load Excel file
file_path = "data.xlsx"   # change to your file name
df = pd.read_excel(file_path)

# Get number of rows and columns
rows, columns = df.shape

print("Number of rows:", rows)
print("Number of columns:", columns)