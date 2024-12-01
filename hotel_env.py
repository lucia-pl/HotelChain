from Hotel_pkg.Hotel import Hotel
from Hotel_pkg.PricePercentage import PricePercentage

class Ht_distribution:
    """
    Class to represent hotel distribution, including name, star rating, location, and capacity.
    Provides functionality for setting room prices based on the season.
    """

    def __init__(self, name, stars, location, capacity):
        """
        Initializes the hotel distribution with basic details.

        Args:
            name (str): Name of the hotel.
            stars (int): Star rating of the hotel (3, 4, or 5 stars).
            location (int): Numeric location value (used in fuzzy logic for price calculation).
            capacity (int): Maximum guest capacity of the hotel.
        """
        self.name = name
        self.stars = stars
        self.location = location
        self.capacity = capacity

    def room_pricing(self, season) -> Hotel:
        """
        Sets up room pricing and quantity based on the season and star rating of the hotel.

        Args:
            season (int): Numeric season value (used in fuzzy logic for price calculation).

        Returns:
            Hotel: A `Hotel` object initialized with calculated room prices and quantities.
        """
        # Create an instance of PricePercentage for price calculation
        obj_pricing = PricePercentage()

        # Determine room configuration based on the star rating of the hotel
        if self.stars == 3:
            # 3-star hotel configuration
            rooms_quantity = {
                "double": (10, obj_pricing.calculated_price(season, 0, self.location, 30)),
                "deluxe": (7, obj_pricing.calculated_price(season, 1, self.location, 50)),
                "suite": (3, obj_pricing.calculated_price(season, 2, self.location, 70))
            }
        elif self.stars == 4:
            # 4-star hotel configuration
            rooms_quantity = {
                "double": (20, obj_pricing.calculated_price(season, 0, self.location, 70)),
                "deluxe": (10, obj_pricing.calculated_price(season, 1, self.location, 100)),
                "suite": (5, obj_pricing.calculated_price(season, 2, self.location, 150))
            }
        else:
            # 5-star hotel configuration
            rooms_quantity = {
                "double": (30, obj_pricing.calculated_price(season, 0, self.location, 100)),
                "deluxe": (15, obj_pricing.calculated_price(season, 1, self.location, 150)),
                "suite": (10, obj_pricing.calculated_price(season, 2, self.location, 200))
            }

        # Create and return a `Hotel` object with the configured room details
        hotel = Hotel(self.name, self.stars, rooms_quantity, self.location, self.capacity)
        return hotel
