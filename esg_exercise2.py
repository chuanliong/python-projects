import numpy as np
import plotly.express as px
import pandas as pd

# Maturities in years
maturities = [1, 2, 3, 5, 7, 10, 15, 20, 30]

# Generate 3 yield curve scenarios
short_rate = 0.02   # base short term rate

def generate_yield_curve(short_rate, spread, curve_shape):
    rates = []
    for t in maturities:
        if curve_shape == "normal":
            rate = short_rate + spread * (1 - np.exp(-t/10))
        elif curve_shape == "inverted":
            rate = short_rate - spread * (1 - np.exp(-t/10))
        elif curve_shape == "flat":
            rate = short_rate + spread * 0.1        
        rates.append(rate)
    return rates

# Generate curves
normal = generate_yield_curve(short_rate, 0.02, "normal")
inverted = generate_yield_curve(short_rate, 0.02, "inverted")
flat = generate_yield_curve(short_rate, 0.02, "flat")

# Create DataFrame
df = pd.DataFrame({
    "Maturity": maturities,
    "Normal": normal,
    "Inverted": inverted,
    "Flat": flat
})

# Plot 
fig = px.line(df, x="Maturity", y=["Normal", "Inverted", "Flat"],
              title="Yield Curve Scenarios",
              labels={"value": "Interest Rate", "variable": "Curve Type"})
fig.show()