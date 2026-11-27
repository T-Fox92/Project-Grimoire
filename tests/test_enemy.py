import pytest

from AdventureManagement.Enemy import Enemy
from CharacterManagement.Character import Character
from CharacterManagement.JobDefinitions import FIGHTER


def test_enemy_initialization():
    enemy = Enemy("Goblin", "A small creature.", 1, 9, 13, 4, 10)

    assert enemy.name == "Goblin"
    assert enemy.level == 1
    assert enemy.minHealth == 9
    assert 9 <= enemy.maxHealth<= 13
    assert enemy.currentHealth == enemy.maxHealth
    assert enemy.attackDamage == 4


def test_enemy_takes_damage():
    enemy = Enemy("Goblin", "A small creature.", 1, 9, 13, 4, 10)

    enemy.take_damage(5)

    assert 4 <= enemy.currentHealth <= 8


def test_enemy_health_cannot_go_below_zero():
    enemy = Enemy("Goblin", "A small creature.", 1, 9, 13, 4, 10)

    enemy.take_damage(30)

    assert enemy.currentHealth == 0
    assert not enemy.is_alive()


def test_enemy_cannot_take_negative_damage():
    enemy = Enemy("Goblin", "A small creature.", 1, 9, 13, 4, 10)

    with pytest.raises(ValueError):
        enemy.take_damage(-5)


def test_enemy_can_attack_character():
    enemy = Enemy("Goblin", "A small creature.", 1, 9, 13, 4, 10)
    character = Character("Test Hero", FIGHTER)

    starting_health = character.currentHealth

    enemy.attack(character)

    assert character.currentHealth == starting_health - 4


def test_dead_enemy_cannot_attack():
    enemy = Enemy("Goblin", "A small creature.", 1, 9, 13, 4, 10)
    character = Character("Test Hero", FIGHTER)

    enemy.take_damage(20)
    starting_health = character.currentHealth

    enemy.attack(character)

    assert character.currentHealth == starting_health


def test_get_enemy_details():
    enemy = Enemy("Goblin", "A small creature.", 1, 9, 13, 4, 10)

    details = enemy.get_details()

    assert "Goblin" in details
    assert f"{enemy.currentHealth}/{enemy.maxHealth}" in details
    assert "Attack Damage: 4" in details

def test_enemy_health_is_within_range():
    enemy = Enemy("Rat", "A dungeon pest.", 1, 9, 13, 2, 15)

    assert 9 <= enemy.currentHealth <= 13


def test_enemy_starts_at_generated_max_health():
    enemy = Enemy("Rat", "A dungeon pest.", 1, 9, 13, 2, 15)

    assert enemy.currentHealth == enemy.maxHealth


def test_enemy_health_range_includes_endpoints():
    # A fixed range should always produce that exact value.
    enemy = Enemy("Rat", "A dungeon pest.", 1, 9, 9, 2, 15)

    assert enemy.currentHealth == 9
    assert enemy.maxHealth == 9


def test_enemy_rejects_invalid_health_range():
    with pytest.raises(ValueError):
        Enemy("Rat", "A dungeon pest.", 1, 13, 9, 2, 15)