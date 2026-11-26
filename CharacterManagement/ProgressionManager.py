import random


class ProgressionManager:

    def get_available_abilites (self, character, ability_type):
        available_abilities = character.job.get_available_abilities().copy()

        # Add abilities belonging to the Job's specializations
        for specialization in character.job.get_specializations ():
            available_abilities.extend (specialization.get_abilities ())

        # Keep only abilities of the requested type that the character is eligible to learn
        eligible_abilities = []

        for ability in available_abilities:
            if (ability.abilityType == ability_type and character.can_learn_ability (ability)):
                eligible_abilities.append (ability)

        return eligible_abilities

    def get_ability_choices (self, character):

        # Level 2 offers three active abilities
        if character.level == 2:
            eligible_abilities = self.get_available_abilites (character, "Active")

            if len(eligible_abilities) > 3:
                return random.sample (eligible_abilities, 3)

            return eligible_abilities

        # level 3 offers passive abilities
        elif character.level == 3:
            return self.get_available_abilites (character, "Passive")

        return []

    def select_ability (self, character, ability):

        # Make sure the selected ability is actually an offered choice
        available_choices = self.get_ability_choices (character)

        if ability not in available_choices:
            return False

        return character.learn_ability (ability)

    def level_up (self, character):
        
        # Our initial implementation only supports levels 1 through 3
        if character.level >= 3:
            return False

        character.level += 1

        return self.get_ability_choices (character)