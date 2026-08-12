import pandas as pd

df = pd.read_csv("../data/processed_dataco_clean.csv")

WEIGHT_MAP = {
    "Apparel & Footwear": 0.5,
    "Sporting Goods & Equipment": 2.5,
    "Electronics Hardware": 3.0,
    "Media & Publishing": 0.3,
    "Home & Lifestyle": 1.5,
}

df["Estimated Unit Weight Kg"] = df["Category Group"].map(WEIGHT_MAP)
df["Estimated Total Weight Kg"] = df["Estimated Unit Weight Kg"] * df["Order Item Quantity"]

print("Unmapped weights:", df["Estimated Unit Weight Kg"].isnull().sum())
print("\nTotal weight stats (kg):")
print(df["Estimated Total Weight Kg"].describe())

df.to_csv("../data/processed_dataco_clean.csv", index=False)
print("\nSaved. Final shape:", df.shape)