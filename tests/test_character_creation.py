from CharacterManagement.CharacterCreationManager import CharacterCreationManager
from CharacterManagement.RaceDefinitions import ELF
from CharacterManagement.Job import Job


def test_elf_mage_attribute_calculation():
    manager = CharacterCreationManager()
    mage = Job("Mage", "A practitioner of magic.", "Intelligence")

    attributes = manager.calculate_attributes(
        race=ELF,
        job=mage,
        selected_attributes=["Intelligence", "Constitution", "Willpower"],
        skip_racial_penalty=True,
        skipped_bonus="Intelligence"
    )

    assert attributes == {
        "Strength": 3,
        "Agility": 3,
        "Constitution": 4,
        "Intelligence": 6,
        "Willpower": 6
    }

def test_create_character():
    manager = CharacterCreationManager()
    mage = Job("Mage", "A practitioner of magic.", "Intelligence")

    character = manager.create_character(
        name="Test Mage",
        race=ELF,
        job=mage,
        selected_attributes=["Intelligence", "Willpower", "Agility"],
        skip_racial_penalty=True,
        skipped_bonus="Intelligence"
    )

    assert character.name == "Test Mage"
    assert character.race.name == "Elf"
    assert character.job.name == "Mage"
    assert character.attributes["Intelligence"] == 6
    assert character.attributes["Willpower"] == 6