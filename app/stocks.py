

print("STOCKS REPORT...")

import os
from dotenv import load_dotenv
from pandas import read_csv
from app.utils import to_usd


load_dotenv()


symbol = input("Please input a crypto symbol (default: 'NFLX'): ") or "NFLX"


df = stocks_data
#print(df.columns)
#breakpoint()

latest = df.iloc[0]

print(symbol)
print(latest["timestamp"])
print(latest["close"])
print(to_usd(latest["close"]))
