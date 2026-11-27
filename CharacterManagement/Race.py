class Race:

    VALID_ATTRIBUTES = [
        "Strength",
        "Agility",
        "Constitution",
        "Intelligence",
        "Willpower"
    ]

    def __init__ (
            self,
            name,
            description,
            attributeBonuses = None,
            attributePenalty = None,
            isHuman = False
    ):

        self.name = name
        self.description = description
        self.attributeBonuses = attributeBonuses if attributeBonuses is not None else {}
        self.attributePenalty = attributePenalty
        self.isHuman = isHuman

    def get_attribute_bonuses (self):
        return self.attributeBonuses

    def get_attribute_penalty (self):
        return self.attributePenalty

    def get_details (self):
        return {
            "name": self.name,
            "description": self.description,
            "attribute_bonuses": self.attributeBonuses,
            "attribute_penalty": self.attributePenalty,
            "is_human": self.isHuman
        }