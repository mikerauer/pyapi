#!/usr/bin/python3

#import stuff
import requests
import json
import pprint

stockapi = "https://www.alphavantage.co/query?function="

#TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"

def stockcall(ticker):
    #makes api request
    stockdata = requests.get(f'{stockapi}TIME_SERIES_DAILY&symbol={ticker}&apikey=267O5WBYN6VOPM3E')
    return stockdata.json()

def main():
    # asks for stock ticket input from user
    ticker = input('What stock ticker would you like to look up?')
        
    #calls the API and prints to screen with pretty print
    stock = stockcall(ticker)
    stockdict = stock["Time Series (Daily)"]
    # loops thru each key and prints close price
    for series in stockdict:
        print(f'Close price is {stockdict[series]["4. close"]}')
   
if __name__ == "__main__":
    main()

#error handle
