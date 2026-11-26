class Ability:
    def __init__ (self, name, description, abilityType, requiredLevel, progressionPath = None, prerequisites = None):
        self.name = name
        self.description = description
        self.abilityType = abilityType
        self.requiredLevel = requiredLevel
        self.progressionPath = progressionPath
        self.prerequisites = prerequisites if prerequisites is not None else []

    def get_details (self):
        return {
            "name": self.name,
            "description": self.description,
            "type": self.abilityType,
            "required_level": self.requiredLevel,
            "progression_path": self.progressionPath
        }