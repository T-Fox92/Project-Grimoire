class RestLocation:

    def __init__ (self, name):
        self.name = name

    def rest (self, character):
        print (f"\n{character.name} rests at {self.name}.")


        # Restore the character's health
        character.currentHealth = character.maxHealth

        print (f"Health has been fully restore!\n{character.name} is ready for more adventures.")