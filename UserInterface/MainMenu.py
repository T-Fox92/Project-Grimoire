from UserInterface.AdventureCreationForm import AdventureCreationForm
from UserInterface.CharacterCreationMenu import CharacterCreationMenu
from SubmissionValidation.AdventureValidator import AdventureValidator


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