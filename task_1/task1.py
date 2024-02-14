import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def save_to_csv(stock_data, ticker):
    file_path = f"data/{ticker}.csv"
    stock_data.to_csv(file_path)

def main():
    # Read tickers from the tickers.txt file
    with open('tickers.txt', 'r') as file:
        tickers = file.read().splitlines()

    start_date = '2021-01-01'
    end_date = '2023-12-31'

    for ticker in tickers:
        try:
            # Fetch historical stock data
            stock_data = fetch_stock_data(ticker, start_date, end_date)

            # Save data to CSV
            save_to_csv(stock_data, ticker)
            print(f"{ticker} data saved successfully.")
        except Exception as e:
            print(f"Error fetching or saving data for {ticker}: {e}")

if __name__ == "__main__":
    main()