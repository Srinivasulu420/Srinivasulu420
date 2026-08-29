# Executive Dashboard Mock-up & KPI Proposal
**Task 2: Exploratory Data Analysis & Business Intelligence**  
**Design Tool Recommendation:** Looker Studio, Power BI, or Tableau

This document outlines the layout, metrics, charts, and business rationale for a proposed **Sales & Demographics Analytics Dashboard** based on our cleaned dataset.

---

## 1. Dashboard Layout Grid (Visual Structure)

```text
+--------------------------------------------------------------------------------------------------+
|  [Logo] APEXPLANET SALES PERFORMANCE DASHBOARD                                                   |
|  Filters: [ Date Range ] | [ Product Category: All ] | [ Shipping Country: All ]                  |
+--------------------------------------------------------------------------------------------------+
|                                                                                                  |
|  +--------------------+  +--------------------+  +--------------------+  +--------------------+  |
|  |   TOTAL REVENUE    |  | TOTAL TRANSACTIONS |  |    AVERAGE ORDER   |  |  UNIQUE CUSTOMERS  |  |
|  |     $623,686       |  |        947         |  |      $658.59       |  |        480         |  |
|  |  [ +5.2% vs last ] |  |  [ +1.1% vs last ] |  |  [ +3.8% vs last ] |  |  [ +2.0% vs last ] |  |
|  +--------------------+  +--------------------+  +--------------------+  +--------------------+  |
|                                                                                                  |
|  +-------------------------------------------------+  +---------------------------------------+  |
|  | CHART A: MONTHLY SALES TREND (LINE/BAR)         |  | CHART B: REVENUE SHARE BY CATEGORY    |  |
|  |                                                 |  |          (DONUT CHART)                |  |
|  | Revenue ($)                                     |  |                                       |  |
|  |   ^                                             |  |         / Sports  \                   |  |
|  |   |     _/\_/\_                                 |  |        |  22.6%    |                  |  |
|  |   |  _/\       \                                |  |         \_________/                   |  |
|  |   +-------------------------------------> Time  |  |  [Apparel 20.5%]   [Home 19.3%]       |  |
|  |   (Monthly Revenue & Transaction Volume)        |  |  [Books 19.2%]     [Elec 18.5%]       |  |
|  +-------------------------------------------------+  +---------------------------------------+  |
|                                                                                                  |
|  +-------------------------------------------------+  +---------------------------------------+  |
|  | CHART C: TOP SHIPPING COUNTRIES (REVENUE)       |  | CHART D: AGE GROUP VS SPENDING (BAR)  |  |
|  |          (HORIZONTAL BAR CHART)                 |  |                                       |  |
|  |                                                 |  | Revenue ($)    Average Spend ($)      |  |
|  | USA  |===========================| $198.9k      |  |   ^                ^                  |  |
|  | UK   |=======================| $180.5k          |  |   |  $223.8k       |   $680.41        |  |
|  | IND  |=========| $66.7k                         |  |   |                |                  |  |
|  | GER  |=======| $55.2k                           |  |   +------------>   +------------>     |  |
|  | AUS  |=======| $53.5k                           |  |      50+              50+               |  |
|  +-------------------------------------------------+  +---------------------------------------+  |
|                                                                                                  |
|  +--------------------------------------------------------------------------------------------+  |
|  | DATA GRID: TOP 5 VIP CUSTOMERS                                                             |  |
|  | Customer ID | Name            | Transactions | Total Spent ($) | Avg Transaction ($)       |  |
|  | CUST-1077   | Michael Miller  | 2            | $5,170.24       | $2,585.12                 |  |
|  | CUST-1016   | Charlie Garcia  | 1            | $4,989.82       | $4,989.82                 |  |
|  | CUST-1029   | Sarah Taylor    | 1            | $4,925.20       | $4,925.20                 |  |
|  | CUST-1067   | Ethan Miller    | 1            | $4,845.41       | $4,845.41                 |  |
|  | CUST-1050   | Bob Moore       | 1            | $4,800.16       | $4,800.16                 |  |
|  +--------------------------------------------------------------------------------------------+  |
+--------------------------------------------------------------------------------------------------+
```

---

## 2. Metric Specifications (KPI Cards)

We propose four high-level summary boxes at the top of the dashboard. These represent the primary health indicators of our sales channels:

1. **Total Revenue**
   * *Formula:* `SUM(purchase_amount)`
   * *Value:* **$623,686.14**
   * *Business Purpose:* Tracks top-line sales growth and overall company financial scale.

2. **Total Transactions**
   * *Formula:* `COUNT(transaction_id)`
   * *Value:* **947**
   * *Business Purpose:* Shows volume of trade; helps monitor order processing capacity and platform activity.

3. **Average Order Value (AOV)**
   * *Formula:* `SUM(purchase_amount) / COUNT(transaction_id)`
   * *Value:* **$658.59**
   * *Business Purpose:* Measures the average transaction size. Expanding this metric directly boosts margins without acquiring new customers.

4. **Unique Customers**
   * *Formula:* `COUNT(DISTINCT customer_id)`
   * *Value:* **~480**
   * *Business Purpose:* Tracks customer acquisition and baseline user base. Combining this with transaction volume reveals repurchase frequency.

---

## 3. Chart Specifications & Business Logic

### Chart A: Monthly Sales Trend (Dual-Axis Line & Column)
* **X-Axis:** `transaction_year` & `transaction_month` (Chronological order)
* **Primary Y-Axis (Columns):** Total Revenue ($)
* **Secondary Y-Axis (Line):** Transaction Volume (count)
* **Actionable Insight:** Identifies sales seasonality. Helps executives plan marketing budget surges, inventory stocking levels, and promotions during key periods.

### Chart B: Category Contribution (Donut Chart)
* **Slices:** `product_category` (Electronics, Home & Kitchen, Apparel, Books, Sports & Outdoors)
* **Values:** Sum of `purchase_amount`
* **Actionable Insight:** Displays product inventory performance. Sports & Outdoors leads in revenue ($140.8k / 22.6%), while Electronics is lowest ($115.2k / 18.5%). This prompts reallocating inventory funds to higher-grossing lines.

### Chart C: Geographic Sales (Horizontal Bar Chart)
* **Y-Axis:** `shipping_country`
* **X-Axis:** Total Revenue ($)
* **Color Dimension:** Customer count
* **Actionable Insight:** Showcases regional hubs. US ($198.9k) and UK ($180.5k) are massive markets, but Germany and India show high AOVs. Helps direct international shipping subsidies and target region-specific ad spend.

### Chart D: Customer Demographic Performance (Double-Column Chart)
* **X-Axis:** `age_segment` (<20, 20-35, 36-50, 50+)
* **Column 1:** Total Revenue ($)
* **Column 2:** Average Purchase Amount ($)
* **Actionable Insight:** Uncovers user-persona value. The 50+ age cohort is our highest spender. Marketing can create campaigns targeting these older demographic buyers with premium packages.

---

## 4. Interactive Filters & User Controls

To allow department leaders to customize their views, we propose adding the following interactive controls at the top right of the dashboard:
* **Date Range Picker:** Toggle analysis periods (e.g., Year-to-Date, Q4, or last 12 months).
* **Category Dropdown:** Drill down to see if geographical trends change when looking strictly at `Electronics` or `Books`.
* **Shipping Country Selector:** Filter down to a specific country (e.g., India) to see their monthly revenue seasonality and product preferences.
* **Age Group Filter:** Filter the view to understand what product categories our younger demographic (Under 20) are buying most.
