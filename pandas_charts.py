import pandas as pd
import plotly.express as px

df = pd.read_csv("contracts.csv")

df["Risk Adjustment"] = df["BEL"] * df["Risk Factor"]
df["Total Liability"] = df["BEL"] + df["Risk Adjustment"]

fig = px.bar(df, x="Contract", y="Total Liability",
             title="Total Liability by Contract",
             color="Type")

fig.show()

fig2 = px.pie(df, values="Total Liability", names="Type",
              title="Total Liability split by Contract Type")
fig2.show()