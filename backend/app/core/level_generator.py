"""AI-powered level generator for dynamic content creation."""

from __future__ import annotations

import json
import random
from typing import Any

from ..models.schemas import Difficulty, GameType, Level, World

# ---------------------------------------------------------------------------
# Object pools per world (used by the generator)
# ---------------------------------------------------------------------------

WORLD_OBJECTS: dict[str, list[str]] = {
    "flower_fruit_mountain": ["peach", "monkey", "banana", "flower", "coconut"],
    "dragon_palace": ["fish", "shell", "pearl", "gem", "coral"],
    "heaven_palace": ["star", "cloud", "peach", "moon", "lantern"],
    "white_bone_cave": ["bone", "flower", "mask", "mirror", "candle"],
    "flaming_mountain": ["flame", "fan", "rock", "ember", "spark"],
    "journey_road": ["peach", "scroll", "staff", "hat", "gem"],
}

WORLD_STORIES: dict[str, list[str]] = {
    "flower_fruit_mountain": [
        "Wukong is picking fruits for his monkey friends!",
        "The little monkeys are playing on the mountain!",
        "Help Wukong count the peaches in the garden!",
        "The waterfall is sparkling today! Count the flowers!",
    ],
    "dragon_palace": [
        "Wukong dives deep to find treasures!",
        "The Dragon King needs help sorting his pearls!",
        "Little fish are swimming in patterns!",
        "Help arrange the coral in the right order!",
    ],
    "heaven_palace": [
        "Wukong jumps between clouds in the sky!",
        "The star children need help counting!",
        "Peaches are growing in the heavenly garden!",
        "Cloud fairies are dancing in a pattern!",
    ],
    "white_bone_cave": [
        "Something looks different here... look carefully!",
        "The White Bone Spirit left clues! Find them!",
        "Help Wukong sort the real from the fake!",
        "Tang Monk needs help remembering the path!",
    ],
    "flaming_mountain": [
        "The fire sprites are blocking the way!",
        "Use the fan to blow away some flames!",
        "Princess Iron Fan needs help counting embers!",
        "Which side of the mountain has more flames?",
    ],
    "journey_road": [
        "The team is almost there! Solve this together!",
        "Bajie is hungry! Help him count the food!",
        "Sha Wujing is organizing the supplies!",
        "One last challenge before reaching the West!",
    ],
}

CHARACTER_DIALOGUES = {
    "wukong": [
        "You're amazing, little hero!",
        "Ha ha! That was easy for you!",
        "My golden eyes knew you could do it!",
        "Let's keep going, friend!",
    ],
    "bajie": [
        "Wow, even I couldn't do that! Great job!",
        "Hehe, you're smarter than me!",
        "My tummy is happy now!",
    ],
    "sha_wujing": [
        "Very organized! Well done!",
        "Everything is in its place. Good job!",
        "Master would be proud of you!",
    ],
    "tang_monk": [
        "Wonderful! You are learning so well!",
        "Patience and wisdom lead to success!",
        "Each step brings us closer to the West!",
    ],
}


def generate_counting_level(
    world: str, difficulty: int, level_num: int
) -> dict[str, Any]:
    """Generate a counting level."""
    objects = WORLD_OBJECTS.get(world, WORLD_OBJECTS["flower_fruit_mountain"])
    obj = random.choice(objects)

    if difficulty == 1:
        count = random.randint(1, 5)
    elif difficulty == 2:
        count = random.randint(4, 7)
    else:
        count = random.randint(6, 10)

    wrong1 = max(1, count - 1)
    wrong2 = count + 1
    options = sorted(set([wrong1, count, wrong2]))
    if len(options) < 3:
        options = [count - 1, count, count + 1]

    return {
        "text": f"How many {obj}s are there?",
        "visual_objects": [obj] * count,
        "options": options,
        "correct_answer": count,
    }


def generate_addition_level(
    world: str, difficulty: int, level_num: int
) -> dict[str, Any]:
    """Generate an addition level."""
    objects = WORLD_OBJECTS.get(world, WORLD_OBJECTS["heaven_palace"])
    obj = random.choice(objects)

    if difficulty == 1:
        a, b = random.randint(1, 3), random.randint(1, 2)
    elif difficulty == 2:
        a, b = random.randint(2, 5), random.randint(1, 4)
    else:
        a, b = random.randint(3, 6), random.randint(2, 4)

    answer = a + b
    wrong1 = max(1, answer - 1)
    wrong2 = answer + 1
    options = sorted(set([wrong1, answer, wrong2]))

    return {
        "text": f"Wukong has {a} {obj}s. He finds {b} more. How many now?",
        "visual_objects": [obj] * a + [f"{obj}_new"] * b,
        "options": options,
        "correct_answer": answer,
    }


def generate_subtraction_level(
    world: str, difficulty: int, level_num: int
) -> dict[str, Any]:
    """Generate a subtraction level."""
    objects = WORLD_OBJECTS.get(world, WORLD_OBJECTS["flaming_mountain"])
    obj = random.choice(objects)

    if difficulty == 1:
        total = random.randint(3, 5)
        remove = random.randint(1, 2)
    elif difficulty == 2:
        total = random.randint(5, 8)
        remove = random.randint(2, 3)
    else:
        total = random.randint(7, 10)
        remove = random.randint(2, 5)

    answer = total - remove
    wrong1 = max(0, answer - 1)
    wrong2 = answer + 1
    options = sorted(set([wrong1, answer, wrong2]))

    return {
        "text": f"There are {total} {obj}s. {remove} fly away. How many are left?",
        "visual_objects": [obj] * total,
        "options": options,
        "correct_answer": answer,
    }


def generate_comparison_level(
    world: str, difficulty: int, level_num: int
) -> dict[str, Any]:
    """Generate a comparison level."""
    objects = WORLD_OBJECTS.get(world, WORLD_OBJECTS["flaming_mountain"])
    obj = random.choice(objects)

    if difficulty == 1:
        left = random.randint(1, 4)
        right = random.choice([left + random.randint(1, 2), max(1, left - random.randint(1, 2))])
    else:
        left = random.randint(3, 8)
        right = random.choice([left + 1, max(1, left - 1)])

    return {
        "text": f"Which group has more {obj}s?",
        "visual_objects": [obj] * left + ["|"] + [obj] * right,
        "options": ["left", "right"],
        "correct_answer": "left" if left > right else "right",
    }


def generate_pattern_level(
    world: str, difficulty: int, level_num: int
) -> dict[str, Any]:
    """Generate a pattern completion level."""
    objects = WORLD_OBJECTS.get(world, WORLD_OBJECTS["dragon_palace"])

    if difficulty == 1:
        # AB pattern
        a, b = random.sample(objects, 2)
        sequence = [a, b, a, b, a, "?"]
        answer = b
        options = random.sample(objects, min(3, len(objects)))
        if answer not in options:
            options[0] = answer
        random.shuffle(options)
    elif difficulty == 2:
        # ABC pattern
        a, b, c = random.sample(objects, 3)
        sequence = [a, b, c, a, b, "?"]
        answer = c
        options = random.sample(objects, min(3, len(objects)))
        if answer not in options:
            options[0] = answer
        random.shuffle(options)
    else:
        # AABB pattern
        a, b = random.sample(objects, 2)
        sequence = [a, a, b, b, a, a, b, "?"]
        answer = b
        options = random.sample(objects, min(3, len(objects)))
        if answer not in options:
            options[0] = answer
        random.shuffle(options)

    return {
        "text": "What comes next in the pattern?",
        "visual_objects": [],
        "options": options,
        "correct_answer": answer,
        "sequence": sequence,
    }


def generate_ordering_level(
    world: str, difficulty: int, level_num: int
) -> dict[str, Any]:
    """Generate a number ordering level."""
    if difficulty == 1:
        numbers = random.sample(range(1, 6), 4)
    elif difficulty == 2:
        numbers = random.sample(range(1, 8), 5)
    else:
        numbers = random.sample(range(1, 11), 6)

    return {
        "text": "Put the numbers in order from smallest to biggest!",
        "visual_objects": [],
        "options": [],
        "correct_answer": sorted(numbers),
        "sequence": numbers,
    }


def generate_level(
    world: str = "flower_fruit_mountain",
    game_type: str = "counting",
    difficulty: int = 1,
    level_num: int = 1,
) -> dict[str, Any]:
    """Generate a single level dynamically.

    This is the main entry point for AI-generated content.
    In production, this could call an LLM API for richer story generation.
    """
    generators = {
        "counting": generate_counting_level,
        "addition": generate_addition_level,
        "subtraction": generate_subtraction_level,
        "comparison": generate_comparison_level,
        "pattern": generate_pattern_level,
        "ordering": generate_ordering_level,
    }

    gen = generators.get(game_type, generate_counting_level)
    question = gen(world, difficulty, level_num)

    stories = WORLD_STORIES.get(world, WORLD_STORIES["flower_fruit_mountain"])
    character = random.choice(["wukong", "bajie", "sha_wujing", "tang_monk"])
    dialogues = CHARACTER_DIALOGUES.get(character, CHARACTER_DIALOGUES["wukong"])

    level = {
        "id": f"ai_{world[:2]}_{level_num:03d}",
        "world": world,
        "level_number": level_num,
        "name": f"AI Challenge {level_num}",
        "story_intro": random.choice(stories),
        "character": character,
        "game_type": game_type,
        "difficulty": difficulty,
        "question": question,
        "reward": {
            "peaches": difficulty,
            "animation": "celebrate",
            "dialogue": random.choice(dialogues),
            "character": character,
        },
        "hints": ["Take your time!", "Count carefully!"],
        "tags": [game_type, f"difficulty_{difficulty}"],
    }

    return level


def generate_daily_challenge(
    completed_levels: list[str] | None = None,
) -> list[dict[str, Any]]:
    """Generate 3 daily challenge levels based on player progress."""
    worlds = list(WORLD_OBJECTS.keys())
    game_types = ["counting", "addition", "subtraction", "pattern", "comparison"]

    challenges = []
    for i in range(3):
        world = random.choice(worlds)
        game_type = random.choice(game_types)
        difficulty = min(i + 1, 3)
        level = generate_level(world, game_type, difficulty, 900 + i)
        level["id"] = f"daily_{i + 1}"
        level["name"] = f"Daily Challenge {i + 1}"
        challenges.append(level)

    return challenges
