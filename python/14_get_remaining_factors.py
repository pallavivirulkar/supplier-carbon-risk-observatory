import pandas as pd

df = pd.read_excel(
    "../data/raw/defra/ghg-conversion-factors-2026-full-set.xlsx",
    sheet_name="Freighting goods",
    header=24,
)
df["Activity"] = df["Activity"].ffill()

targets = [
    ("Vans", "Average (up to 3.5 tonnes)"),
    ("HGV (non-refrigerated, all diesel)", "Average non-refrigerated HGVs"),
    ("Freight flights", "International, to/from non-UK"),
    ("Rail", "Freight train"),
]

for activity, type_ in targets:
    row = df[(df["Activity"] == activity) & (df["Type"] == type_) & (df["Unit"] == "tonne.km")]
    print(activity, "|", type_)
    print(row[["Activity", "Type", "Unit", "kg CO2e"]])
    print()