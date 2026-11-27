class CombatManager:

    def __init__ (self, progression_manager):
        self.progression_manager = progression_manager

    def start_combat (self, character, enemy):

        print (f"\nA {enemy.name} appears!")
        print (enemy.description)

        combat_over = False

        while not combat_over:

            # Player's turn
            self.player_turn (character, enemy)

            # Check if the enemy was defeated
            if not enemy.is_alive():
                print (f"\n{enemy.name} has been defeated!")

                can_level_up = self.progression_manager.award_experience (character, enemy.experienceReward)
                print (f"{character.name} earned {enemy.experienceReward} experience!")

                if can_level_up:
                    print ("You have enough experience to level up!")

                
                combat_over = True
                result = "victory"

            else:
                # Enemy's turn
                print (f"\n{enemy.name} attacks {character.name}!")
                enemy.attack (character)

                print (f"{character.name} has {character.currentHealth}/{character.maxHealth} health remaining.")

                # Check if the player was defeated
                if character.currentHealth <= 0:
                    print (f"\n{character.name} has been defeated!")
                    
                    combat_over = True
                    result = "defeat"

        return result

    def player_turn (self, character, enemy):

        action_complete = False

        while not action_complete:

            print("\n================================")
            print("           YOUR TURN")
            print("================================")
            print("1. Basic Attack")
            print("2. Use Ability")

            choice = input ("Select an action: ")

            if choice == "1":
                damage = character.calculate_strength_attack_damage()
                character.attack (enemy)

                print (f"\n{character.name} deals {damage} damage!")
                action_complete = True

            elif choice == "2":
                action_complete = self.select_ability (character, enemy)

            else:
                print ("\nInvalid selection. Please try again.")

        return action_complete

    def select_ability (self, character, enemy):

        abilities = [
            ability for ability in character.get_learned_abilities ()
            if ability.abilityType == "Active"
        ]

        if not abilities:
            print ("\nYou don't have any active abilities!")
            return False

        print("\n================================")
        print("       AVAILABLE ABILITIES")
        print("================================")

        for index, ability in enumerate (abilities, start = 1):
            print (f"{index}. {ability.name}")

        print ("0. Back")
        print("================================")

        choice = input ("Select an ability: ")

        if choice == "0":
            return False

        if not choice.isdigit ():
            print ("\nInvalid selection.")
            return False

        selection = int (choice)

        if selection < 1 or selection > len (abilities):
            print ("\nInvalid selection.")
            return False

        ability = abilities [selection - 1]

        result = character.use_ability (ability, enemy)

        if not result:
            print ("\nThat ability could not be used.")
            return False

        if ability.healingPercentage > 0:
            print (f"\n{character.name} uses {ability.name}!")
            print (f"Restored {result} health!")

        else:
            print (f"{character.name} uses {ability.name}!")
            print (f"Deals {result} damage to {enemy.name}!")

        return True