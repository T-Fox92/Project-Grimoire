from CharacterManagement.Character import Character


class TestJob:
    name = "Test Job"

    def get_starting_abilities(self):
        return []


def test_default_experience():
    character = Character("Test", TestJob())

    assert character.experience == 0


def test_experience_can_be_updated():
    character = Character("Test", TestJob())

    character.experience += 10

    assert character.experience == 10