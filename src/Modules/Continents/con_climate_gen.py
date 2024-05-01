import random

climate_zones = ["Tropical", "Dry", "Temperate", "Continental", "Polar"]
geographic_features = ["Mountains", "Rivers", "Plains", "Coasts", "Forests", "Savannas", "Taiga", "Rain-Forests", "Swamp"]
bands = ["Northmost", "Northen","Centre","Southern","Southmost"]

def generate_climate(band):
    weights = [
        [0.5, 0.4, 0.1, 0, 0],   #Tropical Band
        [0.35, 0.35, 0.3, 0, 0], #Subtropical Band
        [0.1, 0.2, 0.4, 0.3, 0], #Temperate Band
        [0, 0.1, 0.4, 0.4, 0.1], #Subpolar Band
        [0, 0, 0, 0.2, 0.8],    #Polar Band
    ]
    climate = random.choices(climate_zones, weights=weights[band], k=1)[0]
    climate += " climate"
    feature = random.choice(geographic_features)
    
    # if feature == "Mountains":
    #     climate += " with a rain shadow effect"
    # elif feature == "Rivers":
    #     climate += " characterized by temperate micro-climates"
    # elif feature == "Coasts":
    #     climate += " with moderate seasonal changes and high humidity"
    # elif feature == "Forests":
    #     climate += " with rich biodiversity"
    # elif feature == "Savannas":
    #     climate += " with sparse tree cover and distinct wet and dry seasons"
    # elif feature == "Taiga":
    #     climate += " with long, cold winters and brief, warm summers"
    # elif feature == "Rain-Forests":
    #     climate += " with high precipitation and great species diversity"
    # elif feature == "Swamp":
    #     climate += " with high humidity and a variety of amphibious life"
        
    return climate, feature

# Now to generate a continent.

def generate_con_climates():
    desc = {}
    band_count = 0
    for band in bands:
        climate,feature = generate_climate(band_count)
        # if band == 0: 
        #     desc += f"The northernmost region of the continent is characterized by '{climate}' due to its '{feature}'.\n"
        # elif band == 4:
        #     desc += f"The southernmost region of the continent is marked by a '{climate}' due to its '{feature}'."
        # else:
        #     desc += f"Moving further, the region transitions into a '{climate}' due to the presence of '{feature}'.\n"
        desc[band] = {"climate": climate, "feature": feature}
        band_count += 1

    return desc