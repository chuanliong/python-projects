import pandas as pd

data = {
    "Contract": ["AAA", "BBB", "CCC"],
    "BEL": [100000, 250000, 75000],
    "Risk Factor": [0.05, 0.08, 0.03],
}

df = pd.DataFrame(data)
df["Risk Adjustment"] = df["BEL"] * df["Risk Factor"]
df["Total Liability"] = df["BEL"] + df["Risk Adjustment"]

total = df[["BEL", "Risk Adjustment", "Total Liability"]].sum()

print(df)
print("\nTotal:")
print(total)