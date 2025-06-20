from sqlalchemy import create_engine
import pandas as pd
from pathlib import Path

# Set up database URI for SQLAlchemy
db_path = 'sqlite:///database/retail_data.db'
engine = create_engine(db_path)

# Ensure output directory exists
output_path = Path("data/insights")
output_path.mkdir(parents=True, exist_ok=True)

# Define SQL queries (only if columns are confirmed in your dataset)
queries = {
    "top_10_products_by_sales": """
        SELECT Description, SUM(Revenue) AS Total_Revenue
        FROM retail_cleaned
        GROUP BY Description
        ORDER BY Total_Revenue DESC
        LIMIT 10;
    """,
    "slow_moving_products": """
        SELECT Description, SUM(Quantity) AS Total_Qty, SUM(Revenue) AS Total_Rev
        FROM retail_cleaned
        GROUP BY Description
        HAVING Total_Qty > (SELECT AVG(Quantity) FROM retail_cleaned)
           AND Total_Rev < (SELECT AVG(Revenue) FROM retail_cleaned)
        ORDER BY Total_Rev ASC;
    """,
    "monthly_sales_trends": """
        SELECT Year, Month, ROUND(SUM(Revenue), 2) AS Monthly_Revenue
        FROM retail_cleaned
        GROUP BY Year, Month
        ORDER BY Year, Month;
    """,
    "country_wise_revenue": """
        SELECT Country, ROUND(SUM(Revenue), 2) AS Country_Revenue
        FROM retail_cleaned
        GROUP BY Country
        ORDER BY Country_Revenue DESC;
    """
    # Avoiding Category/Sub-Category/Profit_Margin unless verified
}

# Run queries and export results
for name, query in queries.items():
    try:
        df = pd.read_sql(query, engine)
        df.to_csv(output_path / f"{name}.csv", index=False)
        print(f"Exported: {name}.csv")
    except Exception as e:
        print(f"Failed to export {name}: {e}")
