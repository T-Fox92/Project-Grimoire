from CharacterManagement.Race import Race

HUMAN = Race(
    "Human",
    "An Adaptable and versatile race.",
    {
        "Strength": 1,
        "Agility": 1,
        "Constitution": 1,
        "Intelligence": 1,
        "Willpower": 1
    },
    isHuman = True
)

ELF = Race(
    "Elf",
    "A race that is naturally attuned to magic and mental discipline.",
    {"Intelligence": 2, "Willpower": 2},
    "Constitution"
)

DWARF = Race(
    "Dwarf",
    "A race that is know to be hard, strong, and difficult to bring down.",
    {"Constitution": 2, "Strength": 2},
    "Agility"
)

DEMONKIN = Race (
    "Demonkin",
    "A race that is Physically powerful and strong-willed.",
    {"Strength": 2, "Willpower": 2},
    "Intelligence"
)

LIZARDFOLK = Race (
    "Lizardfolk",
    "A race of resilient survivors adapted to harsh environments.",
    {"Strength": 2, "Constitution": 2},
    "Intelligence"
)

FELIDINE = Race (
    "Felidine",
    "an agile, perceptive, and naturally talented race.",
    {"Agility": 2, "Intelligence": 2},
    "Constitution"
)

LUPINE = Race (
    "Lupine",
    "A race of powerful and agile natural hunters.",
    {"Strength": 2, "Agility": 2},
    "Willpower"
)

PLAYABLE_RACES = [
    HUMAN,
    ELF,
    DWARF,
    DEMONKIN,
    LIZARDFOLK,
    FELIDINE,
    LUPINE
]