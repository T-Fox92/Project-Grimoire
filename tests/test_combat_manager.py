
import pytest

from AdventureManagement.CombatManager import CombatManager
from AdventureManagement.Enemy import Enemy
from CharacterManagement.Character import Character
from CharacterManagement.JobDefinitions import FIGHTER
from CharacterManagement.ProgressionManager import ProgressionManager


def test_player_wins_combat_and_receives_experience():
    character = Character("Test Hero", FIGHTER)
    progression_manager = ProgressionManager()
    combat_manager = CombatManager(progression_manager)

    # Fixed 9 health so the character can defeat the enemy in one hit
    enemy = Enemy(
        "Rat",
        "A common dungeon pest.",
        1,
        9,
        9,
        2,
        15
    )

    result = combat_manager.start_combat(character, enemy)

    assert result == "victory"
    assert enemy.currentHealth == 0
    assert character.experience == 15


def test_player_loses_combat_and_receives_no_experience():
    character = Character("Test Hero", FIGHTER)
    character.currentHealth = 1

    progression_manager = ProgressionManager()
    combat_manager = CombatManager(progression_manager)

    # Rat deals 2 damage, enough to defeat the character
    enemy = Enemy(
        "Rat",
        "A common dungeon pest.",
        1,
        50,
        50,
        2,
        15
    )

    result = combat_manager.start_combat(character, enemy)

    assert result == "defeat"
    assert character.currentHealth == 0
    assert character.experience == 0
