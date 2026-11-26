class Character:
    def __init__ (self, name, job, attributes = None):
        self.name = name
        self.level = 1
        self.job = job
        self.attributes = attributes if attributes is not None else {}
        self.learnedAbilities = []
        self.specializationAffinities = []

        # Automatically learn the Job's starting abilities
        for ability in self.job.get_starting_abilities ():
            self.learnedAbilities.append (ability)

    def can_learn_ability (self, ability):
        
        # Check whether the character already knows this ability
        if ability in self.learnedAbilities:
            return False

        # Check the required level
        if self.level < ability.requiredLevel:
            return False

        # Check whether the character meets the prerequisites
        for prerequisite in ability.prerequisites:
            if prerequisite not in self.learnedAbilities:
                return False

        # check whether the ability belongs to the character's Job
        availableAbilities = self.job.get_available_abilities ().copy ()

        for specialization in self.job.get_specializations ():
            availableAbilities.extend (specialization.get_abilities())

        if ability not in availableAbilities:
            return False

        return True

    def learn_ability (self, ability):
        if not self.can_learn_ability (ability):
            return False

        self.learnedAbilities.append (ability)

        # Record the ability's specialization affinity, if applicable
        if ability.progressionPath is not None:
            if ability.progressionPath not in self.specializationAffinities:
                self.specializationAffinities.append (ability.progressionPath)

        return True

    def get_learned_abilities (self):
        return self.learnedAbilities


    def get_details (self):
        return {
            "name": self.name,
            "level": self.level,
            "job": self.job.name,
            "attributes": self.attributes,
            "learned_abilities": [
                ability.name for ability in self.learnedAbilities
            ],
            "specialization_affinities": self.specializationAffinities
        }