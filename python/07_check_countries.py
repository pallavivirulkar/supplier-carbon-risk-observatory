import pandas as pd

df = pd.read_csv("../data/raw/dataco/DataCoSupplyChainDataset.csv", encoding="latin1")

print("Unique Customer Country values:")
print(sorted(df["Customer Country"].unique()))

print("\nAll unique Order Country values:")
for country in sorted(df["Order Country"].unique()):
    print(country)

print("\nTotal unique Order Country values:", df["Order Country"].nunique())