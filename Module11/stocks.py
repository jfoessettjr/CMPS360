import yfinance as yf  
import matplotlib.pyplot as plt 
import schedule
import time

def fetch_stock_data(ticker, period='1d', intervale='1m'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period, interval=intervale)
    return data

def plot_stock_data(data, tracker):













def main():
    #Set the ticker you want to view
    ticker_symbol = ''
    