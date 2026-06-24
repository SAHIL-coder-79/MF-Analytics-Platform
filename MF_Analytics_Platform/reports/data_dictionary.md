# Mutual Fund Analytics Platform - Data Dictionary

## Project Overview

This document describes the datasets, tables, columns, data types, and business definitions used in the Mutual Fund Analytics Platform.

**Data Sources**
- AMFI India
- mfapi.in
- Public Mutual Fund Datasets

---

# 1. dim_fund

Source: 01_fund_master.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Unique AMFI Scheme Code |
| fund_house | TEXT | Mutual Fund Company |
| scheme_name | TEXT | Scheme Name |
| category | TEXT | Fund Category |
| sub_category | TEXT | Scheme Type |
| plan | TEXT | Direct / Regular |
| launch_date | DATE | Launch Date |
| benchmark | TEXT | Benchmark Index |
| expense_ratio_pct | REAL | Expense Ratio (%) |
| exit_load_pct | REAL | Exit Load (%) |
| min_sip_amount | INTEGER | Minimum SIP Amount |
| min_lumpsum_amount | INTEGER | Minimum Lump Sum Amount |
| fund_manager | TEXT | Fund Manager |
| risk_category | TEXT | Risk Category |
| sebi_category_code | TEXT | SEBI Category Code |

---

# 2. fact_nav

Source: 02_nav_history.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Scheme Code |
| date | DATE | NAV Date |
| nav | REAL | Net Asset Value |

---

# 3. fact_aum

Source: 03_aum_by_fund_house.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| date | DATE | Reporting Date |
| fund_house | TEXT | AMC Name |
| aum_lakh_crore | REAL | AUM (Lakh Crore) |
| aum_crore | REAL | AUM (Crore) |
| num_schemes | INTEGER | Number of Schemes |

---

# 4. monthly_sip

Source: 04_monthly_sip_inflows.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| month | TEXT | Reporting Month |
| sip_inflow_crore | INTEGER | SIP Inflow (Crore) |
| active_sip_accounts_crore | REAL | Active SIP Accounts |
| new_sip_accounts_lakh | REAL | New SIP Accounts |
| sip_aum_lakh_crore | REAL | SIP AUM |
| yoy_growth_pct | REAL | YoY Growth (%) |

---

# 5. category_inflows

Source: 05_category_inflows.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| month | TEXT | Month |
| category | TEXT | Fund Category |
| net_inflow_crore | REAL | Net Inflow |

---

# 6. folio_count

Source: 06_industry_folio_count.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| month | TEXT | Month |
| total_folios_crore | REAL | Total Folios |
| equity_folios_crore | REAL | Equity Folios |
| debt_folios_crore | REAL | Debt Folios |
| hybrid_folios_crore | REAL | Hybrid Folios |
| others_folios_crore | REAL | Other Folios |

---

# 7. fact_performance

Source: 07_scheme_performance.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Scheme Code |
| return_1yr_pct | REAL | 1-Year Return |
| return_3yr_pct | REAL | 3-Year Return |
| return_5yr_pct | REAL | 5-Year Return |
| benchmark_3yr_pct | REAL | Benchmark Return |
| alpha | REAL | Alpha |
| beta | REAL | Beta |
| sharpe_ratio | REAL | Sharpe Ratio |
| sortino_ratio | REAL | Sortino Ratio |
| std_dev_ann_pct | REAL | Annual Standard Deviation |
| max_drawdown_pct | REAL | Maximum Drawdown |
| aum_crore | REAL | Assets Under Management |
| morningstar_rating | INTEGER | Morningstar Rating |

---

# 8. fact_transactions

Source: 08_investor_transactions.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| investor_id | TEXT | Investor ID |
| transaction_date | DATE | Transaction Date |
| amfi_code | INTEGER | Scheme Code |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | REAL | Transaction Amount |
| state | TEXT | State |
| city | TEXT | City |
| city_tier | TEXT | Tier Classification |
| age_group | TEXT | Investor Age Group |
| gender | TEXT | Gender |
| annual_income_lakh | REAL | Annual Income |
| payment_mode | TEXT | Payment Method |
| kyc_status | TEXT | KYC Verification Status |

---

# 9. portfolio_holdings

Source: 09_portfolio_holdings.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Scheme Code |
| stock_symbol | TEXT | Stock Symbol |
| stock_name | TEXT | Company Name |
| sector | TEXT | Sector |
| weight_pct | REAL | Portfolio Weight |
| market_value_cr | REAL | Market Value |
| current_price_inr | REAL | Current Stock Price |
| portfolio_date | DATE | Portfolio Date |

---

# 10. benchmark_indices

Source: 10_benchmark_indices.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| date | DATE | Trading Date |
| index_name | TEXT | Benchmark Index |
| close_value | REAL | Closing Value |

---

## Database

Database Name:
```
bluestock_mf.db
```

Database Type:
```
SQLite
```

---

## ETL Workflow

Raw CSV
↓

Data Cleaning (Pandas)
↓

Processed CSV
↓

SQLite Database
↓

SQL Analytics
↓

Power BI / Tableau Dashboard