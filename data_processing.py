import pandas as pd
import os

# 1. List the paths to all 3 input CSV files
file_paths = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

# Create an empty list to store the cleaned datasets
cleaned_datasets = []

# 2. Process each file one by one
for path in file_paths:
    # Read the data file into a Pandas DataFrame (like an automated spreadsheet)
    df = pd.read_csv(path)
    
    # Filter: Keep ONLY rows where the product column equals "Pink Morsel"
    df = df[df["product"] == "pink morsel"]
    
    # Calculate Sales: Multiply quantity by price (strip the '$' sign from price first)
    df["price"] = df["price"].astype(str).str.replace("$", "", regex=False).astype(float)
    df["sales"] = df["quantity"] * df["price"]
    
    # Clean up fields: Keep only the 3 requested columns (sales, date, region)
    df = df[["sales", "date", "region"]]
    
    # Add this cleaned file data to our main list
    cleaned_datasets.append(df)

# 3. Merge all three cleaned dataframes into a single combined file
combined_df = pd.concat(cleaned_datasets, ignore_index=True)

# 4. Save the final formatted file as 'formatted_output.csv'
combined_df.to_csv("formatted_output.csv", index=False)

print("Successfully cleaned data and created formatted_output.csv!")
