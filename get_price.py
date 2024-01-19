import yfinance as yf

def get_price(symbol):
    ticker_nse = yf.Ticker(symbol+".NS").info.get('currentPrice')
    if ticker_nse is None:
        ticker_bo = yf.Ticker(symbol+".BO").info.get('currentPrice')
        if ticker_bo is None:
            return None
        else:
            return ticker_bo
    else:
        return ticker_nse
        


