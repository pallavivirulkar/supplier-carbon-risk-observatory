# Data Exploration Notes

## DataCo Supply Chain Dataset
- Shape: 180,519 rows x 53 columns
- No duplicate rows
- Columns with meaningful missing data: Product Description (100% missing,
  drop), Order Zipcode (86% missing, drop - not needed for our grain)
- No "Supplier" column exists - will be engineered from Category + Region
  in Phase 4 (documented assumption)
- No product weight column - will be estimated per category in Phase 5
- Key columns for this project: Category Name, Order Country, Order Region,
  Market, Shipping Mode, Order Item Quantity, Order Item Total, Sales,
  order date (DateOrders)
- Columns to drop for privacy/relevance: Customer Email, Customer Password,
  Customer Fname/Lname, Customer Street, Product Image, Product Description

## DEFRA GHG Conversion Factors (Freighting goods sheet)
- Sheet has metadata/guidance rows before the data table
- Header row is at index 24 (0-indexed): Activity, Type, Unit, kg CO2e, ...
- Data starts at row 25
- "Activity" column only populated on the first row of each group
  (Vans, then further down: HGVs, Rail, Sea, Air) - needs forward-fill
- Multiple unit rows per vehicle class: tonne.km, km, miles - we will use
  tonne.km rows since our activity data is weight x distance
- Multiple fuel-type column blocks side by side (Diesel, Petrol, ...) -
  we will use an average/representative factor per mode (documented
  assumption)

## CEPII GeoDist (dist_cepii.xls)
- Shape: 50,176 rows x 14 columns
- One row = one country pair (iso_o, iso_d)
- Key columns: iso_o, iso_d, dist (great-circle distance in km)
- Covers ~224 countries, so self-pairs and all combinations are included