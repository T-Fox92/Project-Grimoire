import pytest

from AdventureManagement.ExplorationManager import ExplorationManager
from AdventureManagement.CombatManager import CombatManager
from AdventureManagement.Scene import Scene
from AdventureManagement.Enemy import Enemy
from CharacterManagement.Character import Character
from CharacterManagement.JobDefinitions import FIGHTER
from CharacterManagement.ProgressionManager import ProgressionManager
from AdventureManagement.EnemyDefinitions import create_feral_rat
from AdventureManagement.Adventure import Adventure


def test_display_scene(capsys):
    manager = ExplorationManager(None)

    entrance = Scene("Dungeon Entrance", "A dark entrance.")
    corridor = Scene("Dark Corridor", "A narrow stone corridor.")

    entrance.add_connection(corridor)
    entrance.add_enemy(create_feral_rat())

    manager.display_scene(entrance)

    output = capsys.readouterr().out

    assert "Dungeon Entrance" in output
    assert "A dark entrance." in output
    assert "Rat" in output
    assert "Dark Corridor" in output


def test_move_to_connected_scene():
    manager = ExplorationManager()

    entrance = Scene("Entrance", "A dungeon entrance.")
    corridor = Scene("Corridor", "A dark corridor.")

    entrance.add_connection(corridor)

    result = manager.move_to_scene(entrance, 1)

    assert result == corridor


def test_move_to_invalid_scene():
    manager = ExplorationManager()

    entrance = Scene("Entrance", "A dungeon entrance.")

    with pytest.raises(ValueError):
        manager.move_to_scene(entrance, 1)

def test_victory_removes_enemy_from_scene(monkeypatch):
    monkeypatch.setattr ("builtins.input", lambda _: "1")
    character = Character("Test Hero", FIGHTER)

    progression_manager = ProgressionManager()
    combat_manager = CombatManager(progression_manager)
    exploration_manager = ExplorationManager(combat_manager)

    scene = Scene("Dungeon", "A dark dungeon.")

    enemy = Enemy(
        "Rat",
        "A common dungeon pest.",
        1,
        9,
        9,
        2,
        15
    )

    scene.add_enemy(enemy)

    result = exploration_manager.enter_scene(character, scene)

    assert result is True
    assert enemy not in scene.enemies
    assert len(scene.enemies) == 0

def test_defeat_stops_exploration(monkeypatch):
    monkeypatch.setattr ("builtins.input", lambda _: "1")
    character = Character("Test Hero", FIGHTER)
    character.currentHealth = 1

    progression_manager = ProgressionManager()
    combat_manager = CombatManager(progression_manager)
    exploration_manager = ExplorationManager(combat_manager)

    scene = Scene("Dungeon", "A dark dungeon.")

    enemy = Enemy(
        "Rat",
        "A common dungeon pest.",
        1,
        50,
        50,
        2,
        15
    )

    scene.add_enemy(enemy)

    result = exploration_manager.enter_scene(character, scene)

    assert result is False
    assert enemy in scene.enemies
    assert character.experience == 0

def test_enter_cleared_scene():
    character = Character("Test Hero", FIGHTER)

    progression_manager = ProgressionManager()
    combat_manager = CombatManager(progression_manager)
    exploration_manager = ExplorationManager(combat_manager)

    scene = Scene("Dungeon", "A cleared dungeon.")

    result = exploration_manager.enter_scene(character, scene)

    assert result is True
    assert len(scene.enemies) == 0
    assert character.experience == 0

def test_player_can_leave_adventure(monkeypatch, capsys):
    progression_manager = ProgressionManager()
    combat_manager = CombatManager(progression_manager)
    manager = ExplorationManager(combat_manager)

    character = Character("Test Hero", FIGHTER)
    adventure = Adventure("Test Adventure", "A test adventure.")

    entrance = Scene("Entrance", "The dungeon entrance.")
    corridor = Scene("Corridor", "A dark corridor.")

    adventure.add_scene(entrance)
    adventure.add_scene(corridor)
    entrance.add_connection(corridor)
    adventure.set_starting_scene(entrance)

    monkeypatch.setattr("builtins.input", lambda _: "0")

    manager.start_exploration(character, adventure)

    output = capsys.readouterr().out

    assert "Entrance" in output
    assert "You have left the adventure." in output

def test_player_can_move_between_scenes(monkeypatch, capsys):
    progression_manager = ProgressionManager()
    combat_manager = CombatManager(progression_manager)
    manager = ExplorationManager(combat_manager)

    character = Character("Test Hero", FIGHTER)
    adventure = Adventure("Test Adventure", "A test adventure.")

    entrance = Scene("Entrance", "The dungeon entrance.")
    corridor = Scene("Corridor", "A dark corridor.")

    adventure.add_scene(entrance)
    adventure.add_scene(corridor)
    entrance.add_connection(corridor)
    adventure.set_starting_scene(entrance)

    
    choices = iter(["1", "0"])

    def mock_input(prompt):
        choice = next(choices)
        print(f"TEST INPUT: {choice}")
        return choice

    monkeypatch.setattr("builtins.input", mock_input)

def test_player_cannot_continue_after_defeat(monkeypatch, capsys):
    monkeypatch.setattr ("builtins.input", lambda _: "1")
    progression_manager = ProgressionManager()
    combat_manager = CombatManager(progression_manager)
    manager = ExplorationManager(combat_manager)

    character = Character("Test Hero", FIGHTER)
    character.currentHealth = 1

    adventure = Adventure("Test Adventure", "A test adventure.")

    entrance = Scene("Entrance", "The dungeon entrance.")
    corridor = Scene("Corridor", "A dark corridor.")

    adventure.add_scene(entrance)
    adventure.add_scene(corridor)
    entrance.add_connection(corridor)
    adventure.set_starting_scene(entrance)

    enemy = Enemy("Rat", "A common dungeon pest.", 1, 50, 50, 2, 15)
    entrance.add_enemy(enemy)

    manager.start_exploration(character, adventure)

    output = capsys.readouterr().out

    assert "Your adventure has ended." in output
    assert "A dark corridor." not in output
    assert character.experience == 0