
class Guest:
    """
    Represents a guest in the hotel reservation system.
    
    Attributes:
        id (int): Unique identifier for the guest.
        name (str): Name of the guest.
        nights_at_hotel (int): Number of nights the guest plans to stay.
        room_type (str): Type of room the guest wishes to book.
    """
    def __init__(self, id, name, nights_at_hotel, room_type):
        """
        Initializes a Guest object with the provided attributes.

        Args:
            id (int): Unique ID for the guest.
            name (str): Name of the guest.
            nights_at_hotel (int): Number of nights the guest wants to book.
            room_type (str): Type of room to book.
        """
        self.id = id
        self.name = name
        self.nights_at_hotel = nights_at_hotel
        self.room_type = room_type

    def book_room(self, hotel):
        """
        Attempts to book a room at the hotel for the guest.

        Args:
            hotel (Hotel): Hotel object that has the `get_room` method.

        Returns:
            None. Prints a message indicating whether the booking was successful or not.
        """
        room = hotel.get_room(self.room_type)  # Returns True if the room is available
        if room:
            print(f"You have successfully booked a {self.room_type} room")
        else:
            print(f"Room type: {self.room_type} is not available")

    def total_guest_price(self, rooms_config):
        """
        Calculates the total price for the guest's stay.

        Args:
            rooms_config (list): List of dictionaries describing the rooms. 
                                 Each dictionary should contain `room_type`, `price`, and `available`.

        Returns:
            float: The total cost of the stay, or None if the room is not available.
        """
        price = None  # Initialize the price variable
        for room in rooms_config:
            if room["room_type"] == self.room_type and room["available"]:
                price = round(room["price"] * self.nights_at_hotel, 2)
                break

        if price is not None:
            print(f'Your total cost for {self.nights_at_hotel} nights is {price}')
        else:
            print(f"Error: Room type '{self.room_type}' is not available or invalid in configuration.")
        return price
