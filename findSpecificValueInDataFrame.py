import pandas as pd

df = pd.DataFrame({
    'Name': ['A', 'B', 'C'],
    'Age': [20, 25, 30]
})

# Find rows where Age = 25
result = df[df['Age'] == 25]
print(result)