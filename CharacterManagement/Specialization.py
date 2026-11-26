class Specialization:
    def __init__ (self, name, description, abilities = None):
        self.name = name
        self.description = description
        self.abilities = abilities if abilities is not None else []

    def add_ability (self, ability):
        self.abilities.append (ability)

    def get_abilities (self):
        return self.abilities
