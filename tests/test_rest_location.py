
from CharacterManagement.Character import Character
from AdventureManagement.RestLocation import RestLocation


class TestJob:
    name = "Test Job"

    def get_starting_abilities(self):
        return []


def test_rest_location_restores_health():
    character = Character("Aria", TestJob())
    campsite = RestLocation("Forest Campsite")

    character.take_damage(40)
    campsite.rest(character)

    assert character.currentHealth == 100


def test_rest_location_does_not_change_experience():
    character = Character("Aria", TestJob())
    campsite = RestLocation("Forest Campsite")

    character.experience = 150
    campsite.rest(character)

    assert character.experience == 150
    assert character.level == 1


def test_rest_location_has_name():
    campsite = RestLocation("Forest Campsite")

    assert campsite.name == "Forest Campsite"
