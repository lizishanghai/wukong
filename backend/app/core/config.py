"""Application configuration."""

from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
LEVELS_FILE = DATA_DIR / "levels.json"

# Game settings
MAX_STARS_PER_LEVEL = 3
PEACHES_FOR_COSTUME = 30

WORLDS_META = {
    "flower_fruit_mountain": {
        "name": "Flower Fruit Mountain",
        "name_cn": "花果山",
        "description": "Wukong's home! Learn to count with monkey friends.",
        "theme_color": "#4CAF50",
        "characters": ["wukong", "monkey_elder", "baby_monkeys"],
        "unlock_requirement": None,
    },
    "dragon_palace": {
        "name": "Dragon Palace",
        "name_cn": "龙宫",
        "description": "Dive underwater to find patterns and treasures!",
        "theme_color": "#2196F3",
        "characters": ["wukong", "dragon_king", "shrimp_soldiers"],
        "unlock_requirement": "flower_fruit_mountain",
    },
    "heaven_palace": {
        "name": "Heaven Palace",
        "name_cn": "天宫",
        "description": "Jump on clouds and learn to add numbers!",
        "theme_color": "#FFC107",
        "characters": ["wukong", "jade_emperor", "cloud_fairies"],
        "unlock_requirement": "dragon_palace",
    },
    "white_bone_cave": {
        "name": "White Bone Cave",
        "name_cn": "白骨洞",
        "description": "Spot the disguises and sort the tricks!",
        "theme_color": "#9C27B0",
        "characters": ["wukong", "tang_monk", "white_bone_spirit"],
        "unlock_requirement": "heaven_palace",
    },
    "flaming_mountain": {
        "name": "Flaming Mountain",
        "name_cn": "火焰山",
        "description": "Fan away the flames with subtraction!",
        "theme_color": "#FF5722",
        "characters": ["wukong", "princess_iron_fan", "fire_sprites"],
        "unlock_requirement": "white_bone_cave",
    },
    "journey_road": {
        "name": "Journey Road",
        "name_cn": "西行之路",
        "description": "The final journey! Use everything you learned!",
        "theme_color": "#FF9800",
        "characters": ["wukong", "tang_monk", "bajie", "sha_wujing"],
        "unlock_requirement": "flaming_mountain",
    },
}

COSTUMES = {
    "default": {"name": "Classic Wukong", "cost": 0},
    "golden_armor": {"name": "Golden Armor", "cost": 30},
    "cloud_rider": {"name": "Cloud Rider", "cost": 30},
    "peach_farmer": {"name": "Peach Farmer", "cost": 20},
    "dragon_warrior": {"name": "Dragon Warrior", "cost": 50},
    "star_cape": {"name": "Star Cape", "cost": 40},
    "fire_king": {"name": "Fire King", "cost": 50},
    "journey_master": {"name": "Journey Master", "cost": 100},
}
