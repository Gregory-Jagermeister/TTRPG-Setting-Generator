import random
import curses
from MarkovChain.MarkovGenerator import MarkovGenerator
from MarkovChain.NationData import NationNameData
from MarkovChain.NationData import NationTitleData
from MarkovChain.NationData import NationGovTypes
from MarkovChain.NationData import NationEconomicTypes
from MarkovChain.NationData import NationMilitaryTroopTypes
from MarkovChain.NationData import NationMilitarySize
from MarkovChain.NationData import NationSocialClassTypes
from MarkovChain.NationData import NationLifeStyles
from MarkovChain.NationData import NationInequalities
from MarkovChain.NationData import NationFamilyTypes

class Civilisation:

    def __init__(self, name = "unknown", mixed_race = False, races = None, hallmarks = None, continent = None, settlements = []):
        self.name = name
        self.mixed_race = mixed_race
        self.races = races
        self.hallmarks = hallmarks if hallmarks else {}
        self.continent = continent
        self.settlements = settlements
    
    def get_civ_name(self):
        return self.name
    
    def set_is_mixed_race(self, is_mixed_race = False):
        self.mixed_race = is_mixed_race
    
    def get_civ_races(self):
        return self.races
    
    def get_civ_is_of_mixed_races(self):
        return self.mixed_race
    
    def get_civ_hallmarks(self):
        return self.hallmarks
    
    def get_civ_continent(self):
        return self.continent
    
    def get_civ_settlements(self):
        return self.settlements
    
    def set_hallmark(self, key, value):
        self.hallmarks[key] = value
    
    def add_hallmark(self, key, value):
        if key in self.hallmarks:
            if type(self.hallmarks[key]) is list:
                self.hallmarks[key].append(value)
            else:
                self.hallmarks[key] = [self.hallmarks[key], value]
        else:
            self.hallmarks[key] = value

    def get_hallmark(self, key):
        return self.hallmarks.get(key)

    def remove_hallmark(self, key, value=None):
        if key in self.hallmarks:
            # If value is specified, try removing it from the list
            if value and type(self.hallmarks[key]) is list:
                self.hallmarks[key].remove(value)
                if len(self.hallmarks[key]) == 1:
                    self.hallmarks[key] = self.hallmarks[key][0]
            else:
                del self.hallmarks[key]
    
    def generate_civ(self, from_continent = None):
        
        #Get the Continent this Nation is attached too
        self.continent = from_continent
        
        #Add the races avalible on the continent to an array
        con_races = None
        
        if from_continent is not None:
            con_races = list(from_continent.get_continent_races().keys())
            
        #Select Races Based on whether the Civilisation is Mixed race or not.
        
        if self.mixed_race :
            if len(con_races) < 2:
                civ_races = con_races[0]
            else: 
                civ_races = random.choices(con_races, k=random.randint(2,len(con_races)))
            self.races = civ_races
        else:
            civ_races = random.choice(con_races)
            self.races = civ_races
        
        #Create a Name Generator utilising Markov Chains
        gen = MarkovGenerator()
        gen.init(NationNameData)
        
        #Generate the Name of the Civilisation
        name = gen.generate()
        
        if random.random() < 0.35:
            additional_word = random.choice(NationTitleData)
            self.name = f"The {name} {additional_word}"
        else:
            self.name = name
        
        #Generate Hallmarks of that Civilisation
        
        #Lets Follow SPERM Nation Building method (Social, Political, Economic, Religious and Military)
        
        #Set Government / Political Type
        gov_type = random.choice(NationGovTypes)
        self.set_hallmark("Political", gov_type)
        
        #Set Economic Focus'
        economic_focus_amount = random.randint(2,5)
        for x in range(economic_focus_amount):
            economic_focus = random.choice(NationEconomicTypes)
            self.add_hallmark("Economy", economic_focus)
        
        #Set The Religious Rate
        amount_religious = random.randint(0, 100)
        self.set_hallmark("Religion", f"The People of this Civilisation are {amount_religious}% religious")
        
        #Set Military power and Army composition
        army_size = random.choice(NationMilitarySize)
        
        moderate_weights = [1,1,1,1,1,1,2,1,1,2,2,2,3,3,3,1,3,3,0,1,2,1,0,0,0,0]
        substantial_weights = [1,2,2,2,2,1,1,2,2,1,3,3,3,3,3,2,3,3,1,1,2,2,0,0,1,0]
        large_weights = [2,3,2,2,2,2,0,2,2,0,3,3,3,3,3,3,3,3,2,2,2,2,1,1,1,1]
        superpower_weights = [2,3,3,3,2,2,0,3,3,0,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2]
        
        troops = NationMilitaryTroopTypes[:]
        
        match army_size:
            case "Non-exsistent":
                self.set_hallmark("Military", {"Army Size" : army_size, "Troops" : "None"})
            case "Small (Militia)":
                troop_comp = str(random.choices(troops, weights=[0,0,0,0,0,0,5,0,0,2,1,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0], k=1)[0])
                self.set_hallmark("Military", {"Army Size" : army_size, "Troops" : troop_comp})
            case "Moderate":
                troop_comp = []
                for _ in range(random.randint(4,10)):
                    troop_selected = random.choices(troops, weights=moderate_weights, k=1)[0]
                    troop_comp.append(troop_selected)
                    index = troops.index(troop_selected)
                    troops.pop(index)
                    moderate_weights.pop(index)
                troop_comp_final = ", ".join(str(troop_comp).strip("[]").replace("'","").split(", "))
                self.set_hallmark("Military", {"Army Size" : army_size, "Troops" : troop_comp_final})
            case "Substantial":
                troop_comp = []
                for _ in range(random.randint(4,10)):
                    troop_selected = random.choices(troops, weights=substantial_weights, k=1)[0]
                    troop_comp.append(troop_selected)
                    index = troops.index(troop_selected)
                    troops.pop(index)
                    substantial_weights.pop(index)
                troop_comp_final = ", ".join(str(troop_comp).strip("[]").replace("'","").split(", "))
                self.set_hallmark("Military", {"Army Size" : army_size, "Troops" : troop_comp_final})
            case "Large":
                troop_comp = []
                for _ in range(random.randint(4,10)):
                    troop_selected = random.choices(troops, weights=large_weights, k=1)[0]
                    troop_comp.append(troop_selected)
                    index = troops.index(troop_selected)
                    troops.pop(index)
                    large_weights.pop(index)
                troop_comp_final = ", ".join(str(troop_comp).strip("[]").replace("'","").split(", "))
                self.set_hallmark("Military", {"Army Size" : army_size, "Troops" : troop_comp_final})
            case "World Military Superpower":
                troop_comp = []
                for _ in range(random.randint(4,10)):
                    troop_selected = random.choices(troops, weights=superpower_weights, k=1)[0]
                    troop_comp.append(troop_selected)
                    index = troops.index(troop_selected)
                    troops.pop(index)
                    superpower_weights.pop(index)
                troop_comp_final = ", ".join(str(troop_comp).strip("[]").replace("'","").split(", "))
                self.set_hallmark("Military", {"Army Size" : army_size, "Troops" : troop_comp_final})
                
        # Set up Social aspects.
        
        class_system = random.choice(NationSocialClassTypes)
        family_type = random.choice(NationFamilyTypes)
        inequalities = random.choice(NationInequalities)
        
        self.set_hallmark("Social", {"Class System" : class_system, "Family Type" : family_type, "Inequality" : inequalities})
        
        return self
        
        
    
