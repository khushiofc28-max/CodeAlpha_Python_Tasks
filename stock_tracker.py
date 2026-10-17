# Hardcoded dictionary for stock prices[cite: 2]
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 175
}

portfolio = {}
total_investment = 0

print("=" * 40)
print("     STOCK PORTFOLIO TRACKER")
print("=" * 40)
print("Available Stocks & Prices:")
for stock, price in stock_prices.items():
    print(f"- {stock}: ${price}")
print("=" * 40)

# User input loop[cite: 2]
while True:
    stock = input("\nEnter stock symbol (or type 'done' to calculate): ").strip().upper()
    
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print("Invalid stock! Please select from the list above.")
        continue
    
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue
        
        # Quantity add karna
        portfolio[stock] = portfolio.get(stock, 0) + quantity
        print(f"Added {quantity} shares of {stock}.")
    except ValueError:
        print("Please enter a valid whole number for quantity.")

# Calculation and display[cite: 2]
print("\n" + "=" * 40)
print("           PORTFOLIO SUMMARY")
print("=" * 40)

if not portfolio:
    print("No stocks added to the portfolio.")
else:
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        stock_total = qty * price
        total_investment += stock_total
        print(f"{stock}: {qty} shares @ ${price} each = ${stock_total}")
    
    print("-" * 40)
    print(f"Total Investment Value: ${total_investment}")
    print("=" * 40)

    # Result save in a text file[cite: 2]
    with open("portfolio_summary.txt", "w") as file:
        file.write("--- Portfolio Summary ---\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock}: {qty} shares @ ${stock_prices[stock]} = ${qty * stock_prices[stock]}\n")
        file.write("-" * 30 + "\n")
        file.write(f"Total Investment Value: ${total_investment}\n")

    print("\n[SUCCESS] Summary has been saved to 'portfolio_summary.txt' file!")