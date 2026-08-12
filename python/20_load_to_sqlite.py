import sqlite3
import pandas as pd

df = pd.read_csv("../data/processed_dataco_clean.csv")

conn = sqlite3.connect("../sql/supplier_carbon_risk.db")
df.to_sql("fact_orders", conn, if_exists="replace", index=False)

row_count = pd.read_sql("SELECT COUNT(*) AS row_count FROM fact_orders", conn).iloc[0, 0]
print(f"Rows loaded into fact_orders: {row_count}")
print(f"Columns: {len(df.columns)}")

conn.close()