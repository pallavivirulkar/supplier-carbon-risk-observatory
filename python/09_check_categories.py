import pandas as pd

df = pd.read_csv("../data/processed_dataco_clean.csv")

print("Total unique categories:", df["Category Name"].nunique())
print("\nAll unique Category Name values:")
for category in sorted(df["Category Name"].unique()):
    print(category)