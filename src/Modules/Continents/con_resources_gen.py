import random

bands = ["Northmost", "Northen","Centre","Southern","Southmost"]
resources = [
    "Minerals",
    "Ordinary Metal Ores",
    "Spices And Herbs",
    "Foodstuff (Crops and Livestock)",
    "Wild Game",
    "Precious Stones & Gems",
    "Medicinal Plants",
    "Lumber",
    "Magical Metal Ores",
    "Magical Infused Locations"
]
type_weights = {
    "Northmost": [0.1, 0.1, 0.15, 0.2, 0.15, 0.1, 0.05, 0.05, 0.05, 0.05],
    "Northen": [0.1, 0.1, 0.15, 0.2, 0.15, 0.1, 0.05, 0.05, 0.05, 0.05],
    "Centre": [0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05],
    "Southern": [0.1, 0.1, 0.05, 0.15, 0.2, 0.15, 0.05, 0.1, 0.05, 0.05],
    "Southmost": [0.1, 0.1, 0.05, 0.15, 0.1, 0.1, 0.15, 0.15, 0.05, 0.05]
}
rarity_levels = ["Very Common", "Common", "Uncommon", "Rare", "Very Rare"]
rarity_weights = [0.4, 0.3, 0.15, 0.1, 0.05]

def generate_resources():
    resource_rarities = {}
    for band in bands:  # Assuming 5 regions
        resources_picked = []
        for _ in range(random.randint(1,3)):
            resource = random.choices(resources, weights = type_weights[band], k=1)[0]
            rarity = random.choices(rarity_levels, rarity_weights, k=1)[0]
            resources_picked.append((resource, rarity))
        resource_rarities[band] = resources_picked
    return resource_rarities
