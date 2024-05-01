import random
from src.Modules.Settlement.Settlement import Settlement

class Village(Settlement):
    def __init__(self):
        """
        Initializes a new instance of the Village class.
        """
        super().__init__()
        
        self.type = "Village"
        self.name = self.generate_name()
        self.hardship_amount = 0
        self.hardships = []
        self.specialty = "Unknown"
        self.resource = "Unknown"
        self.recent_history = "Unknown"
        self.pop_density = "Unknown"
        self.demographics = "Unknown"
        self.disposition = "Unknown"
        self.law_enforcement = "Unknown"
        self.leadership = "Unknown"
        self.pop_wealth = "Unknown"
        self.crime = "Unknown"
        self.place_of_worship_amount = 0
        self.places_of_worship = []
        self.place_of_gathering_amount = 0
        self.places_of_gathering = []
        self.locations = []
        self.supersition = "Unknown"
        
    def generate(self):
        """
        Generates a new village.
        """
        self.age = self.generate_age()
        self.hardship_amount = self.generate_hardship_amount()
        self.hardships = self.generate_hardships()
        self.size = self.generate_size()
        self.condition = self.generate_condition()
        self.environment = self.generate_environment()
        self.specialty = self.generate_specialty()
        self.resource = self.generate_resource()
        self.recent_history = self.generate_recent_history()
        self.pop_density = self.generate_pop_density()
        self.demographics = self.generate_demographics()
        self.disposition = self.generate_disposition()
        self.law_enforcement = self.generate_law_enforcement()
        self.leadership = self.generate_leadership()
        self.pop_wealth = self.generate_pop_wealth()
        self.crime = self.generate_crime()
        self.place_of_worship_amount = self.generate_place_of_worship_amount()
        self.places_of_worship = self.generate_places_of_worship()
        self.place_of_gathering_amount = self.generate_place_of_gathering_amount()
        self.places_of_gathering = self.generate_places_of_gathering()
        self.locations.extend(self.generate_locations())
        self.supersition = self.generate_supersition()
        return self
    
    def generate_age(self):
        result = random.randint(1, 20)
        age_ranges = [
            (range(0, 5), (-5, -4, "Recent")),
            (range(6, 10), (-2,-2, "Established")),
            (range(11, 14), (0,0, "Mature")),
            (range(15, 18), (0, 2, "Old")),
            (range(19, 21), (0, 4, "Ancient"))
        ]
        
        for age_range, age_info in age_ranges:
            if result in age_range:
                pop_density_mod, hardship_mod, description = age_info
                self.modifiers.population_density_modifier += pop_density_mod
                self.modifiers.hardship_likelihood_modifier += hardship_mod
                return description

    
    def generate_hardship_amount(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.hardship_likelihood_modifier, 20), 1)
        
        hardship_ranges = [
            (range(1, 2), (0)),
            (range(3, 6), (1)),
            (range(7, 14), (2)),
            (range(15, 18), (3)),
            (range(19, 21), (4))
        ]
        
        for hardship_range, hardship_info in hardship_ranges:
            if roll in hardship_range:
                return hardship_info

    def create_outcome(self):
        roll = random.randint(1, 10)
        hardship_outcome_table =[
            (range(1, 3), (-5, "Catastrophic")),
            (range(3, 5), (-4, "Terrible")),
            (range(5, 7), (-3, "Heavy")),
            (range(7, 9), (-2, "Small")),
            (range(9, 11), (-1, "Minimal")),     
        ]
        
        for hardship_outcome_range, hardship_outcome_info in hardship_outcome_table:
            if roll in hardship_outcome_range:
                mod, description = hardship_outcome_info
                return {'modifier':mod, 'description': description}
    
    def generate_hardships(self):
        result = []
        hardship_type_table = [
            (1, "Plague, The community fell victim to disease. Impact on Village: "),
            (2, "Bandits took control of the community. Impact on Village: "),
            (3, "The community is under raid by Marauders. Impact on Village: "),
            (4, "The community is struggling with famine or food shortage. Impact on Village: "),
            (5, "The local region is facing harsh weather conditions. Impact on Village: "),
            (6, "Inter-Community Conflict/Violence has broken out. Impact on Village: "),
            (7, "A key member of the community died or went missing. Impact on Village: "),
            (8, "The village was struck by the ravages of war. Impact on Village: "),
        ]
        for index, (hardship_range, hardship_info) in enumerate(hardship_type_table):
            outcome = self.create_outcome()
            roll = random.randint(1, len(hardship_type_table))
            
            for hardship_range, hardship_info in hardship_type_table:
                mod = outcome["modifier"]
                description = hardship_info + outcome["description"]
                if roll == hardship_range:
                    if hardship_range == 1:
                        self.modifiers.population_density_modifier += mod
                    elif hardship_range == 2:
                        self.modifiers.population_wealth_modifier += mod
                    elif hardship_range == 3:
                        self.modifiers.size_modifier += mod
                        self.modifiers.population_wealth_modifier += mod
                        self.modifiers.population_density_modifier += mod
                    elif hardship_range == 4:
                        self.modifiers.population_density_modifier += mod
                    elif hardship_range == 5:
                        self.modifiers.condition_modifier += mod
                        self.modifiers.size_modifier += mod
                    elif hardship_range == 6:
                        self.modifiers.disposition_modifier += mod
                        self.modifiers.population_density_modifier += mod
                    elif hardship_range == 7:
                        self.modifiers.disposition_modifier += mod
                    elif hardship_range == 8:
                        self.modifiers.population_density_modifier += mod
                        self.modifiers.size_modifier += mod
                        self.modifiers.condition_modifier += mod

                    result.append(description)
                    hardship_type_table.pop(index)
        
        return result
                    
    def generate_specialty(self):
        result = random.choice(['None. The village is unremarkable, or not widely known for any particular thing.',
                       'Food or Drink. Someone in the village makes a particular food or drink (such as bread, stew, produce, ale, wine, etc.) that has gained some notoriety. They may own an establishment, but could easily just sell it out of their home.',
                       'Location Proximity. The village itself may not be very special, but it is near somewhere that is, such as a stunning vista, or a site of historical significance.',
                       'Livestock. The village is known for breeding strong and healthy (perhaps, even pedigree) animals, such as horses, cattle, sheep, etc.',
                       'Crop. The village is known for a particularly notable crop. This could mean rare, high-quality, plentiful, or a mix of the three.',
                       'Crafted Goods. The village is known for the craft of a certain item, or type of goods, widely liked and highly valued, such as hand-crafted furniture, a category of clothing item, etc.'])    
        return result
    
    def generate_resource(self):
        resources = {
            1: {
                'Resource': 'Crops',
                'Locations': ['farm(s)', 'mill(s)', 'storage locations (silos or barns)']
            },
            2: {
                'Resource': 'Dairy',
                'Locations': ['cellar', 'creamery', 'field/barn/coop']
            },
            3: {
                'Resource': 'Herbs',
                'Locations': ['herbalist’s hut', 'gardens']
            },
            4: {
                'Resource': 'Fishing',
                'Locations': ['fisherman’s stand', 'wharf/pier']
            },
            5: {
                'Resource': 'Livestock (Labor)',
                'Locations': ['stable', 'barn']
            },
            6: {
                'Resource': 'Livestock (Meat and Hides)',
                'Locations': ['barn', 'pens', 'small butcher’s shop']
            },
            7: {
                'Resource': 'Livestock (Shearing)',
                'Locations': ['shearing shed', 'storage', 'fields/barn', 'small stall/shop']
            },
            8: {
                'Resource': 'Logging and Lumber',
                'Locations': ['logging camp', 'carpenters workshop']
            },
            9: {
                'Resource': 'Mining',
                'Locations': ['foreman’s station', 'mine', 'smithy']
            },
            10: {
                'Resource': 'Quarrying and Masonry',
                'Locations': ['mason or foreman’s station']
            }
        }
        result_key = random.choice(list(resources.keys()))
        result = resources[result_key]
        self.locations.extend(result['Locations'])
        
        return result['Resource']
            
    def generate_recent_history(self):
        recent_history = random.choice([
            "Animal Issues. Livestock, or pets, may have been ravaged by local wildlife, or monsters, or animals may have been struck by sickness or pestilence.",
            "Attacks. Members of the community have been attacked, either by brigands or, perhaps, monsters.",
            "Bumper Production. A staple resource of the village has yielded very well, recently.",
            "Out of Favor. The village has been subject to the ire of a nearby ruler, or entity.",
            "Entertainment. A certain form of entertainment is proving popular, whether a game or pastime, the arrival of a storyteller or musician, or something else.",
            "Fear. Something unnerving, or frightening, has happened recently.",
            "Good Fortune. The village has received favorable notice from a nearby ruler, or entity of note.",
            "Infestation. Some form of vermin, or pest, has recently beset the village, and has become an ongoing issue.",
            "Poor Production. A staple resource of the village has yielded poorly of late.",
            "Power Vacuum. The death, or absence, of a local leadership figure, or figures, has led to internal strife within the community.",
            "Safe Haven. The village has become a sanctuary for refugees, or those in need.",
            "Wartorn. The village was occupied by military forces, and suffered damages, during wartime in the recent past."
            ])
        return recent_history

    def generate_pop_density(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.population_density_modifier, 20), 1)
        pop_density_table =[
            (range(1, 2), (2, "Skeleton. There are only enough people here for the village to function at its most basic level.")),
            (range(3, 6), (1, "Sparse. People are living here, but not many. They are able to handle all tasks that need doing but, perhaps, with some difficulty.")),
            (range(7, 14), (0, "Populous. There are enough people here for the village to manage all tasks without difficulty.")),
            (range(15, 18), (-1, "Dense. The village seems to have a large amount of people for its size. There are many hands available to help with any work that needs doing.")),
            (range(19, 21), (-2, "Congested. The village has as many people in it as it can hold, and camps may be cropping up on the outskirts. There are plenty of hands available to help with work but, unless the work is very large-scale (such as quarrying), there may be at least some idle people.")),       
        ]
        
        for pop_dense_range, pop_dense_info in pop_density_table:
            if roll == pop_dense_range:
                crime_mod, desc = pop_dense_info
                self.modifiers.crime_modifier += crime_mod
                return desc
        
    def generate_demographics(self):
        roll = random.randint(1, 20)
        demographics_ranges = [
            (range(1, 8), "100% Primary Race"),
            (range(9, 12), "60% Primary Race + 40% Secondary Race"),
            (range(13, 15), "50% Primary Race + 25% Secondary Race + 15% tertiary Race + 10% Other Races"),
            (range(16, 17), "20% Primary Race + all other Races in varieties"),
            (range(18, 19), "80% Primary Race + 20% Secondary Race"),
            (range(20, 21), "No Racial Representation, Ever shifting") 
        ]
        for demographics_range, demographics_info in demographics_ranges:
            if roll in demographics_range:
                print(demographics_info)
                return demographics_info
        return "No Racial Representation"
    
    def generate_disposition(self):
        roll = max(min(random.randint(0, 20) + self.modifiers.disposition_modifier, 20), 1)
        disposition_ranges = [
            (range(0, 2), "Hostile"),
            (range(3, 6), "Neutral"),
            (range(7, 14), "Unfriendly"),
            (range(15, 18), "Friendly"),
            (range(19, 21), "Open")
        ]
        for disposition_range, disposition_info in disposition_ranges:
            if roll in disposition_range:
                return disposition_info
        return "Neutral"
    
    def generate_law_enforcement(self):
        roll = random.randint(1, 20)
        law_enforcement_ranges = [
            (range(1, 2), (-2, "Non-Existant")),
            (range(3, 6), (-1, "Disorganized Rabble")),
            (range(7, 14), (0, "Organized Rabble")),
            (range(15, 18), (+1, "Sheriff")),
            (range(19, 21), (+2, "Sheriff and Deputies"))
        ]
        for law_enforcement_range, law_enforcement_info in law_enforcement_ranges:
            if roll in law_enforcement_range:
                crime_mod, desc = law_enforcement_info
                self.modifiers.crime_modifier += crime_mod
                return desc
        return "Organized Rabble"
    
    def generate_leadership(self):
        leadership_choice = random.choice(['No Leader', 'Natural Village Elder', 'External Ruler', 'Local Council', 'Single, Elected Leader', 'Anarcho-Syndicalist Commune'])
        return leadership_choice
    
    def generate_pop_wealth(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.population_wealth_modifier, 20), 1)
        pop_wealth_ranges = [
            (range(1, 2), (-2, "Destitute")),
            (range(3, 6), (-1, "Impoverished")),
            (range(7, 14),  (0, "Average")),
            (range(15, 17), (-1, "Prosperous")),
            (range(18, 19), (-2, "Wealthy")),
            (range(20, 21), (-3, "Affluent"))
        ]
        for pop_wealth_range, pop_wealth_info in pop_wealth_ranges:
            if roll in pop_wealth_range:
                crime_modifier, description = pop_wealth_info
                self.modifiers.crime_modifier += crime_modifier
                return description
        return "Average"
    
    def generate_crime(self):
        roll = max(min(random.randint(1, 20) + self.modifiers.crime_modifier, 20), 1)
        crime_ranges = [
            (range(1, 2), (3, "Average")),
            (range(3, 6), (2, "Uncommon")),
            (range(7, 14), (1, "Rare")),
            (range(15, 18), (0, "Little-to-None"))
        ]
        for crime_range, crime_info in crime_ranges:
            if roll in crime_range:
                urban_modifier, description = crime_info
                self.modifiers.urban_encounter_modifier += urban_modifier
                return description
        return "Average"
    
    def generate_place_of_worship_amount(self):
        roll = 0
        if self.size == "Very Small (20 standing structures)":
            roll += 1
        elif self.size == "Small (40 standing structures)" or self.size == "Medium (60 standing structures)":
            roll += random.randint(1, 2)
        else:
            roll += random.randint(1, 2) + 1
        return roll
    
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
    
    def generate_places_of_worship(self):
        result = []
        worship_place_table = [
            (range(1, 2), "Secret. The place of worship’s size is unclear, as the location is not publicly known."),
            (range(2, 8), "Altar. A small shrine or, perhaps, a tiny shack, usually evincing some various items or images relating to that which the faith venerates."),
            (range(8, 15), "Oratory. A modest building with seating for attendees, appointed with various items or images relating to that which the faith venerates."),
            (range(15, 18), "Sanctuary. A large, well-appointed structure, able to comfortably accommodate up to a few hundred people."),
            (range(18, 20), "Temple. A grand building, replete with elements like high ceilings, plush furnishings, and other impressive ornamental and/or architectural features. It can hold nearly a thousand attendees."),
            (range(20, 21), "Great Temple. An awe-inspiring structure, devoted to that which it venerates. No expense was spared in its construction. It might display such elements as stunning frescos, elaborate stained-glass scenes, and towering, gilded statues. Walking into a great temple is a rare and striking experience for those who do not live near one.")
        ]
        for i in range(self.place_of_worship_amount):
            fervency = self.generate_local_fervency()
            alignment_weights = [10, 40, 50]
            alignment_choices = ['evil', 'neutral', 'good']
            selected_alignment = random.choices(alignment_choices, weights=alignment_weights, k=1)[0]
            roll = random.randint(1,20)
            for worship_place_range, worship_place_info in worship_place_table:
                if roll in worship_place_range:
                    result.append(worship_place_info + " Worship is of a " + selected_alignment + " Deity. This Deities followers are " + fervency)
        return result
        
    def generate_place_of_gathering_amount(self):
        roll = 0
        if self.size == "Very Small (20 standing structures)":
            roll += random.randint(1, 2) - 1
        elif self.size == "Small (40 standing structures)":
            roll += 1
        elif self.size == "Medium (60 standing structures)":
            roll += random.randint(1, 2)
        elif self.size == "Large (80 standing structures)":
            roll += random.randint(1, 2)
        else:
            roll += random.randint(1, 2) + 1
        return roll
    
    def generate_places_of_gathering(self):
        result = []
        for i in range(self.place_of_gathering_amount):
            roll = random.choice(['Amphitheater. Outdoor space with a stage andtiered seating.', 'Dance Hall. Location for dances and festive events.', 'Gathering Hall. General building used for community-organised activities.','Outdoor Recreational Area. A tended space where locals might eat, take leisure time, or duel to the death...'])
            result.append(roll)
        return result
    
    def generate_location_amount(self):
        roll = 0
        if self.size == "Very Small (20 standing structures)":
            roll += random.randint(1, 2) - 1
        elif self.size == "Small (40 standing structures)":
            roll += random.randint(1, 2)
        elif self.size == "Medium (60 standing structures)":
            roll += random.randint(1, 2) + 1
        elif self.size == "Large (80 standing structures)":
            roll += random.randint(1, 2) + random.randint(1, 2)
        else:
            roll += (random.randint(1, 2) + random.randint(1, 2)) + 1
        return roll
    
    def generate_locations(self):
        result = []
        locations = [
            ((1, 5), "Baker. Bakes and sells fresh bread and, possibly, pastries."),
            ((5, 8), "Butcher. Processes and sells fresh and/or dried meat."),
            ((8, 12), "Cooper. Crafts wooden vessels held together with metal hoops, including barrels, buckets, etc."),
            ((12, 16), "Carpenter. Builds with or carves wood, as well as carrying out repairs."),
            ((16, 20), "General Store. Sells basic supplies, groceries, and various odds and ends."),
            ((20, 24), "Herbalist. Sells common herbs and natural, non-magical remedies."),
            ((24, 28), "Smithy. Sells and crafts metal tools and equipment, including very basic weapons and armor."),
            ((28, 32), "Tailor. Makes and sells clothing, including hats and cloaks. Also sells general items made from cloth, such as blankets, and carries out repairs and alterations of cloth goods."),
            ((32, 36), "Tanner/Taxidermist. Processes animal hides for practical or ornamental purposes."),
            ((36, 40), "Thatcher. Builds roofs using layers of dried straw, reeds, rushes, etc."),
            ((40, 44), "Wainwright. Builds carts and wagons."),
            ((44, 48), "Weaver. Weaves raw fabric and baskets."),
            ((48, 50), "Alchemist. Brews and sells potions, as well as mundane herbs and alchemical ingredients."),
            ((50, 52), "Artist. Encompasses painter, sculptor or other visual art as appropriate."),
            ((52, 56), "Cobbler. Makes and mends boots and shoes."),
            ((56, 60), "Mill. Facilities for milling grain."),
            ((60, 62), "Shipwright. Builds and launches boats and/or ships. [Reroll if settlement is not bordering a significant source of water]"),
            ((62, 63), "Rare Botanicals. Cultivates and sells herbs rare to the region."),
            ((63, 64), "Luxury Furnishings. Procures and sells all manner of home items for fine living, including furniture, art, and other high-quality goods."),
            ((64, 65), "Rare Libations & Fare. Sells (and, perhaps, makes or brews) drinks and/or food of surpassing quality or rarity to the region."),
            ((65, 66), "Rare Trade Goods. Procures and sells items and materials, such as ores or textiles, that are rare to the region."),
            ((66, 67), "Magic Shop - Armor. Sells magical items with a focus on armor and protective equipment."),
            ((67, 68), "Magic Shop - Books. Sells magical items with a focus on literature, arcane tomes and lore. They may also carry books and documents (such as maps and records) of a rare and significant nature, though non-magical."),
            ((68, 69), "Magic Shop - Clothing. Sells magical items with a focus on clothing of all types which bear magical properties."),
            ((69, 70), "Magic Shop - Jewelry. Sells magical items with a focus on enchanted, or otherwise magically imbued, jewelry."),
            ((70, 71), "Magic Shop - Weapons. Sells magical items with a focus on weapons with mystic properties and, perhaps, shields."),
            ((71, 72), "Magic Shop - Miscellaneous & Curiosities. Procures and sells magical items with a focus on strange and rare artifacts of a wondrous or intriguing nature."),
            ((72, 74), "Barber. Provides grooming services, such as haircuts or shaves."),
            ((74, 76), "Bathhouse. Provides spaces for bathing."),
            ((76, 78), "Doctor/Apothecary. Provides medical care."),
            ((78, 80), "House of Leisure. Provides entertainment and/or relaxation (GM may decide what kind)."),
            ((80, 85), "Inn. Provides accommodation, as well as a place to have a bath and a decent meal."),
            ((85, 90), "Soothsayer. Provides magical prediction and prophecy - sayers of sooth!"),
            ((90, 95), "Stable. Provides boarding accommodation for mounts, as well as selling carts, animals, and their tack."),
            ((95, 100), "Tavern. Provides food and drink."),
            ((100, 101), "Burned down or abandoned business. This used to be a place of business, but isn’t anymore.")
        ]
        for i in range(self.generate_location_amount()):
            # Extract ranges and descriptions
            ranges = [location[0] for location in locations]
            descriptions = [location[1] for location in locations]

            # Generate a location based on weights
            selected_location = random.choices(descriptions, weights=[end - start + 1 for start, end in ranges])[0]
            result.append(selected_location)
        return result
    
    def generate_supersition(self):
        superstitions = [
            "Burying a dead cat under the doorstep is essential for a building’s prosperity.",
            "Half a chicken will cure any number of ailments (from plague, to pimples) when tied to the afflicted area.",
            "Placing mirrors, or large reflective objects, opposite one another in a room can open an invisible doorway for devils.",
            "Hanging mistletoe above the lintel is a sacred oath that the host will harm none who enter.",
            "Never stick a knife point-down into wood, or a cutting block, as it invites acts of violence among those nearby.",
            "Evil spirits can lurk within the leaves of cabbages and sprouts; you must carve a holy sign into the bottom before cooking them.",
            "After visiting a grave or cemetery, one must take a winding path home, making stops along the way, in order to lose any tag-along spirits.",
            "Giving a knife as a gift will sever a friendship, so they must always be symbolically paid for.",
            "Never use dull scissors as, if you do, you risk accidentally cutting the thread tethering your soul to your body.",
            "Knowing your full name allows those who wish you ill to put a curse on you, so keep your middle names secret.",
            "A carrion bird landing in front of you means you, or someone close to you, will die soon.",
            "A single magpie is bad luck, but saluting the lone magpie (‘Good morning Mr. Magpie, how’s your wife?’) will turn bad luck into good.",
            "In games, never grab the dice. The owner of the dice must give them to the first person who must roll, who must pass them on and so on. Doing otherwise will curse the dice for a fortnight.",
            "A pregnant woman must not go out in the evenings, lest the overwhelming darkness taint the child. If she must go out, she must carry a second lamp directly in front of her stomach, to protect the baby.",
            "When making a wish at a well, the value of coin you throw in should be commensurate with that of your wish.",
            "When speaking with adult men or women, it is bad luck to not address them as ‘sir’ or ‘madam’, at least once, during the exchange.",
            "When mining or cutting stone, the chips from the first strike of the day must be pocketed by the one who struck, lest earth spirits feel taken for granted.",
            "Proclaiming new love at dawn or dusk is bad luck.",
            "Kissing the door frame of your house upon entry or exit asks the gods’ protection upon it.",
            "Never leave an empty spirits glass or cup right-side-up, lest an actual spirit attempt to fill the void, inhabiting the body of the next drinker."
        ]
        return random.choice(superstitions)

    def __str__(self):
        info = [
            f"Type: {self.type}",
            f"Name: {self.name}",
            f"Hardships: {self.format_table(self.hardships)}",
            f"Specialty: {self.specialty}",
            f"Resource: {self.resource}",
            f"Recent History: {self.recent_history}",
            f"Population Density: {self.pop_density}",
            f"Demographics: {self.demographics}",
            f"Disposition: {self.disposition}",
            f"Law Enforcement: {self.law_enforcement}",
            f"Leadership: {self.leadership}",
            f"Population Wealth: {self.pop_wealth}",
            f"Crime: {self.crime}",
            f"Places of Worship: {self.format_table(self.places_of_worship)}",
            f"Places of Gathering: {self.format_table(self.places_of_gathering)}",
            f"Locations: {self.format_table(self.locations)}",
            f"Village superstition: {self.supersition}"
        ]
        return '\n'.join(info)
    
    def format_table(self, items):
        if not items:
            return "Unknown"
        formatted_items = "\n"
        for item in items:
            formatted_items += f"- {item}\n"
        return formatted_items
