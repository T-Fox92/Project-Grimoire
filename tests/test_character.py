
from CharacterManagement.Ability import Ability
from CharacterManagement.Specialization import Specialization
from CharacterManagement.Job import Job
from CharacterManagement.Character import Character

# Create abilities
charge = Ability(
    "Charge",
    "Rush toward an enemy and strike.",
    "Active",
    1
)

magic_weapon = Ability(
    "Magic Weapon",
    "Imbue your weapon with magical energy.",
    "Active",
    2,
    "Spellsword"
)

double_slash = Ability(
    "Double Slash",
    "Strike twice in rapid succession.",
    "Active",
    2,
    "Agile"
)

iron_will = Ability(
    "Iron Will",
    "Increase resistance to incoming damage.",
    "Passive",
    3
)

# Create specializations
spellsword = Specialization(
    "Spellsword",
    "Combines physical combat with magic.",
    [magic_weapon]
)

agile = Specialization(
    "Agile",
    "Focuses on speed and mobility.",
    [double_slash]
)

# Create Job
fighter = Job(
    "Fighter",
    "A versatile physical combatant.",
    startingAbilities=[charge],
    specializations=[spellsword, agile]
)

fighter.add_ability(iron_will)

# Create Character
character = Character(
    "Aria",
    fighter,
    {"Strength": 10, "Agility": 8, "Intelligence": 6}
)

# Display character information
print(character.get_details())

# Attempt to learn an ability at level 1
print("Can learn Magic Weapon:", character.can_learn_ability(magic_weapon))

# Advance to level 2 for testing
character.level = 2

# Learn Magic Weapon
print("Learned Magic Weapon:", character.learn_ability(magic_weapon))

# Display updated character information
print(character.get_details())
