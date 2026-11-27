
class CharacterStatus:

    def display(self, character, progression_manager):

        print("\n================================")
        print("        CHARACTER STATUS")
        print("================================")

        # Basic information
        print(f"Name: {character.name}")
        print(f"Level: {character.level}")

        # Health
        print("\n--- Health ---")
        print(f"Health: {character.currentHealth}/{character.maxHealth}")

        # Experience
        print("\n--- Experience ---")

        if character.level >= progression_manager.MAX_LEVEL:
            print("Maximum level reached.")
            print(f"Total Experience: {character.experience}")

        else:
            next_level = character.level + 1
            required_xp = progression_manager.XP_THRESHOLDS[next_level]
            remaining_xp = max(0, required_xp - character.experience)

            print(f"Total Experience: {character.experience}")
            print(f"Next Level: {required_xp} XP")
            print(f"Experience Remaining: {remaining_xp}")

        # Attributes
        print("\n--- Attributes ---")

        for attribute, value in character.attributes.items():
            print(f"{attribute}: {value}")

        # Learned abilities
        print("\n--- Learned Abilities ---")

        if character.learnedAbilities:
            for ability in character.learnedAbilities:
                print(f"- {ability.name}")
        else:
            print("No abilities learned.")

        print("================================")
