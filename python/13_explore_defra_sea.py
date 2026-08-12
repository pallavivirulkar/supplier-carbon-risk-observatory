import pandas as pd

raw = pd.read_excel(
    "../data/raw/defra/ghg-conversion-factors-2026-full-set.xlsx",
    sheet_name="Freighting goods",
    header=None,
)

sea_idx = raw[raw[0] == "Sea tanker"].index.tolist()
cargo_idx = raw[raw[0] == "Cargo ship"].index.tolist()

print("Sea tanker starts at row:", sea_idx)
print("Cargo ship starts at row:", cargo_idx)

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

print("\n--- Sea tanker section (raw) ---")
print(raw.iloc[sea_idx[0]-2 : sea_idx[0]+15, 0:6])

print("\n--- Cargo ship section (raw) ---")
print(raw.iloc[cargo_idx[0]-2 : cargo_idx[0]+15, 0:6])

container_idx = raw[raw[1] == "Container ship"].index.tolist()
print("\nContainer ship starts at row:", container_idx)
print(raw.iloc[container_idx[0]-1 : container_idx[0]+15, 0:6])