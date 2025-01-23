def phone_book_app():
    """
    Simple phone book application that allows searching, adding, and quitting.
    """
    phone_book = {}  # Dictionary to store names and phone numbers

    while True:
        # Prompt for command
        command = input("command (1 search, 2 add, 3 quit): ").strip()
        
        if command == "1":  # Search
            name = input("name: ").strip()
            if name in phone_book:
                print(phone_book[name])
            else:
                print("no number")
        
        elif command == "2":  # Add
            name = input("name: ").strip()
            number = input("number: ").strip()
            phone_book[name] = number  # Add or update the entry
            print("ok!")
        
        elif command == "3":  # Quit
            print("quitting...")
            break
        
        else:  # Invalid command
            print("Invalid command. Please enter 1, 2, or 3.")

# Run the phone book application
phone_book_app()
