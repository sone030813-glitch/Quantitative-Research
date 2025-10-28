import pandas as pd
from pathlib import Path


RAW_PATH = Path("data/GC_1h.csv")


CLEAN_PATH = Path("Research/EMA_strategies/GC_1h_cleaned.csv")



df_raw = pd.read_csv(RAW_PATH)

#datetime to index
df_raw['Datetime'] = pd.to_datetime(df_raw['Datetime'],utc=True, errors='coerce')
df_raw = df_raw.set_index('Datetime')
df_raw = df_raw.sort_index()

df_raw = df_raw[['Open', 'High', 'Low', 'Close', 'Volume']]

df_raw = df_raw.dropna(how= 'all')
# 4.3 去掉不合理价格（<=0）
df_raw = df_raw[(df_raw['Open'] > 0) &
        (df_raw['High'] > 0) &
        (df_raw['Low']  > 0) &
        (df_raw['Close']> 0)]

# 4.4 去掉 High < Low 这种逻辑上不可能的bar
df_raw = df_raw[df_raw['High'] >= df_raw['Low']]

CLEAN_PATH.parent.mkdir(parents=True, exist_ok=True)
df_raw.to_csv(CLEAN_PATH)

print(df_raw.head())
