
class CampsiteMenu:

    def display(self, rest_location, character, progression_manager):

        while True:
            print("\n================================")
            print(f"       {rest_location.name.upper()}")
            print("================================")
            print("1. Rest")
            print("2. Leave campsite")

            choice = input("\nChoose an option: ").strip()

            if choice == "1":
                self.rest(
                    rest_location,
                    character,
                    progression_manager
                )

            elif choice == "2":
                print("You leave the campsite.")
                break

            else:
                print("Invalid selection. Try again.")

    def rest(self, rest_location, character, progression_manager):

        rest_location.rest(character)

        if not progression_manager.can_level_up(character):
            print("You do not have enough experience to level up.")
            return

        print("\nYou have enough experience to advance!")

        choices = progression_manager.level_up(
            character,
            self.select_attributes(character)
            if character.level + 1 == 4 else None
        )

        if choices is False:
            print("Unable to advance your character.")
            return

        print(f"\nCongratulations! You reached level {character.level}!")

        if choices:
            print("\nAvailable abilities:")
            for index, ability in enumerate(choices, start=1):
                print(f"{index}. {ability.name}")

    def select_attributes(self, character):

        print("\nChoose three attributes to improve:")

        attributes = list(character.attributes.keys())

        for index, attribute in enumerate(attributes, start=1):
            print(f"{index}. {attribute}")

        selected_attributes = []

        while len(selected_attributes) < 3:
            choice = input(
                f"Select attribute {len(selected_attributes) + 1}/3: "
            ).strip()

            if not choice.isdigit():
                print("Please enter a number.")
                continue

            index = int(choice) - 1

            if index < 0 or index >= len(attributes):
                print("Invalid selection.")
                continue

            selected = attributes[index]

            if selected in selected_attributes:
                print("You already selected that attribute.")
                continue

            selected_attributes.append(selected)

        return selected_attributes
