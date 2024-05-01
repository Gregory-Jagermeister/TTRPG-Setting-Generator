import random
import Levenshtein

class Categorical(object):
    def __init__(self, support, prior):
        self.counts = {x: prior for x in support}
        self.total = sum(self.counts.values())

    def observe(self, event, count=1):
        self.counts[event] += count
        self.total += count

    def sample(self, dice=random):
        sample = dice.uniform(0, self.total)
        for event, count in self.counts.items():
            if sample <= count:
                return event
            sample -= count

    def __getitem__(self, event):
        return self.counts[event] / self.total

class MarkovNameGenerator(object):
    def __init__(self, training_data, order=2, prior=0.001):
        self.support = set()
        for name in training_data:
            self.support.update(name)

        self.model = MarkovModel(self.support, order, prior)

        for name in training_data:
            self.model.observe(name)

    def generate(self):
        return ''.join(self.model.generate())

class MarkovModel(object):
    def __init__(self, support, order, prior, boundary_symbol=None):
        self.support = set(support)
        self.support.add(boundary_symbol)
        self.order = order
        self.prior = prior
        self.boundary = boundary_symbol
        self.prefix = [self.boundary] * self.order
        self.postfix = [self.boundary]
        self.counts = {}

    def _categorical(self, context):
        if context not in self.counts:
            self.counts[context] = Categorical(self.support, self.prior)
        return self.counts[context]

    def _backoff(self, context):
        context = tuple(context)
        if len(context) > self.order:
            context = context[-self.order:]
        elif len(context) < self.order:
            context = (self.boundary,) * (self.order - len(context)) + context

        while context not in self.counts and len(context) > 0:
            context = context[1:]
        return context

    def observe(self, sequence, count=1):
        sequence = self.prefix + list(sequence) + self.postfix
        for i in range(self.order, len(sequence)):
            context = tuple(sequence[i - self.order:i])
            event = sequence[i]
            for j in range(len(context) + 1):
                self._categorical(context[j:]).observe(event, count)

    def sample(self, context):
        context = self._backoff(context)
        return self._categorical(context).sample()

    def generate(self):
        sequence = [self.sample(self.prefix)]
        while sequence[-1] != self.boundary:
            sequence.append(self.sample(sequence))
        return sequence[:-1]

    def __getitem__(self, condition):
        event = condition.start
        context = self._backoff(condition.stop)
        return self._categorical(context)[event]

# Example Usage:
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
    "Terrafirma"
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
generator = MarkovNameGenerator(training_data=training_data)

# Generate a name
generated_name = generator.generate()
print(f"Generated Name: {generated_name}")
