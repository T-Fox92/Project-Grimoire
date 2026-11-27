
from CharacterManagement.Race import Race
from CharacterManagement.RaceDefinitions import PLAYABLE_RACES


def test_playable_race_count():
    assert len(PLAYABLE_RACES) == 7


def test_human_racial_bonuses():
    human = PLAYABLE_RACES[0]

    assert human.isHuman is True
    assert len(human.attributeBonuses) == 5
    assert all(value == 1 for value in human.attributeBonuses.values())
    assert human.attributePenalty is None


def test_elf_racial_modifiers():
    elf = PLAYABLE_RACES[1]

    assert elf.attributeBonuses == {
        "Intelligence": 2,
        "Willpower": 2
    }

    assert elf.attributePenalty == "Constitution"


def test_lizardfolk_racial_modifiers():
    lizardfolk = PLAYABLE_RACES[4]

    assert lizardfolk.attributeBonuses == {
        "Strength": 2,
        "Constitution": 2
    }

    assert lizardfolk.attributePenalty == "Intelligence"


def test_all_races_have_descriptions():
    for race in PLAYABLE_RACES:
        assert race.name
        assert race.description
