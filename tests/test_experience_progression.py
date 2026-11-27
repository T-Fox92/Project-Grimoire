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


def test_default_experience_threshold():
    character = Character("Test", TestJob())
    manager = ProgressionManager()

    assert character.experience == 0
    assert manager.can_level_up(character) is False


def test_experience_award():
    character = Character("Test", TestJob())
    manager = ProgressionManager()

    manager.award_experience(character, 90)

    assert character.experience == 90
    assert manager.can_level_up(character) is False


def test_level_two_eligibility():
    character = Character("Test", TestJob())
    manager = ProgressionManager()

    manager.award_experience(character, 100)

    assert manager.can_level_up(character) is True


def test_experience_is_cumulative():
    character = Character("Test", TestJob())
    manager = ProgressionManager()

    manager.award_experience(character, 110)

    assert character.experience == 110
    assert manager.can_level_up(character) is True


def test_experience_does_not_allow_level_five():
    character = Character("Test", TestJob())
    manager = ProgressionManager()

    character.level = 4
    character.experience = 1000

    assert manager.can_level_up(character) is False