import json
import pandas as pd
import requests

class PaperTrader:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.portfolio = {}

    def buy(self, symbol, quantity, price):
        cost = quantity * price
        if cost > self.balance:
            print("Insufficient funds to make the purchase.")
            return

        if symbol not in self.portfolio:
            self.portfolio[symbol] = 0

        self.portfolio[symbol] += quantity
        self.balance -= cost

        print(f"Bought {quantity} shares of {symbol} at ${price:.2f} each.")

    def sell(self, symbol, quantity, price):
        if symbol not in self.portfolio or self.portfolio[symbol] < quantity:
            print("Not enough shares to sell.")
            return

        revenue = quantity * price
        self.portfolio[symbol] -= quantity
        self.balance += revenue

        print(f"Sold {quantity} shares of {symbol} at ${price:.2f} each.")

    def display_portfolio(self):
        print("\nPortfolio Summary:")
        print(f"Balance: ${self.balance:.2f}\n")
        print("Stocks:")
        
        total_portfolio_value = self.balance

        for symbol, quantity in self.portfolio.items():
            price = prices[symbol]
            stock_value = quantity * price
            total_portfolio_value += stock_value

            print(f"{symbol}: {quantity} shares - Current Price: ${price:.2f} - Value: ${stock_value:.2f}")

# Usage: Stocks in US Stock Exchange - Symbol List in .txt File
def read_symbols(file_path):
    with open(file_path, 'r') as file:
        symbols_string = file.read()
        symbols_list = eval(symbols_string)
    
    return symbols_list

symbols_list = read_symbols("stock_symbols_list.txt")

# Usage: API Key From EODHD APIs (https://www.eodhd.com)
"""
def get_exchange_data(key, exchange='US'):
    endpoint = f"https://eodhistoricaldata.com/api/exchange-symbol-list/{exchange}?api_token={key}&fmt=json"
    call = requests.get(endpoint).text
    exchange_data = pd.DataFrame(json.loads(call))
    
    return exchange_data

def get_security_type(exchange_data, type= "Common Stock"):
    symbols = exchange_data[exchange_data.Type == type]
    return symbols.Code.to_list()  

key = "6594a4c32feaf1.06096799"
symbols_list = get_security_type(get_exchange_data(key))
"""

# MAIN
prices = {symbol: 100 for symbol in symbols_list}

while True:
    try:
        balance = int(input("Please enter the initial balance of your trading account: "))
        break

    except ValueError:
        print("Invalid input. Please enter a valid integer for the initial balance.")

trader = PaperTrader(initial_balance = balance)
trader.display_portfolio()

while True:
    action = input("\nDo you want to (b)uy, (s)ell, (v)iew portfolio, or (q)uit? ").lower()

    if action == 'q':
        break

    elif action == 'b':
        symbol = input("Enter the stock symbol: ").upper()

        if symbol not in symbols_list:
            print("Stock Symbol Not Found In Simulation. Please Try Another Stock")
            continue

        quantity = int(input("Enter the quantity to buy: "))
        price = prices[symbol]
        trader.buy(symbol, quantity, price)
    
    elif action == 's':
        symbol = input("Enter the stock symbol: ")

        if symbol not in symbols_list:
            print("Invalid stock symbol.")
            continue

        quantity = int(input("Enter the quantity to sell: "))
        price = prices[symbol]
        trader.sell(symbol, quantity, price)
   
    elif action == 'v':
        trader.display_portfolio()
    
    else:
        print("Invalid option. Please enter 'b', 's', 'v', or 'q'.")

print("Simulation has ended.")
