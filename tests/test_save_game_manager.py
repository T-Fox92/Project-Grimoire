import json

from SaveGameManagement.SaveGameManager import SaveGameManager
from CharacterManagement.Character import Character
from CharacterManagement.JobDefinitions import FIGHTER
from CharacterManagement.RaceDefinitions import HUMAN
from AdventureManagement.Adventure import Adventure
from AdventureManagement.Scene import Scene
from AdventureManagement.TutorialAdventure import create_tutorial_adventure

import pytest


@pytest.fixture
def save_manager(tmp_path):
    manager = SaveGameManager()
    manager.save_directory = tmp_path
    return manager


def create_test_game():

    character = Character(
        name="Test",
        job=FIGHTER,
        race=HUMAN
    )

    adventure = create_tutorial_adventure ()

    scene = adventure.starting_scene

    adventure.add_scene(scene)
    adventure.set_starting_scene(scene)

    return character, adventure, scene


def test_character_can_be_reconstructed():

    manager = SaveGameManager()

    original = Character(
        name="Test",
        job=FIGHTER,
        race=HUMAN
    )

    original.level = 2
    original.experience = 125
    original.currentHealth = 75
    original.attributes["Strength"] = 12

    character_data = original.get_details()

    reconstructed = manager.reconstruct_character(character_data)

    assert reconstructed.name == original.name
    assert reconstructed.job.name == original.job.name
    assert reconstructed.race.name == original.race.name
    assert reconstructed.level == original.level
    assert reconstructed.experience == original.experience
    assert reconstructed.currentHealth == original.currentHealth
    assert reconstructed.attributes == original.attributes

    assert [
        ability.name for ability in reconstructed.learnedAbilities
    ] == [
        ability.name for ability in original.learnedAbilities
    ]

def test_character_can_be_serialized():

    manager = SaveGameManager()

    character = Character(
        name="Test",
        job=FIGHTER,
        race=HUMAN
    )

    character.level = 2
    character.experience = 125
    character.currentHealth = 75
    character.attributes["Strength"] = 12

    character_data = manager.serialize_character(character)

    assert character_data["name"] == "Test"
    assert character_data["race"] == "Human"
    assert character_data["job"] == "Fighter"
    assert character_data["level"] == 2
    assert character_data["experience"] == 125
    assert character_data["current_health"] == 75
    assert character_data["attributes"]["Strength"] == 12

    assert "Charge" in character_data["learned_abilities"]

def test_character_serialization_round_trip():

    manager = SaveGameManager()

    original = Character(
        name="Test",
        job=FIGHTER,
        race=HUMAN
    )

    original.level = 2
    original.experience = 125
    original.currentHealth = 75
    original.attributes["Strength"] = 12

    character_data = manager.serialize_character(original)

    reconstructed = manager.reconstruct_character(character_data)

    assert reconstructed.get_details() == original.get_details()


def test_save_game_creates_file(save_manager):

    character, adventure, scene = create_test_game()

    result = save_manager.save_game(
        1, character, adventure, scene
    )

    assert result is True
    assert save_manager.get_save_path(1).is_file()


def test_save_game_refuses_overwrite_without_confirmation(save_manager):

    character, adventure, scene = create_test_game()

    save_manager.save_game(1, character, adventure, scene)

    character.name = "Changed Name"

    result = save_manager.save_game(
        1, character, adventure, scene
    )

    assert result is False


def test_save_game_allows_overwrite_with_confirmation(save_manager):

    character = Character(
        name="Test",
        job=FIGHTER,
        race=HUMAN
    )

    adventure = create_tutorial_adventure()
    scene = adventure.starting_scene

    save_manager.save_game(1, character, adventure, scene)

    character.name = "Changed Name"

    result = save_manager.save_game(
        1,
        character,
        adventure,
        scene,
        confirm_overwrite=True
    )

    assert result is True

    loaded_game = save_manager.load_game(1)

    assert loaded_game["character"].name == "Changed Name"

def test_load_game_restores_character(save_manager):

    character = Character(
        name="Test",
        job=FIGHTER,
        race=HUMAN
    )

    adventure = create_tutorial_adventure()
    scene = adventure.starting_scene

    character.level = 2
    character.experience = 125
    character.currentHealth = 75
    character.attributes["Strength"] = 12

    save_manager.save_game(1, character, adventure, scene)

    loaded_game = save_manager.load_game(1)
    loaded_character = loaded_game["character"]

    assert loaded_character.name == character.name
    assert loaded_character.job.name == character.job.name
    assert loaded_character.race.name == character.race.name
    assert loaded_character.level == character.level
    assert loaded_character.experience == character.experience
    assert loaded_character.currentHealth == character.currentHealth
    assert loaded_character.attributes == character.attributes


def test_load_game_returns_none_for_empty_slot(save_manager):

    result = save_manager.load_game(1)

    assert result is None


def test_load_game_rejects_corrupted_json(save_manager):

    save_path = save_manager.get_save_path(1)
    save_manager.save_directory.mkdir(parents=True, exist_ok=True)

    save_path.write_text(
        "{ invalid json",
        encoding="utf-8"
    )

    with pytest.raises(ValueError, match="corrupted or invalid"):
        save_manager.load_game(1)

def test_get_available_slots_returns_50_slots(save_manager):

    slots = save_manager.get_available_slots()

    assert len(slots) == 50


def test_get_available_slots_identifies_occupied_slots(save_manager):

    character, adventure, scene = create_test_game()

    save_manager.save_game(3, character, adventure, scene)

    slots = save_manager.get_available_slots()

    assert slots[0]["occupied"] is False
    assert slots[2]["occupied"] is True
    assert slots[3]["occupied"] is False


def test_delete_save_requires_confirmation(save_manager):

    character, adventure, scene = create_test_game()

    save_manager.save_game(1, character, adventure, scene)

    result = save_manager.delete_save(1)

    assert result is False
    assert save_manager.get_save_path(1).is_file()


def test_delete_save_with_confirmation(save_manager):

    character, adventure, scene = create_test_game()

    save_manager.save_game(1, character, adventure, scene)

    result = save_manager.delete_save(1, confirm=True)

    assert result is True
    assert not save_manager.get_save_path(1).exists()


def test_delete_save_returns_false_for_empty_slot(save_manager):

    result = save_manager.delete_save(1, confirm=True)

    assert result is False

@pytest.mark.parametrize("slot", [0, 51, -1, "1", 1.5, True])
def test_invalid_save_slots_are_rejected(save_manager, slot):

    with pytest.raises(ValueError):
        save_manager.get_save_path(slot)


def test_tutorial_adventure_can_be_reconstructed(save_manager):

    adventure_data = {
        "title": "Tutorial",
        "current_scene": "Rat's Den"
    }

    adventure, current_scene = save_manager.reconstruct_adventure(
        adventure_data
    )

    assert adventure.title == "Tutorial"
    assert current_scene.name == "Rat's Den"


def test_reconstructed_adventure_has_enemies(save_manager):

    adventure_data = {
        "title": "Tutorial",
        "current_scene": "Rat's Den"
    }

    adventure, current_scene = save_manager.reconstruct_adventure(
        adventure_data
    )

    assert len(current_scene.enemies) == 1
    assert current_scene.enemies[0].name == "Feral Rat"


def test_load_game_restores_adventure_and_scene(save_manager):

    character = Character (name = "Test", job = FIGHTER, race = HUMAN)

    tutorial = create_tutorial_adventure()
    rat_den = next(
        scene for scene in tutorial.get_scenes()
        if scene.name == "Rat's Den"
    )

    save_manager.save_game(
        1,
        character,
        tutorial,
        rat_den
    )

    loaded_game = save_manager.load_game(1)

    assert loaded_game["adventure"].title == "Tutorial"
    assert loaded_game["current_scene"].name == "Rat's Den"
    assert len(loaded_game["current_scene"].enemies) == 1
