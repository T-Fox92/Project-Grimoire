from AdventureManagement.CombatManager import CombatManager


class ExplorationManager:

    def __init__ (self, combat_manager = None):
        self.combat_manager = combat_manager

    def display_scene (self, scene):
        print (f"\n=== {scene.name} ===")
        print (scene.description)

        if scene.enemies:
            print ("\nEnemies present:")
            for enemey in scene.enemies:
                print(f"- {enemey.name}")

        if scene.connections:
            print ("\nAvailable paths:")
            for index, connection in enumerate (scene.connections, start = 1):
                print (f"{index}. {connection.name}")

        else:
            print ("\nThere are no available paths.")

    def move_to_scene (self, current_scene, choice):
        if choice < 1 or choice > len (current_scene.connections):
            raise ValueError ("Invalid scene selection.")

        return current_scene.connections [choice - 1]

    def enter_scene (self, character, scene):
        for enemy in scene.enemies[:]:
            result = self.combat_manager.start_combat (character, enemy)

            if result == "victory":
                scene.enemies.remove (enemy)

            elif result == "defeat":
                return False

        return True

    def start_exploration (self, character, adventure):

        current_scene = adventure.starting_scene
        exploring = True

        while exploring:

            # Display the current scene
            self.display_scene (current_scene)

            # Enemies in the scene
            survived = self.enter_scene (character, current_scene)

            if not survived:
                print ("\nYour adventure has ended.")
                exploring = False

            else:
                if current_scene.connections:
                    print ("\nChoose a path, or enter 0 to leave the adventure.")

                    choice = input ("Selection: ")

                    if choice == "0":
                        exploring = False

                    elif choice.isdigit():
                        try:
                            current_scene = self.move_to_scene (
                                current_scene, int (choice)
                            )

                        except ValueError:
                            print ("Invalid selection.")

                    else:
                        print ("\nThere are no paths forward.")
                        exploring = False

                print ("\nYou have left the adventure.")