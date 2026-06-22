import pandas as pd
from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA = PROJECT_ROOT / "data" / "raw"

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

print("=" * 100)
print("MF ANALYTICS PLATFORM - DATA INGESTION")
print("=" * 100)

for file in files:

    print("\n" + "=" * 80)
    print(file)

    path = RAW_DATA / file

    df = pd.read_csv(path)

    print(f"\nShape : {df.shape}")

    print("\nData Types")
    print(df.dtypes)

    print("\nFirst 5 Rows")
    print(df.head())

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())

print("\nData ingestion completed successfully.")
print("\n" + "=" * 80)
print("FUND MASTER EXPLORATION")
print("=" * 80)

fund = pd.read_csv(RAW_DATA / "01_fund_master.csv")

print("\nUnique Fund Houses")
print(fund["fund_house"].unique())

print("\nNumber of Fund Houses")
print(fund["fund_house"].nunique())

print("\nCategories")
print(fund["category"].unique())

print("\nSub Categories")
print(fund["sub_category"].unique())

print("\nRisk Categories")
print(fund["risk_category"].unique())

print("\nSEBI Category Codes")
print(fund["sebi_category_code"].unique())

print("\n" + "=" * 80)
print("AMFI CODE VALIDATION")
print("=" * 80)

fund_master = pd.read_csv(RAW_DATA / "01_fund_master.csv")
nav_history = pd.read_csv(RAW_DATA / "02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing = master_codes - nav_codes

print("Fund Master Codes :", len(master_codes))
print("NAV Codes         :", len(nav_codes))
print("Missing Codes     :", len(missing))

if len(missing) == 0:
    print("\nAll AMFI codes are present in NAV history.")
else:
    print("\nMissing Codes:")
    print(sorted(missing))