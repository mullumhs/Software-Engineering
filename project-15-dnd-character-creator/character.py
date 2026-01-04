class Character:
    RACES = [
        "Dwarf", "Elf", "Halfling", "Human", 
        "Dragonborn", "Gnome", "Half-Elf", "Half-Orc", "Tiefling"
    ]
    CLASSES = [
        "Barbarian", "Bard", "Cleric", "Druid", "Fighter", 
        "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"
    ]
    ABILITY_NAMES = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

    RACE_BONUSES = {
        "Dwarf": {"Constitution": 2},
        "Elf": {"Dexterity": 2},
        "Halfling": {"Dexterity": 2},
        "Human": {"all": 1},
        "Dragonborn": {"Strength": 2, "Charisma": 1},
        "Gnome": {"Intelligence": 2},
        "Half-Elf": {"Charisma": 2, "choice": 2},
        "Half-Orc": {"Strength": 2, "Constitution": 1},
        "Tiefling": {"Intelligence": 1, "Charisma": 2}
    }

    CLASS_INFO = {
        "Barbarian": {"hit_die": 12, "primary_ability": "Strength"},
        "Bard": {"hit_die": 8, "primary_ability": "Charisma"},
        "Cleric": {"hit_die": 8, "primary_ability": "Wisdom"},
        "Druid": {"hit_die": 8, "primary_ability": "Wisdom"},
        "Fighter": {"hit_die": 10, "primary_ability": "Strength or Dexterity"},
        "Monk": {"hit_die": 8, "primary_ability": "Dexterity and Wisdom"},
        "Paladin": {"hit_die": 10, "primary_ability": "Strength and Charisma"},
        "Ranger": {"hit_die": 10, "primary_ability": "Dexterity and Wisdom"},
        "Rogue": {"hit_die": 8, "primary_ability": "Dexterity"},
        "Sorcerer": {"hit_die": 6, "primary_ability": "Charisma"},
        "Warlock": {"hit_die": 8, "primary_ability": "Charisma"},
        "Wizard": {"hit_die": 6, "primary_ability": "Intelligence"}
    }