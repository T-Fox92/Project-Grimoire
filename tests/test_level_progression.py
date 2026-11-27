
from CharacterManagement.Character import Character
from CharacterManagement.ProgressionManager import ProgressionManager


class TestJob:
    name = "Test Job"

    def get_starting_abilities(self):
        return []

    def get_available_abilities(self):
        return []

    def get_specializations(self):
        return []


def test_level_up_requires_experience():
    character = Character("Test", TestJob())
    manager = ProgressionManager()

    # Not enough XP for level 2
    manager.award_experience(character, 90)

    assert manager.level_up(character) is False
    assert character.level == 1


def test_level_up_to_level_two():
    character = Character("Test", TestJob())
    manager = ProgressionManager()

    manager.award_experience(character, 100)
    manager.level_up(character)

    assert character.level == 2
    assert character.experience == 100
    assert all(value == 4 for value in character.attributes.values())


def test_level_up_to_level_three():
    character = Character("Test", TestJob())
    manager = ProgressionManager()

    manager.award_experience(character, 250)
    manager.level_up(character)
    manager.level_up(character)

    assert character.level == 3
    assert character.experience == 250
    assert all(value == 5 for value in character.attributes.values())


def test_level_four_requires_three_attributes():
    character = Character("Test", TestJob())
    manager = ProgressionManager()

    manager.award_experience(character, 450)
    manager.level_up(character)
    manager.level_up(character)

    # Missing attribute selection
    assert manager.level_up(character) is False
    assert character.level == 3


def test_level_four_attribute_milestone():
    character = Character("Test", TestJob())
    manager = ProgressionManager()

    manager.award_experience(character, 450)
    manager.level_up(character)
    manager.level_up(character)

    manager.level_up(
        character,
        ["Strength", "Agility", "Constitution"]
    )

    assert character.level == 4
    assert character.attributes["Strength"] == 8
    assert character.attributes["Agility"] == 8
    assert character.attributes["Constitution"] == 8
    assert character.attributes["Intelligence"] == 6
    assert character.attributes["Willpower"] == 6


def test_invalid_attribute_selection_does_not_level_up():
    character = Character("Test", TestJob())
    manager = ProgressionManager()

    manager.award_experience(character, 450)
    manager.level_up(character)
    manager.level_up(character)

    # Duplicate selection
    assert manager.level_up(
        character,
        ["Strength", "Strength", "Agility"]
    ) is False

    assert character.level == 3
    assert all(value == 5 for value in character.attributes.values())


def test_level_four_is_maximum():
    character = Character("Test", TestJob())
    manager = ProgressionManager()

    manager.award_experience(character, 450)
    manager.level_up(character)
    manager.level_up(character)
    manager.level_up(
        character,
        ["Strength", "Agility", "Constitution"]
    )

    assert manager.level_up(character) is False
    assert character.level == 4
