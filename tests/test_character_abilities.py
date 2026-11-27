
import pytest

from CharacterManagement.Character import Character
from CharacterManagement.JobDefinitions import (
    FIGHTER,
    CLERIC,
    ELEMENTALIST,
    CHARGE,
    HEALING_LIGHT,
    TRI_DISASTER
)
from AdventureManagement.Enemy import Enemy


def test_charge_deals_strength_based_damage():
    character = Character("Test Fighter", FIGHTER)

    enemy = Enemy("Rat", "A dungeon pest.", 1, 100, 100, 2, 15)

    damage = character.use_ability(CHARGE, enemy)

    assert damage > character.calculate_strength_attack_damage()
    assert enemy.currentHealth == 100 - damage


def test_healing_light_restores_health():
    character = Character("Test Cleric", CLERIC)
    character.currentHealth = 50

    healing = character.use_ability(HEALING_LIGHT)

    expected_healing = round(character.maxHealth * 0.33)

    assert healing == expected_healing
    assert character.currentHealth == 50 + expected_healing


def test_healing_light_cannot_exceed_max_health():
    character = Character("Test Cleric", CLERIC)
    character.currentHealth = character.maxHealth - 5

    healing = character.use_ability(HEALING_LIGHT)

    assert healing == 5
    assert character.currentHealth == character.maxHealth


def test_tri_disaster_uses_intelligence():
    character = Character("Test Elementalist", ELEMENTALIST)

    enemy = Enemy("Rat", "A dungeon pest.", 1, 100, 100, 2, 15)

    damage = character.use_ability(TRI_DISASTER, enemy)

    assert enemy.currentHealth == 100 - damage


def test_character_cannot_use_unlearned_ability():
    character = Character("Test Fighter", FIGHTER)

    enemy = Enemy("Rat", "A dungeon pest.", 1, 100, 100, 2, 15)

    result = character.use_ability(TRI_DISASTER, enemy)

    assert result is False


def test_character_cannot_activate_passive_ability():
    character = Character("Test Fighter", FIGHTER)

    enemy = Enemy("Rat", "A dungeon pest.", 1, 100, 100, 2, 15)

    from CharacterManagement.JobDefinitions import BRUTAL_FORCE

    result = character.use_ability(BRUTAL_FORCE, enemy)

    assert result is False
