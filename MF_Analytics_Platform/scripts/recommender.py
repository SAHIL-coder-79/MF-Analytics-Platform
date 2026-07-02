import pandas as pd

# Load data
fund_master = pd.read_csv("../data/processed/01_fund_master.csv")
sharpe_df = pd.read_csv("../reports/sharpe_ratio.csv")

# Merge
recommendation_df = sharpe_df.merge(
    fund_master,
    on="amfi_code"
)

def recommend_funds(risk):

    result = (
        recommendation_df[
            recommendation_df["risk_grade"].str.lower() == risk.lower()
        ]
        .sort_values(
            "Sharpe",
            ascending=False
        )
        .head(3)
    )

    return result[
        [
            "amfi_code",
            "scheme_name",
            "risk_grade",
            "Sharpe"
        ]
    ]

risk = input("Enter Risk Appetite (Low / Moderate / High): ")

print("\nRecommended Funds:\n")

print(recommend_funds(risk))