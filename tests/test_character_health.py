from CharacterManagement.Character import Character


class TestJob:
    name = "Test Job"

    def get_starting_abilities(self):
        return []


def test_default_health():
    character = Character("Test", TestJob())

    assert character.currentHealth == 100
    assert character.maxHealth == 100


def test_take_damage():
    character = Character("Test", TestJob())

    character.take_damage(25)

    assert character.currentHealth == 75


def test_health_cannot_fall_below_zero():
    character = Character("Test", TestJob())

    character.take_damage(150)

    assert character.currentHealth == 0


def test_restore_health():
    character = Character("Test", TestJob())

    character.take_damage(50)
    character.restore_health(20)

    assert character.currentHealth == 70


def test_health_cannot_exceed_maximum():
    character = Character("Test", TestJob())

    character.restore_health(50)

    assert character.currentHealth == 100


def test_invalid_health_amount():
    character = Character("Test", TestJob())

    assert character.take_damage(-10) is False
    assert character.restore_health(0) is False
    assert character.currentHealth == 100