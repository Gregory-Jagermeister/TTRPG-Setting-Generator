import random
from collections import defaultdict

def build_transition_matrix(names):
    matrix = defaultdict(list)

    for name in names:
        for i in range(len(name) - 1):
            matrix[name[i]].append(name[i + 1])

    for key in matrix:
        total = len(matrix[key])
        counts = {char: matrix[key].count(char) / total for char in set(matrix[key])}
        matrix[key] = [(char, counts[char]) for char in set(matrix[key])]

    return matrix

def generate_name_struct(seed, transition_matrix, length=8):
    name = seed
    current_char = seed

    for _ in range(length - 1):
        next_char = random.choices(
            [char[0] for char in transition_matrix[current_char]],
            weights=[char[1] for char in transition_matrix[current_char]]
        )
        name += next_char[0]
        current_char = next_char[0]

    # Add a word like "Empire," "Isles," "Wilderness," or "World" with a 10% chance
    if random.random() < 0.25:
        additional_word = random.choice(["Empire", "Isles", "Wilderness", "Realm", "Dominion", "Territory", "Lands", "Providence",
    "Expanse", "Frontier", "Territorium", "Haven", "Commonwealth",
    "Sovereignty", "Federation", "Outlands", "Sanctuary",
    "Dominance", "Outskirts", "Conclave", "Sector", "Colony"])
        name = f"The {name} {additional_word}"

    return name

def generate_name():
    # Example usage with training data
    training_data = [
        "Aldorium",
        "Nordrath",
        "Zephyria",
        "Gloamterra",
        "Eldrialis",
        "Thornhold",
        "Sylvandria",
        "Frostreach",
        "Ironspire",
        "Dragonia",
        "Shadowlands",
        "Silverpeaks",
        "Starhaven",
        "Emberisles",
        "Stormwatch",
        "Mystara",
        "Lunaris",
        "Sunshroud",
        "Dreadmere",
        "Blazefall",
        "Moonshroud",
        "Starlight",
        "Blackthorn",
        "Windwhisper",
        "Darkwater",
        "Celestria",
        "Stonehaven",
        "Bloodfang",
        "Frostspire",
        "Sablewood",
        "Terrafirma",
        "Avalon",
        "Oceanius",
        "Borealia",
        "Zephyrus",
        "Hyperion",
        "Solara",
        "Astralis",
        "Cosmara",
        "Vortexia",
        "Equinoxia",
        "Arcadia",
        "Celestria",
        "Euphoria",
        "Meridianis",
        "Zenithica",
        "Calypso",
        "Neptunia",
        "Aetheris",
        "Luminosa",
        "Terra Nova",
        "Ampliterra",
        "Equatoria",
        "Chronosia",
        "Titanica",
        "Pyroterra",
        "Seraphis",
        "Avalora",
        "Zenterra",
        "Mercuria",
        "Chronotopia",
        "Aquaterra",
        "Arcturia",
        "Terraforma",
        "Chromatis",
        "Venturia",
        "Elysium",
        "Terra",
        "Aurora",
        "Hydrosphere",
        "Viridiana",
        "Cybertopia",
        "Azuria",
        "Aetherea",
        "Volcania",
        "Zephyrion",
        "Omegara",
        "Atlantis",
        "Lunaris",
        "Solstice",
        "Nova",
        "Avalore",
        "Terravita",
        "Ventara",
        "Azimuth",
        "Amplitude",
        "Mysterra",
        "Apollonia",
        "Echoterra",
        "Pyrosphere",
        "Serendipia",
        "Astraluna",
        "Zenara",
        "Terranautica",
        "Aqualis",
        "Arcanum",
        "Solora",
        "Ultrapolis",
        "Caelum",
        "Hyperia",
        "Mythosia",
        "Zephyria",
        "Novaris",
        "Solara",
        "Equinoxia",
        "Terrafina",
        "Luminara",
        "Zenithos",
        "Azuris",
        "Elysia",
        "Europa"
    ]
    transition_matrix = build_transition_matrix(training_data)

    # Example usage:
    randomSeedArray = ["A","B","C","D","E","F","G","H","I","L","M","N","O","P","S","T","U","V","W","Z"]
    seed = random.choice(randomSeedArray)
    return generate_name_struct(seed, transition_matrix)
