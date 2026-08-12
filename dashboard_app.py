import sqlite3
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

DB_PATH = Path(__file__).resolve().parent / "sql" / "supplier_carbon_risk.db"

st.set_page_config(page_title="Supplier Carbon Risk Observatory", layout="wide")


@st.cache_resource
def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)


@st.cache_data
def get_filter_options(_conn):
    categories = pd.read_sql('SELECT DISTINCT "Category Group" FROM fact_orders ORDER BY 1', _conn)
    modes = pd.read_sql('SELECT DISTINCT "Transport Mode" FROM fact_orders ORDER BY 1', _conn)
    countries = pd.read_sql('SELECT DISTINCT "Supplier Country ISO3" FROM fact_orders ORDER BY 1', _conn)
    return categories.iloc[:, 0].tolist(), modes.iloc[:, 0].tolist(), countries.iloc[:, 0].tolist()


def build_where_clause(categories, modes, supplier_countries):
    conditions = []
    params = []

    if categories:
        conditions.append(f'"Category Group" IN ({",".join(["?"] * len(categories))})')
        params.extend(categories)
    if modes:
        conditions.append(f'"Transport Mode" IN ({",".join(["?"] * len(modes))})')
        params.extend(modes)
    if supplier_countries:
        conditions.append(f'"Supplier Country ISO3" IN ({",".join(["?"] * len(supplier_countries))})')
        params.extend(supplier_countries)

    where_sql = f"WHERE {' AND '.join(conditions)}" if conditions else ""
    return where_sql, params


conn = get_connection()
all_categories, all_modes, all_countries = get_filter_options(conn)

st.sidebar.header("Filters")
selected_categories = st.sidebar.multiselect("Category Group", all_categories, default=all_categories)
selected_modes = st.sidebar.multiselect("Transport Mode", all_modes, default=all_modes)
selected_countries = st.sidebar.multiselect("Supplier Country", all_countries, default=all_countries)

where_sql, params = build_where_clause(selected_categories, selected_modes, selected_countries)

st.title("Supplier Carbon Risk Observatory")
st.caption("Procurement & supply chain emissions analytics — DataCo Smart Supply Chain dataset")

kpi_query = f"""
    SELECT
        COUNT(*) AS order_count,
        ROUND(SUM("Emissions Kg CO2e"), 2) AS total_emissions,
        ROUND(AVG("Emissions Kg CO2e"), 2) AS avg_emissions,
        ROUND(SUM("Estimated Total Weight Kg") / 1000, 2) AS total_weight_tonnes
    FROM fact_orders
    {where_sql}
"""
kpis = pd.read_sql(kpi_query, conn, params=params).iloc[0]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Orders", f"{int(kpis['order_count']):,}")
col2.metric("Total Emissions (kg CO2e)", f"{kpis['total_emissions']:,.0f}")
col3.metric("Avg Emissions / Order (kg CO2e)", f"{kpis['avg_emissions']:.2f}")
col4.metric("Total Weight Shipped (tonnes)", f"{kpis['total_weight_tonnes']:,.1f}")

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Emissions by Category Group")
    category_df = pd.read_sql(
        f'''SELECT "Category Group", ROUND(SUM("Emissions Kg CO2e"), 2) AS total_emissions
            FROM fact_orders {where_sql}
            GROUP BY "Category Group" ORDER BY total_emissions DESC''',
        conn, params=params,
    )
    fig = px.bar(category_df, x="total_emissions", y="Category Group", orientation="h",
                 labels={"total_emissions": "Total Emissions (kg CO2e)"})
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("Transport Mode Share")
    mode_df = pd.read_sql(
        f'''SELECT "Transport Mode", COUNT(*) AS order_count
            FROM fact_orders {where_sql}
            GROUP BY "Transport Mode" ORDER BY order_count DESC''',
        conn, params=params,
    )
    fig = px.pie(mode_df, names="Transport Mode", values="order_count", hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Emissions by Supplier")
supplier_df = pd.read_sql(
    f'''SELECT "Supplier Name", "Supplier Country ISO3",
               COUNT(*) AS order_count,
               ROUND(SUM("Emissions Kg CO2e"), 2) AS total_emissions,
               ROUND(AVG("Emissions Kg CO2e"), 2) AS avg_emissions
        FROM fact_orders {where_sql}
        GROUP BY "Supplier Name", "Supplier Country ISO3"
        ORDER BY total_emissions DESC''',
    conn, params=params,
)
fig = px.bar(supplier_df, x="Supplier Name", y="total_emissions", color="Supplier Country ISO3",
             labels={"total_emissions": "Total Emissions (kg CO2e)"})
st.plotly_chart(fig, use_container_width=True)
st.dataframe(supplier_df, use_container_width=True, hide_index=True)

st.subheader("Top 15 Destination Countries by Emissions")
country_df = pd.read_sql(
    f'''SELECT "Order Country ISO3", COUNT(*) AS order_count,
               ROUND(SUM("Emissions Kg CO2e"), 2) AS total_emissions
        FROM fact_orders {where_sql}
        GROUP BY "Order Country ISO3"
        ORDER BY total_emissions DESC LIMIT 15''',
    conn, params=params,
)
fig = px.bar(country_df, x="Order Country ISO3", y="total_emissions",
             labels={"total_emissions": "Total Emissions (kg CO2e)"})
st.plotly_chart(fig, use_container_width=True)

with st.expander("View filtered raw data sample (first 500 rows)"):
    sample_df = pd.read_sql(f"SELECT * FROM fact_orders {where_sql} LIMIT 500", conn, params=params)
    st.dataframe(sample_df, use_container_width=True)
