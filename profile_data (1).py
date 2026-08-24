import pandas as pd
import numpy as np

def profile_data():
    print("=" * 60)
    print("DATA QUALITY PROFILE REPORT - RAW TRANSACTION DATA")
    print("=" * 60)
    
    # 1. Load Data
    try:
        df = pd.read_csv("raw_customer_transactions.csv")
    except Exception as e:
        print(f"Error loading raw_customer_transactions.csv: {e}")
        return
        
    print(f"Dataset Dimensions: {df.shape[0]} rows, {df.shape[1]} columns")
    print("\nColumn Information & Data Types:")
    print(df.dtypes)
    
    # 2. Duplicate Check
    exact_dups = df.duplicated().sum()
    print(f"\nExact Duplicate Rows: {exact_dups} ({exact_dups / len(df) * 100:.2f}%)")
    
    # Transaction ID uniqueness (excluding nulls)
    non_null_txns = df['transaction_id'].dropna()
    dup_txns = non_null_txns.duplicated().sum()
    print(f"Duplicate Transaction IDs (excluding nulls): {dup_txns}")
    
    # 3. Missing Values Analysis
    print("\nMissing Values Count & Percentage:")
    missing = df.isnull().sum()
    for col in df.columns:
        cnt = missing[col]
        pct = (cnt / len(df)) * 100
        print(f" - {col}: {cnt} missing ({pct:.2f}%)")
        
    # 4. Product Category Distribution (Spelling check)
    print("\nProduct Category Values and Frequency (Free-text inconsistencies):")
    cat_counts = df['product_category'].value_counts(dropna=False)
    for val, cnt in cat_counts.items():
        print(f" - {val}: {cnt}")
        
    # 5. Purchase Amount Analysis
    print("\nPurchase Amount Profiling:")
    # Check how many are strings vs numeric
    numeric_count = 0
    string_count = 0
    currency_count = 0
    comma_count = 0
    neg_count = 0
    outlier_high_count = 0
    
    for val in df['purchase_amount']:
        if pd.isnull(val):
            continue
        val_str = str(val).strip()
        if '$' in val_str:
            currency_count += 1
        if ',' in val_str:
            comma_count += 1
            
        try:
            # Attempt parsing
            clean_str = val_str.replace('$', '').replace(',', '')
            num_val = float(clean_str)
            numeric_count += 1
            if num_val < 0:
                neg_count += 1
            elif num_val >= 10000:
                outlier_high_count += 1
        except ValueError:
            string_count += 1
            
    print(f" - Parsable as numeric: {numeric_count}")
    print(f" - Contains currency symbol ($): {currency_count}")
    print(f" - Contains comma separation: {comma_count}")
    print(f" - Non-parsable strings: {string_count}")
    print(f" - Negative values (outliers): {neg_count}")
    print(f" - Extreme values (>= $10,000, outliers): {outlier_high_count}")
    
    # 6. Date Analysis (Formats & Outliers)
    print("\nDate Fields Analysis:")
    # We want to check date of birth anomalies
    dob_anomalies = 0
    dob_nulls = df['date_of_birth'].isnull().sum()
    future_dobs = 0
    unrealistic_old_dobs = 0
    
    # Check formats
    dob_formats = {}
    for val in df['date_of_birth']:
        if pd.isnull(val):
            continue
        val_str = str(val).strip()
        
        # Simple heuristic for format detection
        if '-' in val_str:
            parts = val_str.split('-')
            if len(parts) == 3:
                if len(parts[0]) == 4:
                    dob_formats['YYYY-MM-DD'] = dob_formats.get('YYYY-MM-DD', 0) + 1
                    year = int(parts[0])
                else:
                    dob_formats['DD-MM-YYYY'] = dob_formats.get('DD-MM-YYYY', 0) + 1
                    year = int(parts[2])
            else:
                dob_formats['Other/Invalid'] = dob_formats.get('Other/Invalid', 0) + 1
                continue
        elif '/' in val_str:
            parts = val_str.split('/')
            if len(parts) == 3:
                if len(parts[0]) == 4:
                    dob_formats['YYYY/MM/DD'] = dob_formats.get('YYYY/MM/DD', 0) + 1
                    year = int(parts[0])
                else:
                    dob_formats['MM/DD/YYYY or DD/MM/YYYY'] = dob_formats.get('MM/DD/YYYY or DD/MM/YYYY', 0) + 1
                    year = int(parts[2])
            else:
                dob_formats['Other/Invalid'] = dob_formats.get('Other/Invalid', 0) + 1
                continue
        else:
            dob_formats['Other/Invalid'] = dob_formats.get('Other/Invalid', 0) + 1
            continue
            
        if year > 2026:
            future_dobs += 1
        elif year < 1900:
            unrealistic_old_dobs += 1
            
    print(" - Date of Birth detected formats:")
    for fmt, count in dob_formats.items():
        print(f"   * {fmt}: {count}")
    print(f" - Future DOBs (> 2026): {future_dobs}")
    print(f" - Unreasonable old DOBs (< 1900): {unrealistic_old_dobs}")
    
    # 7. Customer Email validation
    print("\nCustomer Email Analysis:")
    invalid_emails = 0
    for val in df['customer_email']:
        if pd.isnull(val):
            continue
        val_str = str(val).strip()
        if '@' not in val_str:
            invalid_emails += 1
        else:
            parts = val_str.split('@')
            if len(parts) != 2 or '.' not in parts[1] or len(parts[1].split('.')[-1]) < 2:
                invalid_emails += 1
                
    print(f" - Malformed/Invalid Emails: {invalid_emails}")
    
    # 8. Shipping Country inconsistencies
    print("\nShipping Country Unique Values (First 15):")
    country_counts = df['shipping_country'].value_counts(dropna=False).head(15)
    for val, cnt in country_counts.items():
        print(f" - {val}: {cnt}")
        
    print("=" * 60)

if __name__ == "__main__":
    profile_data()
