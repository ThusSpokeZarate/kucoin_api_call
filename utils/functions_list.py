
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
 

#count_buys_sells_df = count_buys_sells(kucoin_data_past_seven_days_df)
#display(count_buys_sells_df.iloc["count_col"])

def list_unique_trade_pairs(df):
    return df["Trading Pair"].unique()
   

