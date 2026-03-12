
def main():
    # 1. Predefined dictionary of groceries with prices
    inventory = {
        "apple": 0.50,
        "orange": 0.30,
        "pear":0.50,
        "banana":0.35,
        "milk": 2.50,
        "bread": 1.50,
        "cheese": 3.00,
        "eggs": 2.00
    }
    
    cart = {}
    print("--- Welcome to the Grocery Store ---")
    print("Available items:", ", ".join(inventory.keys()))
    print("Type 'checkout' to finish.")

    # 2. Keep adding until "checkout"
    while True:
        item = input("\nEnter item to add (or 'checkout'): ").lower().strip()
        
        if item == 'checkout':
            break
        
        # 3. Validate item
        if item in inventory:
            try:
                qty = int(input(f"How many {item}s? "))
                if qty > 0:
                    # Add to cart (if already exists, update quantity)
                    cart[item] = cart.get(item, 0) + qty
                    print(f"Added {qty} {item}(s).")
                else:
                    print("Please enter a positive quantity.")
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        else:
            print("Sorry, we don't have that item.")

    # 4. Display final bill
    print("\n" + "="*30)
    print("        FINAL BILL")
    print("="*30)
    print(f"{'Item':<10} | {'Qty':<3} | {'Subtotal'}")
    print("-" * 30)
    
    total = 0
    for item, qty in cart.items():
        price = inventory[item]
        subtotal = price * qty
        total += subtotal
        print(f"{item.capitalize():<10} | {qty:<3} | ${subtotal:.2f}")
    
    print("-" * 30)
    print(f"Total: ${total:.2f}")
    print("="*30)
    print("Thank you for shopping!")

if __name__ == "__main__":
    main()