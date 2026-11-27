import random


class ProgressionManager:

    MAX_LEVEL = 4

    XP_THRESHOLDS = {
        1: 0,
        2: 100,
        3: 250,
        4: 450
    }

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

    def can_level_up (self, character):

        # check the level limit
        if character.level >= self.MAX_LEVEL:
            return False

        next_level = character.level + 1

        # check whether the character has enough experience
        required_experience = self.XP_THRESHOLDS [next_level]

        return character.experience >= required_experience

    def level_up (self, character, selected_attributes = None):

        # check the level limit
        if not self.can_level_up (character):
            return False

        next_level = character.level + 1

        # Every fourth level is an attribute milestone
        if next_level % 4 == 0:

            # Require the player to select three attributes to boost
            if selected_attributes is None or len (selected_attributes) != 3:
                return False

            if len (set (selected_attributes)) != 3:
                return False

            for attribute in selected_attributes:
                if attribute not in character.attributes:
                    return False

        # Apply level increase
        character.level = next_level

        # Increase all attributes by 1
        # Milestone attributes gain an additional 2 points
        if next_level % 4 == 0:
            character.increase_attributes (selected_attributes)

        else:
            character.increase_attributes ()

        return self.get_ability_choices (character)

    def award_experience (self, character, amount):

        if amount <= 0:
            return False

        character.experience += amount

        return self.can_level_up (character)