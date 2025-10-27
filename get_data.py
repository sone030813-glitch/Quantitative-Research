
import yfinance as yf
from datetime import datetime, timedelta


commodities_tickers = [
    # Energy
    'CL=F',  # WTI Continuous Futures
    'NG=F',  # Natural Gas Continuous Futures
    
    # Precious Metals
    'GC=F',  # Gold Continuous Futures
    'SI=F',  # Silver Continuous Futures
    
    # Base Metals
    'HG=F',  # Copper Continuous Futures (HG is the symbol for Copper)
    
    # Agriculture (Grains)
    'ZS=F',  # Soybeans Continuous Futures
    'ZC=F'   # Corn Continuous Futures
]
agricultural_tickers = [

    # Agriculture (Grains)
    'ZS=F',  # Soybeans Continuous Futures
    'ZC=F'   # Corn Continuous Futures
    'ZW=F'
]
interestrate_tickers = [

    'ZT=F', #2-Year Treasury Note futures

    'ZF=F', #5-Year Treasury Note futures

    'ZN=F', #10-Year Treasury Note futures

    'ZB=F' #30-Year
]


end_date = datetime.now().strftime('%Y-%m-%d')


start_date = (datetime.now() - timedelta(days=550)).strftime('%Y-%m-%d')


# --- 2. Download Data ---



data_1h = yf.download(
    tickers='GC=F', 
    start=start_date, 
    end=end_date, 
    interval='1h',  # Crucial parameter for 1-hour interval data
    actions=False,  # Exclude dividend/split actions (irrelevant for futures)
    threads=True    # Use threading for faster bulk download
)

# --- 3. Data Processing and Inspection ---

# The resulting DataFrame will be a MultiIndex DataFrame (Columns are [Metric, Ticker]).
print("\n--- Download Success: 1-Hour Futures Data Head ---")
print(data_1h.head())



data_1h.to_csv('data_1h')
