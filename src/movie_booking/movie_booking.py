def main():
    
    
    base_seats = [f"{row}{num}" for row in "ABC" for num in range(1, 6)]

    movies = {
        "1": {"title": "The Matrix", "showtime": "18:00", "price": 12.00, "available_seats": base_seats.copy()},
        "2": {"title": "Inception", "showtime": "20:30", "price": 15.00, "available_seats": base_seats.copy()},
        "3": {"title": "Interstellar", "showtime": "22:00", "price": 14.50, "available_seats": base_seats.copy()},
        "4": {"title": "Tenet", "showtime": "19:00", "price": 13.00, "available_seats": base_seats.copy()},
        "5": {"title": "Dune", "showtime": "21:00", "price": 16.00, "available_seats": base_seats.copy()},
        "6": {"title": "Oppenheimer", "showtime": "20:00", "price": 17.50, "available_seats": base_seats.copy()},
        "7": {"title": "The Dark Knight", "showtime": "19:30", "price": 14.00, "available_seats": base_seats.copy()},
        "8": {"title": "Parasite", "showtime": "20:00", "price": 13.50, "available_seats": base_seats.copy()}
    }

    total_cost = 0.0
    user_bookings = []
    
    print("Welcome to Group 8 movie booking system!")
    

    user_name = input("Please enter your name: ").strip()
    if not user_name:
        user_name = "Guest" 

    print(f"\nHello, {user_name}! Let's book some tickets.")

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
            
            
            if num_tickets > len(selected_movie['available_seats']):
                print(f"Sorry, only {len(selected_movie['available_seats'])} seats remain for this movie.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        
        selected_seats = []
        print("\n--- Seat Selection ---")
        print(f"Available seats for {selected_movie['title']}:")
        print(", ".join(selected_movie['available_seats']))
        
        for i in range(num_tickets):
            while True:
                seat = input(f"Enter seat for ticket {i+1} of {num_tickets} (e.g., A1): ").strip().upper()
                if seat in selected_movie['available_seats']:
                    selected_movie['available_seats'].remove(seat)
                    selected_seats.append(seat)
                    break
                else:
                    print("Invalid or already taken seat. Please choose from the available seats listed above.")

        current_cost = selected_movie['price'] * num_tickets
        total_cost += current_cost
        
        user_bookings.append({
            "title": selected_movie['title'],
            "tickets": num_tickets,
            "seats": selected_seats,
            "cost": current_cost
        })
        
        print(f"\nSuccess! Added {num_tickets} ticket(s) for {selected_movie['title']}.")
        print(f"Seats Booked: {', '.join(selected_seats)}")
        print(f"Subtotal for this booking: ${current_cost:.2f}")
        
        another = input("\nWould you like to book another movie? (yes/no): ").strip().lower()
        if another == 'no' or another == 'n':
            break

    print("\n" + "="*40)
   
   
    print(f"{user_name.upper()}'S BOOKING SUMMARY")
    print("="*40)

    if not user_bookings:
        print("No bookings were made.")
    else:
        for i, booking in enumerate(user_bookings, 1):
            print(f"{i}. {booking['title']} - {booking['tickets']} ticket(s)")
            print(f"   Seats: {', '.join(booking['seats'])}")
            print(f"   Cost: ${booking['cost']:.2f}")
            
        print("-" * 40)
        print(f"GRAND TOTAL: ${total_cost:.2f}")
        print("Thank you for using Group 8 movie booking system")

if __name__ == "__main__":
    main()

