import numpy as np
import plotly.express as px
import pandas as pd

#Parameters
num_scenarios = 10
num_years = 30
initial_rate = 0.03     # starting interest rate 3%
volatility = 0.01       # how much rates can move each year

# Generate scenarios
np.random.seed(42)      # makes results reproducible 
scenarios = {}

for i in range(num_scenarios):
    rates = [initial_rate]
    for year in range(1, num_years + 1):
        shock = np.random.normal(0, volatility)
        new_rate = rates[-1] + shock
        new_rate = max(0, new_rate)     # rates can't go below 0
        rates.append(new_rate)
    scenarios[f"Scenarios {i+1}"] = rates

# Convert to DataFrame
years = list(range(0, num_years + 1))
df = pd.DataFrame(scenarios, index=years)

print(df)


# Plot
#fig = px.line(df, title="Interest Rate Scenarios over 30 Years",
#              labels={"index": "Year", "value": "Interest Rate", "variable": "Scenario"})
#fig.show()