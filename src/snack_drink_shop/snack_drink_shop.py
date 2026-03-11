
def main():
	menu = [
		{"type": "Snack", "name": "Chips", "price": 1.50},
		{"type": "Snack", "name": "Chocolate Bar", "price": 2.00},
		{"type": "Snack", "name": "Cookies", "price": 1.75},
		{"type": "Drink", "name": "Water", "price": 1.00},
		{"type": "Drink", "name": "Soda", "price": 1.80},
		{"type": "Drink", "name": "Juice", "price": 2.20},
	]

	print("Welcome to the Snack & Drink Shop!")
	print("Here is our menu:")
	print("--------------------------")
	for idx, item in enumerate(menu, 1):
		print(f"{idx}. {item['type']}: {item['name']} - ${item['price']:.2f}")
	print("--------------------------")
	print('Type the item number to add to your cart, or type "done" to finish.')

	cart = []
	while True:
		choice = input("Enter item number or 'done': ").strip().lower()
		if choice == "done":
			break
		if not choice.isdigit():
			print("Invalid input. Please enter a valid item number or 'done'.")
			continue
		num = int(choice)
		if 1 <= num <= len(menu):
			cart.append(menu[num - 1])
			print(f"Added {menu[num - 1]['name']} to your cart.")
		else:
			print("Invalid item number. Please try again.")

	print("\nYour Receipt:")
	print("--------------------------")
	total = 0.0
	for item in cart:
		print(f"{item['type']}: {item['name']} - ${item['price']:.2f}")
		total += item['price']
	print("--------------------------")
	print(f"Total: ${total:.2f}")
	print("Thank you for shopping with us!")

if __name__ == "__main__":
	main()