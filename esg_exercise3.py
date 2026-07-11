import numpy as np
import plotly.express as px
import pandas as pd

# Future cash flows (claims + expenses) for next 10 years
cash_flows = {
    "Year": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Cash Flow": [50000, 48000, 45000, 42000, 38000,
                  35000, 30000, 25000, 20000, 15000]
}

df = pd.DataFrame(cash_flows)

# Yield curve rates for each year
discount_rates = [0.02, 0.022, 0.024, 0.026, 0.028,
                  0.030, 0.031, 0.032, 0.033, 0.034]

# Calculate discount factors and PV 
df["Discount Rate"] = discount_rates
df["Discount Factor"] = [1 / (1 + r) ** t
                        for r, t in zip(df["Discount Rate"], df["Year"])]
df["PV Cash Flow"] = df["Cash Flow"] * df["Discount Factor"]

# BEL = sum of all discounted cash flows
bel = df["PV Cash Flow"].sum()

print(df.to_string(index=False))
print(f"\nBest Estimate Liability (BEL): {bel:,.2f}")

# Chart
fig = px.bar(df, x="Year", y=["Cash Flow", "PV Cash Flow"],
             title="Cash Flows vs Present Value",
             barmode="group")

fig.show()