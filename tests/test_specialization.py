
from CharacterManagement.Ability import Ability
from CharacterManagement.Specialization import Specialization

double_slash = Ability(
    "Double Slash",
    "Strike twice in rapid succession.",
    "Active",
    2,
    "Agile"
)

evasion = Ability(
    "Evasion",
    "Improve the chance of avoiding incoming attacks.",
    "Passive",
    3,
    "Agile"
)

agile = Specialization(
    "Agile",
    "Focuses on speed, mobility, and multiple attacks."
)

agile.add_ability(double_slash)
agile.add_ability(evasion)

print(agile.name)
print(agile.description)

for ability in agile.get_abilities():
    print(ability.name)
