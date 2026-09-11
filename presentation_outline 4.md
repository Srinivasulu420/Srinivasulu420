# Executive Presentation Storyboard & Slide Outline
**Task 4: Data Storytelling & Statistical Validation**  
**Presenter:** Shaik Abdul Khadar Sadiq | Data Analytics Intern  
**Company:** ApexPlanet Software Pvt. Ltd.  
**File Generated:** `final_presentation.pptx` (16:9 Widescreen)

---

## Slide-by-Slide Narrative & Content Breakdown

### Slide 1: Title Slide
* **Header:** APEXPLANET SOFTWARE PVT. LTD.
* **Title:** Data Analytics Capstone Portfolio: Insights, Strategy & Statistical Validation
* **Subtitle:** Comprehensive Internship Presentation | Tasks 1 - 4
* **Presenter:** Shaik Abdul Khadar Sadiq | Data Analytics Intern
* **Speaker Notes:** "Good morning everyone. I'm Shaik Abdul Khadar Sadiq. Today, I am excited to present the culmination of my Data Analytics Internship at ApexPlanet Software. Over the past several weeks, I took our raw transaction records through the complete data lifecycle: from cleaning and exploratory analysis, to customer segmentation, interactive dashboarding, and formal statistical hypothesis testing."

---

### Slide 2: Executive Summary (Data to Business Impact)
* **Pillar 1 - Immersion & Quality:** Transformed 1,008 messy transaction rows into 947 analysis-ready records with automated Pandas pipelines.
* **Pillar 2 - Business Intelligence:** Uncovered $623.6k revenue patterns, ranking Sports ($140.8k) as #1 and discovering older cohorts as peak spenders.
* **Pillar 3 - Statistical Rigor:** Validated customer RFM lifetime segments ($7.1k LTV) and statistically proved US-UK pricing parity via an independent T-test.
* **Speaker Notes:** "Our objective wasn't just to write code, but to solve operational challenges. We achieved three milestones: establishing automated data cleaning, discovering key revenue drivers, and applying statistical rigor to avoid costly business mistakes."

---

### Slide 3: Task 1 - Automated Data Cleaning Pipeline
* **Left Card (Anomalies):**
  * Duplicate Rows: 5 exact duplicates & duplicate transaction IDs.
  * Missing Values: 13 missing transaction and customer IDs violating primary key integrity.
  * Categorical Inconsistency: Free-text typos (e.g., 'electrnics', 'Elec', 'Home and Kitchen').
  * Corrupted Formats: Inconsistent date formats with birth year outliers (1845 and 2027).
  * Numerical Outliers: Negative amounts (-$150) and error placeholder values ($99,999).
* **Right Card (Pipeline Fixes):**
  * Primary key validation & hyphen stripping.
  * Standardized category mapping into 5 core departments.
  * Imputed missing amounts using category-level medians.
  * Parsed dates to ISO 8601 format (`YYYY-MM-DD`).
  * Engineered `customer_age` and `email_domain` features.
  * Output: 947 verified, zero-defect records.
* **Speaker Notes:** "In Task 1, we tackled the foundational reality of data: raw data is messy. I built an automated Pandas pipeline that handles nulls, repairs corrupted categories, imputes values mathematically, and outputs clean data that ensures downstream analyses are reliable."

---

### Slide 4: Task 2 - Sales Trends & Operational KPIs
* **Top Metric Cards:**
  * Total Revenue: **$623,686**
  * Total Orders: **947**
  * Average Order Value (AOV): **$658.59**
  * Active Time Horizon: **36 Months**
* **Monthly Sales Cycle Analysis:**
  * **Peak Seasons:** Transactions surge during late summer (August, 44 orders) and holiday shopping windows (October-November, 41-48 orders).
  * **Stable Revenue:** Active months maintain a consistent $25,000 to $32,000 baseline.
  * **Recommendation:** Replenish inventory 45 days ahead of August and Q4 holiday periods to prevent stockouts.
* **Speaker Notes:** "Looking at sales trends, our catalog generated over $623k with a healthy $658 average order size. Notice the seasonal cadence: revenue spikes in late summer and Q4. Supply chain planning should directly align with these windows."

---

### Slide 5: Task 2 - Product & Geographic Intelligence
* **Category Revenue Contribution:**
  1. Sports & Outdoors: $140,844 | AOV: $749.17 *(Top Grossing)*
  2. Apparel: $127,696 | AOV: $661.64 *(High Volume)*
  3. Home & Kitchen: $120,147 | AOV: $652.97 *(Steady Core)*
  4. Books: $119,730 | AOV: $633.50 *(Reliable Margin)*
  5. Electronics: $115,267 | AOV: $597.24 *(Lowest Basket)*
* **Geographic Distribution:**
  * **US & UK:** Account for >60% of total revenue ($198.9k and $180.5k).
  * **India & Germany:** Smaller order counts, but highest Average Order Value ($741.64 and $690.94).
  * **Takeaway:** While US/UK drive volume, international expansion into India and Germany delivers high-ticket transactions.
* **Speaker Notes:** "Our product lines show an interesting contrast: Sports & Outdoors is our biggest revenue winner, driven by high ticket prices. Geographically, while the US and UK give us volume, our Indian and German buyers have the highest average cart values."

---

### Slide 6: Task 3 - RFM Customer Value Segmentation
* **Segment 1: VIP / Champions (44 Customers | 50.6%):**
  * Revenue: **$306,279.00** | LTV: **$6,960.89**
  * High engagement: Avg recency 141.8 days, 10.9 repeat orders.
  * Strategy: Formalize an exclusive VIP loyalty club with early access perks.
* **Segment 2: Loyal Customers - At Risk (43 Customers | 49.4%):**
  * Revenue: **$317,407.14** | LTV: **$7,381.56** *(Highest historical value!)*
  * Inactive: Avg recency 235.9 days (>6-8 months dormant).
  * Strategy: Immediate winback campaign triggered at 180 days with a 15% incentive to prevent churn.
* **Speaker Notes:** "By running RFM segmentation, we made a critical discovery: half of our customer base are VIP champions who buy frequently, but the other half are heavy spenders who haven't bought in over 6 months. This $317k group is our biggest low-hanging fruit for automated re-engagement."

---

### Slide 7: Task 3 - Cohort Retention & Lifetime Value
* **Customer Lifetime Value (LTV):** **$7,172.17 per customer**  
  *(Formula: $658.59 AOV × 10.89 Repeat Orders)*
* **Cohort Decay Observations:**
  * Retention remains remarkably high at 30% - 45% in months 1 through 3.
  * Long-tail repeat activity sustains 15% - 40% re-purchases out to month 24.
  * Customer relationship behaves like an ongoing consumable lifecycle.
  * Marketing CAC ceiling can be set comfortably up to $500 per customer while securing >14x return.
* **Interactive Tooling:** Built `dashboard.html` using Plotly to visualize heatmaps and trendlines interactively.
* **Speaker Notes:** "Our cohort analysis proves that our customers don't abandon the brand after a single purchase. They return steadily over 24 months, driving an impressive $7,172 lifetime value. This gives our marketing team confidence to scale acquisition spend."

---

### Slide 8: Task 4 - Statistical Hypothesis Validation
* **Business Hypothesis:** Does customer spending behavior differ significantly between the United States and the United Kingdom?
  * $H_0: \mu_{US} = \mu_{UK}$ (No difference)
  * $H_1: \mu_{US} \neq \mu_{UK}$ (Statistically significant difference)
  * $\alpha = 0.05$ (Two-tailed independent T-test)
* **Statistical Output:**
  * US Mean: **$656.66** ($N = 303$) | UK Mean: **$626.97** ($N = 288$)
  * Observed Difference: **$29.70** (US higher by 4.7%)
  * Levene's Test: $p = 0.0552$ (Equal variance assumed)
  * T-Statistic: **0.7593** | Degrees of Freedom: **589.00**
  * P-Value: **0.4480** ($p \ge 0.05$)
  * 95% Confidence Interval: **[-$46.27, $105.66]**
* **Statistical & Business Decision:**
  * **FAIL TO REJECT $H_0$**.
  * The $29.70 difference is purely attributable to random sampling variance.
  * Strategic Decision: Harmonize catalog pricing, promotional calendars, and coupon structures across both markets, saving significant localization overhead.
* **Speaker Notes:** "Rather than guessing whether US and UK customers need separate pricing, we ran a two-sample T-test. The p-value was 0.448—far above our 0.05 threshold. This proves scientifically that US and UK spending is virtually identical, allowing us to deploy a unified international marketing strategy."

---

### Slide 9: Actionable Business Recommendations
1. **Automated Re-engagement Workflow:** Deploy triggered email sequences at 180 days of customer inactivity to recapture the 43 'Loyal - At Risk' accounts ($317k revenue opportunity).
2. **Global Pricing Harmonization:** Consolidate promotion calendars and pricing tiers across US and UK territories, eliminating redundant regional campaigns.
3. **Sports & Outdoors Cross-Selling:** Bundle high-AOV Sports & Outdoors products ($749 AOV) with Apparel and Home goods during checkout.
4. **Interactive Dashboard Adoption:** Equip operational team leads with the Plotly interactive dashboard (`dashboard.html`) for monthly KPI tracking.
* **Speaker Notes:** "To summarize, these four data-driven actions will directly expand revenue: reactivating dormant loyalists, simplifying our US/UK pricing strategy, driving cross-category bundles, and using our interactive dashboard for real-time tracking."

---

### Slide 10: Conclusion Slide
* **Title:** Thank You!
* **Summary of Milestones:**
  * Clean & Verified Dataset (947 records)
  * SQL Analytics & EDA Visualizations
  * RFM Customer Segmentation & Cohort Matrix
  * Interactive Plotly HTML Dashboard
  * Statistical Hypothesis Testing (Two-Sample T-Test)
* **Presenter:** Shaik Abdul Khadar Sadiq | Data Analytics Intern
* **Speaker Notes:** "Thank you for your time. This portfolio represents an end-to-end analytics workflow from raw data to statistical validation. I am happy to take any questions!"
