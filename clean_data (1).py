import pandas as pd
import numpy as np
import re

def clean_dataset():
    print("=" * 60)
    print("STARTING DATA CLEANING & TRANSFORMATION PIPELINE")
    print("=" * 60)
    
    # 1. Load Data
    df = pd.read_csv("raw_customer_transactions.csv")
    initial_rows = len(df)
    print(f"Initial row count: {initial_rows}")
    
    # 2. Duplicate Removal
    # Drop exact duplicates
    df = df.drop_duplicates()
    after_exact_dups = len(df)
    print(f" - Removed {initial_rows - after_exact_dups} exact duplicate rows.")
    
    # 3. Clean and Standardize Primary Keys & Identifiers
    # Trim and uppercase transaction_id
    df['transaction_id'] = df['transaction_id'].astype(str).str.strip().str.upper()
    # Remove hyphens in transaction_id (e.g. txn-10023 -> TXN10023)
    df['transaction_id'] = df['transaction_id'].str.replace('-', '', regex=False)
    
    # Drop rows where transaction_id or customer_id is null/NaN
    # In Pandas, reading 'None' or empty strings results in NaN, or string 'NAN' / 'NONE' if cast to str.
    df = df[~df['transaction_id'].isin(['NAN', 'NONE', '', 'NAT'])]
    df = df.dropna(subset=['transaction_id'])
    
    # Clean customer_id
    df['customer_id'] = df['customer_id'].astype(str).str.strip().str.upper()
    df = df[~df['customer_id'].isin(['NAN', 'NONE', '', 'NAT'])]
    df = df.dropna(subset=['customer_id'])
    
    # Drop duplicate transaction_ids (keep the first occurrence)
    dup_txns = df.duplicated(subset=['transaction_id']).sum()
    df = df.drop_duplicates(subset=['transaction_id'], keep='first')
    print(f" - Standardized transaction IDs and removed {dup_txns} duplicate transaction records.")
    
    # 4. Clean Customer Names
    df['customer_name'] = df['customer_name'].astype(str).str.strip()
    # Replace null-like strings with 'Unknown Customer'
    df.loc[df['customer_name'].isin(['NAN', 'NONE', '', 'nan']), 'customer_name'] = 'Unknown Customer'
    # Convert to Title Case
    df['customer_name'] = df['customer_name'].str.title()
    print(" - Standardized customer names to Title Case and handled missing values.")
    
    # 5. Clean and Validate Emails
    # Convert to lowercase and trim
    df['customer_email'] = df['customer_email'].astype(str).str.strip().str.lower()
    
    # Define simple email validation function
    def is_valid_email(email):
        if pd.isnull(email) or email in ['nan', 'none', '']:
            return False
        # Regex for valid email
        pattern = r'^[^@]+@[^@]+\.[^@]+$'
        return bool(re.match(pattern, email))
        
    # Mark invalid emails as NaN
    df['is_email_valid'] = df['customer_email'].apply(is_valid_email)
    invalid_email_count = (~df['is_email_valid']).sum()
    
    # Drop records with invalid or missing emails
    df = df[df['is_email_valid']].drop(columns=['is_email_valid'])
    print(f" - Validated emails: dropped {invalid_email_count} rows with malformed or missing emails.")
    
    # 6. Parse and Clean Dates
    # Parse date_of_birth and transaction_date (using format='mixed' for inconsistent styles)
    df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], format='mixed', errors='coerce')
    df['transaction_date'] = pd.to_datetime(df['transaction_date'], format='mixed', errors='coerce')
    
    # Check for null transaction_dates and drop them
    null_txn_dates = df['transaction_date'].isnull().sum()
    df = df.dropna(subset=['transaction_date'])
    print(f" - Standardized transaction dates to YYYY-MM-DD. Dropped {null_txn_dates} rows with missing transaction dates.")
    
    # Handle Outliers in Date of Birth (birth year < 1920 or birth year > 2026)
    dob_outliers = ((df['date_of_birth'].dt.year < 1920) | (df['date_of_birth'].dt.year > 2026))
    dob_outlier_count = dob_outliers.sum()
    # Replace outliers with NaT, and then drop them to maintain cohort analysis integrity
    df.loc[dob_outliers, 'date_of_birth'] = pd.NaT
    df = df.dropna(subset=['date_of_birth'])
    print(f" - Handled Date of Birth outliers: removed {dob_outlier_count} records with invalid birth years (< 1920 or > 2026).")
    
    # 7. Standardize Product Categories (Categorical text mapping)
    category_mapping = {
        'electrnics': 'Electronics',
        'electronics': 'Electronics',
        'electronics': 'Electronics',
        'electronics': 'Electronics',
        'electronics': 'Electronics',
        'electronics': 'Electronics',
        'electrnics': 'Electronics',
        'electronics': 'Electronics',
        'electronics': 'Electronics',
    }
    # Let's write a robust cleaning function for category mapping
    def map_category(cat):
        if pd.isnull(cat):
            return "Unknown"
        cat_lower = str(cat).lower().strip()
        if 'elec' in cat_lower or 'tron' in cat_lower:
            return 'Electronics'
        elif 'home' in cat_lower or 'kitchen' in cat_lower:
            return 'Home & Kitchen'
        elif 'apparel' in cat_lower or 'cloth' in cat_lower or 'aparel' in cat_lower:
            return 'Apparel'
        elif 'book' in cat_lower or 'bks' in cat_lower:
            return 'Books'
        elif 'sport' in cat_lower or 'outdoor' in cat_lower:
            return 'Sports & Outdoors'
        else:
            return 'Other'
            
    df['product_category'] = df['product_category'].apply(map_category).astype('category')
    print(" - Standardized product categories and mapped free-text inconsistencies to 5 standardized values.")
    
    # 8. Clean Purchase Amount (Remove $, commas, handle nulls and numerical outliers)
    def clean_amount(amount):
        if pd.isnull(amount):
            return np.nan
        amount_str = str(amount).strip().replace('$', '').replace(',', '')
        try:
            return float(amount_str)
        except ValueError:
            return np.nan
            
    df['purchase_amount'] = df['purchase_amount'].apply(clean_amount)
    
    # Impute missing purchase amounts with the median amount of their respective product category
    category_medians = df.groupby('product_category', observed=False)['purchase_amount'].transform('median')
    null_amounts_before = df['purchase_amount'].isnull().sum()
    df['purchase_amount'] = df['purchase_amount'].fillna(category_medians)
    print(f" - Standardized purchase amounts: imputed {null_amounts_before} missing values with product category medians.")
    
    # Outlier handling for purchase amount: drop negative amounts and values >= 10,000 (system errors)
    amount_outliers = (df['purchase_amount'] < 0) | (df['purchase_amount'] >= 10000)
    outlier_amount_count = amount_outliers.sum()
    df = df[~amount_outliers]
    print(f" - Filtered out {outlier_amount_count} purchase amount outliers (negative values and system error values >= $10,000).")
    
    # 9. Clean Shipping Country
    country_mapping = {
        'US': 'United States',
        'USA': 'United States',
        'UNITED STATES': 'United States',
        'US.': 'United States',
        'UK': 'United Kingdom',
        'U.K.': 'United Kingdom',
        'UNITED KINGDOM': 'United Kingdom',
    }
    def standardize_country(country):
        if pd.isnull(country) or str(country).strip().lower() in ['nan', 'none', '']:
            return 'Unknown'
        country_clean = str(country).strip()
        if country_clean in country_mapping:
            return country_mapping[country_clean]
        return country_clean.title()
        
    df['shipping_country'] = df['shipping_country'].apply(standardize_country)
    print(" - Standardized country codes (e.g. USA/US -> United States, UK/U.K. -> United Kingdom).")
    
    # 10. Feature Engineering
    # Extract transaction year and month
    df['transaction_year'] = df['transaction_date'].dt.year.astype('int64')
    df['transaction_month'] = df['transaction_date'].dt.month.astype('int64')
    
    # Calculate customer age at the time of the transaction
    df['customer_age'] = (df['transaction_year'] - df['date_of_birth'].dt.year).astype('int64')
    
    # Extract email domain
    df['email_domain'] = df['customer_email'].apply(lambda x: x.split('@')[1] if '@' in str(x) else 'unknown')
    print(" - Engineered new features: 'customer_age', 'email_domain', 'transaction_year', and 'transaction_month'.")
    
    # Final data type validation
    df['customer_name'] = df['customer_name'].astype(str)
    df['customer_email'] = df['customer_email'].astype(str)
    df['shipping_country'] = df['shipping_country'].astype(str)
    df['purchase_amount'] = df['purchase_amount'].astype(float)
    
    # 11. Save Clean Dataset
    df.to_csv("clean_customer_transactions.csv", index=False)
    final_rows = len(df)
    
    print("=" * 60)
    print("DATA CLEANING COMPLETE")
    print(f"Final row count: {final_rows} (Total rows removed: {initial_rows - final_rows})")
    print(f"Cleaned dataset saved to 'clean_customer_transactions.csv'")
    print("=" * 60)

if __name__ == "__main__":
    clean_dataset()
