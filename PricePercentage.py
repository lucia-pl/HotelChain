import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class PricePercentage:
    """
    Class that calculates price multipliers for hotel rooms based on fuzzy logic.
    The factors include location, season, and room type.
    """
    
    def __init__(self):
        """
        Initializes the fuzzy logic system with input and output variables and their membership functions.
        Defines the fuzzy rules for determining the price multiplier.
        """
        # Fuzzy inputs: location, season, and room type
        self.location = ctrl.Antecedent(np.arange(0, 3, 1), 'location')
        self.season = ctrl.Antecedent(np.arange(0, 3, 1), 'season')  # 0: low, 1: medium, 2: high
        self.room_type = ctrl.Antecedent(np.arange(0, 3, 1), 'room_type')  # 0: double, 1: deluxe, 2: suite
        
        # Fuzzy output: price multiplier
        self.multiplier = ctrl.Consequent(np.arange(0.5, 2.1, 0.1), 'multiplier')

        # Define membership functions for 'season'
        self.season['low'] = fuzz.trimf(self.season.universe, [0, 0, 1])
        self.season['medium'] = fuzz.trimf(self.season.universe, [0, 1, 2])
        self.season['high'] = fuzz.trimf(self.season.universe, [1, 2, 2])

        # Define membership functions for 'room_type'
        self.room_type['double'] = fuzz.trimf(self.room_type.universe, [0, 0, 1])
        self.room_type['deluxe'] = fuzz.trimf(self.room_type.universe, [0, 1, 2])
        self.room_type['suite'] = fuzz.trimf(self.room_type.universe, [1, 2, 2])
        
        # Define membership functions for 'location'
        self.location['rural'] = fuzz.trimf(self.location.universe, [0, 0, 1])
        self.location['ciudad'] = fuzz.trimf(self.location.universe, [0, 1, 2])
        self.location['mar'] = fuzz.trimf(self.location.universe, [1, 2, 2])

        # Define membership functions for 'multiplier'
        self.multiplier['lowest'] = fuzz.trimf(self.multiplier.universe, [0.5, 0.8, 1.0])
        self.multiplier['low'] = fuzz.trimf(self.multiplier.universe, [0.9, 1.0, 1.2])
        self.multiplier['medium'] = fuzz.trimf(self.multiplier.universe, [1.1, 1.3, 1.5])
        self.multiplier['high'] = fuzz.trimf(self.multiplier.universe, [1.4, 1.7, 2.0])
        self.multiplier['very_high'] = fuzz.trimf(self.multiplier.universe, [1.8, 2.1, 2.5])

        # Define fuzzy rules
        self.rules = [
            # Low season, double room
            ctrl.Rule(self.season['low'] & self.room_type['double'] & self.location['mar'], self.multiplier['low']),
            ctrl.Rule(self.season['low'] & self.room_type['double'] & self.location['ciudad'], self.multiplier['lowest']),
            ctrl.Rule(self.season['low'] & self.room_type['double'] & self.location['rural'], self.multiplier['lowest']),
            
            # Low season, deluxe room
            ctrl.Rule(self.season['low'] & self.room_type['deluxe'] & self.location['mar'], self.multiplier['medium']),
            ctrl.Rule(self.season['low'] & self.room_type['deluxe'] & self.location['ciudad'], self.multiplier['low']),
            ctrl.Rule(self.season['low'] & self.room_type['deluxe'] & self.location['rural'], self.multiplier['low']),
            
            # Low season, suite
            ctrl.Rule(self.season['low'] & self.room_type['suite'] & self.location['mar'], self.multiplier['high']),
            ctrl.Rule(self.season['low'] & self.room_type['suite'] & self.location['ciudad'], self.multiplier['medium']),
            ctrl.Rule(self.season['low'] & self.room_type['suite'] & self.location['rural'], self.multiplier['medium']),
            
            # Medium season, double room
            ctrl.Rule(self.season['medium'] & self.room_type['double'] & self.location['mar'], self.multiplier['medium']),
            ctrl.Rule(self.season['medium'] & self.room_type['double'] & self.location['ciudad'], self.multiplier['low']),
            ctrl.Rule(self.season['medium'] & self.room_type['double'] & self.location['rural'], self.multiplier['lowest']),
            
            # Medium season, deluxe room
            ctrl.Rule(self.season['medium'] & self.room_type['deluxe'] & self.location['mar'], self.multiplier['high']),
            ctrl.Rule(self.season['medium'] & self.room_type['deluxe'] & self.location['ciudad'], self.multiplier['medium']),
            ctrl.Rule(self.season['medium'] & self.room_type['deluxe'] & self.location['rural'], self.multiplier['low']),
            
            # Medium season, suite
            ctrl.Rule(self.season['medium'] & self.room_type['suite'] & self.location['mar'], self.multiplier['very_high']),
            ctrl.Rule(self.season['medium'] & self.room_type['suite'] & self.location['ciudad'], self.multiplier['high']),
            ctrl.Rule(self.season['medium'] & self.room_type['suite'] & self.location['rural'], self.multiplier['medium']),
            
            # High season
            ctrl.Rule(self.season['high'] & self.room_type['double'] & self.location['mar'], self.multiplier['high']),
            ctrl.Rule(self.season['high'] & self.room_type['double'] & self.location['ciudad'], self.multiplier['high']),
            ctrl.Rule(self.season['high'] & self.room_type['double'] & self.location['rural'], self.multiplier['medium']),
            ctrl.Rule(self.season['high'] & self.room_type['deluxe'] & self.location['mar'], self.multiplier['high']),
            ctrl.Rule(self.season['high'] & self.room_type['deluxe'] & self.location['ciudad'], self.multiplier['high']),
            ctrl.Rule(self.season['high'] & self.room_type['deluxe'] & self.location['rural'], self.multiplier['medium']),
            ctrl.Rule(self.season['high'] & self.room_type['suite'] & self.location['mar'], self.multiplier['very_high']),
            ctrl.Rule(self.season['high'] & self.room_type['suite'] & self.location['ciudad'], self.multiplier['very_high']),
            ctrl.Rule(self.season['high'] & self.room_type['suite'] & self.location['rural'], self.multiplier['high']),
        ]
        
        self.multiplier_ctrl = ctrl.ControlSystem(self.rules)
        self.multiplier_simulator = ctrl.ControlSystemSimulation(self.multiplier_ctrl)

    def calculate_multiplier(self, season_value, room, location):
        """
        Computes the multiplier based on season, room type, and location.
        """
        self.multiplier_simulator.input['season'] = season_value
        self.multiplier_simulator.input['room_type'] = room
        self.multiplier_simulator.input['location'] = location
        self.multiplier_simulator.compute()
        return self.multiplier_simulator.output['multiplier']

    def calculated_price(self, season_value, room, location, room_price):
        """
        Calculates the final room price using the computed multiplier.

        Args:
            season_value (int): Season (0: low, 1: medium, 2: high).
            room (int): Room type (0: double, 1: deluxe, 2: suite).
            location (int): Location (0: rural, 1: city, 2: sea).
            room_price (float): Base price of the room.

        Returns:
            float: Final room price rounded to 2 decimals.
        """
        final_multiplier = self.calculate_multiplier(season_value, room, location)
        final_price = room_price * final_multiplier
        return round(final_price, 2)
