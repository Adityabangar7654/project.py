import yfinance as yf
import pandas as pd

# Class to manage stock portfolio
class Portfolio:
    def __init__(self):
        # Dictionary to store stock info: quantity and purchase price
        self.stocks = {}

    # Function to add stocks to the portfolio
    def add_stock(self, symbol, quantity, purchase_price):
        if symbol in self.stocks:
            self.stocks[symbol]['quantity'] += quantity
        else:
            self.stocks[symbol] = {'quantity': quantity, 'purchase_price': purchase_price}
        print(f"Added {quantity} shares of {symbol} at ${purchase_price} per share.")

    # Function to remove stocks from the portfolio
    def remove_stock(self, symbol, quantity):
        if symbol in self.stocks:
            if self.stocks[symbol]['quantity'] > quantity:
                self.stocks[symbol]['quantity'] -= quantity
                print(f"Removed {quantity} shares of {symbol}.")
            elif self.stocks[symbol]['quantity'] == quantity:
                del self.stocks[symbol]
                print(f"Removed all shares of {symbol}.")
            else:
                print(f"Cannot remove {quantity} shares. You only own {self.stocks[symbol]['quantity']} shares.")
        else:
            print(f"You don't own any shares of {symbol}.")

    # Function to fetch real-time stock data using yfinance
    def fetch_stock_data(self, symbol):
        try:
            stock = yf.Ticker(symbol)
            stock_info = stock.history(period="1d")
            return stock_info['Close'][0]
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            return None

    # Function to display the portfolio and its performance
    def display_portfolio(self):
        portfolio_data = []
        total_value = 0
        total_investment = 0

        for symbol, data in self.stocks.items():
            current_price = self.fetch_stock_data(symbol)
            if current_price:
                stock_value = current_price * data['quantity']
                purchase_value = data['purchase_price'] * data['quantity']
                gain_loss = stock_value - purchase_value
                total_value += stock_value
                total_investment += purchase_value

                portfolio_data.append([symbol, data['quantity'], f"${current_price:.2f}", f"${data['purchase_price']:.2f}", f"${gain_loss:.2f}"])

        portfolio_df = pd.DataFrame(portfolio_data, columns=['Symbol', 'Quantity', 'Current Price', 'Purchase Price', 'Gain/Loss'])
        print("\nPortfolio Summary:")
        print(portfolio_df)
        print(f"\nTotal Investment: ${total_investment:.2f}")
        print(f"Total Portfolio Value: ${total_value:.2f}")
        print(f"Total Gain/Loss: ${total_value - total_investment:.2f}")

# Function to interact with the portfolio
def portfolio_menu():
    portfolio = Portfolio()

    while True:
        print("\n--- Stock Portfolio Tracker ---")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
            quantity = int(input("Enter quantity: "))
            purchase_price = float(input("Enter purchase price: "))
            portfolio.add_stock(symbol, quantity, purchase_price)

        elif choice == '2':
            symbol = input("Enter stock symbol to remove (e.g., AAPL): ").upper()
            quantity = int(input("Enter quantity to remove: "))
            portfolio.remove_stock(symbol, quantity)

        elif choice == '3':
            portfolio.display_portfolio()

        elif choice == '4':
            print("Exiting portfolio tracker.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the portfolio tracker
portfolio_menu()
