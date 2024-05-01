import random
import curses
from Utilities.util_loading_bar import curses_loading_bar
from MarkovChain.MarkovGenerator import MarkovGenerator
from MarkovChain.WorldNameData import WorldNameData
from Continents.continent import Continent

class World:

    def __init__(self, name="Unknown", continents=None):
        self.name = name
        self.continents = continents or []
        
    def get_world_name(self):
        return self.name
    
    def get_world_continents(self):
        return self.continents
    
    def generate_world(self, continent_amount = random.randint(1,4), win = None, is_mixed = False):
        #Create a Name Generator utilising Markov Chains
        gen = MarkovGenerator()
        gen.init(WorldNameData)
        
        if self.name == "Unknown" or self.name == "r":             
            #Generate that world Name
            self.name = gen.generate()
            
        #Generate Continents
        
        for x in range(continent_amount):
            # Generate each continent (replace with your actual logic)
            random_continent = Continent().generate_random_continent(world=self)
            random_continent.generate_civilsations(is_mixed = is_mixed)
            self.continents.append(random_continent)
            curses_loading_bar(win,x+1, continent_amount,"Generating")
        
        #Wait For input to continue
        #win.getch()
        
        return self