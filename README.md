# Paper-Trading-Simulation

## Description
This Python program implements a simple paper trading simulation using the PaperTrader class. The simulation allows users to buy and sell stocks with an initial balance, displaying the portfolio summary after each transaction. The user interacts with the simulation through a command-line interface, choosing to buy, sell, view the portfolio, or quit the simulation. Stock symbols are read from a predefined list, and historical prices are simulated for each stock. The script provides a basic yet functional introduction to paper trading, allowing users to practice trading strategies without risking real capital.

## Dependencies
### API
The script incorporates the EODHD API to dynamically fetch exchange data. This API, accessible at EODHD APIs, provides historical stock data. The get_exchange_data function is designed to retrieve a list of symbols for a specified exchange, while the get_security_type function filters symbols based on security types, with "Common Stock" being the default. Note that you need to obtain an API key from EODHD to use this functionality.

### File I/O
The script reads stock symbols from a text file, stock_symbols_list.txt. This file contains a list of stock symbols that the user can interact with during the paper trading simulation. The symbols are read from the file and stored in the symbols_list variable.

## Future Updates
- create a webpage for the user to interact with
- use the API to gather real time stock prices
- connect to other stock exchanges (currently it is only the US Stock Exchange)
