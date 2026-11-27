from CharacterManagement.Character import Character
from CharacterManagement.ProgressionManager import ProgressionManager
from CharacterManagement.CharacterCreationManager import CharacterCreationManager
import pytest
from CharacterManagement.RaceDefinitions import ELF
from CharacterManagement.JobDefinitions import ELEMENTALIST



class TestJob:
    name = "Test Job"

    def get_starting_abilities(self):
        return []

    def get_available_abilities(self):
        return []

    def get_specializations(self):
        return []

def test_default_attributes():
    character = Character("Test", TestJob())

    assert character.attributes == {
        "Strength": 3,
        "Agility": 3,
        "Constitution": 3,
        "Intelligence": 3,
        "Willpower": 3
    }


def test_normal_attribute_increase():
    character = Character("Test", TestJob())

    character.increase_attributes()

    assert all(value == 4 for value in character.attributes.values())


def test_specialization_attribute_increase():
    character = Character("Test", TestJob())

    character.increase_attributes(
        ["Strength", "Agility", "Constitution"]
    )

    assert character.attributes["Strength"] == 6
    assert character.attributes["Agility"] == 6
    assert character.attributes["Constitution"] == 6
    assert character.attributes["Intelligence"] == 4
    assert character.attributes["Willpower"] == 4

def test_character_creation_rejects_duplicate_attributes():
    manager = CharacterCreationManager()

    with pytest.raises(ValueError):
        manager.calculate_attributes(
            ELF,
            ELEMENTALIST,
            ["Strength", "Strength", "Strength"]
        )