import random

from src.Modules.Settlement.Settlement import Settlement
from src.Modules.Utilities.utlil_helpers import process_duplicates

class City(Settlement):
    def __init__(self):
        """
        Initializes a new instance of the City class.
        """
        super().__init__()
        
        #Flags
        self.isCapital = False
        self.isProductionPriority = False
        self.isEntertainmentPriority = False
        self.isPlutocracy = False
        self.isMagocracy = False
        self.isTheocracy = False
        self.isSmallGovernmentParty = False
        self.isUnderworldEnterprise = False
        self.isMerchantMonarch = False
        
        #Variables
        self.type = "City"
        self.name = self.generate_name()
        self.origin = "Unknown"
        self.priority = "Unknown"
        self.city_outskirts = []
        self.stewardship = "Unknown"
        self.fortification = "Unknown"
        self.market_square = "Unknown"
        self.merchant_overflow = "Unknown"
        self.underground_passages = "Unknown"
        self.population_density = "Unknown"
        self.demographics = "Unknown"
        self.population_wealth = "Unknown"
        self.visitor_traffic = "Unknown"
        self.disposition = "Unknown"
        self.night_activity = "Unknown"
        self.leadership = "Unknown"
        self.law_enforcement = "Unknown"
        self.general_crime = "Unknown"
        self.organised_crime = "None"
        self.districts = []
        self.noteworthy_officals = []
        self.underground_activities = "Unknown"
        
    def generate(self):
        
        self.origin = self.generate_origin()
        self.priority = self.generate_priority()
        self.age = self.generate_age()
        self.size = self.generate_size()
        self.generate_city_outskirts()
        self.stewardship = self.generate_stewardship()
        self.condition = self.generate_condition()
        self.environment = self.generate_environment()
        self.fortification = self.generate_fortification()
        self.market_square = self.generate_market_square()
        self.merchant_overflow = self.generate_merchant_overflow()
        self.underground_passages = self.generate_underground_passages()
        self.population_density = self.generate_population_density()
        self.demographics = self.generate_demographics()
        self.population_wealth = self.generate_population_wealth()
        self.visitor_traffic = self.generate_visitor_traffic()
        self.disposition = self.generate_disposition()
        self.night_activity = self.generate_night_activity()
        self.leadership = self.generate_leadership()
        self.law_enforcement = self.generate_law_enforcement()
        self.general_crime = self.generate_general_crime()
        self.generate_districts()
        self.generate_noteworthy_officals()
        self.underground_activities = self.generate_underground_activities()
        
        return self
    
    def generate_origin(self):
        return random.choices([
            "Invading Occupation: The city's foundations were laid by an external conquering force that initially established a military camp. Over time, this encampment morphed into permanent structures and the strength of their position ensured the settlement's growth.",
            "Tribal Home: The location of the city was originally a settlement for a native tribe. Through continual development, it expanded into the bustling city that exists today.",
            "Natural Progression - Trading Post: What began as a small trading outpost gradually drew enough commerce to justify expansions. It developed into a town and, as commerce continued to boom, it became a city.",
            "Repurposed History: The city was established upon the site of ancient ruins. While some ruins have been preserved as historical landmarks, others have been repurposed or integrated into the city's new structures.",
            "Natural progression - Village: Originating as a cluster of simple dwellings, the village swelled in population as more individuals settled down, leading to the need for expansion and the transformation into a city. Signs of its modest origins are still present in some areas.",
            "Haven: The location served as sanctum for those escaping a catastrophe or persecution, or perhaps for rebels or outlaws seeking to create an independent community.",
            "Advantageous Position: The city was strategically founded at a location replete with advantageous geographical features like a natural chokepoint or a dominant high ground. As its advantages became apparent, the settlement flourished.",
            "Prison: This place started as a colony for exiles or prisoners. Over time, it transitioned into a recognized city, possibly because of a successful uprising or because the controlling power was overthrown or altered its stance towards the colony.",
            "Agriculture: Beginning as a concentrated farming community, the area attracted cultivation experts and industrious workers. High productivity brought more people to the area, resulting in the formation of buildings to accommodate the population, leading to the city's establishment for the sake of convenience and living standards.",
            "Magical: The birth of the city can be traced back to magical origins, be it through the presence of magical beings, enchanted structures, or a specific location where magical energies converge. Alternatively, it might have been consciously created by a powerful magic user."
        ])
        
    def generate_priority(self):
        city_priority = random.choice([
            "Control: The city is a regional power with patrolled roads and a strong military presence.",
            "Trade: The city thrives on trade, with a bustling economy and beneficial trade taxes.",
            "Enlightenment: The city values enlightenment, with wise leadership and a focus on knowledge and culture.",
            "Entertainment: Known for entertainment, the city has a history of performances, pubs, and celebrations.",
            "Production: The city is centered on production, specializing in a key good or resource like crops or ore.",
            "Faith: The city is a hub of faith with pilgrimages and multiple places of worship."
        ])
        
        if "Control:" in city_priority:
            self.modifiers.law_enforcement_modifier += 3
        elif "Trade:" in city_priority:
            self.modifiers.population_wealth_modifier += 1
        elif "Enlightenment:" in city_priority:
            # Generate a Scholar District
            pass
        elif "Entertainment:" in city_priority:
            self.isEntertainmentPriority = True
        elif "Production:" in city_priority:
            self.isProductionPriority = True
        elif "Faith:" in city_priority:
            # Generate a Temple District
            pass
        
        return city_priority
        
        
    def generate_age(self):
        result = random.randint(1, 10)
        age_ranges = [
            (range(1, 3), (-2, "Recent: City has been around for < 10 years")),
            (range(3, 5), (-1, "Established: Been around anywhere from 10 - 100 years")),
            (range(5, 7), (0, "Mature: Been around for about 100 - 300 years")),
            (range(7, 9), (1, "Old: Been Around for about 300 - 1000 years")),
            (range(9, 11), (2, "Ancient: Older then anyone can remember")),
        ]
        
        for age_range, age_info in age_ranges:
            if result in age_range:
                pop_dense_mod, description = age_info
                self.modifiers.population_density_modifier += pop_dense_mod
                return description
            
    def generate_size(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.size_modifier, 20), 1)
        size_ranges = [
            (range(1, 3), (-4, "Very Small (Supports roughly 8000 - 15000 people)")),
            (range(3, 7), (-1, "Small (Supports roughly 16000 - 23000 people)")),
            (range(7, 15), (0, "Medium (Supports roughly 24000 - 31000 people)")),
            (range(15, 19), (2, "Large (Supports roughly 32000 - 39000 people)")),
            (range(19, 24), (6, "Very Large (supports roughly 40000 - 450000 people )"))
        ]
        
        for size_range, size_info in size_ranges:
            if roll in size_range:
                districts_roll, desc = size_info
                self.modifiers.number_of_districts_modifier += districts_roll
                return desc
    def generate_city_outskirts(self):
        size_roll_outside_city = {
           "Very Small": 5,
           "Small": 4,
           "Medium": 3,
           "Large": 2,
           "Very Large": 1 
        }
        
        roll_amount = 0
        
        for key, value in size_roll_outside_city.items():
            if self.size in key:
                roll_amount += value
        
        outside_city_roll_table = [
            (range(1, 5), "None"),
            (range(5, 7), "Farming [Agriculture]. A group of farms, providing food for the city, are found on the nearest hospitable land under its control."),
            (range(7, 9), "Farming [Livestock]. A group of farms, providing livestock for the city, are found on the nearest hospitable land under its control."),
            (range(9, 11), "Resource Harvesting. Depending on the landscape and available resources (trees, minerals, ore, stone, etc.), a logging camp, mine, or quarry, belonging to the city, has been built nearby to harvest them, which it then uses or sells."),
            (range(11, 13), "Barrows. An area devoted to burial sites."),
            (range(13, 14), "Caravan Community. A nomadic group of people have taken to living on the surrounding land nearby. Does the city’s leadership have an issue with this? What about its residents?"),
            (range(14, 15), "Event Grounds. Tended grounds for games, duels, ceremonies, or other events."),
            (range(15, 16), "Family Estate. A wealthy family’s large estate is situated in the neighboring countryside."),
            (range(16, 17), "Hermit’s Cottage. A hermit lives near the city limits, beneath the notice of most of the inhabitants. They keep to themselves, but who are they? What do they gain by their close proximity?"),
            (range(17, 19), "Makeshift Settlement. A large mass of hovels, lean-tos, tents, and other improvised shelters have been built in the shadow of the city’s walls. Why? Do the leaders and residents care?"),
            (range(19, 21), "Medical Camp. A set of makeshift or, depending on the nature of what is being treated, permanent structures have been erected to tend to, or even quarantine, the sick or injured."),
            (range(20, 21), "Prison. Some sort of structure out here has been designated for holding prisoners or captives (for whatever reason) either temporarily or, perhaps, much longer term.")
        ]
        
        roll = random.randint(1, 20)
        
        for i in range(roll_amount):
            for outside_range, outside_info in outside_city_roll_table:
                if roll in outside_range:
                    self.city_outskirts.append(outside_info)
        
    def generate_stewardship(self):
        roll = random.randint(1, 20)
        
        stewardship_roll_table = [
            (range(1, 2), (-7, -13, -9, "Neglected. All of the fundamental elements of the city are being ignored, or are unable to be addressed.")),
            (range(2, 5), (-4, -6, -5, "Minimal. The fundamental elements of the city are being tended to, but at the bare minimum. This may be because of inexperienced leadership, misplaced priorities, lack of resources, or simple laziness, to name a few possible reasons.")),
            (range(5, 11), (-1, -3, -2, "Passing. The city’s fundamental elements are taken care of to a serviceable degree, though an inequality of attention is noticeable, and some areas seem to take priority over others. It could be that resources are not plentiful enough to cover everything, but those in charge are doing the best they can.")),
            (range(11, 17), (0, 0, 0, "Adequate. The city’s fundamental elements are all taken care of relatively competently, but some room for improvement still exists. Lack of capital, or involvement in more pressing matters such as external conflicts or disaster management, are possible explanations.")),
            (range(17, 20), (1, 3, 4, "Managed. The city’s fundamental elements are all accounted for and well attended to. Whoever is responsible is doing an admirable job.")),
            (range(20, 21), (5, 6, 8, "Disciplined. The city’s fundamental elements are firmly in hand, providing what it needs to perform at peak functionality. There is little to no room for improvement. Whoever is managing things is doing so expertly."))
        ]
        
        for roll_range, roll_info in stewardship_roll_table:
            if roll in roll_range:
                condition_mod, pop_wealth_mod, law_mod, desc = roll_info
                self.modifiers.general_condition_modifier += condition_mod
                self.modifiers.population_wealth_modifier += pop_wealth_mod
                self.modifiers.law_enforcement_modifier += law_mod
                return desc

    def generate_condition(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.general_condition_modifier, 20), 1)
        general_condition_roll_table = [
            (range(1, 2), (-2, "Squalid. The city is in a deplorable state, falling apart and filthy. Most buildings are a disgrace or in dire need of repair.")),
            (range(2, 5), (-1, "Dilapidated. Dirty and in disrepair, with some token efforts at cleanliness. Streets may be uneven or muddy, and structures are poorly maintained.")),
            (range(5, 13), (0, "Decent. Passable but not exceptional. Structures may lack aesthetics but are generally functional.")),
            (range(13, 20), (1, "Impressive. Well taken care of, with cleanliness a priority. Signs of wear may be apparent, but overall respectable quality.")),
            (range(20, 21), (2, "Magnificent. Incredible cleanliness, maintenance, and structural integrity. Attention to detail is evident throughout the city.")),
        ]

        for roll_range, roll_info in general_condition_roll_table:
            if roll in roll_range:
                district_con_mod, desc = roll_info
                self.modifiers.administration_district_condition_modifier += district_con_mod
                self.modifiers.arcane_district_condition_modifier += district_con_mod
                self.modifiers.botanical_district_condition_modifier += district_con_mod
                self.modifiers.craft_district_condition_modifier += district_con_mod
                self.modifiers.docks_district_condition_modifier += district_con_mod
                self.modifiers.industrial_district_condition_modifier += district_con_mod
                self.modifiers.market_district_condition_modifier += district_con_mod
                self.modifiers.merchant_district_condition_modifier += district_con_mod
                self.modifiers.scholar_district_condition_modifier += district_con_mod
                self.modifiers.slums_district_condition_modifier += district_con_mod
                return desc

    def generate_fortification(self):
        roll = random.randint(1, 20)
        fortification_roll_table = [
            (range(1, 2), (-5, "Unfortified. The city is exposed on all sides, lacking proper defenses except for natural barriers or buildings.")),
            (range(2, 9), (1, "Lightly Fortified. Basic fortifications provide minimal obstacle for enemies but deter wild animals. A simple gate can be barred in the evenings.")),
            (range(9, 16), (3, "Fortified. The city is surrounded by a substantial wall of wood or stone, patrolled by guards. Visitors pass through a main gate that can be barred at night.")),
            (range(16, 20), (5, "Heavily Fortified. A heavy wall with watchtowers surrounds the city. The gate is reinforced and additional watchtowers dot the countryside.")),
            (range(20, 21), (7, "Extremely Fortified. An imposing wall with manned watchtowers at regular intervals. The gate is reinforced and always guarded. The surrounding countryside is enclosed with its own fortified wall and watchtowers.")),
        ]
        for roll_range, roll_info in fortification_roll_table:
            if roll in roll_range:
                disposition_mod, desc = roll_info
                self.modifiers.disposition_modifier += disposition_mod
                return desc 
        
    def generate_market_square(self):
        market_square_size_roll = max(min(random.randint(1, 6) + self.modifiers.market_square_modifier, 6), 1)
        market_square_size_table = [
            (range(1, 3), 'Tight'),
            (range(3, 5), 'Ample'),
            (range(5, 6), 'Spacious'),
        ]
        market_square_rules = random.choice([
            'First Come, First Served - No Fee basis',
            'First Come, First Served - Fee basis',
            'Lease',
            'Bid'
        ])
        
        market_size =''
        
        for size_range, size_info in market_square_size_table:
            if market_square_size_roll in size_range:
                market_size = size_info
        
        market_square = 'The Market Square is of a ' + market_size + " size. The rules of running a stall comes in the form of a " + market_square_rules + "."
        
        return market_square
        
    def generate_merchant_overflow(self):
        roll = random.choice([
            "Banned: No extra vendors allowed outside the town. Guards enforce this.",
            "Unpatrolled: Extra vendors allowed, but not monitored. Riskier areas.",
            "Monitored: Guards patrol occasionally. Areas less maintained, fewer people.",
            "Encouraged: Extra vendors welcomed outside town. Regular patrols if possible."
        ])
        
        if 'Banned:' in roll:
            self.modifiers.law_enforcement_modifier += 1
            
        return roll   
        
    def generate_underground_passages(self):
        roll = random.randint(1,20)
        underground_passages_roll_table = [
            (range(1, 9), "None. No significant underground passages exist beneath the city."),
            (range(9, 15), "Sewers. A network of drains, pipes, and trenches lies beneath the city. The condition of the sewers reflects the overall condition of the settlement."),
            (range(15, 18), "Natural Caves. Natural cave systems exist below the city, possibly undiscovered."),
            (range(18, 20), "Tunnels. A series of purpose-built or clandestine tunnels exist beneath the city, possibly constructed for maintenance, defense, or secret purposes."),
            (range(20, 21), "Forgotten Crypts. Old burial chambers and tombs lie deep beneath the city, likely unknown to most residents.")
        ]
        for roll_range, roll_info in underground_passages_roll_table:
            if roll in roll_range:
                return roll_info
        
    def generate_population_density(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.population_density_modifier, 20), 1)
        population_density_roll_table = [
            (range(1, 3), (-2, "Skeleton. The city has a minimal population, just enough for basic functioning.")),
            (range(3, 7), (-1, "Sparse. There are people in the city, but it's not bustling. Few individuals are seen on the streets.")),
            (range(7, 15), (0, "Populous. A moderate number of people reside in the city. The streets are populated, but not crowded.")),
            (range(15, 19), (1, "Dense. The city has a large population with few vacant buildings. In busy areas, space is limited.")),
            (range(19, 21), (2, "Crowded. The city is packed with people, even camping outside the walls. Movement is difficult and bumping into others is common."))
        ]
        
        for density_range, density_info in population_density_roll_table:
            if roll in density_range:
                night_mod, description = density_info
                self.modifiers.night_activity_modifier += night_mod
                return description

    def generate_demographics(self):
        roll = random.randint(1,20)
        
        demographics_table = [
            (range(1, 5), "100% Primary Race"),
            (range(5, 8), "60% Primary Race + 40% Secondary Race"),
            (range(9, 15), "50% Primary Race + 25% Secondary Race + 15% tertiary Race + 10% Other Races"),
            (range(15, 18), "20% Primary Race + all other Races in varieties"),
            (range(18, 20), "80% Primary Race + 20% Secondary Race"),
            (range(20, 21), "No Racial Representation, Ever shifting")
        ]
        
        for demographic_range, demograhpic_info in demographics_table:
            if roll in demographic_range:
                return demograhpic_info
            
    def generate_population_wealth(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.population_wealth_modifier, 20), 1)
        population_wealth_roll_table = [
            (range(1, 3), (-2, "Destitute. The majority of the population lacks the barest essentials for survival.")),
            (range(3, 7), (-1, "Impoverished. About half of the population struggles to meet basic needs.")),
            (range(7, 15), (0, "Average. Most residents live modestly, with only a minority facing significant hardship.")),
            (range(15, 18), (-1, "Prosperous. The majority enjoy a good standard of living, with some living comfortably.")),
            (range(18, 20), (-2, "Wealthy. Nearly everyone lives comfortably, with many living well and some very prosperous.")),
            (range(20, 21), (-3, "Affluent. The entire city lives comfortably, with a significant portion enjoying luxury."))
        ]
        for roll_range, roll_info in population_wealth_roll_table:
            if roll in roll_range:
                crime_mod, description = roll_info
                self.modifiers.general_crime_modifier += crime_mod
                return description

    def generate_visitor_traffic(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.visitor_traffic_modifier, 20), 1)
        visitor_traffic_roll_table = [
            (range(1, 3), (0, "Mostly Locals. Few visitors from outside the city, not impacting congestion.")),
            (range(3, 7), (1, "Groups. Fair amount of visitors, slightly increasing congestion.")),
            (range(7, 13), (2, "Crowds. Noticeable number of visitors, increasing congestion.")),
            (range(13, 18), (3, "Droves. Large groups of people regularly visit, significantly increasing congestion.")),
            (range(18, 20), (4, "Masses. Huge groups of people frequently visit, potentially causing difficulties if the city can't handle the influx.")),
            (range(20, 21), (5, "Multitudes. Massive groups of people throng the streets, causing congestion to be an ever-present issue."))
        ]
        
        for roll_range, roll_info in visitor_traffic_roll_table:
            if roll in roll_range:
                night_mod, description = roll_info
                self.modifiers.night_activity_modifier += night_mod
                return description

    def generate_disposition(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.disposition_modifier, 20), 1)
        disposition_table = [
            (range(1, 3), "Hostile: Locals are unwelcoming of vistors (Cityfolk are cold, passive-aggressive or violent)"),
            (range(3, 7), "Unfriendly: Locals are suspious of vistors (Cityfolk are full of contempt, fear or suspicion)"),
            (range(7, 15), "Neutral: Locals are standoffish showing no emotion but can be made friendly (Cityfolk are Indifferent)"),
            (range(15, 19), "Friendly: Locals are Welcoming within the bounds of their rules (Cityfolk are Happy or Content)"),
            (range(19, 21), "Open: Local revel in the idea of vistors and their town is build to show it (Cityfolk are Joyous or Celebatory.)")
        ]
        
        for disposition_range, disposition_info in disposition_table:
            if roll in disposition_range:
                return disposition_info
            
    def generate_night_activity(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.night_activity_modifier, 20), 1)
        night_activity_table = [
            (range(1, 2), "Dark - Streets empty, town closed, quiet and peaceful. If city has a Gate it is closed barring outsiders from entry"),
            (range(2, 4), "Quiet - Only inns and taverns open till midnight. Innkeeper must be woken for late guests. If the city has a gate, it is closed and barred. Guards will usually let visitors in, but will discourage wandering."),
            (range(4, 13), "Slow - Almost everything closed except taverns open till early morning, inns open perpetually. Gate is Closed but guards will open it if needed."),
            (range(13, 18), "Active - Inns and taverns open perpetually, some shops and services available. if City has a gate it is open but ready to be closed by guards."),
            (range(18, 20), "Lively - Little difference between day and night, shops and services remain open constantly. If there is a Gate it is only closed in dire circumstances."),
            (range(20, 21), "Raucous - The city comes alive at night. Inns and taverns bustle with customers, and parties can often be heard. Some establishments only open after dark. Night markets offer goods and services for those who keep late hours or don't need sleep."),
        ]
        
        for night_range, night_info in night_activity_table:
            if roll in night_range:
                return night_info
        
    def generate_leadership(self):
        roll = random.randint(1, 100)
        
        leadership_ranges = [
            (range(1, 16), ("Elected Council")),
            (range(16, 31), ("Mayor")),
            (range(31, 46), ("Hereditary")),
            (range(46, 61), ("Merchant Monarch")),
            (range(61, 76), ("Military Officer")),
            (range(76, 91), (f"Oligarchy Run by {random.choice(['Merchants (plutocracy)', 'Mages (Magocracy)', 'Priests (Theocracy)', 'A small group of people'])}")),
            (range(91, 100), ("Underworld or Criminal Enterprise")),
            (range(100, 101), ("Anarcho-Syndicalist Commune"))
        ]
        for leadership_range, leadership_info in leadership_ranges:
            if roll in leadership_range:
                if leadership_info == "Merchant Monarch":
                    self.isMerchantMonarch = True
                elif leadership_info == "Military Officer":
                    self.modifiers.law_enforcement_modifier += 1
                elif "Oligarchy" in leadership_info:
                    if "plutocracy" in leadership_info:
                        self.isPlutocracy = True
                    elif "Magocracy" in leadership_info:
                        self.isMagocracy = True
                    elif "Theocracy" in leadership_info:
                        self.isTheocracy = True
                    elif "A small group of people" in leadership_info:
                        self.isSmallGovernmentParty = True
                elif leadership_info == "Underworld or Criminal Enterprise":
                    self.isUnderworldEnterprise = True
                    self.modifiers.general_crime_modifier += -2
                return leadership_info
        
    def generate_law_enforcement(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.law_enforcement_modifier, 20), 1)
        law_enforcement_roll_table = [
            (range(1, 2), (-5, "None. Without a significant law enforcement presence, crime can easily flourish, leading to lawlessness and disorder.")),
            (range(2, 5), (-3, "Skeleton City Watch. Minimal staffing allows for basic gate and watchtower monitoring, but crime control is severely limited.")),
            (range(5, 12), (-1, "City Watch. Led by a single captain, the watch maintains basic security with periodic patrols but struggles to cover all areas effectively.")),
            (range(12, 18), (+0, "Robust City Watch. With additional sergeants, the watch can provide extra support at key points and establish multiple daily patrols, maintaining a moderate level of security.")),
            (range(18, 21), (+2, "Extensive City Watch. With several sergeants, the watch ensures thorough guarding of key points, constant perimeter patrols, and regular citywide patrols, significantly reducing crime rates."))
        ]
        
        for roll_range, roll_info in law_enforcement_roll_table:
            if roll in roll_range:
                crime_mod, description = roll_info
                self.modifiers.general_crime_modifier += crime_mod
                return description

    def generate_general_crime(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.general_crime_modifier, 20), 1)
        hasOrgansiedCrime = False
        
        if self.isUnderworldEnterprise:
            hasOrgansiedCrime = True
            
        general_crime_roll_table = [
            (range(1, 3), (True, 4, "Dangerous. High levels of crime plague the streets, with frequent incidents of vandalism, muggings, and violence. Organized crime is prevalent.")),
            (range(3, 7), (True, 4, "Frequent. Theft and violence are common, making the streets unsafe. Organized crime operates openly.")),
            (range(7, 15), (True, 3, "Common. Incidents of crime occur regularly, with many residents having been victims. Organized crime is known but not pervasive.")),
            (range(15, 19), (False, 2, "Uncommon. Theft and violence occur occasionally, requiring vigilance.")),
            (range(19, 21), (False, 1, "Infrequent. Crime is rare, and most residents feel safe in their city."))
        ]
        
        for roll_range, roll_info in general_crime_roll_table:
            if roll in roll_range:
                organsied_crime, urban_mod, description = roll_info
                self.modifiers.urban_encounter_modifier += urban_mod
                if hasOrgansiedCrime == False:
                    hasOrgansiedCrime = organsied_crime
 
                if hasOrgansiedCrime:
                    self.organised_crime = self.generate_organised_crime()
                return description
        
    def generate_organised_crime(self):    
        roll = random.randint(1,20)
        organized_crime_roll_table = [
            (range(1, 3), "Completely Secret. The organization operates covertly, with contacts handled through multiple layers of separation to maintain secrecy."),
            (range(3, 7), "Whispers. Rumors of a criminal organization circulate quietly, with few openly acknowledging its existence."),
            (range(7, 15), "Talk. Most believe in the existence of organized crime, which operates quietly yet ambitiously, often with ties to government officials."),
            (range(15, 19), "Barely Hidden. The organization casts a looming shadow, its presence felt but its members unknown. Obstacles to its interests are swiftly dealt with."),
            (range(19, 21), "Open. The organization's presence is widely known, possibly even involved in running the city. It operates with impunity, with little fear of reprisal.")
        ]

        for roll_range, roll_info in organized_crime_roll_table:
            if roll in roll_range:
                return roll_info
    
    def calculate_district_size(self):
        roll_size = random.randint(1,20)
        district_size_table = [
            (range(1,3), 2),
            (range(3,11), 3),
            (range(11,16), 4),
            (range(16,20), 5),
            (range(20,21), 6),
        ]
        
        for roll_range, roll_info in district_size_table:
            if roll_size in roll_range:
                return roll_info
    
    def generate_local_fervency(self):
        roll = random.randint(1, 20)
        visibility_table = [
            (range(1, 4), "Unseen. To those outside the following, it is not clear that the group exists."),
            (range(4, 8), "Quiet. Adherents to the faith are inconspicuous, unless one knows what to look for (perhaps particular gestures, items of clothing, or phrases)."),
            (range(8, 13), "Subtle. Followers of the faith may be identifiable, but remain very reserved."),
            (range(13, 17), "Moderate. The pious are confident and unafraid to display their faith openly, but do not encroach upon the wider populus uncalled for."),
            (range(17, 20), "Fervent. Followers are outspoken, with little or no fear of reproach. They may sing or speak to the masses."),
            (range(20, 21), "Zealous. Adherents are utterly and unthinkingly devout, forcing their doctrine upon their surroundings and peers, or taking actions that further their cause regardless of personal cost. Though typically seen as negative, this could also be a positive, such as a church of light rising up in an evil kingdom, helping those in need, even if it puts themselves in peril.")
        ]

        for visibility_range, visibility_description in visibility_table:
            if roll in visibility_range:
                return visibility_description
    
    def generate_worship_place(self):
        worship_place_table = [
            (range(1, 2), "Secret. The place of worship’s size is unclear, as the location is not publicly known."),
            (range(2, 8), "Altar. A small shrine or, perhaps, a tiny shack, usually evincing some various items or images relating to that which the faith venerates."),
            (range(8, 15), "Oratory. A modest building with seating for attendees, appointed with various items or images relating to that which the faith venerates."),
            (range(15, 18), "Sanctuary. A large, well-appointed structure, able to comfortably accommodate up to a few hundred people."),
            (range(18, 20), "Temple. A grand building, replete with elements like high ceilings, plush furnishings, and other impressive ornamental and/or architectural features. It can hold nearly a thousand attendees."),
            (range(20, 21), "Great Temple. An awe-inspiring structure, devoted to that which it venerates. No expense was spared in its construction. It might display such elements as stunning frescos, elaborate stained-glass scenes, and towering, gilded statues. Walking into a great temple is a rare and striking experience for those who do not live near one.")
        ]
        
        fervency = self.generate_local_fervency()
        alignment_weights = [10, 40, 50]
        alignment_choices = ['evil', 'neutral', 'good']
        selected_alignment = random.choices(alignment_choices, weights=alignment_weights, k=1)[0]
        roll = roll = max(min(random.randint(1, 20) + self.modifiers.worship_place_size_modifier, 20), 1)
        for worship_place_range, worship_place_info in worship_place_table:
            if roll in worship_place_range:
                return worship_place_info + " Worship is of a " + selected_alignment + " Deity. This Deities followers are " + fervency
    
    
    def generate_districts(self):
        size = self.calculate_district_size()
        
        if self.isMerchantMonarch:
            size -= 1
            self.districts.append(self.generate_merchant_district())
        elif self.isPlutocracy:
            size -= 1
            self.districts.append(self.generate_merchant_district())
        elif self.isMagocracy:
            size -= 1
            self.districts.append(random.choice([self.generate_arcane_district(), self.generate_scholar_district()]))
        elif self.isTheocracy:
            size -= 1
            self.districts.append(self.generate_temple_district())
        elif self.isSmallGovernmentParty:
            size -= 1
            self.districts.append(random.choices(self.generate_administration_district(), self.generate_craft_district(), self.generate_industrial_district(), self.generate_upper_class_district()))
        
        district_types = {
            1: self.generate_administration_district(),
            2: self.generate_arcane_district(),
            3: self.generate_botanical_district(),
            4: self.generate_craft_district(),
            5: self.generate_docks_district(),
            6: self.generate_industrial_district(),
            7: self.generate_market_district(),
            8: self.generate_merchant_district(),
            9: self.generate_scholar_district(),
            10: self.generate_slums_district(),
            11: self.generate_temple_district(),
            12: self.generate_upper_class_district()
        }
        
        for _ in range(size):
            roll = random.randint(1,12)
            self.districts.append(district_types[roll])
    
    def generate_district_condition(self, condition_modifier, quality_modifier, isSlums = False):
        
        general_condition = {
            1:"Squalid. The city is in a deplorable state, falling apart and filthy. Most buildings are a disgrace or in dire need of repair.",
            2:"Dilapidated. Dirty and in disrepair, with some token efforts at cleanliness. Streets may be uneven or muddy, and structures are poorly maintained.",
            3:"Decent. Passable but not exceptional. Structures may lack aesthetics but are generally functional.",
            4:"Impressive. Well taken care of, with cleanliness a priority. Signs of wear may be apparent, but overall respectable quality.",
            5:"Magnificent. Incredible cleanliness, maintenance, and structural integrity. Attention to detail is evident throughout the city.",
        }
        
        district_conditions = [
            (range(1, 4), -2, -2),
            (range(4, 8), -1, -1),
            (range(8, 14), 0, 0),
            (range(14, 18), 1, 1),
            (range(18, 21), 2, 2)
        ]
        roll = 0
        if isSlums:
            roll = max(min(random.randint(1, 4) + condition_modifier, 4), 1)
        else:
            roll =  max(min(random.randint(1, 20) + condition_modifier, 20), 1)
        for condition_range, modifier, condition_adjustment in district_conditions:
            if roll in condition_range:
                quality_modifier += modifier
                condition = ''
                for k, v in general_condition.items():
                    if self.condition in v:
                        condition = general_condition[max(min(k+condition_adjustment, 5),1)]
                        break
                return condition

    def generate_district_entry(self, crime_modifier):
        roll = random.randint(1,12)
        district_entry_table = [
            (range(1, 5), 0,"Open. Entrance to the district is unrestricted."),
            (range(5, 8), 1,"Lightly Guarded. The district entrance has a token guard presence."),
            (range(8, 11), 2,"Guarded. The district entrance has a strong guard presence."),
            (range(11, 13), 3,"Gated & Guarded. The district entrance is barred by a gate with guards."),
        ]
        for condition_range, modifier, description in district_entry_table:
            if roll in condition_range:
                crime_modifier += modifier
                return description
    
    def generate_district_crime(self, condition, modifier):
        if "Squaild" in condition:
            modifier += -2
        elif "Dilapidated" in condition:
            modifier += -1
        elif "Decent" in condition:
            modifier += 0
        elif "Impressive" in condition:
            modifier += -1
        elif "Magnificent" in condition:
            modifier += -2
        
        general_crime = {
            1:"Dangerous. High levels of crime plague the streets, with frequent incidents of vandalism, muggings, and violence. Organized crime is prevalent.",
            2:"Frequent. Theft and violence are common, making the streets unsafe. Organized crime operates openly.",
            3:"Common. Incidents of crime occur regularly, with many residents having been victims. Organized crime is known but not pervasive.",
            4:"Uncommon. Theft and violence occur occasionally, requiring vigilance.",
            5:"Infrequent. Crime is rare, and most residents feel safe in their city."
        }   
        
        district_crime = [
            (range(1, 4), -2),
            (range(4, 8), -1),
            (range(8, 14), 0),
            (range(14, 18), 1),
            (range(18, 21), 2)
        ] 
        
        roll =  max(min(random.randint(1, 20) + modifier, 20), 1)
        for condition_range, crime_adjustment in district_crime:
            if roll in condition_range:
                crime = ''
                for k, v in general_crime.items():
                    if self.general_crime in v:
                        crime = general_crime[max(min(k+crime_adjustment, 5),1)]
                        break
                return crime
    
    def generate_district_housing(self, type):
        roll = random.randint(1,12)
        district_housing_table = [
            (range(1, 6), "None"),
            (range(6, 10), "Limited: Only a few live here; the district may be predominantly a place of business or functionality, or perhaps people avoid living here for another, less innocent reason."),
            (range(10, 12), "Moderate. A fair amount of the buildings in the district house residents."),
            (range(12, 13), "Extensive. A significant amount of the district`s buildings are housing for residents."),
        ]
        for condition_range, housing in district_housing_table:
            if roll in condition_range:
                if ("Slums" in type and housing == "None") or ("Upper Class" in type and housing == "None"):
                    return self.generate_district_housing(type)
                else:
                    return housing
    
    def calculate_additional_location_amount(self):
        district_additional_locations_map = {
           "Very Small": 1,
           "Small": 2,
           "Medium": 3,
           "Large": 4,
           "Very Large": 5
        }
        
        for key in district_additional_locations_map.keys():
            if key in self.size:
                return district_additional_locations_map[key]
    def calculate_quality(self, condition_modifier):
        quality = [
            (range(1,5), "Poor"),
            (range(5,11), "Good"),
            (range(11,13), "Fine")
        ]
        roll = max(min(random.randint(1, 12) + condition_modifier, 12), 1)
        for roll_range, roll_info in quality:
            if roll in roll_range:
                return roll_info
    def generate_magic_shop(self):
        return "Magic Shop: " + random.choice(["Armour", "Books", "Clothing", "Jewelry", "Weapons", "Miscellaneous & Curiosities" ])
    def generate_administration_district(self):
        district_type = "Administration. This district has a focus on government and civil matters."
        condition = self.generate_district_condition(self.modifiers.administration_district_condition_modifier, self.modifiers.administration_district_quality_modifier)
        additional_locations = self.calculate_additional_location_amount()
        non_commerical_locations = ["Courthouse", "Chancery", "Townhall", "Treasury"]
        shops = []
        services = ["Hired Help: Scribes and Clerks"]
        religious_sites = []
        
        if random.randint(1, 100) < 30:
            amount = random.randint(1,3)
            for _ in range(amount):
                religious_sites.append(self.generate_worship_place())
        else:
            religious_sites.append("None")
            
        if self.isEntertainmentPriority:
            entertainment_buildings = {
                1: ("House of Leisure", "service"),
                2: ("Club", "service"),
                3: ("Tavern", "service"),
                4: ("Inn", "service"),
                5: ("Bathhouse", "service"),
                6: ("Amphitheater", "non-commercial")
            }
            
            building_info = entertainment_buildings[random.randint(1,6)]
            building, building_type = building_info
            if building_type == "shop":
                shops.append(building + " (Of " + self.calculate_quality(self.modifiers.administration_district_quality_modifier) + " quality.)")
            elif building_type == "service":
                    services.append(building)
            else:
                non_commerical_locations.append(building)

        locations = {
            1: ("Baker", "shop"),
            2: ("Tailor", "shop"),
            3: ("Alchemist", "shop"),
            4: ("Cobbler", "shop"),
            5: ("Luxury Furnishings", "shop"),
            6: ("Rare Libations & Fare", "shop"),
            7: ("Barber", "service"),
            8: ("Bathhouse", "service"),
            9: ("Doctor/Apothecary", "service"),
            10: ("House of Leisure", "service"),
            11: ("Inn", "service"),
            12: ("Club", "service"),
            13: ("Tavern", "service"),
            14: ("Hired Help", "service"),
            15: ("Archives/Library", "non-commercial"),
            16: ("Academy/University", "non-commercial"),
            17: ("Schoolhouse", "non-commercial"),
            18: ("Amphitheater", "non-commercial")
        }
        
        hired_help = {
            1: "Brutes & Brawlers",
            2: "Cloak & Dagger",
            3: "Bows & Slings",
            4: "Scribes & Clerks",
            5: "Guides & Trackers",
            6: "Caravan & Mount",
            7: "Arcane Academics",
            8: "Magic Mercenaries",
            9: "Priestly Guidance",
            10: "Hands of the Divine"
        }

        for _ in range(additional_locations):
            roll = random.randint(1,18)
            location, location_type = locations[roll]
            
            if location_type == "shop":
                shops.append(location + " (Of " + self.calculate_quality(self.modifiers.administration_district_quality_modifier) + " quality.)")
            elif location_type == "service":
                if location == "Hired Help":
                    services.append(location + ": " + hired_help[random.randint(1,10)])
                else:
                    services.append(location)
            else:
                non_commerical_locations.append(location)
            
        
        district = {
            "type": district_type,
            "condition": condition,
            "entry": self.generate_district_entry(self.modifiers.administration_district_crime_modifier),
            "crime": self.generate_district_crime(condition, self.modifiers.administration_district_crime_modifier),
            "housing": self.generate_district_housing(district_type), 
            "non_commercial": non_commerical_locations,
            "shops": shops,
            "services": services,
            "religious_places" : religious_sites
        }
        
        return district
    def generate_arcane_district(self):
        district_type = "Arcane. This district has a focus on magical matters."
        condition = self.generate_district_condition(self.modifiers.arcane_district_condition_modifier, self.modifiers.arcane_district_quality_modifier)
        additional_locations = self.calculate_additional_location_amount()
        non_commerical_locations = ["Archives/Library", "Academy/University"]
        shops = [self.generate_magic_shop(), self.generate_magic_shop()]
        services = ["Hired Help: " + random.choice(["Arcane Academics", "Magic Mercenaries"])]
        religious_sites = []
        
        if random.randint(1, 100) < 10:
            amount = random.randint(1,3)
            for _ in range(amount):
                religious_sites.append(self.generate_worship_place())
        else:
            religious_sites.append("None")
            
        if self.isEntertainmentPriority:
            entertainment_buildings = {
                1: ("House of Leisure", "service"),
                2: ("Club", "service"),
                3: ("Tavern", "service"),
                4: ("Inn", "service"),
                5: ("Bathhouse", "service"),
                6: ("Amphitheater", "non-commercial")
            }
            
            building_info = entertainment_buildings[random.randint(1,6)]
            building, building_type = building_info
            if building_type == "shop":
                shops.append(building + " (Of " + self.calculate_quality(self.modifiers.administration_district_quality_modifier) + " quality.)")
            elif building_type == "service":
                    services.append(building)
            else:
                non_commerical_locations.append(building)
        
        locations = {
            1: ("General Store", "shop"),
            2: ("Tailor", "shop"),
            3: ("Weaver", "shop"),
            4: ("Alchemist", "shop"),
            5: ("Artist", "shop"),
            6: ("Rare Botanicals", "shop"),
            7: (self.generate_magic_shop(), "shop"),
            8: (self.generate_magic_shop(), "shop"),
            9: ("Barber", "shop"),
            10: ("Soothsayer", "service"),
            11: ("House of Leisure", "service"),
            12: ("Club", "service"),
            13: ("Tavern", "service"),
            14: ("Hired Help: Arcane Academics", "service"),
            15: ("Hired Help: Magic Mercenaries", "service"),
            16: ("Forum", "non-commercial"),
            17: ("Schoolhouse", "non-commercial"),
            18: ("Lodge", "non-commercial")
        }
        
        

        for _ in range(additional_locations):
            roll = random.randint(1,18)
            location, location_type = locations[roll]
            
            if location_type == "shop":
                shops.append(location + " (Of " + self.calculate_quality(self.modifiers.arcane_district_quality_modifier) + " quality.)")
            elif location_type == "service":
                services.append(location)
            else:
                non_commerical_locations.append(location)
            
        
        district = {
            "type": district_type,
            "condition": condition,
            "entry": self.generate_district_entry(self.modifiers.arcane_district_crime_modifier),
            "crime": self.generate_district_crime(condition, self.modifiers.arcane_district_crime_modifier),
            "housing": self.generate_district_housing(district_type), 
            "non_commercial": non_commerical_locations,
            "shops": shops,
            "services": services,
            "religious_places" : religious_sites
        }
        
        return district
    def generate_botanical_district(self):
        district_type = "Botanical. This district has a focus on nature."
        condition = self.generate_district_condition(self.modifiers.botanical_district_condition_modifier, self.modifiers.botanical_district_quality_modifier)
        additional_locations = self.calculate_additional_location_amount()
        non_commerical_locations = ["Outdoor Recreational Area"]
        shops = []
        services = ["Inn", "Stable"]
        religious_sites = []
        
        if random.randint(1, 100) < 30:
            amount = random.randint(1,3)
            for _ in range(amount):
                religious_sites.append(self.generate_worship_place())
        else:
            religious_sites.append("None")
        
        if self.isEntertainmentPriority:
            entertainment_buildings = {
                1: ("House of Leisure", "service"),
                2: ("Club", "service"),
                3: ("Tavern", "service"),
                4: ("Inn", "service"),
                5: ("Bathhouse", "service"),
                6: ("Amphitheater", "non-commercial")
            }
            
            building_info = entertainment_buildings[random.randint(1,6)]
            building, building_type = building_info
            if building_type == "shop":
                shops.append(building + " (Of " + self.calculate_quality(self.modifiers.administration_district_quality_modifier) + " quality.)")
            elif building_type == "service":
                    services.append(building)
            else:
                non_commerical_locations.append(building)
        
        locations = {
            1: ("Baker", "shop"),
            2: ("Tailor", "shop"),
            3: ("Weaver", "shop"),
            4: ("Alchemist", "shop"),
            5: ("Artist", "shop"),
            6: ("Cobbler", "shop"),
            7: ("Rare Botanicals", "shop"),
            8: ("Rare Libations and Fare", "shop"),
            9: (self.generate_magic_shop(), "shop"),
            10: ("Doctor/Apothecary", "service"),
            11: ("House of Leisure", "service"),
            12: ("Inn", "service"),
            13: ("Soothsayer", "service"),
            14: ("Tavern", "service"),
            15: ("Hired Help: Guides and Trackers", "service"),
            16: ("Outdoor Recreational Area", "non-commercial"),
            17: ("Dance Hall", "non-commercial"),
            18: ("Garden", "non-commercial")
        }
        
        

        for _ in range(additional_locations):
            roll = random.randint(1,18)
            location, location_type = locations[roll]
            
            if location_type == "shop":
                shops.append(location + " (Of " + self.calculate_quality(self.modifiers.botanical_district_quality_modifier) + " quality.)")
            elif location_type == "service":
                services.append(location)
            else:
                non_commerical_locations.append(location)
            
        
        district = {
            "type": district_type,
            "condition": condition,
            "entry": self.generate_district_entry(self.modifiers.botanical_district_crime_modifier),
            "crime": self.generate_district_crime(condition, self.modifiers.botanical_district_crime_modifier),
            "housing": self.generate_district_housing(district_type), 
            "non_commercial": non_commerical_locations,
            "shops": shops,
            "services": services,
            "religious_places" : religious_sites
        }
        
        return district
    def generate_craft_district(self):
        district_type = "Craft. This district has a focus on the creation of different goods."
        condition = self.generate_district_condition(self.modifiers.craft_district_condition_modifier, self.modifiers.craft_district_quality_modifier)
        additional_locations = self.calculate_additional_location_amount()
        non_commerical_locations = []
        shops = ["Smithy", "Carpenter", "General Store", "Tailor", self.generate_magic_shop()]
        services = []
        religious_sites = []
        
        if random.randint(1, 100) < 5:
            for _ in range(1):
                religious_sites.append(self.generate_worship_place())
        else:
            religious_sites.append("None")                

        if self.isEntertainmentPriority:
            entertainment_buildings = {
                1: ("House of Leisure", "service"),
                2: ("Club", "service"),
                3: ("Tavern", "service"),
                4: ("Inn", "service"),
                5: ("Bathhouse", "service"),
                6: ("Amphitheater", "non-commercial")
            }
            
            building_info = entertainment_buildings[random.randint(1,6)]
            building, building_type = building_info
            if building_type == "shop":
                shops.append(building + " (Of " + self.calculate_quality(self.modifiers.administration_district_quality_modifier) + " quality.)")
            elif building_type == "service":
                    services.append(building)
            else:
                non_commerical_locations.append(building)

        shipwright = "Mechanics (Land Vessels)"        
        if self.environment == "Coastal" or self.environment == "River": 
            shipwright = "Shipwright (Sea Vessels)"
        elif self.environment == "Mountains":
            shipwright = "Shipwright (Air Vessels)"
        
        locations = {
            1: ("Cooper", "shop"),
            2: ("Carpenter", "shop"),
            3: ("Thatcher", "shop"),
            4: ("Wainwright", "shop"),
            5: ("Armorsmith", "shop"),
            6: ("Artist", "shop"),
            7: ("Bank & Exchange", "shop"),
            8: ("Cobbler", "shop"),
            9: ("Foundry/Smelting", "shop"),
            10: ("Miller", "shop"),
            11: ("Textile Production", "shop"),
            12: (shipwright, "shop"),
            13: (self.generate_magic_shop(), "shop"),
            14: ("Luxury Furnishing", "shop"),
            15: ("Rare Trade Goods", "shop"),
            16: ("Weaponsmith", "shop"),
            17: ("Tavern", "service"),
            18: ("Hired Help", "service")
        }
        
        hired_help = {
            1: "Brutes & Brawlers",
            2: "Cloak & Dagger",
            3: "Bows & Slings",
            4: "Scribes & Clerks",
            5: "Guides & Trackers",
            6: "Caravan & Mount",
            7: "Arcane Academics",
            8: "Magic Mercenaries",
            9: "Priestly Guidance",
            10: "Hands of the Divine"
        }

        for _ in range(additional_locations):
            roll = random.randint(1,18)
            location, location_type = locations[roll]
            
            if location_type == "shop":
                shops.append(location + " (Of " + self.calculate_quality(self.modifiers.craft_district_quality_modifier) + " quality.)")
            elif location_type == "service":
                if location == "Hired Help":
                    services.append(location + ": " + hired_help[random.randint(1,10)])
                else:
                    services.append(location)
            else:
                non_commerical_locations.append(location)
            
        
        district = {
            "type": district_type,
            "condition": condition,
            "entry": self.generate_district_entry(self.modifiers.craft_district_crime_modifier),
            "crime": self.generate_district_crime(condition, self.modifiers.craft_district_crime_modifier),
            "housing": self.generate_district_housing(district_type), 
            "non_commercial": non_commerical_locations,
            "shops": shops,
            "services": services,
            "religious_places" : religious_sites
        }
        
        return district
    def generate_docks_district(self):
        district_type = "Docks. This district has a focus on all naval and seafaring matters."
        condition = self.generate_district_condition(self.modifiers.docks_district_condition_modifier, self.modifiers.docks_district_quality_modifier)
        additional_locations = self.calculate_additional_location_amount()
        non_commerical_locations = []
        shops = ["Shipwright (Sea Vessals)", "Weaver"]
        services = ["House of Leisure", "Inn", "Tavern"]
        religious_sites = []
        
        if random.randint(1, 100) < 2:
            for _ in range(1):
                religious_sites.append(self.generate_worship_place())
        else:
            religious_sites.append("None")
        
        if self.isEntertainmentPriority:
            entertainment_buildings = {
                1: ("House of Leisure", "service"),
                2: ("Club", "service"),
                3: ("Tavern", "service"),
                4: ("Inn", "service"),
                5: ("Bathhouse", "service"),
                6: ("Amphitheater", "non-commercial")
            }
            
            building_info = entertainment_buildings[random.randint(1,6)]
            building, building_type = building_info
            if building_type == "shop":
                shops.append(building + " (Of " + self.calculate_quality(self.modifiers.administration_district_quality_modifier) + " quality.)")
            elif building_type == "service":
                    services.append(building)
            else:
                non_commerical_locations.append(building)
         
        locations = {
            1: ("Cooper", "shop"),
            2: ("Carpenter", "shop"),
            3: ("Smithy", "shop"),
            4: ("Bank & Exchange", "shop"),
            5: ("Shipwright", "shop"),
            6: ("Rare Botanicals", "shop"),
            7: ("Rare Libations and Fare", "shop"),
            8: ("Rare Trade Goods", "shop"),
            9: (self.generate_magic_shop, "shop"),
            10: ("Barber", "service"),
            11: ("Bathhouse", "service"),
            12: ("Doctor/Apothecary", "service"),
            13: ("House of Leisure", "service"),
            14: ("Inn", "service"),
            15: ("Club", "service"),
            16: ("Tavern", "service"),
            17: ("Hired Help", "service"),
            18: ("Casino", "service")
        }
        
        hired_help = {
            1: "Brutes & Brawlers",
            2: "Cloak & Dagger",
            3: "Bows & Slings",
            4: "Scribes & Clerks",
            5: "Guides & Trackers",
            6: "Caravan & Mount",
            7: "Arcane Academics",
            8: "Magic Mercenaries",
            9: "Priestly Guidance",
            10: "Hands of the Divine"
        }

        for _ in range(additional_locations):
            roll = random.randint(1,18)
            location, location_type = locations[roll]
            
            if location_type == "shop":
                shops.append(location + " (Of " + self.calculate_quality(self.modifiers.docks_district_quality_modifier) + " quality.)")
            elif location_type == "service":
                if location == "Hired Help":
                    services.append(location + ": " + hired_help[random.randint(1,10)])
                else:
                    services.append(location)
            else:
                non_commerical_locations.append(location)
            
        
        district = {
            "type": district_type,
            "condition": condition,
            "entry": self.generate_district_entry(self.modifiers.docks_district_crime_modifier),
            "crime": self.generate_district_crime(condition, self.modifiers.docks_district_crime_modifier),
            "housing": self.generate_district_housing(district_type), 
            "non_commercial": non_commerical_locations,
            "shops": shops,
            "services": services,
            "religious_places" : religious_sites
        }
        
        return district
    def generate_industrial_district(self):
        district_type = "Industrial. This district has a focus on large-scale production facilities."
        condition = self.generate_district_condition(self.modifiers.industrial_district_condition_modifier, self.modifiers.industrial_district_quality_modifier)
        additional_locations = self.calculate_additional_location_amount()
        non_commerical_locations = []
        shops = ["Smithy", random.choice(["foundry/Smelting", "Textiles Production", "Miller"])]
        services = []
        religious_sites = ["None"]
                    
        shipwright = "Mechanics (Land Vessels)"        
        if self.environment == "Coastal" or self.environment == "River": 
            shipwright = "Shipwright (Sea Vessels)"
        elif self.environment == "Mountains":
            shipwright = "Shipwright (Air Vessels)"
            
        if self.isEntertainmentPriority:
            entertainment_buildings = {
                1: ("House of Leisure", "service"),
                2: ("Club", "service"),
                3: ("Tavern", "service"),
                4: ("Inn", "service"),
                5: ("Bathhouse", "service"),
                6: ("Amphitheater", "non-commercial")
            }
            
            building_info = entertainment_buildings[random.randint(1,6)]
            building, building_type = building_info
            if building_type == "shop":
                shops.append(building + " (Of " + self.calculate_quality(self.modifiers.administration_district_quality_modifier) + " quality.)")
            elif building_type == "service":
                    services.append(building)
            else:
                non_commerical_locations.append(building)
        
        locations = {
            1: ("Cooper", "shop"),
            2: ("Carpenter", "shop"),
            3: ("General Store", "shop"),
            4: ("Smithy", "shop"),
            5: ("Tailor", "shop"),
            6: ("Thatcher", "shop"),
            7: ("Wainwright", "shop"),
            8: ("Weaver", "shop"),
            9: ("Foundry/Smelting", "shop"),
            10: ("Miller", "shop"),
            11: ("Textile Production", "shop"),
            12: (shipwright, "shop"),
            13: ("House of Leisure", "service"),
            14: ("Club", "service"),
            15: ("Tavern", "service"),
            16: ("Hired Help", "service"),
            17: ("Gathering Hall", "non-commercial"),
            18: ("Treasury", "non-commercial")
        }
        
        hired_help = {
            1: "Brutes & Brawlers",
            2: "Cloak & Dagger",
            3: "Bows & Slings",
            4: "Scribes & Clerks",
            5: "Guides & Trackers",
            6: "Caravan & Mount",
            7: "Arcane Academics",
            8: "Magic Mercenaries",
            9: "Priestly Guidance",
            10: "Hands of the Divine"
        }

        for _ in range(additional_locations):
            roll = random.randint(1,18)
            location, location_type = locations[roll]
            
            if location_type == "shop":
                shops.append(location + " (Of " + self.calculate_quality(self.modifiers.industrial_district_quality_modifier) + " quality.)")
            elif location_type == "service":
                if location == "Hired Help":
                    services.append(location + ": " + hired_help[random.randint(1,10)])
                else:
                    services.append(location)
            else:
                non_commerical_locations.append(location)
            
        
        district = {
            "type": district_type,
            "condition": condition,
            "entry": self.generate_district_entry(self.modifiers.industrial_district_crime_modifier),
            "crime": self.generate_district_crime(condition, self.modifiers.industrial_district_crime_modifier),
            "housing": self.generate_district_housing(district_type), 
            "non_commercial": non_commerical_locations,
            "shops": shops,
            "services": services,
            "religious_places" : religious_sites
        }
        
        return district
    def generate_market_district(self):
        district_type = "Market. This district has a focus on the sale of practical goods."
        condition = self.generate_district_condition(self.modifiers.market_district_condition_modifier, self.modifiers.market_district_quality_modifier)
        additional_locations = self.calculate_additional_location_amount()
        non_commerical_locations = []
        shops = ["Baker", "Butcher", "General Store","Smithy", "Tailor"]
        services = []
        religious_sites = []
        
        if random.randint(1, 100) < 15:
            amount = random.randint(1,3)
            for _ in range(amount):
                religious_sites.append(self.generate_worship_place())
        else:
            religious_sites.append("None")
                    
        if self.isEntertainmentPriority:
            entertainment_buildings = {
                1: ("House of Leisure", "service"),
                2: ("Club", "service"),
                3: ("Tavern", "service"),
                4: ("Inn", "service"),
                5: ("Bathhouse", "service"),
                6: ("Amphitheater", "non-commercial")
            }
            
            building_info = entertainment_buildings[random.randint(1,6)]
            building, building_type = building_info
            if building_type == "shop":
                shops.append(building + " (Of " + self.calculate_quality(self.modifiers.administration_district_quality_modifier) + " quality.)")
            elif building_type == "service":
                    services.append(building)
            else:
                non_commerical_locations.append(building)
        
        locations = {
            1: ("Wainwright", "shop"),
            2: ("Weaver", "shop"),
            3: ("Alchemist", "shop"),
            4: ("Artist", "shop"),
            5: ("Bank & Exchange", "shop"),
            6: ("Cobbler", "shop"),
            7: ("Rare Botanicals", "shop"),
            8: ("Luxury Furnishings", "shop"),
            9: ("Rare Libations & Fare", "shop"),
            10: ("Rare Trade Goods", "shop"),
            11: (self.generate_magic_shop(), "shop"),
            12: ("Barber", "service"),
            13: ("Inn", "service"),
            14: ("Club", "service"),
            15: ("Soothsayer", "service"),
            16: ("Stable", "service"),
            17: ("Tavern", "service"),
            18: ("Hired Help", "service")
        }

        
        hired_help = {
            1: "Brutes & Brawlers",
            2: "Cloak & Dagger",
            3: "Bows & Slings",
            4: "Scribes & Clerks",
            5: "Guides & Trackers",
            6: "Caravan & Mount",
            7: "Arcane Academics",
            8: "Magic Mercenaries",
            9: "Priestly Guidance",
            10: "Hands of the Divine"
        }

        for _ in range(additional_locations):
            roll = random.randint(1,18)
            location, location_type = locations[roll]
            
            if location_type == "shop":
                shops.append(location + " (Of " + self.calculate_quality(self.modifiers.market_district_quality_modifier) + " quality.)")
            elif location_type == "service":
                if location == "Hired Help":
                    services.append(location + ": " + hired_help[random.randint(1,10)])
                else:
                    services.append(location)
            else:
                non_commerical_locations.append(location)
            
        
        district = {
            "type": district_type,
            "condition": condition,
            "entry": self.generate_district_entry(self.modifiers.market_district_crime_modifier),
            "crime": self.generate_district_crime(condition, self.modifiers.market_district_crime_modifier),
            "housing": self.generate_district_housing(district_type), 
            "non_commercial": non_commerical_locations,
            "shops": shops,
            "services": services,
            "religious_places" : religious_sites
        }
        
        return district
    def generate_merchant_district(self):
        district_type = "Merchant. This district has a focus on business and non-essential goods."
        condition = self.generate_district_condition(self.modifiers.merchant_district_condition_modifier, self.modifiers.merchant_district_quality_modifier)
        additional_locations = self.calculate_additional_location_amount()
        non_commerical_locations = []
        shops = ["Bank & Exchange", "Tailor", "Artist", "Cobbler", "Magic Shop: Miscellaneous & Curiosities"]
        services = []
        religious_sites = []
        
        if random.randint(1, 100) < 15:
            for _ in range(1):
                religious_sites.append(self.generate_worship_place())
        else:
            religious_sites.append("None")
        
        if self.isEntertainmentPriority:
            entertainment_buildings = {
                1: ("House of Leisure", "service"),
                2: ("Club", "service"),
                3: ("Tavern", "service"),
                4: ("Inn", "service"),
                5: ("Bathhouse", "service"),
                6: ("Amphitheater", "non-commercial")
            }
            
            building_info = entertainment_buildings[random.randint(1,6)]
            building, building_type = building_info
            if building_type == "shop":
                shops.append(building + " (Of " + self.calculate_quality(self.modifiers.administration_district_quality_modifier) + " quality.)")
            elif building_type == "service":
                    services.append(building)
            else:
                non_commerical_locations.append(building)
                    
        locations = {
            2: ("General Store", "shop"),
            3: ("Wainwright", "shop"),
            4: ("Alchemist", "shop"),
            5: ("Artist", "shop"),
            6: ("Bank & Exchange", "shop"),
            7: ("Cobbler", "shop"),
            8: ("Luxury Furnishings", "shop"),
            9: ("Rare Libations & Fare", "shop"),
            10: ("Rare Trade Goods", "shop"),
            11: (self.generate_magic_shop, "shop"),
            12: (self.generate_magic_shop, "shop"),
            13: ("Barber", "service"),
            14: ("Bathhouse", "service"),
            15: ("House of Leisure", "service"),
            16: ("Inn", "service"),
            17: ("Club", "service"),
            18: ("Tavern", "service"),
            19: ("Hired Help", "service")
        }
        
        hired_help = {
            1: "Brutes & Brawlers",
            2: "Cloak & Dagger",
            3: "Bows & Slings",
            4: "Scribes & Clerks",
            5: "Guides & Trackers",
            6: "Caravan & Mount",
            7: "Arcane Academics",
            8: "Magic Mercenaries",
            9: "Priestly Guidance",
            10: "Hands of the Divine"
        }

        for _ in range(additional_locations):
            roll = random.randint(2,19)
            location, location_type = locations[roll]
            
            if location_type == "shop":
                shops.append(location + " (Of " + self.calculate_quality(self.modifiers.merchant_district_quality_modifier) + " quality.)")
            elif location_type == "service":
                if location == "Hired Help":
                    services.append(location + ": " + hired_help[random.randint(1,10)])
                else:
                    services.append(location)
            else:
                non_commerical_locations.append(location)
            
        
        district = {
            "type": district_type,
            "condition": condition,
            "entry": self.generate_district_entry(self.modifiers.merchant_district_crime_modifier),
            "crime": self.generate_district_crime(condition, self.modifiers.merchant_district_crime_modifier),
            "housing": self.generate_district_housing(district_type), 
            "non_commercial": non_commerical_locations,
            "shops": shops,
            "services": services,
            "religious_places" : religious_sites
        }
        
        return district
    def generate_scholar_district(self):
        district_type = "Scholar. This district has a focus on education and the pursuit of knowledge."
        condition = self.generate_district_condition(self.modifiers.scholar_district_condition_modifier, self.modifiers.scholar_district_quality_modifier)
        additional_locations = self.calculate_additional_location_amount()
        non_commerical_locations = ["Archives/Library", "Academy/University", "Forum", "Schoolhouse"]
        shops = []
        services = ["Hired Help: Scribes and clerks"]
        religious_sites = []
        
        if random.randint(1, 100) < 20:
            amount = random.randint(1,2)
            for _ in range(amount):
                religious_sites.append(self.generate_worship_place())
        else:
            religious_sites.append("None")
        
        if self.isEntertainmentPriority:
            entertainment_buildings = {
                1: ("House of Leisure", "service"),
                2: ("Club", "service"),
                3: ("Tavern", "service"),
                4: ("Inn", "service"),
                5: ("Bathhouse", "service"),
                6: ("Amphitheater", "non-commercial")
            }
            
            building_info = entertainment_buildings[random.randint(1,6)]
            building, building_type = building_info
            if building_type == "shop":
                shops.append(building + " (Of " + self.calculate_quality(self.modifiers.administration_district_quality_modifier) + " quality.)")
            elif building_type == "service":
                    services.append(building)
            else:
                non_commerical_locations.append(building)
        
        locations = {
            2: ("General Store", "shop"),
            3: ("Tailor", "shop"),
            4: ("Thatcher", "shop"),
            5: ("Weaver", "shop"),
            6: ("Alchemist", "shop"),
            7: ("Bank & Exchange", "shop"),
            8: ("Rare Botanicals", "shop"),
            9: ("Luxury Furnishings", "shop"),
            10: ("Rare Libations & Fare", "shop"),
            11: ("Rare Trade Goods", "shop"),
            12: ("Magic Shop - Books", "shop"),
            13: ("Doctor/Apothecary", "service"),
            14: ("Hired Help: Scholars & Clerics", "service"),
            15: ("Archives/Library", "non-commercial"),
            16: ("Academy/University", "non-commercial"),
            17: ("Forum", "non-commercial"),
            18: ("Schoolhouse", "non-commercial"),
            19: ("Gathering Hall", "non-commercial")
        }

        for _ in range(additional_locations):
            roll = random.randint(2,19)
            location, location_type = locations[roll]
            
            if location_type == "shop":
                shops.append(location + " (Of " + self.calculate_quality(self.modifiers.scholar_district_quality_modifier) + " quality.)")
            elif location_type == "service":
                    services.append(location)
            else:
                non_commerical_locations.append(location)
            
        
        district = {
            "type": district_type,
            "condition": condition,
            "entry": self.generate_district_entry(self.modifiers.scholar_district_crime_modifier),
            "crime": self.generate_district_crime(condition, self.modifiers.scholar_district_crime_modifier),
            "housing": self.generate_district_housing(district_type), 
            "non_commercial": non_commerical_locations,
            "shops": shops,
            "services": services,
            "religious_places" : religious_sites
        }
        
        return district
    def generate_slums_district(self):
        district_type = "Slums. This district is an area where those with lesser means might live."
        condition = self.generate_district_condition(self.modifiers.slums_district_condition_modifier, self.modifiers.slums_district_quality_modifier, isSlums=True)
        additional_locations = self.calculate_additional_location_amount()
        non_commerical_locations = []
        shops = ["Butcher"]
        services = ["House of Leisure", "Inn", "Tavern"]
        religious_sites = ["None"]
        
        if self.isEntertainmentPriority:
            entertainment_buildings = {
                1: ("House of Leisure", "service"),
                2: ("Club", "service"),
                3: ("Tavern", "service"),
                4: ("Inn", "service"),
                5: ("Bathhouse", "service"),
                6: ("Amphitheater", "non-commercial")
            }
            
            building_info = entertainment_buildings[random.randint(1,6)]
            building, building_type = building_info
            if building_type == "shop":
                shops.append(building + " (Of " + self.calculate_quality(self.modifiers.administration_district_quality_modifier) + " quality.)")
            elif building_type == "service":
                    services.append(building)
            else:
                non_commerical_locations.append(building)
        
        locations = {
            1: ("Baker", "shop"),
            2: ("Butcher", "shop"),
            3: ("General Store", "shop"),
            4: ("Smithy", "shop"),
            5: ("Thatcher", "shop"),
            6: ("Weaver", "shop"),
            7: ("Alchemist", "shop"),
            8: ("Foundry/Smelting", "shop"),
            9: ("Miller", "shop"),
            10: ("Textile Production", "shop"),
            11: ("Barber", "service"),
            12: ("Bathhouse", "service"),
            13: ("Doctor/Apothecary", "service"),
            14: ("House of Leisure", "service"),
            15: ("Inn", "service"),
            16: ("Club", "service"),
            17: ("Soothsayer", "service"),
            18: ("Tavern", "service")
        }

        for _ in range(additional_locations):
            roll = random.randint(1,18)
            location, location_type = locations[roll]
            
            if location_type == "shop":
                shops.append(location + " (Of " + self.calculate_quality(self.modifiers.slums_district_quality_modifier) + " quality.)")
            elif location_type == "service":
                    services.append(location)
            else:
                non_commerical_locations.append(location)
            
        
        district = {
            "type": district_type,
            "condition": condition,
            "entry": self.generate_district_entry(self.modifiers.slums_district_crime_modifier),
            "crime": self.generate_district_crime(condition, self.modifiers.slums_district_crime_modifier),
            "housing": self.generate_district_housing(district_type), 
            "non_commercial": non_commerical_locations,
            "shops": shops,
            "services": services,
            "religious_places" : religious_sites
        }
        
        return district 
    def generate_temple_district(self):
        district_type = "Temple. This district has a focus on religion and/or spiritual enlightenment."
        condition = self.generate_district_condition(self.modifiers.temple_district_condition_modifier, self.modifiers.temple_district_quality_modifier)
        additional_locations = self.calculate_additional_location_amount()
        non_commerical_locations = ["Archives/Library"]
        shops = []
        services = ["Hired Help: Scribes", "Hired Help: Priestly Guidance", "Hired Help: Hands of the Divine"]
        religious_sites = []
        amount = random.randint(1,4)
        for _ in range(amount):
            religious_sites.append(self.generate_worship_place())
        
        if self.isEntertainmentPriority:
            entertainment_buildings = {
                1: ("House of Leisure", "service"),
                2: ("Club", "service"),
                3: ("Tavern", "service"),
                4: ("Inn", "service"),
                5: ("Bathhouse", "service"),
                6: ("Amphitheater", "non-commercial")
            }
            
            building_info = entertainment_buildings[random.randint(1,6)]
            building, building_type = building_info
            if building_type == "shop":
                shops.append(building + " (Of " + self.calculate_quality(self.modifiers.administration_district_quality_modifier) + " quality.)")
            elif building_type == "service":
                    services.append(building)
            else:
                non_commerical_locations.append(building)
        
        locations = {
            2: ("Cooper", "shop"),
            3: ("Carpenter", "shop"),
            4: ("Tailor", "shop"),
            5: ("Alchemist", "shop"),
            6: ("Artist", "shop"),
            7: ("Bank & Exchange", "shop"),
            8: ("Rare Botanicals", "shop"),
            9: ("Luxury Furnishings", "shop"),
            10: ("Rare Libations & Fare", "shop"),
            11: (self.generate_magic_shop(), "shop"),
            12: ("Barber", "service"),
            13: ("Bathhouse", "service"),
            14: ("Doctor/Apothecary", "service"),
            15: ("Inn", "service"),
            16: ("Soothsayer", "service"),
            17: ("Hired Help: " + random.choice(["Priestly Guidance", "Hands of the Divine"]), "service"),
            18: ("Schoolhouse", "non-commercial"),
            19: ("Amphitheater", "non-commercial")
        }

        for _ in range(additional_locations):
            roll = random.randint(2,19)
            location, location_type = locations[roll]
            
            if location_type == "shop":
                shops.append(location + " (Of " + self.calculate_quality(self.modifiers.temple_district_quality_modifier) + " quality.)")
            elif location_type == "service":
                    services.append(location)
            else:
                non_commerical_locations.append(location)
            
        
        district = {
            "type": district_type,
            "condition": condition,
            "entry": self.generate_district_entry(self.modifiers.temple_district_crime_modifier),
            "crime": self.generate_district_crime(condition, self.modifiers.temple_district_crime_modifier),
            "housing": self.generate_district_housing(district_type), 
            "non_commercial": non_commerical_locations,
            "shops": shops,
            "services": services,
            "religious_places" : religious_sites
        }
        
        return district 
    def generate_upper_class_district(self):
        district_type = "Upper Class. This district is an area where those with greater means might live."
        condition = self.generate_district_condition(self.modifiers.upper_class_district_condition_modifier, self.modifiers.upper_class_district_quality_modifier)
        additional_locations = self.calculate_additional_location_amount()
        non_commerical_locations = []
        shops = ["Bank & Exchange", "Baker", "Tailor", "Luxury Furnishings"]
        services = ["Doctor/Apothecary"]
        religious_sites = []
        
        if random.randint(1, 100) < 20:
            religious_sites.append(self.generate_worship_place())
        else:
            religious_sites.append("None")
        
        if self.isEntertainmentPriority:
            entertainment_buildings = {
                1: ("House of Leisure", "service"),
                2: ("Club", "service"),
                3: ("Tavern", "service"),
                4: ("Inn", "service"),
                5: ("Bathhouse", "service"),
                6: ("Amphitheater", "non-commercial")
            }
            
            building_info = entertainment_buildings[random.randint(1,6)]
            building, building_type = building_info
            if building_type == "shop":
                shops.append(building + " (Of " + self.calculate_quality(self.modifiers.administration_district_quality_modifier) + " quality.)")
            elif building_type == "service":
                    services.append(building)
            else:
                non_commerical_locations.append(building)
        
        locations = {
            1: ("Butcher", "shop"),
            2: ("Tailor", "shop"),
            3: ("Weaver", "shop"),
            4: ("Alchemist", "shop"),
            5: ("Artist", "shop"),
            6: ("Cobbler", "shop"),
            7: ("Rare Botanicals", "shop"),
            8: ("Luxury Furnishings", "shop"),
            9: ("Rare Libations & Fare", "shop"),
            10: (self.generate_magic_shop(), "shop"),
            11: ("Barber", "service"),
            12: ("Bathhouse", "service"),
            13: ("House of Leisure", "service"),
            14: ("Inn", "service"),
            15: ("Club", "service"),
            16: ("Soothsayer", "service"),
            17: ("Stable", "service"),
            18: ("Tavern", "service")
        }


        for _ in range(additional_locations):
            roll = random.randint(2,19)
            location, location_type = locations[roll]
            
            if location_type == "shop":
                shops.append(location + " (Of " + self.calculate_quality(self.modifiers.temple_district_quality_modifier) + " quality.)")
            elif location_type == "service":
                    services.append(location)
            else:
                non_commerical_locations.append(location)
            
        
        district = {
            "type": district_type,
            "condition": condition,
            "entry": self.generate_district_entry(self.modifiers.temple_district_crime_modifier),
            "crime": self.generate_district_crime(condition, self.modifiers.temple_district_crime_modifier),
            "housing": self.generate_district_housing(district_type), 
            "non_commercial": non_commerical_locations,
            "shops": shops,
            "services": services,
            "religious_places" : religious_sites
        }
        
        return district     
    def generate_noteworthy_officals(self):
        amount_roll = random.randint(1, 8)
        
        noteworthy_officials = [
            "Adviser. Second in command of the city. Can be an official, or unofficial, position.",
            "Ambassador. Regularly acts as a representative for the city/nation when traveling abroad.",
            "Catchpole. Catches and brings in debtors.",
            "Champion. Ready to stand in for the city leadership for any martial matters, either ceremonially or officially.",
            "Clerk. Recordkeeper for the city.",
            "Exchequer. Responsible for taxes.",
            "Guildmaster. Oversees one of the official (or underground) guilds, or factions, within the city.",
            "Herald. Responsible for disseminating official edicts, and other news, to the general populace. If serving in a courtly capacity, bears responsibility for knowing the names and titles of important individuals, and announcing them, when appropriate.",
            "High Priest/Druid. The primary representative of the faithful to the city leadership.",
            "High Mage. The representative of the practitioners of arcane arts to the city leadership.",
            "Jailer. In charge of confining prisoners.",
            "Judge. Decision-maker in legal matters.",
            "Liner. Determines property boundaries.",
            "Master of Intelligence. Responsible for seeking and utilizing information vital for city/nation’s security.",
            "Master of Revels. Lead organizer of festivals and special events.",
            "Master of Stores. Oversees the city’s stores of supplies, such as grain or building materials.",
            "Master of Trade. Responsible for the management of imports and exports.",
            "Master of the Treasury. Responsible for the city’s expenditures and paying contracts and debts.",
            "Master of the Wild. Surveys the surrounding areas, mapping the wilderness, looking for monsters or other threats, and regulating hunting.",
            "Roadwarden/Dockwarden. In charge of some, or all, of the city’s transportation systems."
        ]

        officials_competence = {
            1: "Corrupt. Taking advantage of the position for personal gain.",
            2: "Incompetent. Doesn’t truly understand how to execute the position.",
            3: "Incompetent. Doesn’t truly understand how to execute the position.",
            4: "Committed. Utterly committed to the job, truly feeling it is of vital importance.",
            5: "Committed. Utterly committed to the job, truly feeling it is of vital importance.",
            6: "Overqualified. Based on skills and experience, ought to be in a higher position."
        }
        
        for i in range(amount_roll):
            competence_roll = random.randint(1, 6)
            competence = officials_competence[competence_roll]
            offical = random.choice(noteworthy_officials)
            self.noteworthy_officals.append(offical + " They are " + competence)
        
    def generate_underground_activities(self):
        return random.choice([
            "Pack. A pack of particularly feral animals roams the city.",
            "Monster. A monster lurks somewhere in the city.",
            "Markings. Strange markings have been showing up around the city.",
            "Fight Club. A fight club has started somewhere in the city, and may be gaining more participants.",
            "Secret. Some portion of the populace is not as they seem.",
            "Outside Contact. Someone in the city is in regular communication with an interesting external contact.",
            "Tampering. Someone is interfering with forces best left alone.",
            "Unsafe. There is a structural problem with a location within the city (or, possibly, the land, or environment, it is built on). The longer it goes unnoticed, the more damaging it could be.",
            "Parties. A guerilla party scene has been emerging within the city, with semi-frequent, secret, invitation-only parties being held at ever-changing locations.",
            "Black Market. An underground black-market has been established, dealing in the movement of illicit goods or services.",
            "Races. A racing circuit has been established outside the city.",
            "Haunted. The city is being haunted by some kind of spirit."
        ])
    
        
    def __str__(self):
        city_str = f"City of {self.name}\n"  # City's name
        city_str += f"Origin: {self.origin}\n"  # Information about the city's origin
        city_str += f"Stewardship: {self.stewardship}\n"  # City's leadership and governance
        city_str += f"Fortification: {self.fortification}\n"  # Information about city defenses
        
        city_str += "\nCity Outskirts:\n"  # Listing features or locations in the outskirts
        for location in self.city_outskirts:
            city_str += f" - {location}\n"

        city_str += f"\nMarket Square: {self.market_square}\n"  # Central economic hub
        city_str += f"Merchant Overflow: {self.merchant_overflow}\n"  # Space for additional vendors
        city_str += f"Underground Passages: {self.underground_passages}\n"  # Covert networks beneath the city
        
        city_str += f"Population Density: {self.population_density}\n"  # How crowded the city is
        city_str += f"Demographics: {self.demographics}\n"  # Breakdown of the city's population
        city_str += f"Population Wealth: {self.population_wealth}\n"  # Economic status of inhabitants
        city_str += f"Visitor Traffic: {self.visitor_traffic}\n"  # Rate of visitors coming into the city
        
        city_str += f"Disposition: {self.disposition}\n"  # General attitude of the population
        city_str += f"Night Activity: {self.night_activity}\n"  # What happens after dark
        city_str += f"Leadership: {self.leadership}\n"  # Details about ruling figures or governing body
        city_str += f"Law Enforcement: {self.law_enforcement}\n"  # The state of city guards and policing
        city_str += f"General Crime: {self.general_crime}\n"  # The level of petty crime in the city
        city_str += f"Organised Crime: {self.organised_crime}\n"  # Any known crime syndicates or guilds
        
        # Districts information
        city_str += "\nDistricts Information:\n"
        for district in self.districts:
            district_info = "District Details:\n"
            district_info += f" - Type: {district['type'] or 'Various'}\n"
            district_info += f" - Condition: {district['condition'] or 'Various'}\n"
            district_info += f" - Entry Accessibility: {district['entry'] or 'Various'}\n"
            district_info += f" - Crime Level: {district['crime'] or 'Various'}\n"
            district_info += f" - Housing: {district['housing'] or 'Various'}\n"

            # Non-commercial places, iterate or provide a default
            if district['non_commercial']:
                non_commercial_str = ', '.join(district['non_commercial'])
            else:
                non_commercial_str = "None"
            district_info += f" - Non-Commercial Locations: {non_commercial_str}\n"

            # Shops, iterate or provide a default
            if district['shops']:
                shops_str = ', '.join(district['shops'])
            else:
                shops_str = "None"
            district_info += f" - Shops: {shops_str}\n"

            # Services, iterate or provide a default
            if district['services']:
                services_str = ', '.join(district['services'])
            else:
                services_str = "None"
            district_info += f" - Services: {services_str}\n"

            # Religious places, iterate or provide a default
            if district['religious_places']:
                religious_places_str = ', '.join(district['religious_places'])
            else:
                religious_places_str = "None"
            district_info += f" - Religious Establishments: {religious_places_str}\n"

            city_str += f"{district_info}\n"

        # Noteworthy officials
        city_str += "\nNoteworthy Officials:\n"
        for official in self.noteworthy_officals:
            # Format based on the structure of `official` entries
            city_str += f" - {official}.\n"
        
        # Underground activities
        activity_str = self.underground_activities if self.underground_activities != "Unknown" else "None to note."
        city_str += f"\nUnderground Activities: {activity_str}\n"
        
        return city_str