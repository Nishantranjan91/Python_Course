import os

folder_path = "C:/Users/YourName/Documents"

for file in os.listdir(folder_path):
    if file.endswith(".xlsx"):
        print(file)