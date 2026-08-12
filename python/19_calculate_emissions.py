import pandas as pd

df = pd.read_csv("../data/processed_dataco_clean.csv")

EMISSION_FACTORS = {
    "Road": 0.10356,
    "Air": 0.89939,
    "Sea": 0.01612,
}

def assign_transport_mode(row):
    if row["Supplier Country ISO3"] == row["Order Country ISO3"]:
        return "Road"
    if row["Shipping Mode"] in ["Same Day", "First Class"]:
        return "Air"
    return "Sea"

df["Transport Mode"] = df.apply(assign_transport_mode, axis=1)
df["Emission Factor"] = df["Transport Mode"].map(EMISSION_FACTORS)

df["Emissions Kg CO2e"] = (
    (df["Estimated Total Weight Kg"] / 1000) * df["Distance Km"] * df["Emission Factor"]
)

print("Transport mode distribution:")
print(df["Transport Mode"].value_counts())

print("\nEmissions stats (kg CO2e):")
print(df["Emissions Kg CO2e"].describe())

df.to_csv("../data/processed_dataco_clean.csv", index=False)
print("\nSaved. Final shape:", df.shape)