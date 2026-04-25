import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create sample data
data = pd.DataFrame({
    "x": [1, 2, 3, 4, 5],
    "y": [10, 20, 25, 30, 40]
})

print("=== DIFFERENCE BETWEEN MATPLOTLIB AND SEABORN ===\n")

# 1. Library Type
print("1. Type:")
print("Matplotlib -> Basic plotting library")
print("Seaborn    -> High-level statistical visualization library\n")

# 2. Default Style
print("2. Default Style:")
print("Matplotlib -> Plain/basic look")
print("Seaborn    -> Attractive and styled by default\n")

# 3. Ease of Use
print("3. Ease of Use:")
print("Matplotlib -> Requires more code")
print("Seaborn    -> Less code, easier for complex plots\n")

# 4. Data Handling
print("4. Data Handling:")
print("Matplotlib -> Works with lists/arrays")
print("Seaborn    -> Works well with pandas DataFrames\n")

# 5. Example Plot (Matplotlib)
plt.figure()
plt.plot(data["x"], data["y"])
plt.title("Matplotlib Plot")
plt.show()

# 6. Example Plot (Seaborn)
sns.lineplot(x="x", y="y", data=data)
plt.title("Seaborn Plot")
plt.show()