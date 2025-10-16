# {expression for item in items if condition}

# Dictionary
# inr = indian rupees
tea_prices_inr = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 200
}

# Convert all prices into US Dollars
tea_prices_usd = { tea:price / 80 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)