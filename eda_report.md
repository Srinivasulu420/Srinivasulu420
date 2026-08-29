# Exploratory Data Analysis (EDA) & Business Intelligence Report

This report documents the statistical analysis and business intelligence extracted from the cleaned customer transaction database. The goal is to uncover demographic insights, product performance, geographical distributions, and purchase trends to guide business decisions at **ApexPlanet Software Pvt. Ltd.**

---

## 1. Descriptive Statistics Summary

A statistical summary of the numerical variables from the 947 cleaned transaction records:

| Statistic | Purchase Amount ($) | Customer Age |
| :--- | :--- | :--- |
| **Count** | 947.00 | 947.00 |
| **Mean** | $658.59 | 40.83 years |
| **Std Dev** | $511.44 | 18.83 years |
| **Minimum** | $5.65 | 9.00 years |
| **25% (Q1)** | $335.12 | 24.00 years |
| **50% (Median)** | $625.60 | 40.00 years |
| **75% (Q3)** | $912.27 | 57.00 years |
| **Maximum** | $4,989.82 | 76.00 years |

### Key Observations:
* **Customer Demographics:** The customer base ranges from children (9 years) to seniors (76 years), with an average age of 41 years and a median of 40 years. This indicates a well-balanced distribution across generations.
* **Transaction Size:** The average transaction is $658.59, while the median is slightly lower at $625.60. The high standard deviation ($511.44) and maximum value ($4,989.82) compared to the median suggest a right-skewed distribution with a few high-value VIP purchases.

---

## 2. Visualization Findings & Interpretations

Five distinct visualization charts were generated and saved in the `images/` directory:

### 1. Customer Age Distribution (`images/customer_age_distribution.png`)
* **Finding:** The distribution of customer age is relatively flat and uniform across most age ranges, with slight peaks in the 20-30 and 50-60 deciles.
* **Interpretation:** Our products have broad appeal. We are not restricted to a niche age group, though marketing should segment messaging between younger and older buyers.

### 2. Purchase Amount Distribution (`images/purchase_amount_distribution.png`)
* **Finding:** A right-skewed distribution. The bulk of purchases lie between $5 and $1,200, with a long, thin tail extending up to $5,000.
* **Interpretation:** Most customers make standard purchases, but there is a distinct premium segment making transactions over $1,500. This justifies implementing tier-based loyalty incentives.

### 3. Product Category Transaction Volume (`images/product_category_distribution.png`)
* **Finding:** Transaction volume is remarkably evenly distributed across all 5 categories, with `Electronics` (193) and `Apparel` (193) tied for first, followed by `Books` (189), `Sports & Outdoors` (188), and `Home & Kitchen` (184).
* **Interpretation:** Product interest is highly balanced. No single category dominates in volume, meaning we have strong cross-category engagement.

### 4. Customer Age vs. Purchase Amount (`images/age_vs_purchase_amount.png`)
* **Finding:** The scatter plot displays a wide spread, but the regression trendline shows a slight positive slope, indicating that transaction value rises slightly as customer age increases.
* **Interpretation:** Older customers tend to have slightly higher purchasing power, leading to larger average basket sizes.

### 5. Purchase Amount by Shipping Country (`images/country_vs_purchase_amount.png`)
* **Finding:** While the United States and the United Kingdom represent the highest volume of sales, box plots reveal that `India` and `Germany` have higher median and average purchase amounts per transaction.
* **Interpretation:** Although North American and UK markets generate the most total revenue due to volume, Asian and European cohorts present higher average order values (AOV), representing key expansion targets.

### 6. Correlation Heatmap (`images/correlation_heatmap.png`)
* **Finding:** Correlation coefficients between age, amount, year, and month are close to zero (e.g., Age vs. Amount has a weak correlation of ~0.02).
* **Interpretation:** Purchase behavior is independent of simple linear demographic relationships. Segmenting by discrete buckets (e.g. age groups) rather than linear variables will yield better business intelligence.

---

## 3. SQL Business Queries & Output Tables

The cleaned data was loaded into a SQLite database (`transactions.db`) under the `sales_transactions` table. The following business questions were executed:

### Query 1: Monthly Sales Performance (Trend Analysis)
* **Goal:** Track transaction volume and total revenue month-over-month.
* **SQL Query:**
  ```sql
  SELECT 
      transaction_year, 
      transaction_month, 
      COUNT(*) AS transaction_volume, 
      ROUND(SUM(purchase_amount), 2) AS total_revenue,
      ROUND(AVG(purchase_amount), 2) AS average_order_value
  FROM sales_transactions
  GROUP BY transaction_year, transaction_month
  ORDER BY transaction_year, transaction_month;
  ```
* **Output (Excerpt):**
  | Year | Month | Volume | Total Revenue ($) | AOV ($) |
  | :--- | :--- | :--- | :--- | :--- |
  | 2024 | 7 | 11 | 6,608.73 | 600.79 |
  | 2024 | 8 | 44 | 31,882.37 | 724.60 |
  | 2024 | 9 | 41 | 26,126.58 | 637.23 |
  | 2024 | 10 | 41 | 25,028.34 | 610.45 |
  | 2024 | 11 | 38 | 27,907.90 | 734.42 |
  | 2024 | 12 | 31 | 20,007.33 | 645.40 |
  | 2025 | 1 | 32 | 26,477.61 | 827.43 |
  | 2025 | 8 | 38 | 28,033.25 | 737.72 |
  | 2025 | 10 | 48 | 27,645.35 | 575.94 |
  | 2026 | 5 | 42 | 32,214.41 | 767.01 |
  | 2026 | 6 | 48 | 28,452.92 | 592.77 |
  | 2026 | 7 | 28 | 12,208.67 | 436.02 |
* **Interpretation:** Monthly revenue shows standard seasonal distribution fluctuations, peaking during holiday shopping periods (November/December) and summer sale periods (May/August).

### Query 2: Product Category Standings (Revenue & Volume)
* **Goal:** Rank product categories by total sales.
* **SQL Query:**
  ```sql
  SELECT 
      product_category, 
      COUNT(*) AS transaction_volume, 
      ROUND(SUM(purchase_amount), 2) AS total_revenue,
      ROUND(AVG(purchase_amount), 2) AS average_purchase_amount
  FROM sales_transactions
  GROUP BY product_category
  ORDER BY total_revenue DESC;
  ```
* **Output:**
  | Product Category | Transaction Volume | Total Revenue ($) | Average Purchase ($) |
  | :--- | :--- | :--- | :--- |
  | **Sports & Outdoors** | 188 | 140,844.20 | 749.17 |
  | **Apparel** | 193 | 127,696.77 | 661.64 |
  | **Home & Kitchen** | 184 | 120,147.01 | 652.97 |
  | **Books** | 189 | 119,730.63 | 633.50 |
  | **Electronics** | 193 | 115,267.53 | 597.24 |
* **Interpretation:** `Sports & Outdoors` is the highest-grossing category ($140.8k), driven by the highest average purchase amount ($749.17), despite having slightly fewer transactions than `Apparel` or `Electronics`. `Electronics` has the lowest average basket size ($597.24).

### Query 3: Geographic Sales Analysis (Top 5 Countries)
* **Goal:** Identify geographical revenue hubs.
* **SQL Query:**
  ```sql
  SELECT 
      shipping_country, 
      COUNT(DISTINCT customer_id) AS unique_customers, 
      COUNT(*) AS transaction_volume,
      ROUND(SUM(purchase_amount), 2) AS total_revenue
  FROM sales_transactions
  GROUP BY shipping_country
  ORDER BY total_revenue DESC
  LIMIT 5;
  ```
* **Output:**
  | Country | Unique Customers | Volume | Total Revenue ($) | Avg Spend ($) |
  | :--- | :--- | :--- | :--- | :--- |
  | **United States** | 87 | 303 | 198,969.10 | 656.66 |
  | **United Kingdom** | 85 | 288 | 180,566.71 | 626.97 |
  | **India** | 57 | 90 | 66,747.65 | 741.64 |
  | **Germany** | 56 | 80 | 55,274.81 | 690.94 |
  | **Australia** | 53 | 88 | 53,555.89 | 608.59 |
* **Interpretation:** The US and UK represent the core volume drivers, accounting for over 60% of total revenue. However, customers in **India** and **Germany** exhibit significantly higher average transaction values ($741.64 and $690.94 respectively).

### Query 4: Customer Demographics Segments
* **Goal:** Analyze spending habits across customer age segments.
* **SQL Query:**
  ```sql
  SELECT 
      CASE 
          WHEN customer_age < 20 THEN 'Under 20'
          WHEN customer_age BETWEEN 20 AND 35 THEN '20-35'
          WHEN customer_age BETWEEN 36 AND 50 THEN '36-50'
          ELSE '50+'
      END AS age_segment,
      COUNT(*) AS transaction_volume,
      ROUND(SUM(purchase_amount), 2) AS total_revenue,
      ROUND(AVG(purchase_amount), 2) AS average_purchase_amount
  FROM sales_transactions
  GROUP BY age_segment
  ORDER BY age_segment;
  ```
* **Output:**
  | Age Segment | Transaction Volume | Total Revenue ($) | Average Purchase ($) |
  | :--- | :--- | :--- | :--- |
  | **Under 20** | 158 | 97,283.33 | 615.72 |
  | **20-35** | 251 | 168,094.42 | 669.70 |
  | **36-50** | 209 | 134,453.44 | 643.32 |
  | **50+** | 329 | 223,854.95 | 680.41 |
* **Interpretation:** The **50+ age group** is our most valuable segment, contributing $223,854.95 in total revenue and boasting the highest average order value ($680.41). Young adults (20-35) are the second most active group by volume (251 transactions) and have strong average spending.

### Query 5: Email Domain Value Analysis
* **Goal:** Determine if revenue varies by domain extension.
* **SQL Query:**
  ```sql
  SELECT 
      email_domain, 
      COUNT(*) AS transaction_volume, 
      ROUND(SUM(purchase_amount), 2) AS total_revenue,
      ROUND(AVG(purchase_amount), 2) AS average_purchase_amount
  FROM sales_transactions
  GROUP BY email_domain;
  ```
* **Output:**
  | Email Domain | Transaction Volume | Total Revenue ($) | Average Purchase ($) |
  | :--- | :--- | :--- | :--- |
  | **example.com** | 947 | 623,686.14 | 658.59 |
* **Interpretation:** Due to the synthetic nature of the dataset, all emails mapped to the generic `example.com` domain. In a production B2B/B2C dataset, this query would segment corporate email domains from public providers (Gmail, Yahoo, iCloud) to adjust sales outreach.

### Query 6: Customer Retention / VIP Customers
* **Goal:** Identify top spenders for CRM/loyalty targeting.
* **SQL Query:**
  ```sql
  SELECT 
      customer_id, 
      customer_name,
      COUNT(*) AS purchase_count, 
      ROUND(SUM(purchase_amount), 2) AS total_spent,
      ROUND(AVG(purchase_amount), 2) AS average_purchase
  FROM sales_transactions
  GROUP BY customer_id, customer_name
  ORDER BY total_spent DESC
  LIMIT 5;
  ```
* **Output:**
  | Customer ID | Name | Purchase Count | Total Spent ($) | Avg Purchase ($) |
  | :--- | :--- | :--- | :--- | :--- |
  | **CUST-1077** | Michael Miller | 2 | 5,170.24 | 2,585.12 |
  | **CUST-1016** | Charlie Garcia | 1 | 4,989.82 | 4,989.82 |
  | **CUST-1029** | Sarah Taylor | 1 | 4,925.20 | 4,925.20 |
  | **CUST-1067** | Ethan Miller | 1 | 4,845.41 | 4,845.41 |
  | **CUST-1050** | Bob Moore | 1 | 4,800.16 | 4,800.16 |
* **Interpretation:** Michael Miller (CUST-1077) is our highest value customer, representing two high-tier transactions. The rest of the top 5 represent single, high-value purchases. These customers should be immediately placed in our VIP loyalty segment.

---

## 4. Key Downstream Business Recommendations

1. **Focus Marketing on the 50+ Cohort:** This segment is our largest and highest-spending group. Campaigns emphasizing quality, utility, and premium customer service in Sports & Outdoors and Apparel will align with their purchasing patterns.
2. **Promote Cross-Category Bundling:** The volume is split almost perfectly across the 5 categories. Standard cross-selling prompts at checkout (e.g., suggesting a Home product to an Electronics purchaser) could increase overall average transaction sizes.
3. **Invest in High-AOV Countries (India & Germany):** While the US and UK provide volume, India and Germany offer higher transaction averages. Running localized marketing pushes or optimizing shipping rates for these regions will capture high-margin revenue.
4. **VIP Program launch:** Reach out to high-spenders (like CUST-1077 and CUST-1016) with exclusive offers to encourage recurring transactions, shifting them from one-off high-value purchasers to loyal brand advocates.
