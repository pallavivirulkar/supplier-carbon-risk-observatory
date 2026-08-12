import pandas as pd

df = pd.read_csv("../data/processed_dataco_clean.csv")
cepii = pd.read_excel("../data/raw/cepii/dist_cepii.xls")

cepii_subset = cepii[["iso_o", "iso_d", "dist"]]

df = df.merge(
    cepii_subset,
    left_on=["Supplier Country ISO3", "Order Country ISO3"],
    right_on=["iso_o", "iso_d"],
    how="left",
)

df = df.drop(columns=["iso_o", "iso_d"])
df = df.rename(columns={"dist": "Distance Km"})

print("Unmatched distance rows:", df["Distance Km"].isnull().sum())
print("\nDistance stats:")
print(df["Distance Km"].describe())

df.to_csv("../data/processed_dataco_clean.csv", index=False)
print("\nSaved. Final shape:", df.shape)