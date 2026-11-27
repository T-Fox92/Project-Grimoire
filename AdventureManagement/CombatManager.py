class CombatManager:

    def __init__ (self, progression_manager):
        self.progression_manager = progression_manager

    def start_combat (self, character, enemy):

        print (f"\nA {enemy.name} appears!")
        print (enemy.description)

        combat_over = False

        while not combat_over:

            # Player's turn
            print (f"\n{character.name} attacks {enemy.name}!")
            character.attack(enemy)

            print (f"{enemy.name} has {enemy.currentHealth}/{enemy.maxHealth} health remaining")

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