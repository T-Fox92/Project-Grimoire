from CharacterManagement.RaceDefinitions import PLAYABLE_RACES
from CharacterManagement.JobDefinitions import PLAYABLE_JOBS
from CharacterManagement.Race import Race
from CharacterManagement.CharacterCreationManager import CharacterCreationManager


class CharacterCreationMenu:
    def __init__ (self):
        self.creation_manager = CharacterCreationManager()


    def create_character (self):

        print("\n================================")
        print("       CHARACTER CREATION")
        print("================================")

        # Collect character name
        valid_name = False

        while not valid_name:
            name = input ("\nEnter your character's name: ").strip()

            if name:
                valid_name = True

            print ("Character name cannot be empty.")

        # Select race and job
        race = self.select_race()
        job = self.select_job()

        # Collect racial penalty decisions
        if race.isHuman:
            human_penalty, skip_penalty, skipped_bonus = self.select_human_penalty()
        else:
            human_penalty, skip_penalty, skipped_bonus = self.select_racial_penalty_option(race)


        # Distribute three attribute points
        selected_attributes = self.select_attributes (race, job)

        # Create the character using CharacterCreationManager
        character = self.creation_manager.create_character (
            name = name,
            race = race,
            job = job,
            selected_attributes = selected_attributes,
            human_penalty = human_penalty,
            skip_racial_penalty = skip_penalty,
            skipped_bonus = skipped_bonus
        )

        # Display the completed character
        self.display_character_summary (character)

        return character

    def display_character_summary (self, character):

        print("\n================================")
        print("       CHARACTER CREATED")
        print("================================")

        print(f"\nName: {character.name}")
        print(f"Race: {character.race.name}")
        print(f"Job: {character.job.name}")
        print(f"Level: {character.level}")
        print(f"Health: {character.currentHealth}/{character.maxHealth}")

        print("\nAttributes:")

        for attribute, value in character.attributes.items():
            print(f"  {attribute}: {value}")

        print("\nStarting Abilities:")

        for ability in character.get_learned_abilities():
            print(f"  {ability.name} - {ability.description}")

        print("\n================================")

    def display_races (self):
        print ("\n=== Choose Your Race ===")

        for index, race in enumerate (PLAYABLE_RACES, start = 1):
            print (f"\n{index}. {race.name}")
            print (f"   {race.description}")

            # Display racial attribute bonuses
            bonuses = race.get_attribute_bonuses ()


            if race.isHuman:
                print ("    Bonuses: +1 to all attributes")
                print ("    Penalty: -2 to one chosen attribute")

            else:
                bonus_text = ", ".join(
                    f"+{amount} {attribute}"
                    for attribute, amount in bonuses.items()
                )

                print (f"   Bonuses: {bonus_text}")
                print (f"   Penalty: -1 {race.get_attribute_penalty()}")


    def select_race (self):

        valid_selection = False
        
        while not valid_selection:
            self.display_races ()

            try:
                selection = int (input("\nChoose your race: "))

                if 1 <= selection <= len (PLAYABLE_RACES):
                    return PLAYABLE_RACES [selection - 1]

                print ("Invalid selection. Please choose a listed race.")

            except ValueError:
                print ("Please enter a number.")

    def display_jobs (self):
        print ("\n=== Choose Your Job ===")

        for index, job in enumerate (PLAYABLE_JOBS, start = 1):
            print (f"\n{index}. {job.name}")
            print (f"   {job.description}")
            print (f"   Core Attribute: {job.get_core_attribute()}")

    def select_job (self):

        valid_selection = False
        
        while not valid_selection:
            self.display_jobs()

            try: 
                selection = int (input ("\nChoose your job: "))

                if 1 <= selection <= len (PLAYABLE_JOBS):
                    return PLAYABLE_JOBS [selection - 1]

                print ("Invalid selection. Please choose a listed job.")

            except ValueError:
                print ("Please enter a number.")

    def select_human_penalty(self):
        print("\n=== Choose Your Attribute Penalty ===")
        print("Humans receive +1 to every attribute, but must choose one attribute to receive -2.")

        for index, attribute in enumerate(Race.VALID_ATTRIBUTES, start=1):
            print(f"{index}. {attribute}")

        valid_selection = False

        while not valid_selection:
            try:
                selection = int(input("\nChoose an attribute to penalize: "))

                if 1 <= selection <= len(Race.VALID_ATTRIBUTES):
                    selected_attribute = Race.VALID_ATTRIBUTES[selection - 1]

                    return selected_attribute, False, None

                print("Invalid selection. Please choose a listed attribute.")

            except ValueError:
                print("Please enter a number.")

    def select_racial_penalty_option(self, race):
        print("\n=== Racial Penalty ===")
        print(f"Your race normally receives a -1 penalty to {race.get_attribute_penalty()}.")

        print("\nChoose an option:")
        print("1. Accept the -1 racial penalty")
        print("2. Ignore the penalty by giving up one +2 racial bonus")

        valid_selection = False
        
        while not valid_selection:
            try:
                selection = int(input("\nYour choice: "))

                if selection == 1:
                    return None, False, None

                elif selection == 2:
                    bonuses = list(race.get_attribute_bonuses().keys())

                    print("\nChoose which racial bonus to give up:")

                    for index, attribute in enumerate(bonuses, start=1):
                        print(f"{index}. {attribute} (+2)")

                    second_validation = False

                    while not second_validation:
                        try:
                            bonus_selection = int(input("\nChoose a bonus: "))

                            if 1 <= bonus_selection <= len(bonuses):
                                selected_bonus = bonuses[bonus_selection - 1]

                                return None, True, selected_bonus

                            print("Invalid selection. Please choose a listed bonus.")

                        except ValueError:
                            print("Please enter a number.")

                else:
                    print("Invalid selection. Please choose 1 or 2.")

            except ValueError:
                print("Please enter a number.")

    def select_attributes(self, race, job):
        attributes = Race.VALID_ATTRIBUTES
        selected_attributes = []

        print("\n=== Distribute Attribute Points ===")
        print("Choose three different attributes to increase by +1.")
        print(f"Your job's core attribute is {job.get_core_attribute()}.")

        print("\nYour race's bonuses:")
        for attribute, bonus in race.get_attribute_bonuses().items():
            print(f"  {attribute}: +{bonus}")

        while len(selected_attributes) < 3:
            print("\nAvailable attributes:")

            for index, attribute in enumerate(attributes, start=1):
                if attribute in selected_attributes:
                    print(f"{index}. {attribute} (Already selected)")
                else:
                    print(f"{index}. {attribute}")

            try:
                selection = int(input(
                    f"\nSelect attribute {len(selected_attributes) + 1} of 3: "
                ))

                if not 1 <= selection <= len(attributes):
                    print("Invalid selection. Please choose a listed attribute.")
                    continue

                selected_attribute = attributes[selection - 1]

                if selected_attribute in selected_attributes:
                    print("You have already selected that attribute.")
                    continue

                selected_attributes.append(selected_attribute)
                print(f"{selected_attribute} selected!")

            except ValueError:
                print("Please enter a number.")

        return selected_attributes
