from AdventureManagement.Adventure import Adventure
from AdventureManagement.Scene import Scene
import pytest


def test_adventure_can_add_scene():
    adventure = Adventure("The Forgotten Forest", "A mysterious forest.")

    entrance = Scene("Forest Entrance", "The edge of a dark forest.")

    adventure.add_scene(entrance)

    assert len(adventure.get_scenes()) == 1
    assert adventure.get_scenes()[0] == entrance


def test_scenes_can_connect():
    entrance = Scene("Forest Entrance", "The forest entrance.")
    clearing = Scene("Forest Clearing", "An open clearing.")

    entrance.add_connection(clearing)

    assert clearing in entrance.connections

def test_adventure_sets_starting_scene():
    adventure = Adventure("Test Adventure", "A test.")

    scene = Scene("Entrance", "The entrance.")

    adventure.add_scene(scene)
    adventure.set_starting_scene(scene)

    assert adventure.starting_scene == scene

def test_adventure_rejects_scene_not_in_adventure():
    adventure = Adventure("Test Adventure", "A test.")

    scene = Scene("Entrance", "The entrance.")

    with pytest.raises(ValueError):
        adventure.set_starting_scene(scene)