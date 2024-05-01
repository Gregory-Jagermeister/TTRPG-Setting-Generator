class SettlementModifiers:
    def __init__(self):
        
        # Trading post Specific Attributes / Common Attributes
        self.size_modifier = 0
        self.crime_modifier = 0
        self.population_wealth_modifier = 0
        self.visitor_traffic_modifier = 0
        self.quality_modifier = 0
        self.urban_encounter_modifier = 0
        
        # Village/Town Specific Attributes
        self.population_density_modifier = 0
        self.hardship_likelihood_modifier = 0
        self.condition_modifier = 0
        
        # Town Specific Attributes
        self.fortifcation_modifier = 0
        self.law_enforcement_modifier = 0
        self.market_square_modifier = 0
        self.worship_place_size_modifier = 0
        self.population_overflow_modifier = 0
        self.disposition_modifier = 0
        self.night_activity_modifier = 0
        self.farm_resource_modifier = 0
        self.commercial_locations_modifier = 0
        
        # City Specific Attributes
        
        self.number_of_districts_modifier = 0
        self.general_condition_modifier = 0
        self.general_crime_modifier = 0
        self.administration_district_crime_modifier = 0
        self.administration_district_condition_modifier = 0
        self.administration_district_quality_modifier = 0
        
        self.arcane_district_crime_modifier = 0
        self.arcane_district_condition_modifier = 0
        self.arcane_district_quality_modifier = 0
        
        self.botanical_district_crime_modifier = 0
        self.botanical_district_condition_modifier = 0
        self.botanical_district_quality_modifier = 0
        
        self.craft_district_crime_modifier = 0
        self.craft_district_condition_modifier = 0
        self.craft_district_quality_modifier = 0
        
        self.docks_district_crime_modifier = 0
        self.docks_district_condition_modifier = 0
        self.docks_district_quality_modifier = 0
        
        self.industrial_district_crime_modifier = 0
        self.industrial_district_condition_modifier = 0
        self.industrial_district_quality_modifier = 0
        
        self.market_district_crime_modifier = 0
        self.market_district_condition_modifier = 0
        self.market_district_quality_modifier = 0
        
        self.merchant_district_crime_modifier = 0
        self.merchant_district_condition_modifier = 0
        self.merchant_district_quality_modifier = 0
        
        self.scholar_district_crime_modifier = 0
        self.scholar_district_condition_modifier = 0
        self.scholar_district_quality_modifier = 0
        
        self.slums_district_crime_modifier = 0
        self.slums_district_condition_modifier = 0
        self.slums_district_quality_modifier = -1
        
        self.temple_district_crime_modifier = 0
        self.temple_district_condition_modifier = 0
        self.temple_district_quality_modifier = 0
        
        self.upper_class_district_crime_modifier = 0
        self.upper_class_district_condition_modifier = 3
        self.upper_class_district_quality_modifier = 3
        
        # Capital Specific Attributes
        self.residence_modifier = 0
        