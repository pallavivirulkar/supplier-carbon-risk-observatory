import pandas as pd

df = pd.read_csv("../data/raw/dataco/DataCoSupplyChainDataset.csv", encoding="latin1")

DROP_COLS = [
    "Customer Email",
    "Customer Password",
    "Customer Fname",
    "Customer Lname",
    "Customer Street",
    "Product Image",
    "Product Description",
    "Order Zipcode",
]

df = df.drop(columns=DROP_COLS)

print("Shape after drop:", df.shape)
print("\nRemaining columns:")
for col in df.columns:
    print(col)

df = df.dropna(subset=["Customer Zipcode"])

print("\nShape after dropping missing rows:", df.shape)
print("Missing values remaining:")
print(df.isnull().sum()[df.isnull().sum() > 0])

mapping_df = pd.read_csv("../data/reference_country_mapping.csv")
country_map = dict(zip(mapping_df["raw_country_name"], mapping_df["iso3"]))

df["Order Country ISO3"] = df["Order Country"].map(country_map)
df["Customer Country ISO3"] = df["Customer Country"].map(country_map)

print("\nUnmapped Order Country values:", df["Order Country ISO3"].isnull().sum())
print("Unmapped Customer Country values:", df["Customer Country ISO3"].isnull().sum())

df.to_csv("../data/processed_dataco_clean.csv", index=False)
print("\nSaved cleaned file. Final shape:", df.shape)