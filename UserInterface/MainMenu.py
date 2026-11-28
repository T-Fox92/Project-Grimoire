from UserInterface.AdventureCreationForm import AdventureCreationForm
from UserInterface.CharacterCreationMenu import CharacterCreationMenu
from SubmissionValidation.AdventureValidator import AdventureValidator
from AdventureManagement.CombatManager import CombatManager
from AdventureManagement.ExplorationManager import ExplorationManager
from CharacterManagement.ProgressionManager import ProgressionManager
from AdventureManagement.TutorialAdventure import create_tutorial_adventure
from SaveGameManagement.SaveGameManager import SaveGameManager


class MainMenu:

    def __init__ (self):
        self.current_character = None
        self.current_adventure = None
        self.current_scene = None
        self.save_manager = SaveGameManager ()

    def display (self):
        running = True

        while running:
            print("\n================================")
            print("       PROJECT GRIMOIRE")
            print("================================")
            print("1. Create Character")
            print("2. Load Game")
            print("3. Save Game")
            print("4. Create Adventure")
            print("5. Exit")
            print("================================")

            choice = input ("Select an option: ")

            if choice == "1":
                self.create_character()

            elif choice == "2":
                self.load_game ()

            elif choice == "3":
                self.save_game ()

            elif choice == "4":
                self.create_adventure ()

            elif choice == "5":
                print ("Thank you for playing Project Grimoire!")
                running = False

            else:
                print ("\nInvalid selection. Please choose 1, 2, 3, 4, or 5.")

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


    def save_game(self):

        if (self.current_character is None or
                self.current_adventure is None or
                self.current_scene is None):
            print("\nThere is no active game to save.")
            return

        print("\nAvailable save slots:")

        for slot in self.save_manager.get_available_slots():
            status = "Occupied" if slot["occupied"] else "Empty"
            print(f"{slot['slot']}. {status}")

        try:
            slot = int(input("\nChoose a save slot (1-50): "))

            confirm = False

            if self.save_manager.get_available_slots()[slot - 1]["occupied"]:
                answer = input("Overwrite this save? (y/n): ").lower()

                if answer != "y":
                    print("\nSave cancelled.")
                    return

                confirm = True

            result = self.save_manager.save_game(
                slot,
                self.current_character,
                self.current_adventure,
                self.current_scene,
                confirm_overwrite=confirm
            )

            if result:
                print("\nGame saved successfully!")

        except (ValueError, IndexError):
            print("\nInvalid save slot.")


    def load_game(self):

        print("\nAvailable save slots:")

        slots = self.save_manager.get_available_slots()

        for slot in slots:
            status = "Occupied" if slot["occupied"] else "Empty"
            print(f"{slot['slot']}. {status}")

        try:
            slot = int(input("\nChoose a save slot (1-50): "))

            loaded_game = self.save_manager.load_game(slot)

            if loaded_game is None:
                print("\nThat save slot is empty.")
                return

            self.current_character = loaded_game["character"]
            self.current_adventure = loaded_game["adventure"]
            self.current_scene = loaded_game["current_scene"]

            print(f"\nWelcome back, {self.current_character.name}!")
            print(f"Resuming: {self.current_adventure.title}")

            progression_manager = ProgressionManager()
            combat_manager = CombatManager(progression_manager)
            exploration_manager = ExplorationManager(combat_manager)

            self.current_scene = exploration_manager.start_exploration(
                self.current_character,
                self.current_adventure,
                self.current_scene
            )

        except ValueError as error:
            print(f"\nCould not load game: {error}")


    def play_tutorial (self):

        self.current_adventure = create_tutorial_adventure ()

        progression_manager = ProgressionManager()
        combat_manager = CombatManager (progression_manager)
        exploration_manager = ExplorationManager (combat_manager)

        self.current_scene = exploration_manager.start_exploration (self.current_character, self.current_adventure)