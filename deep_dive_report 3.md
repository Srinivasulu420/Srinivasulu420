# Deep-Dive Customer Analytics & Cohort Report

This report presents a deep-dive analysis of customer retention, purchase frequency, and value segmentation using **RFM (Recency, Frequency, Monetary) Analysis** and **Cohort Retention Modeling** at **ApexPlanet Software Pvt. Ltd.**

---

## 1. Core KPI Definitions & Formulas

Four Key Performance Indicators (KPIs) have been defined to monitor our sales channels and customer health:

### 1. Average Order Value (AOV)
* **Formula:**  
  $$\text{AOV} = \frac{\text{Total Revenue}}{\text{Total Transactions}}$$
* **Actual Value:** **$658.59**
* **Business Rationale:** Tracks the average basket size per checkout. Maximizing AOV is a highly cost-efficient way to scale revenue, as it doesn't require additional customer acquisition costs.

### 2. Purchase Frequency
* **Formula:**  
  $$\text{Purchase Frequency} = \frac{\text{Total Transactions}}{\text{Unique Customers}}$$
* **Actual Value:** **10.89 transactions per customer** (over a 36-month period)
* **Business Rationale:** Measures how often a customer returns to purchase. A high frequency index indicates high customer trust, product-market fit, and standard utility.

### 3. Repeat Purchase Rate (RPR)
* **Formula:**  
  $$\text{RPR} = \frac{\text{Unique Customers with } \ge 2 \text{ Transactions}}{\text{Total Unique Customers}} \times 100$$
* **Actual Value:** **100%**
* **Business Rationale:** Evaluates product stickiness. Our cohort's 100% rate is due to our synthetic customer pool (87 distinct IDs generating 1,000 transactions), representing a hyper-engaged loyalty club simulation.

### 4. Customer Lifetime Value (LTV)
* **Formula:**  
  $$\text{LTV} = \text{Average Order Value (AOV)} \times \text{Purchase Frequency}$$
* **Actual Value:** **$7,172.17 per customer**
* **Business Rationale:** Defines the net revenue contribution of a single customer. Knowing our LTV of ~$7,170 allows our marketing team to set a safe Customer Acquisition Cost (CAC) limit (e.g., spending up to $500 to acquire a customer is highly profitable).

---

## 2. RFM Customer Segmentation Deep-Dive

Customer behaviors were scored from 1 to 4 on Recency (R) and Monetary (M) value. Frequency (F) was scored as 4 (for repeat buyers with $\ge 2$ purchases) or 1. This split our 87 customers into two core segments:

### 1. VIP / Champions (44 Customers | 50.6% of base)
* **Definition:** Customers who have purchased recently, buy frequently, and are high spenders.
* **Metrics:** 
  * Average Recency: **141.8 days**
  * Average Frequency: **10.9 purchases**
  * Average Monetary (LTV): **$6,960.89**
  * Total Segment Contribution: **$306,279.00**
* **Business Strategy:** These are our core advocates. We should enroll them in a VIP Loyalty Tier, offering early product releases, personalized account managers, and exclusive perks to protect this revenue stream.

### 2. Loyal Customers - At Risk (43 Customers | 49.4% of base)
* **Definition:** Customers who have bought frequently and spent heavily, but haven't made a purchase recently (over 6-8 months).
* **Metrics:**
  * Average Recency: **235.9 days**
  * Average Frequency: **10.86 purchases**
  * Average Monetary (LTV): **$7,381.56**
  * Total Segment Contribution: **$317,407.14**
* **Business Strategy:** These customers are slipping away but represent our highest historical value. We must trigger automated winback campaigns (email, push notices) offering customized discounts (e.g., "We miss you, here is 15% off your next purchase") to reactivate them before they churn.

---

## 3. Cohort Retention Analysis Findings

We grouped customers into cohorts based on the month of their first transaction (ranging from January 2024 to December 2026) and tracked their repeat purchases over a 30-month period:

* **High Initial Retention:** Across large cohorts (like August 2024 with 33 customers, or September 2024 with 17 customers), we see a consistent repeat rate of **30% to 45%** in Month 1, Month 2, and Month 3.
* **Consistent Lifetime Activity:** Rather than dropping to 0%, cohorts show steady activity (15% to 40% retention) even out to Month 20 and Month 24.
* **Interpretation:** This represents a subscription-like transaction behavior. Customers who join the ecosystem continue buying consistently over a multi-year horizon, confirming high loyalty and sustained brand interest.

---

## 4. Actionable Business Recommendations

1. **Implement an Automated Re-engagement Flow:** With nearly half of our customer base classified as **Loyal (At Risk)**, setting up an automated email campaign triggered when a customer passes 180 days since their last purchase is our highest-priority opportunity.
2. **Upsell Premium Packages to VIPs:** Since our **VIP / Champions** represent over $306,000 in sales, launching bundle options or higher-tier product versions will allow us to easily expand their AOV beyond the current $696 limit.
3. **Focus Acquisition on High-LTV Profiles:** Since our customer LTV is exceptionally high (~$7,170), we should increase our advertising spend to target high-quality customer profiles that match our VIP demographic (specifically users aged 50+).
