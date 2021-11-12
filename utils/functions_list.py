
ticker = "HAKA-USDT"

def count_unique_pair(df):
    describe_df = df.describe()
    print(f"You traded {describe_df.iloc[1][0]} different trading pairs in the last seven days.")
    """
    Counts the number of unique trading pairs which were traded by user in the last 7 days, up to 500 transactions
    """
    

def most_freq_trade_pair(df):
    describe_df = df.describe()
    print(f"You traded {describe_df.iloc[2][0]} {describe_df.iloc[3][0]} times, in the last seven days.") 

def count_buys_sells(df):
    """
    Creates table showing the total buys and sells of the different assests traded within the last 7 days, up to 500 transactions

    The table created by 'Named Agg' function is not being read as a normal dataframe.  Need to return to this to see how to visualize the data created by this function.

    """
    buy_sell_count = df.groupby(["Trading Pair", "Order Type"], as_index=False).agg(count_col=pd.NamedAgg(column="Order Type", aggfunc="count"))
    buy_sell_count_df = pd.DataFrame(buy_sell_count)
    display(buy_sell_count)
 

def list_unique_trade_pairs(df):
    return df["Trading Pair"].unique()
   
def select_trade_pair(ticker):
    trading_pair = sum_all_data_df[sum_all_data_df["Trading Pair"] == ticker]
    return trading_pair

def get_trade_pair_stats(trading_pair):
    trading_pair_buy = trading_pair[trading_pair["Order Type"]=="buy"]
    trading_pair_buy_cost = np.array(trading_pair_buy["Cost USDT"])
    trading_pair_buy_fee = np.array(trading_pair_buy["Fee USDT"])
    trading_pair_total_buy_expense = (trading_pair_buy_cost + trading_pair_buy_fee)

    trading_pair_sell = trading_pair[trading_pair["Order Type"]=="sell"]
    trading_pair_sell_cost = np.array(trading_pair_sell["Cost USDT"])
    trading_pair_sell_fee = np.array(trading_pair_sell["Fee USDT"])
    trading_pair_total_sell_revenue = (trading_pair_sell_cost - trading_pair_sell_fee)

    ticker_data = [{"Buy Cost":trading_pair_buy_cost}, {"Buy Fee":trading_pair_buy_fee}, {"Total Expense": trading_pair_total_buy_expense}, 
    {"Sell Value":trading_pair_sell_cost}, {"Sell Fee":trading_pair_sell_fee}, {"Total Revenue": trading_pair_total_sell_revenue}]
    ticker_table = {ticker:ticker_data}

    return ticker_table
  

def ticker_profit_loss(ticker_table):
   profit_loss = ticker_table[ticker][5]['Total Revenue'] - ticker_table[ticker][2]['Total Expense']
   profit_loss = str(profit_loss[0])
   #print(type(profit_loss))
   print(f"Your profit/loss for this ticker is ${profit_loss}")