import pandas as pd

df = pd.read_excel(
    "../data/raw/defra/ghg-conversion-factors-2026-full-set.xlsx",
    sheet_name="Freighting goods",
    header=24,
)

df["Activity"] = df["Activity"].ffill()

print("Unique Activity values:")
for activity in df["Activity"].dropna().unique():
    print(activity)

print("\nUnique Unit values:")
print(df["Unit"].unique())

print("\nActivity + Type combinations where Unit is tonne.km:")
tonne_km = df[df["Unit"] == "tonne.km"]
print(tonne_km[["Activity", "Type"]].to_string())
