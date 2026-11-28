
from CharacterManagement.Ability import Ability
from CharacterManagement.Specialization import Specialization
from CharacterManagement.Job import Job


# ============================================================
# FIGHTER
# ============================================================

# Starting ability
CHARGE = Ability(
    "Charge",
    "Rush toward an enemy and strike with a physical attack.",
    "Active",
    1,
    damageMultiplier = 1.25,
    scalingAttribute = "Strength"
) 

# Level 2 active choices
MAGIC_WEAPON = Ability(
    "Magic Weapon",
    "Enhance your weapon with arcane energy to increase its damage.",
    "Active",
    2
)

DOUBLE_SLASH = Ability(
    "Double Slash",
    "Strike an enemy twice in rapid succession.",
    "Active",
    2
)

POWER_SLASH = Ability(
    "Power Slash",
    "Deliver a powerful physical attack against an enemy.",
    "Active",
    2
)

# Heavy passive abilities
BRUTAL_FORCE = Ability(
    "Brutal Force",
    "Increases physical damage dealt with two-handed weapons.",
    "Passive",
    3,
    "Heavy"
)

IRONCLAD = Ability(
    "Ironclad",
    "Reduces incoming physical damage while a shield is equipped.",
    "Passive",
    3,
    "Heavy"
)

# Agile passive abilities
QUICK_REFLEXES = Ability(
    "Quick Reflexes",
    "Reduces incoming damage based on your Agility.",
    "Passive",
    3,
    "Agile"
)

PRECISE_STRIKES = Ability(
    "Precise Strikes",
    "Increases your chance to land critical hits.",
    "Passive",
    3,
    "Agile"
)

# Spellsword passive abilities
ARCANE_INFUSION = Ability(
    "Arcane Infusion",
    "Increases active ability damage, scaling with Intelligence.",
    "Passive",
    3,
    "Spellsword"
)

ARCANE_RESILIENCE = Ability(
    "Arcane Resilience",
    "Converts a portion of qualifying incoming enemy attack damage into health.",
    "Passive",
    3,
    "Spellsword"
)

HEAVY = Specialization(
    "Heavy",
    "Focuses on powerful two-handed attacks and physical resilience.",
    [BRUTAL_FORCE, IRONCLAD]
)

AGILE = Specialization(
    "Agile",
    "Focuses on speed, precision, and avoiding incoming damage.",
    [QUICK_REFLEXES, PRECISE_STRIKES]
)

SPELLSWORD = Specialization(
    "Spellsword",
    "Combines physical combat with arcane power.",
    [ARCANE_INFUSION, ARCANE_RESILIENCE]
)

FIGHTER = Job(
    name="Fighter",
    description="A physical combatant specializing in weapon mastery and martial prowess.",
    coreAttribute="Strength",
    startingAbilities=[CHARGE],
    availableAbilities=[MAGIC_WEAPON, DOUBLE_SLASH, POWER_SLASH],
    specializations=[HEAVY, AGILE, SPELLSWORD]
)


# ============================================================
# CLERIC
# ============================================================

# Starting ability
HEALING_LIGHT = Ability(
    "Healing Light",
    "Restore health to yourself or a selected ally.",
    "Active",
    1,
    healingPercentage = 0.33
)

# Level 2 active choices
HOLY_NOVA = Ability(
    "Holy Nova",
    "Unleash an area-of-effect burst of divine damage.",
    "Active",
    2
)

HOLY_STRIKE = Ability(
    "Holy Strike",
    "Strike an enemy with a weapon imbued with divine energy.",
    "Active",
    2
)

CHALLENGE = Ability(
    "Challenge",
    "Taunt enemies, forcing them to prioritize attacking you for a limited duration.",
    "Active",
    2
)

# Holy passive abilities
DIVINE_FAVOR = Ability(
    "Divine Favor",
    "Increases the effectiveness of your healing abilities.",
    "Passive",
    3,
    "Holy"
)

RADIANT_POWER = Ability(
    "Radiant Power",
    "Increases damage dealt by holy abilities.",
    "Passive",
    3,
    "Holy"
)

# Inquisitor passive abilities
DIVINE_WEAPON = Ability(
    "Divine Weapon",
    "Increases damage dealt by attacks enhanced with holy magic.",
    "Passive",
    3,
    "Inquisitor"
)

ZEALOT = Ability(
    "Zealot",
    "Increases physical damage dealt to enemies recently affected by divine abilities.",
    "Passive",
    3,
    "Inquisitor"
)

# Guardian passive abilities
PROTECTIVE_AURA = Ability(
    "Protective Aura",
    "Reduces damage received by a selected companion.",
    "Passive",
    3,
    "Guardian"
)

MARTYRS_RESOLVE = Ability(
    "Martyr's Resolve",
    "Reduces incoming damage while you are actively being targeted by taunted enemies.",
    "Passive",
    3,
    "Guardian"
)

HOLY = Specialization(
    "Holy",
    "Focuses on divine healing and holy damage.",
    [DIVINE_FAVOR, RADIANT_POWER]
)

INQUISITOR = Specialization(
    "Inquisitor",
    "Combines physical combat with divine offensive magic.",
    [DIVINE_WEAPON, ZEALOT]
)

GUARDIAN = Specialization(
    "Guardian",
    "Protects allies and draws enemy attention away from the party.",
    [PROTECTIVE_AURA, MARTYRS_RESOLVE]
)

CLERIC = Job(
    name="Cleric",
    description="A divine practitioner specializing in healing, holy magic, and protecting allies.",
    coreAttribute="Willpower",
    startingAbilities=[HEALING_LIGHT],
    availableAbilities=[HOLY_NOVA, HOLY_STRIKE, CHALLENGE],
    specializations=[HOLY, INQUISITOR, GUARDIAN]
)


# ============================================================
# ELEMENTALIST
# ============================================================

# Starting ability
TRI_DISASTER = Ability(
    "Tri-Disaster",
    "Deals Fire, Ice, and Lightning damage. Gains additional effects based on your elemental specialization.",
    "Active",
    1,
    damageMultiplier = 1.0,
    scalingAttribute = "Intelligence"
)

# Level 2 active choices
FLAME_BURST = Ability(
    "Flame Burst",
    "Deal area-of-effect fire damage and apply or refresh Burning.",
    "Active",
    2
)

FROSTBOLT = Ability(
    "Frostbolt",
    "Deal ice damage and slow the target.",
    "Active",
    2
)

LIGHTNING_BOLT = Ability(
    "Lightning Bolt",
    "Unleash concentrated lightning damage against a single target.",
    "Active",
    2
)

# Fire passive abilities
PYROMANCY = Ability(
    "Pyromancy",
    "Increases damage dealt by direct fire abilities.",
    "Passive",
    3,
    "Fire"
)

LINGERING_FLAMES = Ability(
    "Lingering Flames",
    "Increases the damage dealt by Burning effects.",
    "Passive",
    3,
    "Fire"
)

# Ice passive abilities
FROST_MASTERY = Ability(
    "Frost Mastery",
    "Increases the damage and effectiveness of ice spells.",
    "Passive",
    3,
    "Ice"
)

DEEP_FREEZE = Ability(
    "Deep Freeze",
    "Increases the effectiveness and duration of slowing effects.",
    "Passive",
    3,
    "Ice"
)

# Lightning passive abilities
ELECTROMANCY = Ability(
    "Electromancy",
    "Increases damage dealt by lightning spells.",
    "Passive",
    3,
    "Lightning"
)

CONDUCTIVITY = Ability(
    "Conductivity",
    "Improves Chain Lightning by increasing its reach or reducing damage loss between jumps.",
    "Passive",
    3,
    "Lightning"
)

ELEMENTALIST_PATH = Specialization(
    "Elementalist",
    "Studies the destructive and controlling powers of the elements.",
    [
        PYROMANCY,
        LINGERING_FLAMES,
        FROST_MASTERY,
        DEEP_FREEZE,
        ELECTROMANCY,
        CONDUCTIVITY
    ]
)

ELEMENTALIST = Job(
    name="Elementalist",
    description="A master of fire, ice, and lightning who manipulates elemental forces to destroy and control enemies.",
    coreAttribute="Intelligence",
    startingAbilities=[TRI_DISASTER],
    availableAbilities=[FLAME_BURST, FROSTBOLT, LIGHTNING_BOLT],
    specializations=[ELEMENTALIST_PATH]
)


# ============================================================
# PLAYABLE JOBS
# ============================================================

PLAYABLE_JOBS = [
    FIGHTER,
    CLERIC,
    ELEMENTALIST
]
