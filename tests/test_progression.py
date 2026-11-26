
from CharacterManagement.Ability import Ability
from CharacterManagement.Specialization import Specialization
from CharacterManagement.Job import Job
from CharacterManagement.Character import Character
from CharacterManagement.ProgressionManager import ProgressionManager

# Create abilities
charge = Ability(
    "Charge", "Rush toward an enemy and strike.",
    "Active", 1
)

magic_weapon = Ability(
    "Magic Weapon", "Imbue your weapon with magical energy.",
    "Active", 2, "Spellsword"
)

double_slash = Ability(
    "Double Slash", "Strike twice in rapid succession.",
    "Active", 2, "Agile"
)

power_slash = Ability(
    "Power Slash", "Deliver a powerful weapon strike.",
    "Active", 2, "Heavy"
)

iron_will = Ability(
    "Iron Will", "Increase resistance to incoming damage.",
    "Passive", 3
)

arcane_resistance = Ability(
    "Arcane Resistance", "Improve resistance to magical damage.",
    "Passive", 3, "Spellsword"
)

# Create specializations
spellsword = Specialization(
    "Spellsword", "Combines physical combat with magic.",
    [magic_weapon, arcane_resistance]
)

agile = Specialization(
    "Agile", "Focuses on speed and mobility.",
    [double_slash]
)

heavy = Specialization(
    "Heavy", "Focuses on powerful attacks and defense.",
    [power_slash]
)

# Create Job
fighter = Job(
    "Fighter",
    "A versatile physical combatant.",
    startingAbilities=[charge],
    availableAbilities=[iron_will],
    specializations=[spellsword, agile, heavy]
)

# Create Character
character = Character(
    "Aria",
    fighter,
    {"Strength": 10, "Agility": 8, "Intelligence": 6}
)

# Create progression manager
progression = ProgressionManager()

print("Character:", character.name)
print("Starting level:", character.level)

# Level 2
print("\n--- Level 2 ---")

choices = progression.level_up(character)

for index, ability in enumerate(choices, start=1):
    print(f"{index}. {ability.name}")

# Select Magic Weapon
print("\nSelecting Magic Weapon:")
print(progression.select_ability(character, magic_weapon))

print("\nLearned abilities:")
for ability in character.get_learned_abilities():
    print("-", ability.name)

# Level 3
print("\n--- Level 3 ---")

choices = progression.level_up(character)

for index, ability in enumerate(choices, start=1):
    print(f"{index}. {ability.name}")

# Select Arcane Resistance
print("\nSelecting Arcane Resistance:")
print(progression.select_ability(character, arcane_resistance))

print("\nFinal character details:")
print(character.get_details())
