import requests
import os
from dotenv import load_dotenv
import pandas as pd
import json

load_dotenv()
api = os.getenv("API")
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=' + api
r = requests.get(url)
data = r.json()

#print(data)
# Parse JSON string
#data = json.loads(data)

# Extract time series data
time_series = data["Time Series (5min)"]

# Convert to DataFrame
df = pd.DataFrame.from_dict(time_series, orient='index')

# Rename columns for better readability
df.columns = ["open", "high", "low", "close", "volume"]

# Convert data types to appropriate formats
df = df.astype({
    "open": float,
    "high": float,
    "low": float,
    "close": float,
    "volume": int
})

# Convert the index to datetime
df.index = pd.to_datetime(df.index)
df = df.rename_axis("IBM", axis=1)
# Display the DataFrame
print(df)