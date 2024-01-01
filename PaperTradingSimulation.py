import random
import requests
from alpha_vantage.timeseries import TimeSeries

class PaperTrader:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.portfolio = {}

    def cost(self, quantity, price):
        return price * quantity
    
    def buy(self, symbol, quantity, price):
        if self.cost(quantity, price) > self.balance:
            print("You do not have the required funds to confirm this purchase.")
            print(f"You currently have {self.balance} and the required cost is {self.cost(quantity, price)}")
            return
        
        if symbol not in self.portfolio:
            self.portfolio[symbol] = 0

        self.portfolio[symbol] += quantity
        self.balance -= self.cost(quantity, price)
        
        print(f"Bought {quantity} shares of {symbol} at ${price:.2f} each.")

    def sell(self, symbol, quantity, price):
        if symbol not in self.portfolio or self.portfolio[symbol] < quantity:
            print(f"You do not own enough shares of {symbol}.")
            return

        self.portfolio[symbol] -= quantity
        self.balance += self.cost(quantity, price)
        
        print(f"Sold {quantity} shares of {symbol} at ${price:.2f} each.")

def stock_symbols(API_key):
    endpoint = f"https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={API_key}&datatype=csv"
    
    try:
        response = requests.get(endpoint)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)

        data = response.text
        lines = data.split('\n')[1:]  # Skip the header
        symbols = [line.split(',')[0] for line in lines if line]
        return symbols

    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return []
    
# MAIN
API_key = 'PI52LS9BXFLZCCSB'
symbol_list = stock_symbols(API_key)

initial_balance = float(input("Enter your initial balance: "))
trader = PaperTrader(initial_balance=initial_balance)

trader.display_portfolio()

while True:
    action = input("\nDo you want to (b)uy, (s)ell, (v)iew portfolio, or (q)uit? ").lower()

    if action == 'q':
        break
    
    elif action == 'b':
        symbol = input("Enter the stock symbol: ").upper()
        
        if symbol not in symbol_list:
            print("Invalid stock symbol. Please choose from the available symbols.")
            continue

        quantity = int(input("Enter the quantity to buy: "))
        price = random.uniform(50, 200)  # You can fetch the real-time price using another API
        trader.buy(symbol, quantity, price)
    
    elif action == 's':
        symbol = input("Enter the stock symbol: ").upper()
        
        if symbol not in symbol_list:
            print("Invalid stock symbol. Please choose from the available symbols.")
            continue

        quantity = int(input("Enter the quantity to sell: "))
        price = random.uniform(50, 200)  # You can fetch the real-time price using another API
        trader.sell(symbol, quantity, price)
    
    elif action == 'v':
        trader.display_portfolio()
        print("Available Stock Symbols:", symbol_list)
    
    else:
        print("Invalid option. Please enter 'b', 's', 'v', or 'q'.")

print("Simulation ended.")
