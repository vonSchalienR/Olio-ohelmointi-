import uuid


class Carriage:


    def __init__(self, new_identifier, number_of_seats):
        """Initializes the current object."""
        self.__id = new_identifier
        self.__max_number_of_seats = number_of_seats
        self.__seats = []
        self.reset_seats()

    def reserve(self, free_seat_number):
        """Precondition: is_free(free_seat_number) 
                         and is_legal(free_seat_number) """
        self.__seats[free_seat_number] = 1


    def make_free(self, reserved_seat_number):
        """Precondition: not is_free(reserved_seat_number) 
                         and is_legal(reserved_seat_number) """
        self.__seats[reserved_seat_number] = 0


    def count_reserved(self):
        """Precondition: True """
        i = 1
        result = 0
        while (i < len(self.__seats)):
            if (self.__seats[i] != 0):
                result = result + 1
            i = i + 1
        return result


    def is_free(self, free_seat_number):
        """Precondition: True
                         and is_legal(free_seat_number)"""
        return self.__seats[free_seat_number] == 0

    def is_legal(self, seat_number):
        """Precondition: True """
        return 1 <= seat_number <= self.__max_number_of_seats   

    def max_seats(self):
        """Precondition: True """
        return self.__max_number_of_seats

    def is_full(self):
        """Precondition: True """
        return self.count_reserved() >= self.max_seats()

    def reset_seats(self):
        self.__seats = []
        i = 0
        while (i <= self.__max_number_of_seats):
            self.__seats.append(0)
            i = i + 1


    def reserved_seats_as_list(self):
        result = []
        i = 1
        while (i < len(self.__seats)):
            if (not self.is_free(i)):
                result.append(i)
            i = i + 1
        return result


    def __str__(self):
        result = ""
        result = result + self.__id + ": "
        result = result + str(self.__seats[1:len(self.__seats)])
        return result



def just_a_test():
    c01 = Carriage("Carr01", 10)
    print(c01)

    c01.reserve(6)
    c01.reserve(9)
    c01.reserve(10)
    c01.reserve(1)

    a_seat = 12
    if (c01.is_legal(a_seat)):
        if (c01.is_free(a_seat)):
            c01.reserve(a_seat)

    print(c01)
    print(c01.count_reserved())
    print(c01.reserved_seats_as_list())
    c01.make_free(10)
    print(c01)
    print(c01.reserved_seats_as_list())



just_a_test()

class Train:
    def __init__(self, new_identifier, departure, destination, initial_carriage):
        """
        Initializes the Train object with at least one carriage.
        :param new_identifier: Unique identifier for the train.
        :param departure: Departure location.
        :param destination: Destination location.
        :param initial_carriage: A Carriage object to start the train.
        """
        assert isinstance(initial_carriage, Carriage), "The train must have at least one valid Carriage."
        
        self.__id = new_identifier if new_identifier else str(uuid.uuid4())
        self.__departure = departure
        self.__destination = destination
        self.__carriages = [initial_carriage]
    
    def add_carriage(self, carriage):
        """Adds a new carriage to the train at the end."""
        assert isinstance(carriage, Carriage), "Invalid Carriage object."
        self.__carriages.append(carriage)
    
    def remove_carriage(self, carriage):
        """Removes a carriage from the train while ensuring at least one remains."""
        assert len(self.__carriages) > 1, "A train must have at least one carriage."
        assert carriage in self.__carriages, "Carriage not found in train."
        self.__carriages.remove(carriage)
    
    def reserve_seat(self):
        """Reserves the first available seat in the train's carriages."""
        for carriage in self.__carriages:
            for seat in range(1, carriage.max_seats() + 1):
                if carriage.is_free(seat):
                    carriage.reserve(seat)
                    return f"Seat {seat} reserved in {carriage.get_id()}"
        return "No available seats."
    
    def visualize_seats(self):
        """Displays a text-based representation of seat reservations."""
        report = f"Train {self.__id} from {self.__departure} to {self.__destination}\n"
        for carriage in self.__carriages:
            report += str(carriage) + "\n"
        return report
    
    def get_train_info(self):
        """Returns train details including ID, departure, destination, and carriages."""
        return {
            "Train ID": self.__id,
            "Departure": self.__departure,
            "Destination": self.__destination,
            "Carriages": [str(carriage) for carriage in self.__carriages]
        }
    
    def __str__(self):
        return f"Train {self.__id}: {len(self.__carriages)} carriages from {self.__departure} to {self.__destination}"
