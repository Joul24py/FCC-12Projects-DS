import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google

""")

tickerSymbol = 'GOOGL' # Definir Ticker Symbol
tickerData = yf.Ticker(tickerSymbol) # Se obtienen sus datos
tickerDf = tickerData.history(period = '1d', start = '2010-05-31', end = '2023-05-31') # Obtenemos precios históricos del Ticker

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)