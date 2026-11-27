from AdventureManagement.Enemy import Enemy

def create_feral_rat ():
    return Enemy (
        name = "Feral Rat",
        description = "A surprisingly large, aggressive rat.",
        level = 1,
        minHealth = 9,
        maxHealth = 13,
        attackDamage = 4,
        experienceReward = 10
    )