import pandas as pd

df = pd.read_csv("contracts.csv")

df["Risk Adjustment"] = df["BEL"] * df["Risk Factor"]
df["Total Liability"] = df["BEL"] + df["Risk Adjustment"]

total = df[["BEL", "Risk Adjustment", "Total Liability"]].sum()


sorted_df = df.sort_values("BEL", ascending=False)
print("\nContracts sorted by BEL (highest first):")
print(sorted_df)

grouped = df.groupby("Type")["BEL"].sum()
print("\nTotal BEL by Contract Type:")
print(grouped)

grouped_ra = df.groupby("Type")["Risk Factor"].mean()
print("\nAverage Risk Factor by Contract Type:")
print(grouped_ra)