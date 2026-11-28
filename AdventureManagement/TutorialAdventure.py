from AdventureManagement.Adventure import Adventure
from AdventureManagement.Scene import Scene
from AdventureManagement.EnemyDefinitions import create_feral_rat


def create_tutorial_adventure ():

        adventure = Adventure(
            "Tutorial",
            "Welcome to Project Grimoire!"
        )

        entrance = Scene(
            "Training Grounds",
            "You find yourself in a quiet training area."
        )

        dungeon = Scene(
            "Rat's Den",
            "A dark corner of the training grounds. Something moves in the shadows."
        )

        entrance.add_connection(dungeon)
        dungeon.add_connection(entrance)

        dungeon.add_enemy(create_feral_rat())

        adventure.add_scene(entrance)
        adventure.add_scene(dungeon)

        adventure.set_starting_scene(entrance)

        return adventure