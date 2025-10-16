def process_order(item, quntity):
    try:
        price = {"masala": 20}[item]
        cost = price * quntity
        print(f"Total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on the menu")
    except TypeError:
        print("Quantity must in number")

process_order("ginger", 2)
process_order("masala", "two")
        