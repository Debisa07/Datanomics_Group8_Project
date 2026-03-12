def main():
   
    movies = {
        "1": {"title": "The Matrix", "showtime": "18:00", "price": 12.00 Birr},
        "2": {"title": "Inception", "showtime": "20:30", "price": 15.00 Birr},
        "3": {"title": "Interstellar", "showtime": "22:00", "price": 14.50 Birr}
    }

    
    total_cost = 0.0
    user_bookings = []
    
    print("Welcome to the Python Movie Theater!")

    while True:
        
        print("\n--- Available Movies ---")
        for key, info in movies.items():
            print(f"{key}. {info['title']} at {info['showtime']} - ${info['price']:.2f} per ticket")

        
        choice = input("\nEnter the movie number you want to book: ").strip()
        
        if choice not in movies:
            print("Invalid selection. Please try again.")
            continue
            
        selected_movie = movies[choice]

        
        try:
            num_tickets = int(input(f"How many tickets for {selected_movie['title']}? "))
            if num_tickets <= 0:
                print("You must book at least 1 ticket.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        
        current_cost = selected_movie['price'] * num_tickets
        total_cost += current_cost
        
        user_bookings.append({
            "title": selected_movie['title'],
            "tickets": num_tickets,
            "cost": current_cost
        })
        
        print(f"\nSuccess! Added {num_tickets} ticket(s) for {selected_movie['title']}.")
        print(f"Subtotal for this booking: ${current_cost:.2f}")

        
        another = input("\nWould you like to book another movie? (yes/no): ").strip().lower()
        if another == 'no' or another == 'n':
            break

    print("\n" + "="*30)
    print("YOUR BOOKING SUMMARY")
    print("="*30)

    if not user_bookings:
        print("No bookings were made.")
    else:
        for i, booking in enumerate(user_bookings, 1):
            print(f"{i}. {booking['title']} - {booking['tickets']} ticket(s) - ${booking['cost']:.2f}")
            
        print("-" * 30)
        print(f"GRAND TOTAL: ${total_cost:.2f}")
        print("Thank you for using the Python Movie Theater!")

if __name__ == "__main__":
    main()
