import pandas as pd

df = pd.read_excel("../data/raw/cepii/dist_cepii.xls")

print("Shape:", df.shape)
print("\nColumns:")
print(list(df.columns))
print("\nSample rows:")
print(df.head(5))