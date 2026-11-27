from UserInterface.AdventureCreationForm import AdventureCreationForm
from UserInterface.CharacterCreationMenu import CharacterCreationMenu
from SubmissionValidation.AdventureValidator import AdventureValidator
from AdventureManagement.Adventure import Adventure
from AdventureManagement.Scene import Scene
from AdventureManagement.EnemyDefinitions import create_feral_rat
from AdventureManagement.CombatManager import CombatManager
from AdventureManagement.ExplorationManager import ExplorationManager
from CharacterManagement.ProgressionManager import ProgressionManager


class MainMenu:

    def __init__ (self):
        self.current_character = None

    def display (self):
        running = True

        while running:
            print("\n================================")
            print("       PROJECT GRIMOIRE")
            print("================================")
            print("1. Create Character")
            print("2. Load Character")
            print("3. Create Adventure")
            print("4. Exit")
            print("================================")

            choice = input ("Select an option: ")

            if choice == "1":
                self.create_character()

            elif choice == "2":
                print ("\nLoading characters is not yet implemented.")

            elif choice == "3":
                self.create_adventure ()

            elif choice == "4":
                print ("Thank you for playing Project Grimoire!")
                running = False

            else:
                print ("\nInvalid selection. Please choose 1, 2, 3 or 4.")

    def create_character (self):
        menu = CharacterCreationMenu()
        self.current_character = menu.create_character()

        if self.current_character is not None:
            self.play_tutorial()

    def create_adventure (self):
        form = AdventureCreationForm()
        validator = AdventureValidator()

        adventure_created = False

        while not adventure_created:
            adventure_data = form.display ()

            errors = validator.validate_adventure (adventure_data)

            if errors:
                print ("\nAdventure could not be submitted:")

                for error in errors:
                    print (f"- {error}")

                print ("\nPlease try again.")

            else:
                print ("\nAdventure successfully submitted!")
                print (f"Title: {adventure_data['title']}")
                break

    def play_tutorial(self):

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

        progression_manager = ProgressionManager()
        combat_manager = CombatManager(progression_manager)
        exploration_manager = ExplorationManager(combat_manager)

        exploration_manager.start_exploration(
            self.current_character,
            adventure
        )