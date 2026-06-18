# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0

print("Available Stocks:")
for stock, price in stock_prices.items():
    print(stock, "- $", price)

while True:
    stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print(f"{stock_name}: {quantity} shares × ${stock_prices[stock_name]} = ${investment}")
    else:
        print("Stock not found!")

print("\nTotal Investment Value: $", total_investment)
