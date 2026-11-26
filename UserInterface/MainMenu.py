from UserInterface.AdventureCreationForm import AdventureCreationForm
from SubmissionValidation.AdventureValidator import AdventureValidator


class MainMenu:

    def display (self):
        while True:
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
                print ("\nCharacter creation is not yet implemented.")

            elif choice == "2":
                print ("\nLoading characters is not yet implemented.")

            elif choice == "3":
                self.create_adventure ()

            elif choice == "4":
                print ("Thank you for playing Project Grimoire!")
                break

            else:
                print ("\nInvalid selection. Please choose 1, 2, 3 or 4.")

    def create_adventure (self):
        form = AdventureCreationForm()
        validator = AdventureValidator()

        while True:
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