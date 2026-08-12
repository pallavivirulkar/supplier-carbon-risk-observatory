import pandas as pd

df = pd.read_csv("../data/raw/dataco/DataCoSupplyChainDataset.csv", encoding="latin1")

print("Shape:", df.shape)

print("\nColumns:")
for col in df.columns:
    print(col)

print("\nSample rows:")
print(df.head(3))

print("\nData types:")
print(df.dtypes)