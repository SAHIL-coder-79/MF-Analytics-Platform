import pandas as pd
from pathlib import Path
import shutil


PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW = PROJECT_ROOT / "data" / "raw"
PROCESSED = PROJECT_ROOT / "data" / "processed"

PROCESSED.mkdir(parents=True, exist_ok=True)

print("=" * 80)
print("DAY 2 - DATA CLEANING")
print("=" * 80)



print("\nCleaning nav_history...")

nav = pd.read_csv(RAW / "02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(["amfi_code", "date"])

nav = nav.drop_duplicates()

nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

nav = nav[nav["nav"] > 0]

nav.to_csv(PROCESSED / "02_nav_history.csv", index=False)

print("Rows:", len(nav))


print("\nCleaning investor_transactions...")

txn = pd.read_csv(RAW / "08_investor_transactions.csv")

txn["transaction_type"] = (
    txn["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

mapping = {
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
}

txn["transaction_type"] = txn["transaction_type"].replace(mapping)

txn["transaction_date"] = pd.to_datetime(txn["transaction_date"])

txn = txn[txn["amount_inr"] > 0]

valid_kyc = ["Verified", "Pending", "Rejected"]

invalid_kyc = txn[~txn["kyc_status"].isin(valid_kyc)]

print("Invalid KYC Records:", len(invalid_kyc))

txn.to_csv(PROCESSED / "08_investor_transactions.csv", index=False)

print("Rows:", len(txn))


print("\nCleaning scheme_performance...")

perf = pd.read_csv(RAW / "07_scheme_performance.csv")

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct"
]

for col in return_columns:
    perf[col] = pd.to_numeric(perf[col], errors="coerce")

anomalies = perf[perf[return_columns].isna().any(axis=1)]

print("Anomalies Found:", len(anomalies))

invalid_expense = perf[
    (perf["expense_ratio_pct"] < 0.1) |
    (perf["expense_ratio_pct"] > 2.5)
]

print("Expense Ratio Issues:", len(invalid_expense))

perf.to_csv(PROCESSED / "07_scheme_performance.csv", index=False)

print("Rows:", len(perf))

print("\nCopying remaining datasets...")

remaining_files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in remaining_files:
    shutil.copy(RAW / file, PROCESSED / file)
    print(f"Copied: {file}")

print("\nAll datasets are now available in data/processed.")