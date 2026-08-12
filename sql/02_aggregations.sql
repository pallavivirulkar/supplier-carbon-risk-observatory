-- Supplier-wise total emissions
SELECT
    "Supplier Name",
    "Supplier Country ISO3",
    COUNT(*) AS order_count,
    ROUND(SUM("Emissions Kg CO2e"), 2) AS total_emissions_kg,
    ROUND(AVG("Emissions Kg CO2e"), 2) AS avg_emissions_per_order
FROM fact_orders
GROUP BY "Supplier Name", "Supplier Country ISO3"
ORDER BY total_emissions_kg DESC;

-- Category-wise total emissions
SELECT
    "Category Group",
    COUNT(*) AS order_count,
    ROUND(SUM("Emissions Kg CO2e"), 2) AS total_emissions_kg,
    ROUND(AVG("Emissions Kg CO2e"), 2) AS avg_emissions_per_order
FROM fact_orders
GROUP BY "Category Group"
ORDER BY total_emissions_kg DESC;

-- Country-wise total emissions (destination country)
SELECT
    "Order Country ISO3",
    COUNT(*) AS order_count,
    ROUND(SUM("Emissions Kg CO2e"), 2) AS total_emissions_kg,
    ROUND(AVG("Emissions Kg CO2e"), 2) AS avg_emissions_per_order
FROM fact_orders
GROUP BY "Order Country ISO3"
ORDER BY total_emissions_kg DESC
LIMIT 15;