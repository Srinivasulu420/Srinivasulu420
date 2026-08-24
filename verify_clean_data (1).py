import pandas as pd

def verify():
    print("=" * 60)
    print("VERIFYING CLEANED DATASET PROPERTIES")
    print("=" * 60)
    
    # 1. Load Data
    try:
        df = pd.read_csv("clean_customer_transactions.csv")
    except Exception as e:
        print(f"Error loading clean_customer_transactions.csv: {e}")
        return
        
    print(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    
    # 2. Check for missing values
    missing = df.isnull().sum()
    print("\nMissing Values Check (Should all be 0 or expected NaT):")
    for col, val in missing.items():
        print(f" - {col}: {val} nulls")
        
    # 3. Check for duplicates
    dups = df.duplicated(subset=['transaction_id']).sum()
    print(f"\nDuplicate Transaction IDs (Should be 0): {dups}")
    
    # 4. Check product categories
    print("\nStandardized Product Categories:")
    cats = df['product_category'].value_counts()
    for cat, cnt in cats.items():
        print(f" - {cat}: {cnt}")
        
    # 5. Check age stats
    print("\nCustomer Age Statistics:")
    print(df['customer_age'].describe())
    
    # Check if there are any outliers
    young_count = (df['customer_age'] < 0).sum()
    old_count = (df['customer_age'] > 120).sum()
    print(f" - Customers aged < 0 (Should be 0): {young_count}")
    print(f" - Customers aged > 120 (Should be 0): {old_count}")
    
    # 6. Check emails
    print("\nInvalid Email Check:")
    invalid_emails = df[~df['customer_email'].str.contains(r'^[^@]+@[^@]+\.[^@]+$', na=False)]
    print(f" - Invalid email count (Should be 0): {len(invalid_emails)}")
    if len(invalid_emails) > 0:
        print(invalid_emails['customer_email'])
        
    # 7. Check countries
    print("\nStandardized Country Counts:")
    countries = df['shipping_country'].value_counts()
    for country, cnt in countries.items():
        print(f" - {country}: {cnt}")
        
    print("=" * 60)

if __name__ == "__main__":
    verify()
