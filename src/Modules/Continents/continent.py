import random
import curses
from Continents.con_name_gen import generate_name
from Continents.con_climate_gen import generate_con_climates
from Continents.con_resources_gen import generate_resources
from Civilisations.Civilisation import Civilisation

class Continent: 

    def __init__(self, name="Unknown", climate="Unknown", inhabiting_races=None, nat_resources="Unknown", civilisations=None, world=None):
        self.name = name
        self.climate = climate
        self.inhabiting_races = inhabiting_races
        self.nat_resources = nat_resources
        self.world = world
        self.civilisations = civilisations or []

    def get_continent_name(self):
        return self.name
    
    def get_continent_climate(self):
        return self.climate

    def get_continent_races(self):
        return self.inhabiting_races

    def get_continent_nat_resources(self):
        return self.nat_resources
    
    def get_continent_world(self):
        return self.world
    
    def get_continent_civilisations(self):
        return self.civilisations
    
    def generate_civilsations(self, is_mixed = False):
        #Generate Civilisations for this Continent
        con_civilisations = []
        for i in range(1, random.randint(2, 7)):
            new_civ = Civilisation(mixed_race=is_mixed).generate_civ(from_continent=self)
            con_civilisations.append(new_civ)
        
        self.civilisations = con_civilisations
    
    def edit_name(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "Enter new name: ")
        stdscr.refresh()
        curses.echo()
        new_name = stdscr.getstr(0, len("Enter new name: "))
        self.name = new_name.decode("utf-8")

    @classmethod
    def generate_random_continent(cls, world=None):
        # You can customize these lists based on your world-building needs
        possible_races = ["Humans", "Elves", "Dwarves", "Orcs", "Goblinoids", "Half-Elves", "Half-Orcs", "Dragonborn", "Gnomes", "Halflings", "Tiefling", "Genasi", "Shifters", "Changlings", "Goliaths", "Giff", "Hadozee", "Owlin", "Kenku's", "Warforged"]

        # Define weights for each race category
        weights_mapping = {
            "main_races": 5,
            "uncommon_races": 2,
            "rare_races": 1
        }

        # Generate the weights list based on the categories
        weights = [weights_mapping["main_races"] if race in ["Humans", "Elves", "Dwarves", "Orcs", "Gnomes", "Halflings", "Dragonborn", "Tieflings"] else
                weights_mapping["uncommon_races"] if race in ["Half-Elves", "Half-Orcs","Shifters", "Goliath", "Changling"] else
                weights_mapping["rare_races"] for race in possible_races]
        num_selected_races = random.choices(range(1, len(possible_races) + 1), weights)[0]

        # Select the races
        inhabiting_races = random.sample(possible_races, min(num_selected_races + 1, len(possible_races)))

        # Check if Elves or Orcs are in the inhabiting races and if so, add Half-elves or Half-orcs and likewise the inverse.
        if "Elves" in inhabiting_races and "Half-Elves" not in inhabiting_races:
            inhabiting_races.append("Half-Elves")
        if "Orcs" in inhabiting_races and "Half-Orcs" not in inhabiting_races:
            inhabiting_races.append("Half-Orcs")
        if "Half-Elves" in inhabiting_races and "Elves" not in inhabiting_races:
            inhabiting_races.remove("Half-Elves")
        if "Half-Orcs" in inhabiting_races and "Orcs" not in inhabiting_races:
            inhabiting_races.remove("Half-Orcs")
    
        # Generate a population distribution list
        population_distribution = []

        # Generate a pseudo-"population" for each race
        for race in inhabiting_races:
            race_weight = weights[possible_races.index(race)]
            race_population = random.randrange(race_weight, race_weight*10)
            population_distribution.append(race_population)

        # Calculate the total simulated population
        total_population = sum(population_distribution)

        # Calculate the demographic percentages
        race_demographics = {}
        for i, race in enumerate(inhabiting_races):
            demographic_percent = (population_distribution[i] / total_population) * 100
            race_demographics[race] = round(demographic_percent)

        # Generate a random continent
        name = generate_name()
        climate = generate_con_climates()
        nat_resources = generate_resources()

        return cls(name, climate, race_demographics, nat_resources,None, world)
    
    def __str__(self):
        result = "\n----Welcome to the Continent of {}----".format(self.name)

        # Climate
        result += "\n\n\t----Climate Information----"
        for region, details in self.climate.items():
            result += "\n\tThe {} region is characterized by a {}, mainly due to its {}.".format(region.capitalize(), details['climate'], details['feature'])

        # Inhabiting races
        result += "\n\n\t----Demographics----"
        result += "\n\t{:<15s} {:<15s}".format("Race", "Population %")  # Table header
        for race, population in self.inhabiting_races.items():
            result += "\n\t{:<15s} {:<15d}".format(race, population)  # Table rows

        # Natural resources
        result += "\n\n\t----Natural Resources----"
        for region, resources in self.nat_resources.items():
            result += "\n\tIn the {} region:".format(region.capitalize())
            for resource, rarity in resources:
                result += "\n\t\t- {} (Rarity: {})".format(resource, rarity)

        result += "\n"   # Ending the result with a newline for cleaner output
        return result