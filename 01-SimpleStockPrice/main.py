import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of:

- Google
- Apple
- Microsoft
- IBM
- Amazon

""")

# Google
tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(start = '2010-05-31', end = '2023-09-20')

closeDf = tickerDf.Close.rename('Google')
volumeDf = tickerDf.Volume.rename('Google')

# Apple
tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(start = '2010-05-31', end = '2023-09-20')

closeDf = pd.concat([closeDf, tickerDf.Close.rename('Apple')], axis = 1)
volumeDf = pd.concat([volumeDf, tickerDf.Volume.rename('Apple')], axis = 1)

# Microsoft
tickerSymbol = 'MSFT'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(start = '2010-05-31', end = '2023-09-20')

closeDf = pd.concat([closeDf, tickerDf.Close.rename('Microsoft')], axis = 1)
volumeDf = pd.concat([volumeDf, tickerDf.Volume.rename('Microsoft')], axis = 1)

# IBM
tickerSymbol = 'IBM'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(start = '2010-05-31', end = '2023-09-20')

closeDf = pd.concat([closeDf, tickerDf.Close.rename('IBM')], axis = 1)
volumeDf = pd.concat([volumeDf, tickerDf.Volume.rename('IBM')], axis = 1)

# Amazon
tickerSymbol = 'AMZN'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(start = '2010-05-31', end = '2023-09-20')

closeDf = pd.concat([closeDf, tickerDf.Close.rename('Amazon')], axis = 1)
volumeDf = pd.concat([volumeDf, tickerDf.Volume.rename('Amazon')], axis = 1)

st.line_chart(closeDf)
st.line_chart(volumeDf)