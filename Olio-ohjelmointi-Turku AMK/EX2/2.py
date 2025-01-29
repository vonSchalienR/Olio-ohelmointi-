class TrainCarriage:
    def __init__(self, carriage_id, total_seats):
        # Initialize the carriage with ID and the number of seats.
        self.carriage_id = carriage_id
        self.total_seats = total_seats
        self.seats = [False] * total_seats  # A list where False means unreserved, True means reserved
    
    def reserve_seat(self, seat_number):
        """Reserves a seat if it is not already reserved."""
        if 1 <= seat_number <= self.total_seats:
            if self.seats[seat_number - 1]:
                print(f"Seat {seat_number} is already reserved.")
            else:
                self.seats[seat_number - 1] = True
                print(f"Seat {seat_number} has been reserved.")
        else:
            print("Invalid seat number.")
    
    def cancel_reservation(self, seat_number):
        """Cancels the reservation of a seat."""
        if 1 <= seat_number <= self.total_seats:
            if not self.seats[seat_number - 1]:
                print(f"Seat {seat_number} is not reserved.")
            else:
                self.seats[seat_number - 1] = False
                print(f"Reservation for seat {seat_number} has been canceled.")
        else:
            print("Invalid seat number.")
    
    def reset_reservations(self):
        """Resets all reservations."""
        self.seats = [False] * self.total_seats
        print("All reservations have been reset.")
    
    def is_full(self):
        """Checks if the carriage is full (i.e., all seats are reserved)."""
        return all(self.seats)
    
    def report(self):
        """Returns a report of reserved and unreserved seats as a string."""
        reserved_seats = [str(i + 1) for i, reserved in enumerate(self.seats) if reserved]
        unreserved_seats = [str(i + 1) for i, reserved in enumerate(self.seats) if not reserved]
        
        reserved_report = ", ".join(reserved_seats) if reserved_seats else "None"
        unreserved_report = ", ".join(unreserved_seats) if unreserved_seats else "None"
        
        return (f"Carriage {self.carriage_id} Report:\n"
                f"Reserved seats: {reserved_report}\n"
                f"Unreserved seats: {unreserved_report}")


# Creating a train carriage with 5 seats and ID "C1"
carriage = TrainCarriage("C1", 5)

# Reserving some seats
carriage.reserve_seat(1)  # Reserve seat 1
carriage.reserve_seat(3)  # Reserve seat 3
carriage.reserve_seat(5)  # Reserve seat 5

# Report status
print(carriage.report())

# Canceling a reservation
carriage.cancel_reservation(3)  # Cancel seat 3 reservation

# Report status after cancellation
print(carriage.report())

# Check if the carriage is full
print(f"Is the carriage full? {carriage.is_full()}")

# Resetting all reservations
carriage.reset_reservations()

# Final report after resetting
print(carriage.report())
