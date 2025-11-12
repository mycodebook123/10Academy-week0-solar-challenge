import pandas as pd
import numpy as np

# Create sample solar data for demonstration
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=100, freq='D')

sample_data = {
    'Timestamp': dates,
    'GHI': np.random.normal(450, 100, 100),  # Global Horizontal Irradiance
    'DNI': np.random.normal(600, 150, 100),  # Direct Normal Irradiance  
    'DHI': np.random.normal(150, 50, 100),   # Diffuse Horizontal Irradiance
    'Tamb': np.random.normal(25, 5, 100),    # Ambient Temperature
    'RH': np.random.normal(60, 15, 100),     # Relative Humidity
    'WS': np.random.normal(3, 1, 100),       # Wind Speed
}

df = pd.DataFrame(sample_data)
df.to_csv('data/sample_benin_data.csv', index=False)
print("Sample data created!")