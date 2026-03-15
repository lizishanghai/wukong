"""Regenerate all 100 game levels with proper difficulty progression."""

import json
import random
import shutil
from pathlib import Path

random.seed(42)  # reproducible

# ---------------------------------------------------------------------------
# World configuration
# ---------------------------------------------------------------------------

WORLDS = [
    {
        "id": "flower_fruit_mountain",
        "prefix": "w1",
        "count": 18,
        "diff_range": (1, 2),
        "num_range": (1, 5),
        "options": 3,
        "objects": ["peach", "monkey", "banana", "flower", "coconut"],
        "names_en": [
            "Wake Up Wukong", "Peach Picking", "Flowers on the Hill",
            "One Little Monkey", "Banana Party", "Gem Counting",
            "Mountain Monkeys", "Coconut Split", "Peach Tree",
            "Flower Garden", "Monkey School", "Counting Stars",
            "Two Plus Two", "Three Bananas", "Fruit Basket",
            "Shape Garden", "Color Flowers", "Mountain Shapes",
        ],
        "stories": [
            "Wukong wakes up on Flower Fruit Mountain!",
            "Help Wukong pick some peaches.",
            "Beautiful flowers are blooming on the mountain.",
            "A baby monkey is hiding behind a rock.",
            "The monkeys are having a banana party!",
            "Shiny gems sparkle in the cave.",
            "Count all the monkeys playing on the hill.",
            "Help split coconuts for the monkeys.",
            "How many peaches are on the tree?",
            "The flower garden is blooming beautifully.",
            "Monkey school is starting! Time to learn.",
            "Stars are shining above the mountain.",
            "Wukong is learning addition!",
            "How many bananas does Wukong have?",
            "Help sort the fruit basket.",
            "What shapes do you see in the garden?",
            "The flowers come in many colors!",
            "Wukong finds shapes on the mountain.",
        ],
        "game_types": [
            "counting", "counting", "counting", "counting",
            "counting", "counting", "counting", "counting",
            "addition", "addition", "addition",
            "comparison", "comparison",
            "pattern", "pattern", "pattern",
            "shape_pattern", "shape_pattern",
        ],
    },
    {
        "id": "dragon_palace",
        "prefix": "w2",
        "count": 17,
        "diff_range": (1, 2),
        "num_range": (1, 8),
        "options": 3,
        "objects": ["fish", "shell", "pearl", "gem", "coral"],
        "names_en": [
            "Dragon's Treasure", "Shell Collection", "Pearl Diving",
            "Fish Parade", "Coral Reef", "Ocean Patterns",
            "Sea Memory", "Treasure Sort", "Shell Shapes",
            "Pearl Patterns", "Ocean Colors", "Fish School",
            "Sea Clock", "Dragon Gems", "Reef Ordering",
            "Wave Patterns", "Deep Sea Shapes",
        ],
        "stories": [
            "Welcome to the Dragon King's palace!",
            "Collect shells from the ocean floor.",
            "Dive deep to find shining pearls.",
            "Watch the fish swim in a parade!",
            "The coral reef is full of life.",
            "Can you find the pattern in the waves?",
            "Remember where the sea creatures hide!",
            "Sort the treasures for the Dragon King.",
            "What shapes do you see in the shells?",
            "The pearls form a beautiful pattern.",
            "The ocean is full of colorful creatures!",
            "Count the fish in the school.",
            "What time is it in the Dragon Palace?",
            "Help count the Dragon's gems.",
            "Put the reef creatures in order!",
            "The waves make interesting patterns.",
            "Deep sea shapes are mysterious!",
        ],
        "game_types": [
            "counting", "counting",
            "pattern", "pattern", "pattern",
            "shape_pattern", "shape_pattern", "shape_pattern",
            "memory", "memory",
            "classification", "classification",
            "find_difference", "find_difference",
            "clock_reading",
            "ordering", "ordering",
        ],
    },
    {
        "id": "heaven_palace",
        "prefix": "w3",
        "count": 18,
        "diff_range": (2, 3),
        "num_range": (1, 10),
        "options": 4,
        "objects": ["star", "cloud", "gem", "moon", "lantern"],
        "names_en": [
            "Heaven's Gate", "Star Counting", "Cloud Addition",
            "Moon Subtraction", "Lantern Light", "Sky Patterns",
            "Heavenly Shapes", "Star Clock", "Cloud Shapes",
            "Gem Comparison", "Moon Ordering", "Heaven Maze",
            "Sky Memory", "Lantern Math", "Cloud Clock",
            "Star Patterns", "Heaven Shapes", "Golden Gate",
        ],
        "stories": [
            "Wukong arrives at the gate of Heaven!",
            "Count the stars in the night sky.",
            "Clouds are joining together!",
            "Some moons are hiding behind clouds.",
            "The lanterns light up the palace.",
            "Can you find the pattern in the stars?",
            "Heavenly shapes float in the sky.",
            "What time does the heavenly clock show?",
            "The clouds form interesting shapes!",
            "Which group of gems is bigger?",
            "Put the moons in order from small to big.",
            "Find your way through the heavenly maze!",
            "Remember where the stars are hiding.",
            "Lanterns need some math to light up!",
            "The cloud clock is hard to read!",
            "Stars make beautiful patterns.",
            "More heavenly shapes to discover!",
            "The golden gate holds a challenge!",
        ],
        "game_types": [
            "addition", "addition", "addition",
            "subtraction", "subtraction",
            "pattern", "pattern",
            "shape_pattern", "shape_pattern", "shape_pattern",
            "clock_reading", "clock_reading", "clock_reading",
            "comparison", "comparison",
            "ordering",
            "maze", "maze",
        ],
    },
    {
        "id": "white_bone_cave",
        "prefix": "w4",
        "count": 17,
        "diff_range": (2, 4),
        "num_range": (5, 15),
        "options": 4,
        "objects": ["bone", "mask", "mirror", "candle", "scroll"],
        "names_en": [
            "Cave Entrance", "Bone Counting", "Mask Subtraction",
            "Mirror Addition", "Candle Light", "Cave Patterns",
            "Skeleton Shapes", "Bone Clock", "Dark Shapes",
            "Mirror Memory", "Cave Sort", "Scroll Math",
            "Shadow Patterns", "Candle Clock", "Bone Ordering",
            "Cave Shapes", "Dark Difference",
        ],
        "stories": [
            "Wukong enters the White Bone Cave!",
            "Count the bones in the dark cave.",
            "Some masks have disappeared!",
            "Mirrors are reflecting more images!",
            "Light the candles to see better.",
            "Strange patterns appear on the walls.",
            "Skeleton shapes are dancing!",
            "What time does the bone clock show?",
            "Dark shapes lurk in the cave.",
            "Remember where the mirrors reflect!",
            "Sort the cave treasures carefully.",
            "Ancient scrolls contain math puzzles.",
            "Shadow patterns shift on the walls.",
            "The candle clock flickers!",
            "Put the bones in order by size.",
            "More cave shapes to discover!",
            "Find differences in the cave scenes.",
        ],
        "game_types": [
            "addition", "addition",
            "subtraction", "subtraction", "subtraction",
            "shape_pattern", "shape_pattern", "shape_pattern",
            "pattern", "pattern",
            "clock_reading", "clock_reading",
            "classification", "classification",
            "memory", "memory",
            "find_difference",
        ],
    },
    {
        "id": "flaming_mountain",
        "prefix": "w5",
        "count": 15,
        "diff_range": (3, 4),
        "num_range": (5, 18),
        "options": 4,
        "objects": ["flame", "fan", "rock", "ember", "spark"],
        "names_en": [
            "Fire Wall", "Flame Counting", "Ember Addition",
            "Spark Subtraction", "Fan Power", "Fire Patterns",
            "Flame Shapes", "Fire Clock", "Lava Shapes",
            "Rock Ordering", "Mountain Maze", "Ember Patterns",
            "Spark Shapes", "Flame Clock", "Fire Challenge",
        ],
        "stories": [
            "The Flaming Mountain blocks the path!",
            "Count the flames to find a way through.",
            "Embers are joining together to grow bigger!",
            "Some sparks are going out!",
            "Use the magic fan to control the fire.",
            "Fire patterns dance before Wukong.",
            "Flames create interesting shapes!",
            "What time does the fire clock show?",
            "Lava shapes flow down the mountain.",
            "Put the rocks in order by size.",
            "Navigate the mountain maze!",
            "Embers form mysterious patterns.",
            "Sparks create dazzling shapes!",
            "The flickering flame clock is tricky!",
            "The final fire challenge awaits!",
        ],
        "game_types": [
            "addition", "addition",
            "subtraction", "subtraction",
            "pattern", "pattern",
            "shape_pattern", "shape_pattern", "shape_pattern",
            "clock_reading", "clock_reading",
            "ordering", "ordering",
            "maze", "maze",
        ],
    },
    {
        "id": "journey_road",
        "prefix": "w6",
        "count": 15,
        "diff_range": (3, 5),
        "num_range": (10, 20),
        "options": 4,
        "objects": ["scroll", "staff", "hat", "gem", "star"],
        "names_en": [
            "Journey Begins", "Road Counting", "Staff Addition",
            "Scroll Subtraction", "Hat Comparison", "Road Patterns",
            "Journey Shapes", "Traveler Clock", "Path Shapes",
            "Star Ordering", "Final Maze", "Gem Patterns",
            "Journey Clock", "Road Shapes", "Thunder Monastery",
        ],
        "stories": [
            "The final stretch of the journey!",
            "Count the travelers on the road.",
            "Wukong's staff grows longer!",
            "Ancient scrolls are being lost!",
            "Whose hat collection is bigger?",
            "The road has mysterious patterns.",
            "Journey shapes appear along the path.",
            "What time should we arrive?",
            "The path reveals interesting shapes.",
            "Put the stars in order by brightness.",
            "The final maze before the monastery!",
            "Gems form the hardest patterns.",
            "The journey clock is almost done!",
            "Road shapes challenge Wukong's mind.",
            "Wukong reaches Thunder Monastery!",
        ],
        "game_types": [
            "addition", "addition",
            "subtraction", "subtraction",
            "pattern", "pattern",
            "shape_pattern", "shape_pattern", "shape_pattern",
            "clock_reading", "clock_reading",
            "comparison", "comparison",
            "ordering",
            "maze",
        ],
    },
]

# ---------------------------------------------------------------------------
# Shape pattern config
# ---------------------------------------------------------------------------

SHAPES = ["circle", "square", "triangle", "diamond", "heart"]
COLORS = ["red", "blue", "green", "yellow"]

SHAPE_EMOJIS = {
    "red_circle": "red_circle", "blue_circle": "blue_circle",
    "green_circle": "green_circle", "yellow_circle": "yellow_circle",
    "red_square": "red_square", "blue_square": "blue_square",
    "green_square": "green_square", "yellow_square": "yellow_square",
    "red_triangle": "red_triangle",
    "blue_diamond": "blue_diamond", "orange_diamond": "orange_diamond",
    "purple_heart": "purple_heart", "red_heart": "red_heart",
    "star_shape": "star_shape",
}

# ---------------------------------------------------------------------------
# Generator helpers
# ---------------------------------------------------------------------------

def make_wrong_options(correct: int, count: int, lo: int, hi: int) -> list[int]:
    """Generate `count` unique wrong integer options near the correct answer."""
    wrongs: set[int] = set()
    candidates = list(range(max(lo, correct - 3), min(hi + 1, correct + 4)))
    candidates = [c for c in candidates if c != correct]
    random.shuffle(candidates)
    for c in candidates:
        wrongs.add(c)
        if len(wrongs) >= count:
            break
    # If not enough, expand range
    r = 4
    while len(wrongs) < count:
        r += 1
        for c in [correct - r, correct + r]:
            if lo <= c <= hi and c != correct and c not in wrongs:
                wrongs.add(c)
                if len(wrongs) >= count:
                    break
    return list(wrongs)[:count]


def make_time_options(correct: str, minute_step: int, count: int) -> list[str]:
    """Generate wrong time options."""
    h, m = correct.split(":")
    hour, minute = int(h), int(m)
    wrongs: set[str] = set()

    # Vary hour
    for dh in [1, -1, 2, -2, 3]:
        nh = ((hour - 1 + dh) % 12) + 1
        t = f"{nh}:{minute:02d}"
        if t != correct:
            wrongs.add(t)

    # Vary minute if applicable
    if minute_step > 0:
        for dm in [minute_step, -minute_step, minute_step * 2]:
            nm = (minute + dm) % 60
            t = f"{hour}:{nm:02d}"
            if t != correct:
                wrongs.add(t)

    return random.sample(list(wrongs), min(count, len(wrongs)))


# ---------------------------------------------------------------------------
# Game type generators
# ---------------------------------------------------------------------------

def gen_counting(world_cfg, difficulty):
    lo, hi = world_cfg["num_range"]
    n_opts = world_cfg["options"]
    objs = world_cfg["objects"]

    # Scale number by difficulty within range
    frac = (difficulty - world_cfg["diff_range"][0]) / max(1, world_cfg["diff_range"][1] - world_cfg["diff_range"][0])
    mid = lo + frac * (hi - lo)
    count = random.randint(max(lo, int(mid - 2)), min(hi, int(mid + 2)))
    count = max(1, count)

    obj = random.choice(objs)
    visual = [obj] * count
    wrongs = make_wrong_options(count, n_opts - 1, max(1, lo), hi)
    options = wrongs + [count]
    random.shuffle(options)

    return {
        "text": f"How many {obj}s do you see?",
        "visual_objects": visual,
        "options": options,
        "correct_answer": count,
    }


def gen_addition(world_cfg, difficulty):
    lo, hi = world_cfg["num_range"]
    n_opts = world_cfg["options"]
    objs = world_cfg["objects"]

    max_sum = hi
    a = random.randint(max(1, lo), max(1, max_sum // 2))
    b = random.randint(1, max_sum - a)
    total = a + b
    obj = random.choice(objs)
    visual = [obj] * a + ["|"] + [obj] * b
    wrongs = make_wrong_options(total, n_opts - 1, max(2, lo), hi)
    options = wrongs + [total]
    random.shuffle(options)

    return {
        "text": f"{a} + {b} = ?",
        "visual_objects": visual,
        "options": options,
        "correct_answer": total,
    }


def gen_subtraction(world_cfg, difficulty):
    lo, hi = world_cfg["num_range"]
    n_opts = world_cfg["options"]
    objs = world_cfg["objects"]

    a = random.randint(max(2, lo + 1), hi)
    b = random.randint(1, a - max(0, lo))
    result = a - b
    obj = random.choice(objs)
    visual = [obj] * a
    wrongs = make_wrong_options(result, n_opts - 1, 0, hi)
    options = wrongs + [result]
    random.shuffle(options)

    return {
        "text": f"{a} - {b} = ?",
        "visual_objects": visual,
        "options": options,
        "correct_answer": result,
    }


def gen_comparison(world_cfg, difficulty):
    lo, hi = world_cfg["num_range"]
    n_opts = world_cfg["options"]
    objs = world_cfg["objects"]

    a = random.randint(lo, hi - 1)
    b = random.randint(a + 1, hi)
    if random.random() < 0.5:
        a, b = b, a  # swap so answer varies

    obj = random.choice(objs)
    visual_a = [obj] * a
    visual_b = [obj] * b
    correct = max(a, b)
    wrongs = make_wrong_options(correct, n_opts - 1, lo, hi)
    options = wrongs + [correct]
    random.shuffle(options)

    return {
        "text": f"Which group has more? {a} or {b}?",
        "visual_objects": visual_a + ["|"] + visual_b,
        "options": options,
        "correct_answer": correct,
    }


def gen_ordering(world_cfg, difficulty):
    lo, hi = world_cfg["num_range"]
    n = min(4, 3 + (difficulty - 1))  # 3-4 numbers to order
    nums = sorted(random.sample(range(lo, hi + 1), min(n, hi - lo + 1)))
    shuffled = nums[:]
    random.shuffle(shuffled)

    return {
        "text": "Put the numbers in order from smallest to biggest!",
        "visual_objects": [],
        "options": shuffled,
        "correct_answer": nums,
        "sequence": shuffled,
    }


def gen_pattern(world_cfg, difficulty):
    objs = world_cfg["objects"]
    n_opts = world_cfg["options"]

    if difficulty <= 2:
        # Simple AB pattern
        a, b = random.sample(objs, 2)
        seq = [a, b, a, b, a, b, "?"]
        answer = a
        wrong_pool = [o for o in objs if o != answer]
    elif difficulty <= 3:
        # ABC pattern
        items = random.sample(objs, min(3, len(objs)))
        seq = items * 2 + ["?"]
        answer = items[0]
        wrong_pool = [o for o in objs if o != answer]
    else:
        # AABB pattern
        a, b = random.sample(objs, 2)
        seq = [a, a, b, b, a, a, "?"]
        answer = b
        wrong_pool = [o for o in objs if o != answer]

    wrongs = random.sample(wrong_pool, min(n_opts - 1, len(wrong_pool)))
    options = wrongs + [answer]
    random.shuffle(options)

    return {
        "text": "What comes next in the pattern?",
        "visual_objects": [],
        "options": options,
        "correct_answer": answer,
        "sequence": seq,
    }


def gen_shape_pattern(world_cfg, difficulty):
    n_opts = world_cfg["options"]

    if difficulty <= 2:
        # Color-only pattern with one shape
        shape = random.choice(SHAPES)
        c1, c2 = random.sample(COLORS, 2)
        s1 = f"{c1}_{shape}"
        s2 = f"{c2}_{shape}"
        seq = [s1, s2, s1, s2, s1, "?"]
        answer = s2
        wrong_candidates = [f"{c}_{shape}" for c in COLORS if f"{c}_{shape}" != answer]
    elif difficulty <= 3:
        # Shape-only pattern with one color
        color = random.choice(COLORS)
        sh1, sh2 = random.sample(SHAPES, 2)
        s1 = f"{color}_{sh1}"
        s2 = f"{color}_{sh2}"
        seq = [s1, s2, s1, s2, s1, "?"]
        answer = s2
        wrong_candidates = [f"{color}_{s}" for s in SHAPES if f"{color}_{s}" != answer]
    else:
        # Color + shape ABC pattern
        items = []
        used = set()
        while len(items) < 3:
            c = random.choice(COLORS)
            s = random.choice(SHAPES)
            key = f"{c}_{s}"
            if key not in used:
                items.append(key)
                used.add(key)
        seq = items + items + ["?"]
        answer = items[0]
        wrong_candidates = [f"{random.choice(COLORS)}_{random.choice(SHAPES)}" for _ in range(10)]
        wrong_candidates = [w for w in wrong_candidates if w != answer]

    wrongs = random.sample(wrong_candidates, min(n_opts - 1, len(wrong_candidates)))
    options = wrongs + [answer]
    random.shuffle(options)

    return {
        "text": "What shape comes next in the pattern?",
        "visual_objects": [],
        "options": options,
        "correct_answer": answer,
        "sequence": seq,
    }


def gen_clock(world_cfg, difficulty):
    n_opts = world_cfg["options"]

    hour = random.randint(1, 12)
    if difficulty <= 2:
        minute = 0
        minute_step = 0
    elif difficulty <= 3:
        minute = random.choice([0, 30])
        minute_step = 30
    elif difficulty <= 4:
        minute = random.choice([0, 15, 30, 45])
        minute_step = 15
    else:
        minute = random.choice([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
        minute_step = 5

    answer = f"{hour}:{minute:02d}"
    wrongs = make_time_options(answer, minute_step, n_opts - 1)
    options = wrongs + [answer]
    random.shuffle(options)

    return {
        "text": "What time does the clock show?",
        "visual_objects": [],
        "options": options,
        "correct_answer": answer,
        "clock_time": {"hour": hour, "minute": minute},
    }


def gen_memory(world_cfg, difficulty):
    objs = world_cfg["objects"]
    n_pairs = min(3, 2 + (difficulty - 1))  # 2-4 pairs
    selected = random.sample(objs, min(n_pairs, len(objs)))
    pairs = [[s, s] for s in selected]

    return {
        "text": "Find the matching pairs!",
        "visual_objects": [],
        "options": [],
        "correct_answer": 0,
        "pairs": pairs,
    }


def gen_find_difference(world_cfg, difficulty):
    objs = world_cfg["objects"]
    scene_size = min(4, 3 + (difficulty - 1))
    scene_a = random.sample(objs, min(scene_size, len(objs)))
    scene_b = scene_a[:]
    idx = random.randint(0, len(scene_b) - 1)
    replacement = random.choice([o for o in objs if o != scene_b[idx]])
    original = scene_b[idx]
    scene_b[idx] = replacement

    return {
        "text": "Find what's different!",
        "visual_objects": [],
        "options": [],
        "correct_answer": replacement,
        "scene_a": scene_a,
        "scene_b": scene_b,
        "differences": [f"{original} replaced by {replacement}"],
    }


def gen_classification(world_cfg, difficulty):
    objs = world_cfg["objects"]
    # Pick 2 categories of 2 objects each
    selected = random.sample(objs, min(4, len(objs)))
    half = len(selected) // 2
    group_a = selected[:half]
    group_b = selected[half:]
    name_a = group_a[0] + "s"
    name_b = group_b[0] + "s"

    all_items = group_a + group_b
    random.shuffle(all_items)

    return {
        "text": f"Sort the items into {name_a} and {name_b}!",
        "visual_objects": all_items,
        "options": [],
        "correct_answer": {name_a: group_a, name_b: group_b},
        "groups": {name_a: group_a, name_b: group_b},
    }


def gen_maze(world_cfg, difficulty):
    size = min(6, 4 + (difficulty - 1))  # 4x4 to 6x6
    grid = [[0] * size for _ in range(size)]
    # Add some walls
    wall_count = size * size // 4
    for _ in range(wall_count):
        r, c = random.randint(0, size - 1), random.randint(0, size - 1)
        if (r, c) != (0, 0) and (r, c) != (size - 1, size - 1):
            grid[r][c] = 1

    # Ensure path exists (simple: clear a path)
    for i in range(size):
        grid[0][i] = 0  # top row clear
        grid[i][size - 1] = 0  # right column clear

    return {
        "text": "Help Wukong find the way!",
        "visual_objects": [],
        "options": [],
        "correct_answer": [size - 1, size - 1],
        "grid": grid,
        "start": [0, 0],
        "end": [size - 1, size - 1],
    }


# ---------------------------------------------------------------------------
# Main generator
# ---------------------------------------------------------------------------

GENERATORS = {
    "counting": gen_counting,
    "addition": gen_addition,
    "subtraction": gen_subtraction,
    "comparison": gen_comparison,
    "ordering": gen_ordering,
    "pattern": gen_pattern,
    "shape_pattern": gen_shape_pattern,
    "clock_reading": gen_clock,
    "memory": gen_memory,
    "find_difference": gen_find_difference,
    "classification": gen_classification,
    "maze": gen_maze,
}

CHARACTERS = ["wukong", "pigsy", "sandy", "tripitaka"]
REWARD_DIALOGUES = [
    "Great job!", "Amazing!", "You're so smart!",
    "Wonderful!", "Keep going!", "The mountain is so pretty!",
    "Brilliant work!", "Wukong is proud of you!",
    "You did it!", "Fantastic!",
]


def generate_all_levels():
    all_levels = []

    for world_cfg in WORLDS:
        diff_lo, diff_hi = world_cfg["diff_range"]
        game_types = world_cfg["game_types"]

        for i in range(world_cfg["count"]):
            level_num = i + 1
            level_id = f"{world_cfg['prefix']}_{level_num:02d}"

            # Difficulty ramps within world
            frac = i / max(1, world_cfg["count"] - 1)
            difficulty = round(diff_lo + frac * (diff_hi - diff_lo))
            difficulty = max(diff_lo, min(diff_hi, difficulty))

            game_type = game_types[i] if i < len(game_types) else random.choice(game_types)

            # Generate question
            gen_func = GENERATORS[game_type]
            question = gen_func(world_cfg, difficulty)

            # Remove None values from question
            question = {k: v for k, v in question.items() if v is not None}

            level = {
                "id": level_id,
                "world": world_cfg["id"],
                "level_number": level_num,
                "name": world_cfg["names_en"][i] if i < len(world_cfg["names_en"]) else f"Level {level_num}",
                "story_intro": world_cfg["stories"][i] if i < len(world_cfg["stories"]) else "A new challenge awaits!",
                "character": random.choice(CHARACTERS),
                "game_type": game_type,
                "difficulty": difficulty,
                "question": question,
                "reward": {
                    "peaches": min(3, 1 + difficulty // 2),
                    "animation": "celebrate",
                    "dialogue": random.choice(REWARD_DIALOGUES),
                    "character": "wukong",
                },
                "hints": [
                    "Take your time and look carefully!",
                    "Try counting one by one.",
                ],
                "tags": [game_type, f"world_{world_cfg['prefix']}"],
            }

            all_levels.append(level)

    return all_levels


def print_stats(levels):
    from collections import Counter
    print(f"\nTotal levels: {len(levels)}")

    # By world
    worlds = {}
    for l in levels:
        w = l["world"]
        if w not in worlds:
            worlds[w] = []
        worlds[w].append(l)

    for w, wl in worlds.items():
        avg_d = sum(l["difficulty"] for l in wl) / len(wl)
        types = Counter(l["game_type"] for l in wl)
        opts = [len(l["question"].get("options", [])) for l in wl if l["question"].get("options")]
        avg_opts = sum(opts) / len(opts) if opts else 0
        print(f"\n{w}: {len(wl)} levels, avg diff {avg_d:.1f}, avg options {avg_opts:.1f}")
        for t, c in sorted(types.items()):
            print(f"  {t}: {c}")

    # Pattern/shape proportion
    total_pattern = sum(1 for l in levels if l["game_type"] in ("pattern", "shape_pattern"))
    print(f"\nPattern + Shape Pattern: {total_pattern}/{len(levels)} ({total_pattern/len(levels)*100:.0f}%)")

    # Clock reading count
    total_clock = sum(1 for l in levels if l["game_type"] == "clock_reading")
    print(f"Clock Reading: {total_clock}/{len(levels)} ({total_clock/len(levels)*100:.0f}%)")


if __name__ == "__main__":
    levels = generate_all_levels()
    print_stats(levels)

    # Write to backend/data
    backend_path = Path(__file__).parent.parent / "data" / "levels.json"
    with open(backend_path, "w", encoding="utf-8") as f:
        json.dump(levels, f, indent=2, ensure_ascii=False)
    print(f"\nWritten to {backend_path}")

    # Copy to frontend/src/data
    frontend_path = Path(__file__).parent.parent.parent / "frontend" / "src" / "data" / "levels.json"
    shutil.copy2(backend_path, frontend_path)
    print(f"Copied to {frontend_path}")
