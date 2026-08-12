import pandas as pd

df = pd.read_csv("../data/processed_dataco_clean.csv")

unmatched = df[df["Distance Km"].isnull()]
print("Total unmatched rows:", len(unmatched))

print("\nUnmatched by Order Country ISO3:")
print(unmatched["Order Country ISO3"].value_counts())

print("\nUnmatched by Supplier Country ISO3:")
print(unmatched["Supplier Country ISO3"].value_counts())
