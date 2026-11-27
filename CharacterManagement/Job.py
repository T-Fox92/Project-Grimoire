class Job:
    def __init__ (
            self, 
            name, 
            description,
            coreAttribute = None, 
            startingAbilities = None, 
            availableAbilities = None, 
            specializations = None
            ):
        
        self.name = name
        self.description = description
        self.coreAttribute = coreAttribute
        self.startingAbilities = startingAbilities if startingAbilities is not None else []
        self.availableAbilities = availableAbilities if availableAbilities is not None else []
        self.specializations = specializations if specializations is not None else []

    def get_core_attribute (self):
        return self.coreAttribute

    def get_starting_abilities (self):
        return self.startingAbilities

    def get_available_abilities (self):
        return self.availableAbilities

    def get_specializations (self):
        return self.specializations

    def add_specializations (self, specializations):
        self.specializations.append (specializations)

    def add_ability (self, ability):
        self.availableAbilities.append (ability)