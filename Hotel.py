from Hotel_pkg.PricePercentage import PricePercentage

class Hotel:
    """
    Class that represents a hotel with methods to manage its rooms, prices, and availability.
    """
    
    def __init__(self, name, stars, rooms_config, location, capacity):
        """
        Initializes a hotel with given attributes and configures its rooms.

        Args:
            name (str): Name of the hotel.
            stars (int): Star rating of the hotel.
            rooms_config (dict): Room configuration as {room_type: (quantity, base_price)}.
            location (str): Location of the hotel.
            capacity (int): Maximum capacity of the hotel (total number of guests).
        """
        self.name = name
        self.stars = stars
        self.rooms_config = []  # List to store details of all rooms
        self.location = location
        self.capacity = capacity

        # Create room entries based on the provided configuration
        for room_type, (num, base_price) in rooms_config.items():
            for _ in range(num):
                room = {
                    "room_type": room_type,     # Type of the room (e.g., double, deluxe, suite)
                    "price": base_price,       # Base price of the room
                    "available": True          # Availability status of the room
                }
                self.rooms_config.append(room)
    
    def price_setting(self, final_price, room_type):
        """
        Updates the price of all rooms of a specific type.

        Args:
            final_price (float): The new price for the room type.
            room_type (str): The type of room whose price will be updated.
        """
        for room in self.rooms_config:
            if room["room_type"] == room_type:
                room["price"] = final_price
                
    def available_rooms_summary(self, type=None):
        """
        Displays a summary of available rooms and their prices.

        Args:
            type (str, optional): Filter for a specific room type. If not provided, shows all types.
        """
        room_count = {}  # Dictionary to count and store room details

        for room in self.rooms_config:
            if room["available"]:
                if type is None or room["room_type"] == type:
                    if room["room_type"] in room_count:
                        room_count[room["room_type"]]["quantity"] += 1
                    else:
                        room_count[room["room_type"]] = {
                            "price": room["price"],
                            "quantity": 1
                        }
        
        # Display the summary of available rooms
        if not room_count:
            print("There are no available rooms")
        else:
            for room_type, info in room_count.items():
                print(f'Room {room_type} - Price (per night): {info["price"]} - Availables: {info["quantity"]}')

    def get_room(self, type):
        """
        Books a room of a specified type if available.

        Args:
            type (str): Type of the room to be booked.

        Returns:
            bool: True if booking was successful, False otherwise.
        """
        for room in self.rooms_config:
            if room["room_type"] == type and room["available"]:
                room["available"] = False  # Mark the room as booked
                print(f"Room {type} booked")

                # Remove the booked room from the list if necessary
                if hasattr(self, 'rooms_config'):
                    self.rooms_config = [r for r in self.rooms_config if r is not room]
                return True
        
        # If no room is available
        print(f"Room {type} not available")
        return False


                   
    
   