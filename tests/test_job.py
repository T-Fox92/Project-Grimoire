
from CharacterManagement.Ability import Ability
from CharacterManagement.Specialization import Specialization
from CharacterManagement.Job import Job


def test_job_core_attribute():
    job = Job("Mage", "A practitioner of magic.", "Intelligence")

    assert job.coreAttribute == "Intelligence"
    assert job.get_core_attribute() == "Intelligence"

# Create abilities
charge = Ability(
    "Charge",
    "Rush toward an enemy and strike.",
    "Active",
    1
)

shield_wall = Ability(
    "Shield Wall",
    "Reduce incoming damage while defending.",
    "Passive",
    3
)

double_slash = Ability(
    "Double Slash",
    "Strike twice in rapid succession.",
    "Active",
    2,
    "Agile"
)

# Create specialization
agile = Specialization(
    "Agile",
    "Focuses on speed, mobility, and multiple attacks.",
    [double_slash]
)

# Create Job
fighter = Job(
    "Fighter",
    "A versatile physical combatant.",
    startingAbilities=[charge],
    availableAbilities=[shield_wall],
    specializations=[agile]
)

# Display Job information
print(fighter.name)
print("Starting abilities:")

for ability in fighter.get_starting_abilities():
    print(f"- {ability.name}")

print("Available abilities:")

for ability in fighter.get_available_abilities():
    print(f"- {ability.name}")

print("Specializations:")

for specialization in fighter.get_specializations():
    print(f"- {specialization.name}")

print("Agile specialization abilities:")

for specialization in fighter.get_specializations():
    for ability in specialization.get_abilities():
        print(f"- {ability.name}")

