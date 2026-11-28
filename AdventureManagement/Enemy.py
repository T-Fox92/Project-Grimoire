import random


class Enemy:

    def __init__ (self, name, description, level,minHealth, maxHealth, attackDamage, experienceReward):

        if minHealth <= 0 or maxHealth < minHealth:
            raise ValueError ("Invalid enemy health range.")

        self.name = name
        self.description = description
        self.level = level
        self.minHealth = minHealth
        self.maxHealth = random.randint (minHealth, maxHealth)
        self.currentHealth = self.maxHealth
        self.attackDamage = attackDamage
        self.experienceReward = experienceReward

    def take_damage (self, amount):
        if amount < 0:
            raise ValueError ("Damage cannot be negative.")

        self.currentHealth = max (0, self.currentHealth - amount)

    def attack (self, target):
        if not self.is_alive():
            return

        target.take_damage (self.attackDamage)

    def is_alive (self):
        return self.currentHealth > 0

    def get_details (self):
        return (
            f"Name: {self.name}\n"
            f"Level: {self.level}\n"
            f"Health: {self.currentHealth}/{self.maxHealth}\n"
            f"Attack Damage: {self.attackDamage}"
        )
