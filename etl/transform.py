def transform_data(df):
    # Add Revenue per Unit
    df['Revenue_per_Unit'] = df['Revenue'] / df['Quantity']

    # Weekday vs Weekend
    df['Day_Type'] = df['Weekday'].apply(lambda x: 'Weekend' if x in ['Saturday', 'Sunday'] else 'Weekday')

    # High Value Customer tag
    df['High_Value_Customer'] = df['Revenue'] > df['Revenue'].quantile(0.90)

    # Optional: Save customer-level summary
    customer_summary = df.groupby('CustomerID').agg({
        'InvoiceNo': 'nunique',
        'Revenue': 'sum',
        'Quantity': 'sum'
    }).rename(columns={
        'InvoiceNo': 'Total_Orders',
        'Revenue': 'Total_Revenue',
        'Quantity': 'Total_Units'
    }).reset_index()

    customer_summary.to_csv('data/processed/customer_summary.csv', index=False)

    print("Transformations applied and customer summary exported.")
    return df
