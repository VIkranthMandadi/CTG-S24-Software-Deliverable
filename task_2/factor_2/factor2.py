# factor2.py
import pandas as pd
import os
import sys

def calculate_volume_adjusted_momentum(stock_data, n=15):
    # Calculate the Volume Adjusted Momentum factor backward over the last n days
    stock_data['Factor_Volume_Adjusted_Momentum'] = ((stock_data['Close'] - stock_data['Close'].shift(n)) / stock_data['Close'].shift(n)) / stock_data['Volume']
    stock_data = stock_data[['Factor_Volume_Adjusted_Momentum']]
    return stock_data

def process_csv_file(csv_path):
    # Read data from the CSV file
    df = pd.read_csv(csv_path, index_col="Date")
    
    # Calculate Volume Adjusted Momentum factor backward over the last 15 days
    df = calculate_volume_adjusted_momentum(df, n=15)
    
    # Extract the ticker symbol from the file name
    ticker = os.path.splitext(os.path.basename(csv_path))[0]

    # Rename the 'Factor_Volume_Adjusted_Momentum' column with the ticker symbol
    df.rename(columns={'Factor_Volume_Adjusted_Momentum': ticker}, inplace=True)

    return df

def main(data_directory):
    # Create an empty DataFrame to store all factors
    all_factors_df = pd.DataFrame()

    for csv_file in os.listdir(data_directory):
        if csv_file.endswith(".csv"):
            csv_path = os.path.join(data_directory, csv_file)
            # Process each CSV file and append factors to the main DataFrame
            factors_df = process_csv_file(csv_path)
            all_factors_df = pd.concat([all_factors_df, factors_df], axis=1)
    
    # Save all factors to a single CSV file
    all_factors_file_path = os.path.join('factor2.csv')
    all_factors_df.to_csv(all_factors_file_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python factor2.py /path/to/data_directory")
    else:
        main(sys.argv[1])
