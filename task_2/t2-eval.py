import sys
import pandas as pd
import matplotlib.pyplot as plt


if len(sys.argv) < 2:
    print("Please provide the path to the factor CSV file as a command-line argument.")
    sys.exit(1)

csv_path = sys.argv[1]
df = pd.read_csv(csv_path, index_col="Date")

top_5_stocks = df.apply(lambda x: x.nlargest(1).index.tolist(), axis=1)
stock_counts = pd.Series([stock for stocks in top_5_stocks for stock in stocks]).value_counts()

stock_counts = pd.Series([stock for stocks in top_5_stocks for stock in stocks]).value_counts()

# Code to create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(stock_counts.index, stock_counts.values)
plt.xlabel('Stock')
plt.ylabel('Count')
plt.title('Stock Counts')
plt.xticks(rotation=90)
plt.savefig(f'{csv_path.split(".")[0]}.png')

print(stock_counts)