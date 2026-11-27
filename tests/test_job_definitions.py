from CharacterManagement.JobDefinitions import (
    FIGHTER,
    CLERIC,
    ELEMENTALIST
)
from CharacterManagement.Character import Character
from CharacterManagement.ProgressionManager import ProgressionManager


def test_jobs_have_correct_starting_abilities():
    fighter = Character("Fighter Test", FIGHTER)
    cleric = Character("Cleric Test", CLERIC)
    elementalist = Character("Elementalist Test", ELEMENTALIST)

    assert [ability.name for ability in fighter.get_learned_abilities()] == ["Charge"]
    assert [ability.name for ability in cleric.get_learned_abilities()] == ["Healing Light"]
    assert [ability.name for ability in elementalist.get_learned_abilities()] == ["Tri-Disaster"]

    from CharacterManagement.ProgressionManager import ProgressionManager


def test_jobs_have_three_level_two_active_choices():
    progression = ProgressionManager()

    fighter = Character("Fighter Test", FIGHTER)
    cleric = Character("Cleric Test", CLERIC)
    elementalist = Character("Elementalist Test", ELEMENTALIST)

    fighter.level = 2
    cleric.level = 2
    elementalist.level = 2

    assert {ability.name for ability in progression.get_ability_choices(fighter)} == {
        "Magic Weapon", "Double Slash", "Power Slash"
    }

    assert {ability.name for ability in progression.get_ability_choices(cleric)} == {
        "Holy Nova", "Holy Strike", "Challenge"
    }

    assert {ability.name for ability in progression.get_ability_choices(elementalist)} == {
        "Flame Burst", "Frostbolt", "Lightning Bolt"
    }

def test_jobs_have_correct_level_three_passives():
    progression = ProgressionManager()

    fighter = Character("Fighter Test", FIGHTER)
    cleric = Character("Cleric Test", CLERIC)
    elementalist = Character("Elementalist Test", ELEMENTALIST)

    fighter.level = 3
    cleric.level = 3
    elementalist.level = 3

    fighter_passives = progression.get_ability_choices(fighter)
    cleric_passives = progression.get_ability_choices(cleric)
    elementalist_passives = progression.get_ability_choices(elementalist)

    assert len(fighter_passives) == 6
    assert len(cleric_passives) == 6
    assert len(elementalist_passives) == 6

    assert all(ability.abilityType == "Passive" for ability in fighter_passives)
    assert all(ability.abilityType == "Passive" for ability in cleric_passives)
    assert all(ability.abilityType == "Passive" for ability in elementalist_passives)

def test_learning_passives_records_specialization_affinity():
    progression = ProgressionManager()

    fighter = Character("Fighter Test", FIGHTER)
    cleric = Character("Cleric Test", CLERIC)
    elementalist = Character("Elementalist Test", ELEMENTALIST)

    fighter.level = 3
    cleric.level = 3
    elementalist.level = 3

    fighter_ability = next(
        ability for ability in progression.get_ability_choices(fighter)
        if ability.name == "Brutal Force"
    )

    cleric_ability = next(
        ability for ability in progression.get_ability_choices(cleric)
        if ability.name == "Divine Favor"
    )

    elementalist_ability = next(
        ability for ability in progression.get_ability_choices(elementalist)
        if ability.name == "Pyromancy"
    )

    assert progression.select_ability(fighter, fighter_ability)
    assert progression.select_ability(cleric, cleric_ability)
    assert progression.select_ability(elementalist, elementalist_ability)

    assert fighter_ability in fighter.get_learned_abilities()
    assert cleric_ability in cleric.get_learned_abilities()
    assert elementalist_ability in elementalist.get_learned_abilities()

    assert "Heavy" in fighter.specializationAffinities
    assert "Holy" in cleric.specializationAffinities
    assert "Fire" in elementalist.specializationAffinities

def test_cannot_learn_unavailable_ability():
    progression = ProgressionManager()
    fighter = Character("Fighter Test", FIGHTER)
    cleric = Character("Cleric Test", CLERIC)

    fighter.level = 2

    # Healing Light belongs to the Cleric, not the Fighter.
    unavailable_ability = CLERIC.startingAbilities[0]

    assert progression.select_ability(fighter, unavailable_ability) is False
    assert unavailable_ability not in fighter.get_learned_abilities()

def test_cannot_learn_same_ability_twice():
    progression = ProgressionManager()
    fighter = Character("Fighter Test", FIGHTER)

    fighter.level = 2

    charge = FIGHTER.startingAbilities[0]

    assert charge in fighter.get_learned_abilities()

    # Charge is already learned and isn't a level 2 choice.
    assert progression.select_ability(fighter, charge) is False

    assert fighter.get_learned_abilities().count(charge) == 1