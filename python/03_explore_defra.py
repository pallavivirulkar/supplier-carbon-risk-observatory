import pandas as pd

xls = pd.ExcelFile("../data/raw/defra/ghg-conversion-factors-2026-full-set.xlsx")

print("Total sheets:", len(xls.sheet_names))
for name in xls.sheet_names:
    print(name)