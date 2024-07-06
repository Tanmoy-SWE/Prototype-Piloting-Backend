import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load Data
# Assuming data is loaded into a DataFrame called df with a 'Temperature' column
# For this example, we will create a sample DataFrame
data = {'Temperature': np.random.normal(loc=30, scale=5, size=365)}
df = pd.DataFrame(data)
df['Date'] = pd.date_range(start='1/1/2023', periods=len(df))

# Step 2: Define Heatwave Criteria
threshold_percentile = 90
threshold_value = np.percentile(df['Temperature'], threshold_percentile)

# Step 3: Identify Heatwave Days
df['Is_Heatwave_Day'] = df['Temperature'] > threshold_value

# Step 4: Detect Consecutive Heatwave Days
def detect_heatwave_periods(df, min_duration=3):
    heatwave_periods = []
    current_period = []
    for i, row in df.iterrows():
        if row['Is_Heatwave_Day']:
            current_period.append(row['Date'])
            if len(current_period) >= min_duration:
                heatwave_periods.append(current_period.copy())
        else:
            current_period = []
    return heatwave_periods

heatwave_periods = detect_heatwave_periods(df)

# Step 5: Visualize Results
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Temperature'], label='Temperature')
for period in heatwave_periods:
    plt.axvspan(period[0], period[-1], color='red', alpha=0.3)
plt.axhline(threshold_value, color='gray', linestyle='--', label=f'{threshold_percentile}th Percentile')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Heatwave Detection')
plt.legend()
plt.show()
