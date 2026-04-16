import pandas as pd

data = {
    "Name": ["Aman", "Rahul", "Neha"],
    "Age": [21, 22, 20]
}

df = pd.DataFrame(data)

# Find row where Name is Rahul
result = df[df["Name"] == "Rahul"]
print(result)