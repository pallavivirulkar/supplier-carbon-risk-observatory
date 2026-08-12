import pandas as pd

df = pd.read_csv("../data/processed_dataco_clean.csv")
cepii = pd.read_excel("../data/raw/cepii/dist_cepii.xls")
cepii_subset = cepii[["iso_o", "iso_d", "dist"]]

CEPII_ALIAS = {
    "ROU": "ROM",
    "COD": "ZAR",
    "SRB": "YUG",
    "MNE": "YUG",
    "SSD": "SDN",
}

missing_mask = df["Distance Km"].isnull()
print("Rows to fix:", missing_mask.sum())

df.loc[missing_mask, "Order Country ISO3 Alias"] = df.loc[missing_mask, "Order Country ISO3"].map(CEPII_ALIAS)

fix_df = df.loc[missing_mask].merge(
    cepii_subset,
    left_on=["Supplier Country ISO3", "Order Country ISO3 Alias"],
    right_on=["iso_o", "iso_d"],
    how="left",
)

df.loc[missing_mask, "Distance Km"] = fix_df["dist"].values
df = df.drop(columns=["Order Country ISO3 Alias"], errors="ignore")

print("Remaining unmatched:", df["Distance Km"].isnull().sum())

df.to_csv("../data/processed_dataco_clean.csv", index=False)
print("Saved. Final shape:", df.shape)