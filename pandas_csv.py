import pandas as pd

df = pd.read_csv("contracts.csv")

df["Risk Adjustment"] = df["BEL"] * df["Risk Factor"]
df["Total Liability"] = df["BEL"] + df["Risk Adjustment"]

total = df[["BEL", "Risk Adjustment", "Total Liability"]].sum()

print(df)
print("\nTotal:")
print(total)  

high_risk = df[df["Risk Factor"] > 0.05]
print("\nHigh Risk Contracts:")
print(high_risk)