import pandas as pd

df = pd.read_csv("../data/raw/dataco/DataCoSupplyChainDataset.csv", encoding="latin1")

print("Missing values per column (only columns with missing values):")
missing = df.isnull().sum()
print(missing[missing > 0].sort_values(ascending=False))

print("\nTotal duplicate rows:", df.duplicated().sum())

print("\nUnique values in key columns:")
print("Category Name:", df["Category Name"].nunique())
print("Order Country:", df["Order Country"].nunique())
print("Order Region:", df["Order Region"].nunique())
print("Market:", df["Market"].nunique())
print("Shipping Mode:", df["Shipping Mode"].nunique())