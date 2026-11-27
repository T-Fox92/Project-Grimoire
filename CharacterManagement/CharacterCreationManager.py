from CharacterManagement.Character import Character

class CharacterCreationManager:

    BASE_ATTRIBUTES = {
        "Strength": 3,
        "Agility": 3,
        "Constitution": 3,
        "Intelligence": 3,
        "Willpower": 3
    }

    def calculate_attributes (self, race, job, selected_attributes, human_penalty = None, skip_racial_penalty = False, skipped_bonus = None):
        
        attributes = self.BASE_ATTRIBUTES.copy()

        # Apply racial bonuses
        for attribute, bonus in race.get_attribute_bonuses().items():
            attributes [attribute] += bonus

        # Apply racial penalty rules
        if race.isHuman:
            if human_penalty not in attributes:
                raise ValueError ("Humans must select an attribute for their -2 penalty.")

            attributes [human_penalty] -= 2

        elif not skip_racial_penalty:
            penalty = race.get_attribute_penalty()
            attributes[penalty] -= 1

        elif skipped_bonus is not None:
            # forgoing the penalty also means giving up one +2 bonus
            if skipped_bonus not in race.get_attribute_bonuses():
                raise ValueError ("Invalid racial bonus selection.")

            attributes [skipped_bonus] -= 2

        else:
            raise ValueError ("You must give up a +2 bonus when skipping the racial penalty.")

        # Apply the job's core attribute bonus
        core_attribute = job.get_core_attribute()

        if core_attribute not in attributes:
            raise ValueError ("Job has an invalid core attribute.")

        attributes[core_attribute] += 2

        # Apply the player's three freely distributed points
        if len(selected_attributes) != 3:
            raise ValueError ("You must distribute exactly three attribute points.")

        if len (set (selected_attributes)) != 3:
            raise ValueError ("You must select three different attributes.")

        for attribute in selected_attributes:
            if attribute not in attributes:
                raise ValueError (f"Invalid attribute: {attribute}")

            attributes [attribute] += 1

        return attributes

    def create_character (
            self, 
            name, 
            race, 
            job, 
            selected_attributes, 
            human_penalty = None, 
            skip_racial_penalty = False, 
            skipped_bonus = None
        ):

        attributes = self.calculate_attributes (
            race,
            job,
            selected_attributes,
            human_penalty,
            skip_racial_penalty,
            skipped_bonus
        )

        character = Character (
            name = name,
            job = job,
            race = race,
            attributes = attributes
        )

        return character