stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420
}

total = 0

name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

if name in stocks:
    total = stocks[name] * quantity
    print("Total investment: $", total)
else:
    print("Stock not found")