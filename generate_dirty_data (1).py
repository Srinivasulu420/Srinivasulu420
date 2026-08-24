import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Generate synthetic customer transaction data
n_records = 1000

# Base pools
first_names = ["John", "Jane", "Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ian", "Julia", "Kevin", "Laura", "Michael", "Sarah"]
last_names = ["Smith", "Doe", "Johnson", "Brown", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson", "Martinez", "Anderson", "Taylor", "Thomas", "Hernandez", "Moore", "Martin"]
categories = ["Electronics", "Home & Kitchen", "Apparel", "Books", "Sports & Outdoors"]
typos_categories = {
    "Electronics": ["electrnics", "ELECTronics", "Elec", "Electronics"],
    "Home & Kitchen": ["home", "Home & Kitchen", "Home and Kitchen", "Kitchen"],
    "Apparel": ["apparel", "aparel", "Clothing", "Apparel"],
    "Books": ["books", "Books", "Bks"],
    "Sports & Outdoors": ["sports", "Sports & Outdoors", "Sports", "Outdoors"]
}
countries = ["United States", "USA", "US", "United Kingdom", "UK", "U.K.", "Canada", "Germany", "India", "Australia"]

# Arrays to populate
txn_ids = []
cust_ids = []
names = []
emails = []
dobs = []
txn_dates = []
product_cats = []
amounts = []
shipping_countries = []

for i in range(n_records):
    # Transaction ID (most are TXNxxxxx, some malformed, some null, some duplicates)
    if i % 100 == 0:
        txn_ids.append(None)
    elif i % 150 == 0:
        txn_ids.append(f"txn-{10000 + i}")
    else:
        txn_ids.append(f"TXN{10000 + i}")
        
    # Customer ID
    if i % 80 == 0:
        cust_ids.append(None)
    else:
        cust_ids.append(f"CUST-{1000 + (i % 87)}")
        
    # Names with varying casing, trailing spaces, or nulls
    first = random.choice(first_names)
    last = random.choice(last_names)
    name = f"{first} {last}"
    if i % 12 == 0:
        name = name.upper()
    elif i % 15 == 0:
        name = name.lower()
    elif i % 18 == 0:
        name = f"  {name}  "
    elif i % 95 == 0:
        name = None
    names.append(name)
    
    # Emails - some invalid, some null, some uppercase
    if name is None:
        emails.append(None)
    elif i % 110 == 0:
        emails.append(None)
    elif i % 70 == 0:
        emails.append(f"{first.lower()}.{last.lower()}@com")  # Malformed
    elif i % 60 == 0:
        emails.append(f"{first.upper()}.{last.upper()}@EXAMPLE.COM")
    else:
        emails.append(f"{first.lower()}.{last.lower()}@example.com")
        
    # Date of Birth - inconsistent formats
    # Let's generate a birth year between 1950 and 2015
    birth_year = random.randint(1950, 2015)
    # Inject outlier age (too young or future)
    if i == 500:
        birth_year = 2027  # Future birth date (outlier)
    elif i == 600:
        birth_year = 1845  # Too old (outlier)
        
    birth_month = random.randint(1, 12)
    birth_day = random.randint(1, 28)
    dob_dt = datetime(birth_year, birth_month, birth_day)
    
    if i % 10 == 0:
        dobs.append(dob_dt.strftime("%d-%m-%Y"))
    elif i % 13 == 0:
        dobs.append(dob_dt.strftime("%m/%d/%Y"))
    elif i % 100 == 0:
        dobs.append(None)
    else:
        dobs.append(dob_dt.strftime("%Y-%m-%d"))
        
    # Transaction Date - inconsistent formats, occurred in last 2 years (relative to fixed current year 2026)
    days_ago = random.randint(0, 730)
    txn_dt = datetime(2026, 7, 19) - timedelta(days=days_ago)
    if i % 8 == 0:
        txn_dates.append(txn_dt.strftime("%d/%m/%Y"))
    elif i % 11 == 0:
        txn_dates.append(txn_dt.strftime("%Y/%m/%d"))
    elif i % 90 == 0:
        txn_dates.append(None)
    else:
        txn_dates.append(txn_dt.strftime("%Y-%m-%d"))
        
    # Product Category with spelling typos/inconsistencies
    cat = random.choice(categories)
    product_cats.append(random.choice(typos_categories[cat]))
    
    # Purchase Amount - outliers, symbols, formats, missing
    if i % 95 == 0:
        amounts.append(None)
    elif i == 250:
        amounts.append(-150.00)  # Negative amount (outlier)
    elif i == 450:
        amounts.append(99999.00)  # Extremely high amount (outlier)
    elif i % 15 == 0:
        val = round(random.uniform(5.0, 1500.0), 2)
        amounts.append(f"${val}")  # Currency symbol
    elif i % 25 == 0:
        val = round(random.uniform(1000.0, 5000.0), 2)
        amounts.append(f"{val:,.2f}")  # Comma formatting
    else:
        amounts.append(round(random.uniform(5.0, 1200.0), 2))
        
    # Shipping Address Country
    if i % 85 == 0:
        shipping_countries.append(None)
    else:
        shipping_countries.append(random.choice(countries))

# Build dataframe
df = pd.DataFrame({
    "transaction_id": txn_ids,
    "customer_id": cust_ids,
    "customer_name": names,
    "customer_email": emails,
    "date_of_birth": dobs,
    "transaction_date": txn_dates,
    "product_category": product_cats,
    "purchase_amount": amounts,
    "shipping_country": shipping_countries
})

# Inject duplicate rows
# Exact duplicates
dup_indices = [10, 50, 100, 200, 300]
df_dups = df.iloc[dup_indices].copy()
# Add duplicate transaction_id but other details might differ slightly (partial duplicates)
df_partial_dups = df.iloc[[15, 65, 115]].copy()
df_partial_dups["purchase_amount"] = 999.99  # change amount slightly

df = pd.concat([df, df_dups, df_partial_dups], ignore_index=True)

# Shuffle the dataframe to distribute duplicates
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save to CSV
df.to_csv("raw_customer_transactions.csv", index=False)
print("raw_customer_transactions.csv generated successfully! Shape:", df.shape)
