import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine



PROJECT_ROOT = Path(__file__).resolve().parent.parent

PROCESSED = PROJECT_ROOT / "data" / "processed"

DATABASE = PROJECT_ROOT / "bluestock_mf.db"

engine = create_engine(f"sqlite:///{DATABASE}")

print("=" * 80)
print("LOADING DATA INTO SQLITE")
print("=" * 80)
print("\nLoading dim_fund...")

fund = pd.read_csv(PROCESSED / "01_fund_master.csv")

fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

print("Rows:", len(fund))


print("\nLoading fact_nav...")

nav = pd.read_csv(PROCESSED / "02_nav_history.csv")

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("Rows:", len(nav))




print("\nLoading fact_transactions...")

transactions = pd.read_csv(PROCESSED / "08_investor_transactions.csv")

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("Rows:", len(transactions))


print("\nLoading fact_performance...")

performance = pd.read_csv(PROCESSED / "07_scheme_performance.csv")

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Rows:", len(performance))



print("\nLoading fact_aum...")

aum = pd.read_csv(PROCESSED / "03_aum_by_fund_house.csv")

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("Rows:", len(aum))

print("\nAll datasets loaded successfully into SQLite.")