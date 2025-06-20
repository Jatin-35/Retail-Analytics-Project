-- 1. Total Revenue by Category
SELECT Category, ROUND(SUM(Revenue), 2) AS Total_Revenue
FROM retail_cleaned
GROUP BY Category
ORDER BY Total_Revenue DESC;

-- 2. Average Profit Margin by Sub-Category
SELECT "Sub-Category", ROUND(AVG(Profit_Margin), 2) AS Avg_Profit_Margin
FROM retail_cleaned
GROUP BY "Sub-Category"
ORDER BY Avg_Profit_Margin DESC;

-- 3. Top 10 Products by Total Sales
SELECT Description, SUM(Revenue) AS Total_Revenue
FROM retail_cleaned
GROUP BY Description
ORDER BY Total_Revenue DESC
LIMIT 10;

-- 4. Slow-Moving Products (High quantity, low sales)
SELECT Description, SUM(Quantity) AS Total_Qty, SUM(Revenue) AS Total_Rev
FROM retail_cleaned
GROUP BY Description
HAVING Total_Qty > (SELECT AVG(Quantity) FROM retail_cleaned)
   AND Total_Rev < (SELECT AVG(Revenue) FROM retail_cleaned)
ORDER BY Total_Rev ASC;

-- 5. Monthly Sales Trends
SELECT Year, Month, ROUND(SUM(Revenue), 2) AS Monthly_Revenue
FROM retail_cleaned
GROUP BY Year, Month
ORDER BY Year, Month;

-- 6. Country-wise Revenue
SELECT Country, ROUND(SUM(Revenue), 2) AS Country_Revenue
FROM retail_cleaned
GROUP BY Country
ORDER BY Country_Revenue DESC;
