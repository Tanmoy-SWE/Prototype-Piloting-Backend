import pandas as pd
import numpy as np

# Sample data generation
np.random.seed(0)
dates = pd.date_range('2023-06-01', periods=60)
temperatures = np.random.normal(loc=30, scale=5, size=len(dates))

# Create a DataFrame
data = pd.DataFrame({'Date': dates, 'Temperature': temperatures})

# Define heatwave detection function
def detect_heatwaves(df, threshold_percentile=90, min_duration=3):
    # Calculate the threshold temperature
    threshold = np.percentile(df['Temperature'], threshold_percentile)
    
    # Identify days exceeding the threshold
    df['Heatwave'] = df['Temperature'] > threshold
    
    # Group consecutive heatwave days
    df['Heatwave_Group'] = (df['Heatwave'] != df['Heatwave'].shift()).cumsum()
    
    # Filter groups with heatwaves
    heatwave_groups = df[df['Heatwave']].groupby('Heatwave_Group').filter(lambda x: len(x) >= min_duration)
    
    # Extract heatwave periods
    heatwave_periods = heatwave_groups.groupby('Heatwave_Group').agg(Start=('Date', 'min'), End=('Date', 'max'), Duration=('Date', 'count'))
    
    return heatwave_periods

# Detect heatwaves
heatwave_periods = detect_heatwaves(data)
print(heatwave_periods)
