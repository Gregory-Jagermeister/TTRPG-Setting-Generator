import random
from src.Modules.MarkovChain.MarkovGenerator import MarkovGenerator
from src.Modules.MarkovChain.SettlementData import SettlementNames
from src.Modules.Settlement.SettlementModifers import SettlementModifiers

class Settlement:
    def __init__(self):
        self.type = "Basic"
        self.name = "Empty Settlement"
        self.age = "Unknown"
        self.condition = "Unknown"
        self.environment = "Unknown"
        self.size = "Unknown"
        self.modifiers = SettlementModifiers()

    def generate_name(self):
        gen = MarkovGenerator()
        gen.init(SettlementNames)
        return gen.generate()

    def generate_age(self):
        result = random.randint(1, 20)
        age_ranges = [
            (range(0, 4), (-1, "Recent")),
            (range(4, 9), (0, "Established")),
            (range(9, 14), (1, "Mature")),
            (range(14, 18), (2, "Old")),
            (range(18, 20), (3, "Ancient")),
            (range(20, 21), (4, "Unknown"))  # range(20, 21) is just 20
        ]
        
        for age_range, age_info in age_ranges:
            if result in age_range:
                visitor_traffic_mod, description = age_info
                self.modifiers.visitor_traffic_modifier += visitor_traffic_mod
                return description

    def generate_condition(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.condition_modifier, 20), 1)
        if self.type == "Trading Post" or  self.type == "Town" or self.type == "Village":
            condition_ranges = [
                (range(0, 1), (-6, "Rambshackled")),
                (range(2, 4), (-3, "Poor")),
                (range(5, 12), (0, "Average")),
                (range(13, 19), (+3, "Good")),
                (range(20, 21), (+6, "Excellent"))
            ]
            
            for condition_range, condition_info in condition_ranges:
                if roll in condition_range:
                    pop_wealth, description = condition_info
                    self.modifiers.population_wealth_modifier += pop_wealth
                    return description
        else:
            return "Superb"

    def generate_environment(self):
        return random.choice(['Coastal','Forest', 'Desert', 'Mountain', 'Plains', 'River', 'Swamp', 'Underground', 'Valley', 'Tundra'])

    def generate_size(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.size_modifier, 20), 1)
        size_ranges = [
            (range(1, 2), "Very Small (20 standing structures)"),
            (range(3, 6), "Small (40 standing structures)"),
            (range(7, 14), "Medium (60 standing structures)"),
            (range(15, 18), "Large (80 standing structures)"),
            (range(19, 24), "Very Large (100 standing structures)")
        ]
        
        for size_range, description in size_ranges:
            if roll in size_range:
                return description

    def generate(self):
        self.name = self.generate_name()
        self.age = self.generate_age()
        self.condition = self.generate_condition()
        self.environment = self.generate_environment()
        self.size = self.generate_size()

    def get_type(self):
        return self.type
    
    def set_type(self, type):
        self.type = type

    def __str__(self):
        return f"{self.size} of {self.name}, aged: {self.age}, Condition: {self.condition}, Located in the {self.environment}"
