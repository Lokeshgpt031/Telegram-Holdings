import os
from get_price import get_price
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from sendTelegramMsg import send_telegram_image,send_telegram_message
from dotenv import load_dotenv
load_dotenv()


df=pd.read_csv(os.environ.get("SHEET_SECRET"))
print(df)# df1=pd.read_csv(os.environ.get("SHEET"))

# #df1 update keys to lower case
# df.columns = df.columns.str.upper()

# #in df add df1
# df=pd.concat([df, df1], ignore_index=True)
# print(df)
unwanted_columns = ['EXCHANGE', 'ISIN', 'T1QTY', 'TOTALQTY', 'DPQTY', 'T1QTY', 'COLLATERALQTY',"Live"]

# Remove unwanted columns
df = df.drop(columns=unwanted_columns)
print(df)
#loop through the dataframe and get the price of each TickerSymbol in the dataframe and add it to the dataframe


for index, row in df.iterrows():
    df.at[index, 'LIVEPRICE'] = get_price(row['TRADINGSYMBOL'])
print(df)
#Calculate Profit using availableQty, avgCostPrice, LivePrice

for index, row in df.iterrows():
    df.at[index, 'PROFIT'] = row['AVAILABLEQTY']*(row['LIVEPRICE']-row['AVGCOSTPRICE'])
print(df)
# Calculate invested amount and Profit

InvestedAmount = 0
Profit=0

for index, row in df.iterrows():
    InvestedAmount = InvestedAmount + row['AVGCOSTPRICE']*row['AVAILABLEQTY']
    Profit = Profit + row['PROFIT']


print("Invested Amount = ",InvestedAmount)
print("Profit = ",Profit)

#Calculate ROI
ROI = (Profit/InvestedAmount)*100
print("ROI = ",round(ROI,2),end="%")

#Calculate Profit Margin
ProfitMargin = (Profit/InvestedAmount)*100
print("Profit Margin = ",round(ProfitMargin,2),end="%")


result=f"""
Invested Amount = {round(InvestedAmount,2)}
Profit = {round(Profit,2)}
Profit Margin = {round(ProfitMargin,2)}
ROI = {round(ROI,2)}
"""

send_telegram_message(result)

#from df get best performing stocks

stock=df[df['PROFIT']==df['PROFIT'].max()]
send_telegram_message(stock.to_markdown)

send_telegram_message(df.to_markdown)

# df group by TRADINGSYMBOL and sum the PROFIT column

df.groupby('TRADINGSYMBOL')['PROFIT'].sum().plot(kind='bar').get_figure().savefig('bestPerformingStocks.png')


send_telegram_image('bestPerformingStocks.png')




