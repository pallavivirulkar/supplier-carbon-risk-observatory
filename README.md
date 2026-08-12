# Supplier Carbon Risk Observatory

Procurement and supply chain sustainability analytics project. Estimates shipment-level carbon emissions across a global supplier network, identifies high-risk suppliers and categories, and surfaces cost/emissions trade-offs for sourcing decisions.

## Business Problem

Procurement teams typically optimize for cost and lead time, with limited visibility into the carbon footprint of sourcing decisions. This project builds a reproducible pipeline that estimates emissions per order using shipment weight, transport mode, and distance, then aggregates results by supplier, product category, and destination country to answer:

- Which suppliers and categories contribute the most to logistics-related emissions?
- How does transport mode (road / air / sea) affect emissions per order?
- Where are the highest-emitting trade lanes, and is there room to shift transport mode or sourcing without breaking cost/lead-time constraints?

See [docs/business_problem.md](docs/business_problem.md) and [docs/business_questions.md](docs/business_questions.md) for full detail.

## Tech Stack

| Layer | Tools |
|---|---|
| Data cleaning & feature engineering | Python (pandas) |
| Emissions calculation | Python |
| Aggregation & validation | SQL (SQLite) |
| Interactive dashboard | Streamlit, Plotly |
| BI dashboard & DAX | Power BI (in progress) |

## Pipeline

```
Raw Data (DataCo + DEFRA + CEPII)
        │
        ▼
Python: cleaning, country standardization, feature engineering
        │
        ▼
Python: emissions calculation (transport mode + distance + weight)
        │
        ▼
SQLite: aggregation & validation queries
        │
        ├──► Streamlit dashboard (interactive, code-based)
        │
        └──► Power BI: star schema, DAX, dashboard (planned)
```

## Data Sources

1. **[DataCo Smart Supply Chain Dataset](https://data.mendeley.com/datasets/8gx2fvg2k6/5)** (Kaggle/Mendeley) — 180,519 order-level transactional records.
2. **UK DEFRA GHG Conversion Factors 2026** — transport-mode emission factors (kg CO2e per tonne-km).
3. **CEPII GeoDist** — country-pair great-circle distances.

Full details in [docs/data_sources.md](docs/data_sources.md).

## Repository Structure

```
├── data/
│   └── reference_country_mapping.csv   # Spanish → ISO3 country mapping (166 entries)
├── python/                             # Cleaning, feature engineering, emissions calc (scripts 01-20)
├── sql/
│   ├── 01_validation.sql               # Data quality checks
│   └── 02_aggregations.sql             # Supplier/category/country emissions aggregation
├── docs/                               # Business problem, data sources, exploration notes
├── dashboard_app.py                    # Streamlit dashboard
├── requirements_streamlit.txt
└── powerbi/                            # Power BI dashboard (in progress)
```

Note: raw and processed data files, and the generated SQLite database, are excluded from version control (see `.gitignore`) to keep the repository lightweight. Run the pipeline locally to regenerate them.

## Key Methodology Notes

- **Emissions formula:** `Emissions (kg CO2e) = (Total Weight Kg / 1000) × Distance Km × Emission Factor`
- **Transport mode assignment:** domestic shipments assumed road freight; international shipments assigned air or sea freight based on shipping speed tier.
- Several dimensions (supplier identity, product weight) are not present in the source dataset and were engineered using documented, realistic assumptions — see [docs/data_exploration_notes.md](docs/data_exploration_notes.md) for the full list.

## Running Locally

```bash
git clone https://github.com/pallavivirulkar/supplier-carbon-risk-observatory.git
cd supplier-carbon-risk-observatory
python3 -m venv venv
source venv/bin/activate
pip install -r requirements_streamlit.txt
# Re-run python/ scripts 01-20 in order against your own copy of the raw datasets
# to regenerate data/processed_dataco_clean.csv and sql/supplier_carbon_risk.db
streamlit run dashboard_app.py
```

## Status

- [x] Data cleaning & feature engineering
- [x] Emissions calculation
- [x] SQL aggregation & validation
- [x] Interactive Streamlit dashboard
- [ ] Power BI star schema, DAX measures, dashboard
- [ ] What-if scenario analysis
- [ ] Business insights write-up

## Author

Pallavi Virulkar
