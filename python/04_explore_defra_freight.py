import pandas as pd

raw = pd.read_excel(
    "../data/raw/defra/ghg-conversion-factors-2026-full-set.xlsx",
    sheet_name="Freighting goods",
    header=None,
)

print("Shape:", raw.shape)
print("\nRows 15 to 40, first 10 columns:")
print(raw.iloc[15:40, :10].to_string())