-- Row count check
SELECT COUNT(*) AS total_rows FROM fact_orders;

-- Null check on key columns
SELECT
    SUM(CASE WHEN "Emissions Kg CO2e" IS NULL THEN 1 ELSE 0 END) AS null_emissions,
    SUM(CASE WHEN "Distance Km" IS NULL THEN 1 ELSE 0 END) AS null_distance,
    SUM(CASE WHEN "Transport Mode" IS NULL THEN 1 ELSE 0 END) AS null_transport_mode,
    SUM(CASE WHEN "Supplier Country ISO3" IS NULL THEN 1 ELSE 0 END) AS null_supplier_country
FROM fact_orders;

-- Negative or zero emissions check (should be zero rows)
SELECT COUNT(*) AS invalid_emissions
FROM fact_orders
WHERE "Emissions Kg CO2e" <= 0;

-- Emissions range check
SELECT
    MIN("Emissions Kg CO2e") AS min_emissions,
    MAX("Emissions Kg CO2e") AS max_emissions,
    ROUND(AVG("Emissions Kg CO2e"), 2) AS avg_emissions
FROM fact_orders;

-- Transport mode distribution
SELECT "Transport Mode", COUNT(*) AS order_count
FROM fact_orders
GROUP BY "Transport Mode"
ORDER BY order_count DESC;