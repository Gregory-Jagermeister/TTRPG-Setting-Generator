import random
from src.Modules.Settlement.Settlement import Settlement
from src.Modules.Utilities.utlil_helpers import process_duplicates

class Town(Settlement):
    def __init__(self):
        """
        Initializes a new instance of the Town class.
        """
        super().__init__()
        
        #Flags
        self.isPort = False
        self.isProductionTown = False
        self.isGovernanceTown = False
        self.isEconomicTown = False
        self.isFarmingSpecialty = False
        
        #Variables
        self.type = "Town"
        self.name = self.generate_name()
        self.origin = "Unknown"
        self.priority = "Unknown"
        self.specialty = "Unknown"
        self.prosperity = "Unknown"
        self.market_square = "Unknown"
        self.merchant_overflow = "Unknown"
        self.fortification = "Unknown"
        self.pop_density = "Unknown"
        self.pop_overflow = "Unknown"
        #farms and Resources need a function to get the amount to generate
        self.farms_resources = []
        self.visitor_traffic = "Unknown"
        self.night_activity = "Unknown"
        self.demographics = "Unknown"
        self.disposition = "Unknown"
        self.leadership = "Unknown"
        self.law_enforcement = "Unknown"
        self.pop_wealth = "Unknown"
        self.crime = "Unknown"
        self.non_commercial_locations = []
        self.shops = ["General Store. Sells basic supplies, groceries, and various odds and ends.", "Smithy. Sells and crafts metal tools and equipment, including very basic weapons and armor."]
        self.services = ["Tavern. Provides food and drink.", "Inn. Provides accommodation, as well as a place to have a bath and a decent meal."]
        self.noteworthy_officals = []
    
    def generate(self):

        self.origin = self.generate_origin()
        self.priority = self.generate_priority()
        self.specialty = self.generate_specialty()
        self.age = self.generate_age()
        self.size = self.generate_size()
        self.condition = self.generate_condition()
        self.environment = self.generate_environment()
        self.prosperity = self.generate_prosperity()
        self.market_square = self.generate_market_square()
        self.merchant_overflow = self.generate_merchant_overflow()
        self.fortification = self.generate_fortification()
        self.pop_density = self.generate_pop_density()
        self.pop_overflow = self.generate_pop_overflow()
        self.generate_farms_resources()
        self.farms_resources = process_duplicates(self.farms_resources)
        self.visitor_traffic = self.generate_visitor_traffic()
        self.night_activity = self.generate_night_activity()
        self.demographics = self.generate_demographics()
        self.disposition = self.generate_disposition()
        self.leadership = self.generate_leadership()
        self.law_enforcement = self.generate_law_enforcement() 
        self.pop_wealth = self.generate_pop_wealth()
        self.crime = self.generate_crime()
        self.generate_non_commercial_locations()
        self.non_commercial_locations = process_duplicates(self.non_commercial_locations)
        self.generate_commerical_locations()
        self.shops = process_duplicates(self.shops)
        self.services = process_duplicates(self.services)
        self.generate_noteworthy_officals()
        self.noteworthy_officals = process_duplicates(self.noteworthy_officals)
        
        return self
    
    def generate_origin(self):
        origin = random.choice([
            "Accidental. Settlement grew unexpectedly due to outsiders staying and spreading the word.",
            "Decree. An authority decided a town was needed and established it with allocated resources.",
            "Exodus or Exile. Settlers left their home and built the town upon finding this place.",
            "Key Crossroads. Established at a busy intersection frequented by travelers.",
            "Military Camp. Originally a temporary camp, it evolved into a permanent settlement.",
            "Port. Established on water, attracting merchants and travelers. (Environment: coastal or river.)",
            "Rapid. A group of people rapidly created the town in an important location.",
            "Steady. Built over time through commitment and devotion until it reached fruition."
        ])
        if "Port." in origin:
            self.isPort = True
        
        return origin
        
    def generate_priority(self):
        priority = random.choice([
            "Military. Town prioritizes defenses and law enforcement.",
            "Government. Town prioritizes structure, order, and law.",
            "Production. Town prioritizes generation and movement of resources.",
            "Economic. Town prioritizes market development and commerce.",
            "Religious. Town focuses on substantial temples and places of worship.",
            "Magic. Town is centered around magical pursuits and may feature magic shops."
        ])
        
        if priority == "Military. Town prioritizes defenses and law enforcement.":
            self.modifiers.fortifcation_modifier += 1
            self.modifiers.law_enforcement_modifier += 1
        elif priority == "Government. Town prioritizes structure, order, and law.":
            self.modifiers.law_enforcement_modifier += 1
            self.isGovernanceTown = True
            self.non_commercial_locations.append(self.generate_government_place())
        elif priority == "Production. Town prioritizes generation and movement of resources.":
            self.isProductionTown = True
        elif priority == "Economic. Town prioritizes market development and commerce.":
            self.modifiers.market_square_modifier += 2
            self.isEconomicTown = True
        elif priority == "Religious. Town focuses on substantial temples and places of worship.":
            self.modifiers.worship_place_size_modifier += 5
            self.non_commercial_locations.append(self.generate_worship_place())
        elif priority == "Magic. Town is centered around magical pursuits and may feature magic shops.":
            self.shops.append(random.choice([
                "Magic Shop - Armor. Specializes in armor and protective equipment.",
                "Magic Shop - Books. Specializes in literature, arcane tomes, and lore.",
                "Magic Shop - Clothing. Specializes in magical clothing of all types.",
                "Magic Shop - Jewelry. Specializes in enchanted jewelry.",
                "Magic Shop - Weapons. Specializes in weapons with mystic properties.",
                "Magic Shop - Miscellaneous & Curiosities. Offers strange and rare magical artifacts."
            ]))

        return priority       
        
    def generate_specialty(self):
        specialty = ''
        if self.isProductionTown:
            specialty = random.choice([
                "Craft. The town is known for its skilled artisans and high-quality handmade goods.",
                "Farming or Resource Gathering. The town is renowned for its abundant natural resources, tailored to its environment and climate.",
                "Industry. This town specializes in various industrial processes such as milling, textiles, or smelting.",
                "Unique Shipping Methods. The town excels in unconventional or innovative transportation methods.",
            ])
        else:
            specialty = random.choice([
                "Craft. The town is known for its skilled artisans and high-quality handmade goods.",
                "Farming or Resource Gathering. The town is renowned for its abundant natural resources, tailored to its environment and climate.",
                "Industry. This town specializes in various industrial processes such as milling, textiles, or smelting.",
                "Unique Shipping Methods. The town excels in unconventional or innovative transportation methods.",
                "Connections. The town is a hub of individuals with vast networks capable of acquiring almost anything.",
                "Drink. The town boasts a diverse selection or exceptional quality of beverages.",
                "Education. The town is home to a prestigious educational institution.",
                "Hospitality. The town is famed for its warm and welcoming atmosphere, offering comfortable accommodations."
            ])
            
        if 'Farming or Resource Gathering' in specialty:
            self.isFarmingSpecialty = True
            self.modifiers.farm_resource_modifier += 1
        elif 'Industry' in specialty:
            self.shops.append(random.choices([
                "Textile Production. Larger-scale operations offering a wide variety of materials.",
                "Foundry/Smelting. Facilities for ore processing and metal fabrication.",
                "Mill. Facilities for milling grain into flour or other products."
            ]))
        elif 'Education' in specialty:
            self.non_commercial_locations.append(self.generate_education_place())
        elif 'Hospitality' in specialty:
            inn_quality = random.choice(['good', 'fabulous'])
            specialty = specialty + " The Town boasts Inn's of " + inn_quality + " quality."
            
        return specialty
    def generate_age(self):
        result = random.randint(1, 10)
        age_ranges = [
            (range(1, 3), (-2, "Recent")),
            (range(3, 5), (-1, "Established")),
            (range(5, 7), (0, "Mature")),
            (range(7, 9), (1, "Old")),
            (range(9, 11), (2, "Ancient")),
        ]
        
        for age_range, age_info in age_ranges:
            if result in age_range:
                self.modifiers.population_density_modifier, description = age_info
                return description
            
    def generate_size(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.size_modifier, 20), 1)
        size_ranges = [
            (range(1, 3), (2,"Very Small")),
            (range(3, 7), (1,"Small")),
            (range(7, 15), (0,"Medium")),
            (range(15, 19), (-1,"Large")),
            (range(19, 24), (-2,"Very Large"))
        ]
        
        for size_range, size_info in size_ranges:
            if roll in size_range:
                pop_overflow_mod, description = size_info
                self.modifiers.population_overflow_modifier += pop_overflow_mod
                return description
    
    def generate_environment(self):
        if self.isPort:
            return random.choice([
                'Coastal',
                'River'
            ])
        else:
            return random.choice(['Coastal','Forest', 'Desert', 'Mountain', 'Plains', 'River', 'Swamp', 'Underground', 'Valley', 'Tundra'])
    
    def generate_prosperity(self):
        roll = random.randint(1, 20)
        prosperity_table = [
            (range(1, 2), (-8, -13, "Abysmal Failure: The town has had little to no business, or has been very unfortunate.")),
            (range(2, 5), (-6, -6, "Failure: The town has struggled to generate meaningful wealth or notoriety")),
            (range(5, 11), (-1, -3, "Mildly Successful: The town has attained a mild degree of success and visibility.")),
            (range(11, 17), (0, 0, "Successful: The town is functional and generates a modest to good amount of coin.")),
            (range(17, 20), (2, 3, "Very Successful: The town has achieved real financial success and attracts a large number of visitors.")),
            (range(20, 21), (6, 6, "Incredibly Successful: The town attracts huge amounts of wealth for its citizens and visitors flock to be part of it"))
        ]

        for prosperity_range, prosperity_info in prosperity_table:
            if roll in prosperity_range:
                vis_traffic_mod, pop_wealth_mod, description = prosperity_info
                self.modifiers.visitor_traffic_modifier += vis_traffic_mod
                self.modifiers.population_wealth_modifier += pop_wealth_mod
                return description
        
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

    def generate_fortification(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.fortifcation_modifier, 20), 1)
        fortification_table = [
            (range(1, 3), (-5, "Unfortified: open to entry at all points")),
            (range(3, 7), (1, "Lightly Fortified: Town surrounds by light short walls of stone or wood.")),
            (range(7, 15), (3, "Fortified: Proper Stone/Wood walls surround this Town.")),
            (range(15, 19), (5, "Heavily Fortified: This town has Stone/wood Walls with Watchtowers along their length, Walls are reinforced with Metal bands.")),
            (range(19, 24), (7, "Extremely Fortified: Watchtowers are seen along the Length of Steel Reinforced Stone/Wood walls. Watchtowers could be seen standing in solitude in the neighbouring country around the town providing ample warning of oncoming events."))
        ]
        
        for fortification_range, fortification_info in fortification_table:
            if roll in fortification_range:
                disposition_mod, description = fortification_info
                self.modifiers.disposition_modifier += disposition_mod
                return description
    
    def generate_pop_density(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.population_density_modifier, 20), 1)
        population_density_table = [
            (range(1, 3), (-2, -2, "Skeleton. The town only has enough people to function at its most basic level.")),
            (range(3, 7), (-1, -1, "Sparse. Folk live here, but it would never be called bustling. Walking down the street, you’ll typically only see a few people.")),
            (range(7, 15), (0, 0, "Populous. A moderate amount of people live here. Walking through the streets, you will see plenty of people, but never so many that it would feel cramped.")),
            (range(15, 19), (1, 1, "Dense. There is a large amount of people living here. There are few, if any, vacant buildings. In high traffic areas, one generally has elbow room, but not much more.")),
            (range(19, 21), (2, 2, "Crowded. The town is filled with jostling throngs. Practically all structures are occupied. Some may even camp outside town. Moving about can be difficult, and bumping into other people is typical in higher traffic areas."))
        ]
        
        for density_range, density_info in population_density_table:
            if roll in density_range:
                overflow_mod, night_mod, description = density_info
                self.modifiers.population_overflow_modifier += overflow_mod
                self.modifiers.night_activity_modifier += night_mod
                return description

    def generate_pop_overflow(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.population_overflow_modifier, 20), 1)
        population_overflow_table = [
            (range(1, 2), "Less than a tenth of the town’s population is outside the town proper. This typically means that the only people who live outside the town are those that do so out of necessity, due to requirement of duties (such as owning a farm)."),
            (range(2, 5), "A tenth of the town’s population is outside the town proper."),
            (range(5, 13), "A fifth of the town’s population is outside the town proper."),
            (range(13, 18), "A third of the town’s population is outside the town proper."),
            (range(18, 20), "Just under half the town’s population is outside the town proper."),
            (range(20, 21), "Around half the town’s population is outside the town proper.")
        ]
        
        for overflow_range, overflow_info in population_overflow_table:
            if roll in overflow_range:
                return overflow_info
    
    def generate_farms_resources(self):
        roll_amount = 0 
        if "Very Small" in self.size:
            roll_amount = 1
        elif "Small" in self.size:
            roll_amount = 2
        elif "Medium" in self.size:
            roll_amount = 2
        elif "Large" in self.size:
            roll_amount = 3
        elif "Very Large" in self.size:
            roll_amount = 3
        
        farms_resources_table = [
            (range(1,5), "None."),
            (range(5,12), "Farming (Agriculture): Group of Farms that provide food on lands the town control."),
            (range(12, 17), "Farming (Livestock): Group of Farms that provide livestock on lands the town control."),
            (range(17,21), "Resource Harvesting: Based on the land and resources like trees, minerals, ore, and stone, the town has set up a logging camp, mine, or quarry nearby to gather resources for various purposes, including use or sale.")
        ]
        
        for i in range(roll_amount):
            roll = 0
            if self.isFarmingSpecialty:
                roll = max(min(random.randint(9, 20) + self.modifiers.farm_resource_modifier, 20), 9)
            else:
                roll = max(min(random.randint(1, 20) + self.modifiers.farm_resource_modifier, 20), 1)
            for farm_range, farms_info in farms_resources_table:
                if roll in farm_range:
                    self.farms_resources.append(farms_info)
        
        
    def generate_visitor_traffic(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.visitor_traffic_modifier, 20), 1)
        visitor_traffic_table = [
            (range(1, 4), (0, "Mostly Locals. On any given day, there are typically a few from out-of-town, though not enough to impact congestion.")),
            (range(4, 10), (1, "Groups. There are generally a fair amount of visitors. May slightly increase congestion.")),
            (range(10, 15), (2, "Crowds. A noticeable amount of people come through town on a regular basis. Congestion is increased.")),
            (range(15, 18), (3, "Droves. Large groups of people regularly frequent the town. Congestion is significantly increased.")),
            (range(18, 20), (4, "Masses. Huge groups of people always seem to be visiting. Congestion could cause difficulties, if the town is unable to cope with very large amounts of people.")),
            (range(20, 21), (5, "Multitudes. Massive groups of people throng the streets, likely spilling out onto the roads outside town. Congestion is an ever-present reality, and a regular issue."))
        ]
        
        for traffic_range, traffic_info in visitor_traffic_table:
            if roll in traffic_range:
                night_mod, traffic = traffic_info
                self.modifiers.night_activity_modifier += night_mod                
                return traffic
        
    def generate_night_activity(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.night_activity_modifier, 20), 1)
        night_activity_table = [
            (range(1, 3), "Dark - Streets empty, town closed, quiet and peaceful."),
            (range(3, 7), "Quiet - Only inns and taverns open till midnight. Innkeeper must be woken for late guests."),
            (range(7, 15), "Slow - Almost everything closed except taverns open till early morning, inns open perpetually."),
            (range(15, 19), "Active - Inns and taverns open perpetually, some shops and services available."),
            (range(19, 21), "Lively - Little difference between day and night, shops and services remain open constantly."),
        ]
        
        for night_range, night_info in night_activity_table:
            if roll in night_range:
                return night_info
    
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
        
    def generate_disposition(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.disposition_modifier, 20), 1)
        disposition_table = [
            (range(1, 3), "Hostile: Locals are unwelcoming of vistors (Townsfolk are cold, passive-aggressive or violent)"),
            (range(3, 7), "Unfriendly: Locals are suspious of vistors (Townsfolk are full of contempt, fear or suspicion)"),
            (range(7, 15), "Neutral: Locals are standoffish showing no emotion but can be made friendly (Townsfolk are Indifferent)"),
            (range(15, 19), "Friendly: Locals are Welcoming within the bounds of their rules (Townsfolk are Happy or Content)"),
            (range(19, 21), "Open: Local revel in the idea of vistors and their town is build to show it (Townsfolk are Joyous or Celebatory.)")
        ]
        
        for disposition_range, disposition_info in disposition_table:
            if roll in disposition_range:
                return disposition_info
        
    def generate_leadership(self):
        roll = 0
        if self.isGovernanceTown:
            roll = random.randint(1, 90)
        else:
            roll = random.randint(1, 100)
        
        leadership_ranges = [
            (range(1, 16), ("Town Council")),
            (range(16, 31), ("Mayor")),
            (range(31, 46), ("Hereditary")),
            (range(46, 61), ("Merchant Monarch")),
            (range(61, 76), ("Military Rule")),
            (range(76, 91), (f"Oligarchy Run by {random.choice(['Merchants (plutocracy)', 'Mages (Magocracy)', 'Priests (Theocracy)', 'A small group of people'])}")),
            (range(91, 100), ("Underworld or Criminal Enterprise")),
            (range(100, 101), ("Anarcho-Syndicalist Commune"))
        ]
        for leadership_range, leadership_info in leadership_ranges:
            if roll in leadership_range:
                if leadership_info == "Town Council":
                    self.non_commercial_locations.append("Town Hall. Used for official town business, audiences, and meetings.")
                elif leadership_info == "Merchant Monarch":
                    self.modifiers.commercial_locations_modifier += 2
                elif leadership_info == "Military Rule":
                    self.modifiers.law_enforcement_modifier += 1
                elif "Oligarchy" in leadership_info:
                    if "plutocracy" in leadership_info:
                        self.non_commercial_locations.append(self.generate_government_place())
                    elif "Magocracy" in leadership_info:
                        self.non_commercial_locations.append(self.generate_education_place())
                    elif "Theocracy" in leadership_info:
                        self.non_commercial_locations.append(self.generate_worship_place())
                    elif "A small group of people" in leadership_info:
                        self.non_commercial_locations.append(self.generate_gathering_place())
                elif leadership_info == "Underworld or Criminal Enterprise":
                    self.modifiers.crime_modifier += -1
                return leadership_info
            
    def generate_law_enforcement(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.law_enforcement_modifier, 20), 1)
        law_enforcement_table = [
            (range(1, 2), (-8,"None - Depending on perspective, absence of authority can be advantageous or problematic.")),
            (range(2, 5), (-4,"Sheriff - Officially sanctioned law enforcement with deputies.")),
            (range(5, 10), (-2,"Small Town Watch - Guarded by a captain and a small number of guards, sometimes lacking in presence.")),
            (range(10, 17), (0,"Town Watch - Led by an appointed captain and lieutenant, sufficient guards for key points and token patrols.")),
            (range(17, 20), (4,"Strong Town Watch - Led by an experienced captain with lieutenants, corporals, and ample boots on the ground, allowing for extra patrols.")),
            (range(20, 21), (8,"Extensive Town Watch - Supervised by a decorated captain with lieutenants, corporals, and abundant guards, maintaining an ever-present appearance."))
        ]
        
        for law_enforcement_range, law_enforcement_info in law_enforcement_table:
            if roll in law_enforcement_range:
                crime_mod, law_enforcement = law_enforcement_info
                self.modifiers.crime_modifier += crime_mod
                return law_enforcement
    def generate_pop_wealth(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.population_wealth_modifier, 20), 1)
        pop_wealth_table = [
            (range(1, 3), (-4, -2, "Destitute. Nearly everyone in town consistently lacks the barest essentials of what they need to survive.")),
            (range(3, 7), (-2, -1, "Impoverished. Around half of the town struggles to carve out even a meager existence.")),
            (range(7, 15), (0, 0, "Average. Most of the town’s population have enough to live a modest life. Those without are a minority.")),
            (range(15, 18), (-1, 1, "Prosperous. The majority have enough to live a good life and, of them, a fair amount can even live comfortably.")),
            (range(18, 20), (-2, 2, "Wealthy. Nearly everyone has what they need to live comfortably, many are able to live well, and some are very prosperous.")),
            (range(20, 21), (-3, 3, "Affluent. The entire town is able to live comfortably, with a significant portion living in luxury."))
        ]
        
        for wealth_range, wealth_info in pop_wealth_table:
            if roll in wealth_range:
                crime_mod,quality_mod, pop_wealth = wealth_info
                self.modifiers.crime_modifier += crime_mod
                self.modifiers.quality_modifier += quality_mod
                return pop_wealth
        
    def generate_crime(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.crime_modifier, 20), 1)
        crime_ranges = [
            (range(1, 3), (4, "Regular")),
            (range(3, 7), (3, "Common")),
            (range(7, 15), (2, "Average")),
            (range(15, 19), (1, "Uncommon")),
            (range(19, 21), (0, "Rare"))
        ]
        for crime_range, crime_info in crime_ranges:
            if roll in crime_range:
                urban_modifier, description = crime_info
                self.modifiers.urban_encounter_modifier += urban_modifier
                return description
    def generate_non_commercial_locations(self):
        roll_amount = 0 
        if "Very Small" in self.size:
            roll_amount = 1
        elif "Small" in self.size:
            roll_amount = 2
        elif "Medium" in self.size:
            roll_amount = 3
        elif "Large" in self.size:
            roll_amount = 4
        elif "Very Large" in self.size:
            roll_amount = 5
        
        for i in range(roll_amount):
            non_commercial_location_types = [
                self.generate_education_place(),
                self.generate_government_place(),
                self.generate_gathering_place(),
                self.generate_worship_place()
            ]
            
            self.non_commercial_locations.append(random.choice(non_commercial_location_types))

    def generate_education_place(self):
        return random.choice([
            "Academy/University. A conservatory devoted to the pursuit of higher knowledge, sometimes of a specific area of study.",
            "Archives/Library. A structure devoted to housing records and written information.",
            "Forum. A place designated for the use of intellectual debate and discussion.",
            "Schoolhouse. An institution focused on educating children."
        ])
        
    def generate_government_place(self):
        """
        Returns a randomly selected government building from the list of options.
    
        Returns:
            str: A randomly selected government building.
        """
        return random.choice([
            "Chancery. Used as an office for official documentation and administrative tasks.",
            "Courthouse. Used to hold trials or dispense justice.",
            "Town Hall. Used for official town business, audiences, and meetings.",
            "Treasury. Used to manage town finances and assets."
        ])
        
    def generate_gathering_place(self):
        return random.choice([
            "Amphitheater. Outdoor space with a stage and tiered seating.",
            "Dance Hall. Location for dances and festive events.",
            "Gathering Hall. General, open-use building, such as a community center, used for local activities, or where locals may simply socialize on a day-to-day basis.",
            "Outdoor Recreational Area. A tended space where locals might eat, take leisure time, or duel to the death..."
        ])

        
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
    
    # Commerical location functions need to take into account the 'isEconomicTown' flag and increase the size to be one higher.
    def generate_commerical_locations(self):
        location_amount = 0 + self.modifiers.commercial_locations_modifier
        ecomomic_bonus = 0
        if self.isEconomicTown:
            ecomomic_bonus = 2
        if "Very Small" in self.size:
            location_amount = 4 + ecomomic_bonus
        elif "Small" in self.size:
            location_amount = 6 + ecomomic_bonus
        elif "Medium" in self.size:
            location_amount = 8 + ecomomic_bonus
        elif "Large" in self.size:
            location_amount = 10 + ecomomic_bonus
        else:
            location_amount = 12
    
        shop_count = random.randint(1, location_amount)
        service_count = location_amount - shop_count
        
        for i in range(shop_count):
            self.shops.append(self.generate_shop())
        
        for i in range(service_count):
            self.services.append(self.generate_service())
        
    def generate_shop(self):
        roll = random.randint(1,100)
        locations = [
            (range(1, 5), "Baker. Bakes and sells fresh bread and, possibly, pastries."),
            (range(5, 9), "Butcher. Processes and sells fresh and/or dried meat."),
            (range(9, 13), "Cooper. Crafts wooden vessels held together with metal hoops, including barrels, buckets, etc."),
            (range(13, 17), "Carpenter. Builds with or carves wood, as well as carrying out repairs."),
            (range(17, 25), "General Store. Sells basic supplies, groceries, and various odds and ends."),
            (range(25, 29), "Herbalist. Sells common herbs and natural, non-magical remedies."),
            (range(29, 37), "Smithy. Sells and crafts metal tools and equipment, including very basic weapons and armor."),
            (range(37, 41), "Tailor. Makes and sells clothing, including hats and cloaks. Also sells general items made from cloth, such as blankets, and carries out repairs and alterations of cloth goods."),
            (range(41, 45), "Tanner/Taxidermist. Processes animal hides for practical or ornamental purposes."),
            (range(45, 49), "Thatcher. Builds roofs using layers of dried straw, reeds, rushes, etc."),
            (range(49, 53), "Wainwright. Builds carts and wagons."),
            (range(53, 57), "Weaver. Weaves raw fabric and baskets."),
            (range(57, 60), "Alchemist. Brews and sells potions, as well as mundane herbs and alchemical ingredients."),
            (range(60, 63), "Artist. Encompasses painter, sculptor or other visual art as appropriate."),
            (range(63, 66), "Bank & Exchange. Encompasses auctions, banking, and the specific selling of gems or exchange of currency."),
            (range(66, 69), "Cobbler. Makes and mends boots and shoes."),
            (range(69, 72), "Foundry/Smelting. Ore processing and metal fabrication."),
            (range(72, 75), "Mill. Facilities for milling grain."),
            (range(75, 78), "Textile Production. Larger scale than a single weaver, offering a wider array of materials in larger quantities."),
            (range(78, 81), "Shipwright. Builds and launches boats and/or ships. [Reroll if settlement is not bordering a significant source of water]"),
            (range(81, 83), "Rare Botanicals. Cultivates and sells herbs rare to the region."),
            (range(83, 85), "Luxury Furnishings. Procures and sells all manner of home items for fine living, including furniture, art, and other high-quality goods."),
            (range(85, 87), "Rare Libations & Fare. Sells (and, perhaps, makes or brews) drinks and/or food of surpassing quality or rarity to the region."),
            (range(87, 89), "Rare Trade Goods. Procures and sells items and materials, such as ores or textiles, that are rare to the region."),
            (range(89, 91), "Magic Shop - Armor. Sells magical items with a focus on armor and protective equipment."),
            (range(91, 93), "Magic Shop - Books. Sells magical items with a focus on literature, arcane tomes and lore. They may also carry books and documents of a rare and significant nature, though non-magical."),
            (range(93, 95), "Magic Shop - Clothing. Sells magical items with a focus on clothing of all types which bear magical properties."),
            (range(95, 97), "Magic Shop - Jewelry. Sells magical items with a focus on enchanted, or otherwise magically imbued, jewelry."),
            (range(97, 99), "Magic Shop - Weapons. Sells magical items with a focus on weapons with mystic properties and, perhaps, shields."),
            (range(99, 101), "Magic Shop - Miscellaneous & Curiosities. Procures and sells magical items with a focus on strange and rare artifacts of a wondrous or intriguing nature.")
        ]
        
        for location_range, location_info in locations:
            if roll in location_range:
                return location_info

    def hired_help_size(self):
        roll = random.randint(1, 12)
        hired_help_size = [
            (range(1, 7), "Individual Person. The hired help is a single person hiring out their services."),
            (range(7, 11), "Team. The hired help is a team of individuals who work together."),
            (range(11, 13), "Guild. An organized guild is hiring out their services. When hired, a portion of the guild’s members handle the job, not the entire guild (unless the job is very large).")
        ]
        
        for ranges, info in hired_help_size:
            if roll in ranges:
                return info

    def generate_service(self):
        roll = random.randint(1, 100)
        services = [
            (range(1, 9), "Barber. Provides grooming services, such as haircuts or shaves."),
            (range(9, 17), "Bathhouse. Provides spaces for bathing."),
            (range(17, 25), "Doctor/Apothecary. Provides medical care."),
            (range(25, 33), "House of Leisure. Provides entertainment and/or relaxation (GM may decide what kind)."),
            (range(33, 45), "Inn. Provides accommodation, as well as a place to have a bath and a decent meal."),
            (range(45, 53), "Club. Provides entertainment via comedic, dramatic or musical performance."),
            (range(53, 61), "Soothsayer. Provides magical prediction and prophecy - sayers of sooth!"),
            (range(61, 69), "Stable. Provides boarding accommodation for mounts, as well as selling carts, animals, and their tack."),
            (range(69, 81), "Tavern. Provides food and drink."),
            (range(81, 83), f"Hired Help - Brutes and Brawlers. Thugs, ruffians and muscle. (Size: {self.hired_help_size()})"),
            (range(83, 85), f"Hired Help - Cloak and Dagger. Assassins, thieves and spies. (Size: {self.hired_help_size()})"),
            (range(85, 87), f"Hired Help - Bows and Slings. Archers and ranged attack specialists. (Size: {self.hired_help_size()})"),
            (range(87, 89), f"Hired Help - Scribes and Clerks. Masters of history, literature, mathematics and/or business. (Size: {self.hired_help_size()})"),
            (range(89, 91), f"Hired Help - Guides and Trackers. Scouts, rangers and wilderness experts. (Size: {self.hired_help_size()})"),
            (range(91, 93), f"Hired Help - Caravan and Mount. Specialists in transportation and journeys to various locations as well as expedition organization and management. (Size: {self.hired_help_size()})"),
            (range(93, 95), f"Hired Help - Arcane Academics. Experts in matters of magic and lore (may also be natural magic or something else; it need not be exclusively arcane). (Size: {self.hired_help_size()})"),
            (range(95, 97), f"Hired Help - Magic Mercenaries. Specialists trained the use of arcane or non-divine magic in combat and practical mission scenarios. (Size: {self.hired_help_size()})"),
            (range(97, 99), f"Hired Help - Priestly Guidance. Sages offering counsel in all matters of religion and the divine. (Size: {self.hired_help_size()})"),
            (range(99, 101), f"Hired Help - Hands of the Divine. Specialists trained in the use of divine magic in combat and practical mission scenarios. (Size: {self.hired_help_size()})")
        ]

        for ranges, info in services:
            if roll in ranges:
                return info
    
    def generate_noteworthy_officals(self):
        
        offical_amount = random.randint(1, 4)
        for i in range(offical_amount):
            self.noteworthy_officals.append(random.choice([
                "Catchpole. Catches and brings in debtors.", 
                "Clerk. Recordkeeper for the town.",
                "Exchequer. Responsible for taxes.",
                "Jailer. In charge of confining prisoners.",
                "Judge. Decision-maker in legal matters.",
                "Liner. Determines property boundaries.",
                "Master of Revels. Lead organizer of festivals and special events.",
                "Master of Stores. Oversees the town’s stores of supplies such as grain or building materials."
            ]))
        
    def __str__(self):
        note = f"Town: {self.name}\n"
        note += f"Type: {self.type}\n"
        note += f"Origin: {self.origin}\n"
        note += f"Priority: {self.priority}\n"
        note += f"Specialty: {self.specialty}\n"
        note += f"Age: {self.age}\n"
        note += f"Size: {self.size}\n"
        note += f"Condition: {self.condition}\n"
        note += f"Environment: {self.environment}\n"
        note += f"Prosperity: {self.prosperity}\n"
        note += f"Market Square: {self.market_square}\n"
        note += f"Merchant Overflow: {self.merchant_overflow}\n"
        note += f"Fortification: {self.fortification}\n"
        note += f"Population Density: {self.pop_density}\n"
        note += f"Population Overflow: {self.pop_overflow}\n"
        note += f"Farms and Resources: {', '.join(self.farms_resources)}\n"
        note += f"Visitor Traffic: {self.visitor_traffic}\n"
        note += f"Night Activity: {self.night_activity}\n"
        note += f"Demographics: {self.demographics}\n"
        note += f"Disposition: {self.disposition}\n"
        note += f"Leadership: {self.leadership}\n"
        note += f"Law Enforcement: {self.law_enforcement}\n"
        note += f"Population Wealth: {self.pop_wealth}\n"
        note += f"Crime: {self.crime}\n"
        note += "Shops:\n"
        for shop in self.shops:
            note += f"  - {shop}\n"
        note += "Services:\n"
        for service in self.services:
            note += f"  - {service}\n"
        note += "Noteworthy Officials:\n"
        for official in self.noteworthy_officals:
            note += f"  - {official}\n"
        note += "Non-commercial Locations:\n"
        for location in self.non_commercial_locations:
            note += f"  - {location}\n"
        return note