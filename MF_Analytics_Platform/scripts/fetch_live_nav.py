import requests
import pandas as pd
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA = PROJECT_ROOT / "data" / "raw"

RAW_DATA.mkdir(parents=True, exist_ok=True)


schemes = {
    "HDFC_Top100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

print("=" * 80)
print("LIVE NAV FETCH")
print("=" * 80)

for scheme_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        data = response.json()

        # Meta Information
        meta = data.get("meta", {})
        print(f"\nScheme : {meta.get('scheme_name', scheme_name)}")
        print(f"AMFI Code : {scheme_code}")

        # NAV History
        nav_df = pd.DataFrame(data.get("data", []))

        filename = RAW_DATA / f"{scheme_name}.csv"

        nav_df.to_csv(filename, index=False)

        print(f"Rows Downloaded : {len(nav_df)}")
        print(f"Saved To : {filename}")

    except Exception as e:
        print(f"\nError fetching {scheme_name}")
        print(e)

print("\nAll downloads completed.")