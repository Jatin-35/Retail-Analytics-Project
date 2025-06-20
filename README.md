# 🛍️ Retail Business Performance & Profitability Analysis

This is a real-world, end-to-end **Retail Data Analytics Project** built to demonstrate skills in ETL pipelines, data exploration, SQL-based storytelling, interactive dashboards using Tableau, and machine learning-based revenue prediction.

---

## 📁 Project Structure

```
Retail-Analytics-Project/
├── dashboard/
│   └── retail_dashboard.twb               # Tableau dashboard
│
├── data/
│   ├── raw/
│   │   ├── data.csv                       # Raw input data
│   │   └── online_retail_II.xlsx         # Original dataset
│   │
│   ├── processed/
│   │   ├── cleaned_retail_data.csv       # Final cleaned dataset
│   │   └── customer_summary.csv          # Extra processed insight
│   │
│   └── insights/
│       ├── country_wise_revenue.csv
│       ├── monthly_sales_trends.csv
│       ├── slow_moving_products.csv
│       └── top_10_products_by_sales.csv
│
├── database/
│   └── retail_data.db                    # SQLite database with cleaned data
│
├── etl/
│   ├── extract.py                        # Extract raw data
│   ├── transform.py                      # Data cleaning and feature engineering
│   └── load.py                           # Load into SQLite
│
├── notebooks/
│   ├── 00_preprocessing_insights.ipynb   # Initial analysis
│   ├── 01_data_cleaning.ipynb            # Cleaning & feature creation
│   └── 02_revenue_prediction.ipynb       # Regression model notebook
│
├── scripts/
│   ├── run_sql_queries.py                # Execute SQL & export insights
│   └── retail_queries.sql                # SQL script for insights
│
├── visualizations/
│   ├── boxplot_CustomerID.png
│   ├── boxplot_Quantity.png
│   ├── boxplot_UnitPrice.png
│   ├── missing_matrix.png
│   └── numeric_correlation.png
│
├── run_pipeline.py                       # Main entry for full ETL pipeline
├── requirements.txt                      # Python dependency list
├── .gitignore
└── README.md                             # Project documentation
```
---

## 💡 Key Features

- ✅ **ETL Pipeline**: Cleans raw CSV, creates new features like `Revenue`, stores data in SQLite
- ✅ **SQL Analysis**: Insightful queries for sales trends, top products, slow movers, and regional performance
- ✅ **Interactive Tableau Dashboard**: Filters, KPIs, time trends, and product/category visualizations
- ✅ **Machine Learning Model**: Predicts `Revenue` using `Quantity`, `UnitPrice`, and `Country` via regression
- ✅ **Portfolio-Ready**: Fully structured for GitHub and resumes

---

## 📊 Tableau Dashboard Preview

![Dashboard Preview](visualizations/retail_dashboard_overview.png)

> Includes:
> - KPI Cards: Total Revenue, Quantity Sold, Countries Active  
> - Line Chart: Monthly Revenue Trend  
> - Bar Charts: Top-Selling Products, Country Revenue  
> - Scatter Plot: Slow-Moving Products  
> - Filters: Interactive filtering by Country and Month

---

## 🤖 Revenue Prediction Model

> Located in: `notebooks/03_revenue_prediction.ipynb`

### 🔍 Algorithms Used:
- Linear Regression
- Random Forest Regressor

### 📈 Metrics:
- R² Score
- MAE (Mean Absolute Error)
- RMSE (Root Mean Square Error)

### 📊 Output:
- Actual vs Predicted Revenue (scatter plot)
- Performance metrics comparison

---

## 🛠️ Tech Stack

| Tool / Library        | Purpose                        |
|----------------------|--------------------------------|
| Python (Pandas, NumPy) | Data cleaning, preprocessing   |
| SQLite + SQLAlchemy  | ETL database storage & querying |
| Tableau Public       | Dashboard & storytelling        |
| scikit-learn         | ML model training & evaluation  |
| Matplotlib / Seaborn | Visualization (EDA, prediction) |

---

## 🚀 Getting Started

```bash
# Step 1: Install requirements
pip install pandas scikit-learn matplotlib seaborn sqlalchemy jupyter

# Step 2: Run ETL pipeline
python scripts/etl_pipeline.py

# Step 3: Run SQL insights generator
python scripts/run_sql_queries.py

# Step 4: Launch the ML notebook
jupyter notebook notebooks/03_revenue_prediction.ipynb
```

--> Optional: Open dashboard/retail_dashboard.twb in Tableau Public to explore the interactive dashboard.

---
## 🧠 About the Author

👨‍💻 Jatin Jasrotia

Final year Computer Science student, passionate about data analytics, ML, and building impactful dashboards.
Project built to showcase strong analytical thinking and industry-readiness for internships.
