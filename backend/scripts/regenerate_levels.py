"""Regenerate all 400+ game levels with proper difficulty progression."""

import json
import random
import shutil
from pathlib import Path
from collections import Counter

random.seed(42)  # reproducible

# ---------------------------------------------------------------------------
# World configuration
# ---------------------------------------------------------------------------

WORLDS = [
    {
        "id": "flower_fruit_mountain",
        "prefix": "w1",
        "count": 70,
        "diff_range": (1, 2),
        "num_range": (1, 5),
        "options": 3,
        "objects": ["peach", "monkey", "banana", "flower", "coconut"],
        "game_types": (
            ["counting"] * 10
            + ["addition"] * 4
            + ["make_ten"] * 8
            + ["sight_words"] * 14
            + ["phonics"] * 14
            + ["pattern"] * 6
            + ["shape_pattern"] * 4
            + ["comparison"] * 4
            + ["number_sequence"] * 4
            + ["memory"] * 2
        ),
    },
    {
        "id": "dragon_palace",
        "prefix": "w2",
        "count": 68,
        "diff_range": (1, 2),
        "num_range": (1, 8),
        "options": 3,
        "objects": ["fish", "shell", "pearl", "gem", "coral"],
        "game_types": (
            ["counting"] * 4
            + ["sight_words"] * 10
            + ["phonics"] * 10
            + ["pattern"] * 6
            + ["shape_pattern"] * 6
            + ["memory"] * 4
            + ["classification"] * 4
            + ["find_difference"] * 4
            + ["clock_reading"] * 2
            + ["ordering"] * 4
            + ["number_sequence"] * 4
            + ["make_ten"] * 4
            + ["general_knowledge"] * 4
            + ["phonics"] * 2
        ),
    },
    {
        "id": "heaven_palace",
        "prefix": "w3",
        "count": 70,
        "diff_range": (2, 3),
        "num_range": (1, 10),
        "options": 4,
        "objects": ["star", "cloud", "gem", "moon", "lantern"],
        "game_types": (
            ["addition"] * 6
            + ["subtraction"] * 4
            + ["sudoku"] * 6
            + ["number_sequence"] * 8
            + ["clock_reading"] * 6
            + ["shape_pattern"] * 6
            + ["pattern"] * 4
            + ["sight_words"] * 6
            + ["phonics"] * 4
            + ["comparison"] * 4
            + ["ordering"] * 2
            + ["maze"] * 4
            + ["mirror_symmetry"] * 4
            + ["general_knowledge"] * 4
            + ["make_ten"] * 2
        ),
    },
    {
        "id": "white_bone_cave",
        "prefix": "w4",
        "count": 68,
        "diff_range": (2, 4),
        "num_range": (5, 15),
        "options": 4,
        "objects": ["bone", "mask", "mirror", "candle", "scroll"],
        "game_types": (
            ["subtraction"] * 6
            + ["addition"] * 4
            + ["sudoku"] * 6
            + ["mirror_symmetry"] * 8
            + ["shape_pattern"] * 6
            + ["pattern"] * 4
            + ["clock_reading"] * 4
            + ["classification"] * 4
            + ["memory"] * 4
            + ["general_knowledge"] * 6
            + ["sight_words"] * 4
            + ["number_sequence"] * 4
            + ["find_difference"] * 4
            + ["make_ten"] * 4
        ),
    },
    {
        "id": "flaming_mountain",
        "prefix": "w5",
        "count": 62,
        "diff_range": (3, 4),
        "num_range": (5, 18),
        "options": 4,
        "objects": ["flame", "fan", "rock", "ember", "spark"],
        "game_types": (
            ["addition"] * 4
            + ["subtraction"] * 4
            + ["pattern"] * 4
            + ["shape_pattern"] * 6
            + ["clock_reading"] * 4
            + ["ordering"] * 4
            + ["maze"] * 4
            + ["number_sequence"] * 6
            + ["sudoku"] * 6
            + ["mirror_symmetry"] * 6
            + ["general_knowledge"] * 6
            + ["make_ten"] * 4
            + ["sight_words"] * 2
            + ["phonics"] * 2
        ),
    },
    {
        "id": "journey_road",
        "prefix": "w6",
        "count": 62,
        "diff_range": (3, 5),
        "num_range": (10, 20),
        "options": 4,
        "objects": ["scroll", "staff", "hat", "gem", "star"],
        "game_types": (
            ["addition"] * 4
            + ["subtraction"] * 4
            + ["pattern"] * 4
            + ["shape_pattern"] * 6
            + ["clock_reading"] * 4
            + ["comparison"] * 4
            + ["ordering"] * 2
            + ["maze"] * 2
            + ["sudoku"] * 6
            + ["mirror_symmetry"] * 6
            + ["number_sequence"] * 4
            + ["general_knowledge"] * 6
            + ["make_ten"] * 4
            + ["sight_words"] * 4
            + ["phonics"] * 2
        ),
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
# Story and name templates
# ---------------------------------------------------------------------------

STORY_TEMPLATES = {
    "counting": [
        "Wukong sees some {obj}s. How many are there?",
        "Help Wukong count the {obj}s!",
        "There are {obj}s everywhere! Count them all.",
        "How many {obj}s can you find?",
        "Wukong needs to count {obj}s for his quest.",
        "Look carefully and count the {obj}s!",
        "The {obj}s are hiding. Can you count them?",
        "Wukong is collecting {obj}s. How many does he have?",
    ],
    "addition": [
        "Wukong found more {obj}s! Add them up.",
        "Help Wukong add the {obj}s together!",
        "Two groups of {obj}s need to be combined.",
        "Wukong is collecting {obj}s. How many in total?",
        "Add these {obj}s and find the answer!",
        "The {obj}s are joining together!",
        "More {obj}s arrived! What's the total?",
        "Wukong's {obj}s are growing in number!",
    ],
    "subtraction": [
        "Some {obj}s flew away! How many are left?",
        "Wukong lost some {obj}s. How many remain?",
        "The {obj}s are disappearing! What's left?",
        "Help figure out how many {obj}s remain.",
        "Some {obj}s vanished! Solve the puzzle.",
        "A few {obj}s went missing from the pile.",
        "Wukong gave away some {obj}s. How many now?",
        "The wind blew some {obj}s away!",
    ],
    "comparison": [
        "Which group of {obj}s is bigger?",
        "Compare the {obj}s! Which side has more?",
        "Wukong needs to find the bigger group of {obj}s.",
        "Look at both groups of {obj}s carefully.",
        "Help Wukong compare these {obj}s!",
        "Which pile of {obj}s has more?",
    ],
    "ordering": [
        "Put the {obj}s in order!",
        "Help Wukong sort the numbers.",
        "Arrange from smallest to biggest!",
        "Can you order these {obj}s by size?",
        "Line up the numbers in the right order!",
        "Wukong needs help sorting these numbers.",
    ],
    "pattern": [
        "Wukong found a pattern with {obj}s! What comes next?",
        "The {obj}s follow a pattern. Can you see it?",
        "Complete the {obj} pattern!",
        "What's the next {obj} in the sequence?",
        "The magical {obj} pattern needs your help!",
        "Look at the {obj}s and find the pattern!",
        "A mysterious pattern of {obj}s appeared.",
        "Help Wukong finish the {obj} pattern!",
    ],
    "shape_pattern": [
        "The shapes follow a pattern! What comes next?",
        "Wukong found colorful shapes in a pattern.",
        "Complete the shape pattern!",
        "What shape comes next?",
        "Look at the shapes and find the pattern!",
        "A magical shape pattern appeared.",
        "Help finish the shape sequence!",
        "Can you see what shape is missing?",
    ],
    "clock_reading": [
        "What time does the {obj} clock show?",
        "Wukong needs to read the clock!",
        "Help tell the time on this clock.",
        "The magical clock shows a time. What is it?",
        "Can you read this clock for Wukong?",
        "Time is ticking! What does the clock say?",
    ],
    "memory": [
        "Remember where the {obj}s are hiding!",
        "Find the matching {obj} pairs!",
        "Wukong's memory challenge with {obj}s!",
        "Can you match all the {obj} pairs?",
        "Test your memory with these {obj}s!",
        "The {obj}s are playing hide and seek!",
    ],
    "find_difference": [
        "Something changed! Find the difference.",
        "Look carefully at the {obj}s. What's different?",
        "Spot what changed in the {obj} scene!",
        "One {obj} is not like before. Find it!",
        "Wukong sees something different. Can you?",
        "Compare the two scenes with {obj}s!",
    ],
    "classification": [
        "Sort the {obj}s into the right groups!",
        "Help Wukong organize the {obj}s!",
        "Which {obj}s belong together?",
        "Group the items correctly!",
        "Wukong needs help sorting things.",
        "Put each {obj} in the right category!",
    ],
    "maze": [
        "Help Wukong find the way through the maze!",
        "Guide Wukong through the twisting paths!",
        "The maze is tricky! Can you solve it?",
        "Find the path to the {obj}!",
        "Navigate the maze to help Wukong!",
        "A maze blocks the way! Help Wukong through.",
    ],
    "sight_words": [
        "Wukong finds a {obj}. Can you read the word?",
        "Help Wukong learn new words about {obj}s!",
        "What word matches this picture?",
        "Read the word and pick the right one!",
        "Wukong is learning to read! Help him!",
        "Match the picture to the correct word.",
        "Can you find the right word for Wukong?",
        "Words are magical! Read them with Wukong.",
    ],
    "phonics": [
        "What letter does this word start with?",
        "Listen to the sound! What letter is it?",
        "Wukong hears a sound. What letter makes it?",
        "Help Wukong learn letter sounds!",
        "What sound does this {obj} start with?",
        "Match the sound to the right letter!",
        "The {obj} starts with which letter?",
        "Wukong is learning phonics! Help him!",
    ],
    "make_ten": [
        "Help Wukong make 10 with {obj}s!",
        "What number goes with this to make 10?",
        "Fill in the missing number to reach 10!",
        "Wukong needs 10 {obj}s. How many more?",
        "Complete the pair that makes 10!",
        "The {obj}s need a friend to make 10!",
        "Find the number that adds up to 10!",
        "Make 10! Wukong believes in you!",
    ],
    "number_sequence": [
        "What number comes next in the pattern?",
        "Help Wukong complete the number sequence!",
        "The numbers follow a rule. Find the missing one!",
        "Fill in the missing number!",
        "Wukong sees a number pattern. What's missing?",
        "Complete the number sequence!",
        "The {obj}s are numbered. What comes next?",
        "Find the pattern in these numbers!",
    ],
    "sudoku": [
        "Help Wukong solve the number puzzle!",
        "Each row and column needs 1, 2, 3, and 4!",
        "Fill in the missing numbers!",
        "Wukong found a number grid puzzle!",
        "Complete the grid so no number repeats!",
        "A tricky number puzzle for Wukong!",
        "Solve the {obj} sudoku puzzle!",
        "Can you fill in all the missing numbers?",
    ],
    "mirror_symmetry": [
        "Which image is the mirror reflection?",
        "Wukong looks in a {obj}. What does he see?",
        "Find the correct mirror image!",
        "The {obj} has a reflection. Which one is right?",
        "Help Wukong find the mirror match!",
        "Which one is the correct flip?",
        "Look at the pattern and find its mirror!",
        "Wukong sees a reflection. Pick the right one!",
    ],
    "general_knowledge": [
        "Wukong has a question for you!",
        "Answer this question to help Wukong!",
        "Test your knowledge with Wukong!",
        "Wukong is curious! Do you know the answer?",
        "A fun question from Wukong!",
        "Help Wukong learn about the world!",
        "Wukong wants to know the answer!",
        "Can you answer Wukong's question?",
    ],
}

NAME_TEMPLATES = {
    "counting": ["Counting Fun", "Count the {obj}s", "How Many {obj}s?", "{obj} Counting", "Number Hunt", "Count Along"],
    "addition": ["Adding Up", "Plus {obj}s", "Addition Quest", "{obj} Addition", "Sum Fun", "Add Together"],
    "subtraction": ["Take Away", "Minus {obj}s", "Subtraction Quest", "{obj} Subtraction", "What's Left?", "Subtract Fun"],
    "comparison": ["Which Is More?", "Compare {obj}s", "Bigger Group", "{obj} Compare", "More or Less"],
    "ordering": ["In Order", "Sort Numbers", "Line Them Up", "{obj} Order", "Smallest to Biggest"],
    "pattern": ["Pattern Quest", "{obj} Patterns", "What Comes Next?", "Pattern Fun", "Sequence Magic", "Pattern Puzzle"],
    "shape_pattern": ["Shape Patterns", "Color Shapes", "Shape Sequence", "Shape Magic", "Shape Quest"],
    "clock_reading": ["Tell the Time", "Clock Reading", "What Time?", "Time Quest", "Clock Challenge"],
    "memory": ["Memory Match", "{obj} Memory", "Find the Pairs", "Memory Quest", "Match Up"],
    "find_difference": ["Spot the Difference", "What Changed?", "{obj} Difference", "Sharp Eyes", "Find It"],
    "classification": ["Sort It Out", "Group the {obj}s", "Category Quest", "Sorting Fun", "Organize"],
    "maze": ["Maze Runner", "Find the Way", "Path Quest", "Maze Adventure", "Navigate"],
    "sight_words": ["Word Discovery", "Reading {obj}", "Word Match", "Spelling Fun", "Word Quest", "Read Along"],
    "phonics": ["Letter Sounds", "Phonics Fun", "Sound Match", "ABC Sounds", "Letter Quest", "Sound It Out"],
    "make_ten": ["Make Ten", "Ten Quest", "Perfect Ten", "Add to Ten", "Ten Match", "Making Ten"],
    "number_sequence": ["Number Pattern", "Sequence Quest", "Missing Number", "Number Chain", "Count Pattern"],
    "sudoku": ["Number Grid", "Sudoku Fun", "Grid Quest", "Number Puzzle", "Fill the Grid", "Puzzle Time"],
    "mirror_symmetry": ["Mirror Match", "Flip It", "Symmetry Quest", "Mirror Image", "Reflection Fun"],
    "general_knowledge": ["Fun Facts", "Wukong Asks", "Knowledge Quest", "Brain Teaser", "Quick Quiz", "Think Fast"],
}

# ---------------------------------------------------------------------------
# Word banks for sight_words and phonics
# ---------------------------------------------------------------------------

SIGHT_WORDS_TIER1 = [
    ("apple", "\U0001f34e"), ("cat", "\U0001f431"), ("dog", "\U0001f436"), ("ball", "\u26bd"),
    ("bear", "\U0001f43b"), ("bird", "\U0001f426"), ("book", "\U0001f4da"), ("bus", "\U0001f68c"),
    ("cake", "\U0001f382"), ("car", "\U0001f697"), ("cup", "\u2615"), ("cow", "\U0001f404"),
    ("duck", "\U0001f986"), ("egg", "\U0001f95a"), ("fish", "\U0001f41f"), ("frog", "\U0001f438"),
    ("hand", "\u270b"), ("hat", "\U0001f3a9"), ("horse", "\U0001f434"), ("house", "\U0001f3e0"),
    ("ice", "\U0001f9ca"), ("juice", "\U0001f9c3"), ("key", "\U0001f511"), ("kite", "\U0001fa81"),
    ("leaf", "\U0001f343"), ("lion", "\U0001f981"), ("milk", "\U0001f95b"), ("moon", "\U0001f319"),
    ("nest", "\U0001faba"), ("orange", "\U0001f34a"), ("pen", "\U0001f58a\ufe0f"), ("pig", "\U0001f437"),
    ("rain", "\U0001f327\ufe0f"), ("ring", "\U0001f48d"), ("rose", "\U0001f339"), ("ship", "\U0001f6a2"),
    ("shoe", "\U0001f45f"), ("snake", "\U0001f40d"), ("sun", "\u2600\ufe0f"), ("tree", "\U0001f333"),
    ("van", "\U0001f690"), ("water", "\U0001f4a7"), ("whale", "\U0001f40b"), ("zebra", "\U0001f993"),
    ("star", "\u2b50"), ("bell", "\U0001f514"), ("drum", "\U0001fa98"), ("lamp", "\U0001f4a1"),
    ("boat", "\u26f5"), ("door", "\U0001f6aa"),
]

SIGHT_WORDS_TIER2_SENTENCES = [
    ("I ___ a cat.", "see", ["see", "the", "is", "can"]),
    ("The dog ___ big.", "is", ["is", "am", "see", "to"]),
    ("I ___ run fast.", "can", ["can", "the", "is", "see"]),
    ("She has ___ apple.", "an", ["an", "a", "is", "the"]),
    ("We ___ to school.", "go", ["go", "is", "an", "do"]),
    ("He ___ a book.", "has", ["has", "is", "the", "can"]),
    ("They ___ happy.", "are", ["are", "is", "an", "the"]),
    ("I like ___ play.", "to", ["to", "is", "an", "go"]),
    ("___ cat is small.", "The", ["The", "An", "Is", "Go"]),
    ("She can ___ well.", "run", ["run", "is", "the", "an"]),
    ("I ___ you.", "like", ["like", "the", "is", "go"]),
    ("He is ___ tall boy.", "a", ["a", "an", "is", "the"]),
    ("We ___ at home.", "are", ["are", "is", "an", "go"]),
    ("Look ___ the bird!", "at", ["at", "is", "to", "an"]),
    ("She ___ not here.", "is", ["is", "are", "can", "go"]),
    ("I ___ a new hat.", "have", ["have", "has", "is", "the"]),
    ("It ___ cold today.", "is", ["is", "am", "are", "to"]),
    ("Come ___ me.", "with", ["with", "is", "to", "an"]),
    ("We play ___ the park.", "in", ["in", "is", "on", "at"]),
    ("Do you ___ me?", "see", ["see", "is", "go", "to"]),
]

PHONICS_LETTER_BANK = {
    "B": [("ball", "\u26bd"), ("bear", "\U0001f43b"), ("bird", "\U0001f426")],
    "C": [("cat", "\U0001f431"), ("car", "\U0001f697"), ("cake", "\U0001f382")],
    "D": [("dog", "\U0001f436"), ("duck", "\U0001f986"), ("door", "\U0001f6aa")],
    "F": [("fish", "\U0001f41f"), ("frog", "\U0001f438"), ("flower", "\U0001f33a")],
    "G": [("goat", "\U0001f410"), ("grape", "\U0001f347"), ("gift", "\U0001f381")],
    "H": [("hat", "\U0001f3a9"), ("horse", "\U0001f434"), ("house", "\U0001f3e0")],
    "K": [("key", "\U0001f511"), ("kite", "\U0001fa81"), ("king", "\U0001f451")],
    "L": [("lion", "\U0001f981"), ("leaf", "\U0001f343"), ("lamp", "\U0001f4a1")],
    "M": [("moon", "\U0001f319"), ("milk", "\U0001f95b"), ("mouse", "\U0001f42d")],
    "N": [("nest", "\U0001faba"), ("nut", "\U0001f330"), ("nose", "\U0001f443")],
    "P": [("pig", "\U0001f437"), ("pen", "\U0001f58a\ufe0f"), ("pizza", "\U0001f355")],
    "R": [("rain", "\U0001f327\ufe0f"), ("rose", "\U0001f339"), ("ring", "\U0001f48d")],
    "S": [("sun", "\u2600\ufe0f"), ("star", "\u2b50"), ("snake", "\U0001f40d")],
    "T": [("tree", "\U0001f333"), ("turtle", "\U0001f422"), ("tent", "\u26fa")],
    "A": [("apple", "\U0001f34e"), ("ant", "\U0001f41c"), ("arrow", "\u27a1\ufe0f")],
    "E": [("egg", "\U0001f95a"), ("elephant", "\U0001f418"), ("ear", "\U0001f442")],
    "I": [("ice", "\U0001f9ca"), ("igloo", "\U0001f3d8\ufe0f"), ("insect", "\U0001f41b")],
    "O": [("orange", "\U0001f34a"), ("owl", "\U0001f989"), ("octopus", "\U0001f419")],
    "U": [("umbrella", "\u2602\ufe0f"), ("unicorn", "\U0001f984"), ("up", "\u2b06\ufe0f")],
    "W": [("whale", "\U0001f40b"), ("water", "\U0001f4a7"), ("watch", "\u231a")],
    "Z": [("zebra", "\U0001f993"), ("zero", "0\ufe0f\u20e3"), ("zoo", "\U0001f9f8")],
}

PHONICS_CONSONANTS = ["B", "C", "D", "F", "G", "H", "K", "L", "M", "N", "P", "R", "S", "T"]
PHONICS_VOWELS = ["A", "E", "I", "O", "U"]
PHONICS_BLENDS = {
    "sh": [("ship", "\U0001f6a2"), ("shoe", "\U0001f45f"), ("shell", "\U0001f41a")],
    "ch": [("cheese", "\U0001f9c0"), ("chair", "\U0001fa91"), ("cherry", "\U0001f352")],
    "th": [("thumb", "\U0001f44d"), ("three", "3\ufe0f\u20e3"), ("think", "\U0001f4ad")],
    "wh": [("whale", "\U0001f40b"), ("wheel", "\u2699\ufe0f"), ("whistle", "\U0001f3b6")],
}

# ---------------------------------------------------------------------------
# General knowledge question bank
# ---------------------------------------------------------------------------

GK_QUESTIONS = [
    {"q": "How many days are in a week?", "a": "7", "opts": ["5", "6", "7", "8"]},
    {"q": "What day comes after Monday?", "a": "Tuesday", "opts": ["Sunday", "Tuesday", "Wednesday", "Friday"]},
    {"q": "What day comes after Friday?", "a": "Saturday", "opts": ["Thursday", "Saturday", "Sunday", "Monday"]},
    {"q": "What day comes before Wednesday?", "a": "Tuesday", "opts": ["Monday", "Tuesday", "Thursday", "Friday"]},
    {"q": "What is the first day of the week?", "a": "Sunday", "opts": ["Monday", "Sunday", "Saturday", "Friday"]},
    {"q": "What is the last day of the week?", "a": "Saturday", "opts": ["Friday", "Saturday", "Sunday", "Monday"]},
    {"q": "How many months are in a year?", "a": "12", "opts": ["10", "11", "12", "14"]},
    {"q": "What month comes after March?", "a": "April", "opts": ["February", "April", "May", "June"]},
    {"q": "What month comes after June?", "a": "July", "opts": ["May", "July", "August", "June"]},
    {"q": "What is the first month of the year?", "a": "January", "opts": ["January", "March", "December", "February"]},
    {"q": "What is the last month of the year?", "a": "December", "opts": ["November", "December", "January", "October"]},
    {"q": "What month comes before May?", "a": "April", "opts": ["March", "April", "June", "July"]},
    {"q": "What season comes after winter?", "a": "Spring", "opts": ["Summer", "Spring", "Fall", "Winter"]},
    {"q": "In what season do leaves fall?", "a": "Fall", "opts": ["Spring", "Summer", "Fall", "Winter"]},
    {"q": "What season is the hottest?", "a": "Summer", "opts": ["Spring", "Summer", "Fall", "Winter"]},
    {"q": "What season is the coldest?", "a": "Winter", "opts": ["Spring", "Summer", "Fall", "Winter"]},
    {"q": "In what season do flowers bloom?", "a": "Spring", "opts": ["Spring", "Summer", "Fall", "Winter"]},
    {"q": "The sun rises in the ___", "a": "East", "opts": ["North", "South", "East", "West"]},
    {"q": "Which direction is opposite to North?", "a": "South", "opts": ["East", "West", "South", "North"]},
    {"q": "The sun sets in the ___", "a": "West", "opts": ["North", "South", "East", "West"]},
    {"q": "How many fingers on one hand?", "a": "5", "opts": ["4", "5", "6", "10"]},
    {"q": "How many fingers on two hands?", "a": "10", "opts": ["8", "10", "12", "5"]},
    {"q": "How many legs does a spider have?", "a": "8", "opts": ["6", "8", "10", "4"]},
    {"q": "How many legs does a fish have?", "a": "0", "opts": ["0", "2", "4", "6"]},
    {"q": "How many legs does a dog have?", "a": "4", "opts": ["2", "4", "6", "8"]},
    {"q": "What animal says 'moo'?", "a": "Cow", "opts": ["Dog", "Cat", "Cow", "Pig"]},
    {"q": "What animal says 'woof'?", "a": "Dog", "opts": ["Dog", "Cat", "Cow", "Duck"]},
    {"q": "What animal says 'meow'?", "a": "Cat", "opts": ["Dog", "Cat", "Bird", "Frog"]},
    {"q": "What animal says 'quack'?", "a": "Duck", "opts": ["Frog", "Duck", "Bird", "Fish"]},
    {"q": "What color is the sky on a sunny day?", "a": "Blue", "opts": ["Red", "Blue", "Green", "Yellow"]},
    {"q": "What color is grass?", "a": "Green", "opts": ["Red", "Blue", "Green", "Yellow"]},
    {"q": "What color is the sun?", "a": "Yellow", "opts": ["Red", "Blue", "Green", "Yellow"]},
    {"q": "What color is snow?", "a": "White", "opts": ["Blue", "White", "Gray", "Yellow"]},
    {"q": "How many eyes do you have?", "a": "2", "opts": ["1", "2", "3", "4"]},
    {"q": "How many ears do you have?", "a": "2", "opts": ["1", "2", "3", "4"]},
    {"q": "How many noses do you have?", "a": "1", "opts": ["1", "2", "3", "0"]},
    {"q": "What is the capital of Canada?", "a": "Ottawa", "opts": ["Toronto", "Ottawa", "Vancouver", "Montreal"]},
    {"q": "What leaf is on the Canadian flag?", "a": "Maple", "opts": ["Oak", "Maple", "Pine", "Birch"]},
    {"q": "What color is the Canadian flag?", "a": "Red and White", "opts": ["Red and Blue", "Red and White", "Blue and White", "Green and White"]},
    {"q": "What ocean is on Canada's west coast?", "a": "Pacific", "opts": ["Atlantic", "Pacific", "Arctic", "Indian"]},
    {"q": "How many sides does a triangle have?", "a": "3", "opts": ["2", "3", "4", "5"]},
    {"q": "How many sides does a square have?", "a": "4", "opts": ["3", "4", "5", "6"]},
    {"q": "What shape is a ball?", "a": "Circle", "opts": ["Square", "Triangle", "Circle", "Star"]},
    {"q": "How many hours in a day?", "a": "24", "opts": ["12", "20", "24", "30"]},
]

# ---------------------------------------------------------------------------
# Generator helpers
# ---------------------------------------------------------------------------

def make_wrong_options(correct: int, count: int, lo: int, hi: int) -> list:
    """Generate `count` unique wrong integer options near the correct answer."""
    wrongs = set()
    candidates = list(range(max(lo, correct - 3), min(hi + 1, correct + 4)))
    candidates = [c for c in candidates if c != correct]
    random.shuffle(candidates)
    for c in candidates:
        wrongs.add(c)
        if len(wrongs) >= count:
            break
    r = 4
    while len(wrongs) < count:
        r += 1
        for c in [correct - r, correct + r]:
            if lo <= c <= hi and c != correct and c not in wrongs:
                wrongs.add(c)
                if len(wrongs) >= count:
                    break
    return list(wrongs)[:count]


def make_time_options(correct: str, minute_step: int, count: int) -> list:
    """Generate wrong time options."""
    h, m = correct.split(":")
    hour, minute = int(h), int(m)
    wrongs = set()

    for dh in [1, -1, 2, -2, 3]:
        nh = ((hour - 1 + dh) % 12) + 1
        t = f"{nh}:{minute:02d}"
        if t != correct:
            wrongs.add(t)

    if minute_step > 0:
        for dm in [minute_step, -minute_step, minute_step * 2]:
            nm = (minute + dm) % 60
            t = f"{hour}:{nm:02d}"
            if t != correct:
                wrongs.add(t)

    return random.sample(list(wrongs), min(count, len(wrongs)))


def pick_story(game_type, obj):
    """Pick a random story template and fill in the object."""
    templates = STORY_TEMPLATES.get(game_type, ["A new challenge awaits!"])
    return random.choice(templates).format(obj=obj)


def pick_name(game_type, obj):
    """Pick a random name template and fill in the object."""
    templates = NAME_TEMPLATES.get(game_type, ["Challenge"])
    return random.choice(templates).format(obj=obj.capitalize())


# ---------------------------------------------------------------------------
# Game type generators - EXISTING
# ---------------------------------------------------------------------------

def gen_counting(world_cfg, difficulty):
    lo, hi = world_cfg["num_range"]
    n_opts = world_cfg["options"]
    objs = world_cfg["objects"]

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
        a, b = b, a

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
    n = min(4, 3 + (difficulty - 1))
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
        a, b = random.sample(objs, 2)
        seq = [a, b, a, b, a, b, "?"]
        answer = a
        wrong_pool = [o for o in objs if o != answer]
    elif difficulty <= 3:
        items = random.sample(objs, min(3, len(objs)))
        seq = items * 2 + ["?"]
        answer = items[0]
        wrong_pool = [o for o in objs if o != answer]
    else:
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
        shape = random.choice(SHAPES)
        c1, c2 = random.sample(COLORS, 2)
        s1 = f"{c1}_{shape}"
        s2 = f"{c2}_{shape}"
        seq = [s1, s2, s1, s2, s1, "?"]
        answer = s2
        wrong_candidates = [f"{c}_{shape}" for c in COLORS if f"{c}_{shape}" != answer]
    elif difficulty <= 3:
        color = random.choice(COLORS)
        sh1, sh2 = random.sample(SHAPES, 2)
        s1 = f"{color}_{sh1}"
        s2 = f"{color}_{sh2}"
        seq = [s1, s2, s1, s2, s1, "?"]
        answer = s2
        wrong_candidates = [f"{color}_{s}" for s in SHAPES if f"{color}_{s}" != answer]
    else:
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
    n_pairs = min(3, 2 + (difficulty - 1))
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
    size = min(6, 4 + (difficulty - 1))
    grid = [[0] * size for _ in range(size)]
    wall_count = size * size // 4
    for _ in range(wall_count):
        r, c = random.randint(0, size - 1), random.randint(0, size - 1)
        if (r, c) != (0, 0) and (r, c) != (size - 1, size - 1):
            grid[r][c] = 1

    for i in range(size):
        grid[0][i] = 0
        grid[i][size - 1] = 0

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
# Game type generators - NEW
# ---------------------------------------------------------------------------

def gen_sight_words(world_cfg, difficulty):
    n_opts = world_cfg["options"]

    if difficulty <= 2:
        # Tier 1: match word to emoji
        word, emoji = random.choice(SIGHT_WORDS_TIER1)
        wrong_words = [w for w, e in SIGHT_WORDS_TIER1 if w != word]
        wrongs = random.sample(wrong_words, min(n_opts - 1, len(wrong_words)))
        options = wrongs + [word]
        random.shuffle(options)

        return {
            "text": f"What word matches this picture? {emoji}",
            "visual_objects": [word],
            "options": options,
            "correct_answer": word,
        }
    else:
        # Tier 2: fill in the blank sentence
        sentence, answer, all_opts = random.choice(SIGHT_WORDS_TIER2_SENTENCES)
        opts = all_opts[:]
        random.shuffle(opts)

        return {
            "text": sentence,
            "visual_objects": [],
            "options": opts,
            "correct_answer": answer,
        }


def gen_phonics(world_cfg, difficulty):
    n_opts = world_cfg["options"]

    if difficulty <= 2:
        # Consonant sounds
        letter = random.choice(PHONICS_CONSONANTS)
        word, emoji = random.choice(PHONICS_LETTER_BANK[letter])
        wrong_letters = [l for l in PHONICS_CONSONANTS if l != letter]
        wrongs = random.sample(wrong_letters, min(n_opts - 1, len(wrong_letters)))
        options = wrongs + [letter]
        random.shuffle(options)

        return {
            "text": f"What letter does {emoji} start with?",
            "visual_objects": [word],
            "options": options,
            "correct_answer": letter,
        }
    elif difficulty <= 3:
        # Vowel sounds
        letter = random.choice(PHONICS_VOWELS)
        word, emoji = random.choice(PHONICS_LETTER_BANK[letter])
        wrong_letters = [l for l in PHONICS_VOWELS if l != letter]
        wrongs = random.sample(wrong_letters, min(n_opts - 1, len(wrong_letters)))
        options = wrongs + [letter]
        random.shuffle(options)

        return {
            "text": f"What letter does {emoji} start with?",
            "visual_objects": [word],
            "options": options,
            "correct_answer": letter,
        }
    else:
        # Blends
        blend = random.choice(list(PHONICS_BLENDS.keys()))
        word, emoji = random.choice(PHONICS_BLENDS[blend])
        wrong_blends = [b for b in PHONICS_BLENDS if b != blend]
        wrongs = random.sample(wrong_blends, min(n_opts - 1, len(wrong_blends)))
        options = wrongs + [blend]
        random.shuffle(options)

        return {
            "text": f"What sound does {emoji} start with?",
            "visual_objects": [word],
            "options": options,
            "correct_answer": blend,
        }


def gen_make_ten(world_cfg, difficulty):
    n_opts = world_cfg["options"]

    if difficulty <= 3:
        # N + ? = 10
        n = random.randint(1, 9)
        answer = 10 - n
        wrongs = make_wrong_options(answer, n_opts - 1, 0, 10)
        options = wrongs + [answer]
        random.shuffle(options)

        return {
            "text": f"{n} + ? = 10",
            "visual_objects": [],
            "options": options,
            "correct_answer": answer,
        }
    else:
        # Which two numbers make 10?
        a = random.randint(1, 9)
        b = 10 - a
        correct_pair = f"{a} + {b}"

        wrong_pairs = []
        attempts = 0
        while len(wrong_pairs) < n_opts - 1 and attempts < 50:
            wa = random.randint(1, 9)
            wb = random.randint(1, 9)
            if wa + wb != 10:
                pair_str = f"{wa} + {wb}"
                if pair_str not in wrong_pairs and pair_str != correct_pair:
                    wrong_pairs.append(pair_str)
            attempts += 1

        options = wrong_pairs + [correct_pair]
        random.shuffle(options)

        return {
            "text": "Which two numbers make 10?",
            "visual_objects": [],
            "options": options,
            "correct_answer": correct_pair,
        }


def gen_number_sequence(world_cfg, difficulty):
    n_opts = world_cfg["options"]
    lo, hi = world_cfg["num_range"]

    if difficulty <= 2:
        # +1 or +2 sequences
        step = random.choice([1, 2])
        start = random.randint(lo, max(lo, hi - step * 6))
        length = random.randint(5, 7)
        seq = [start + step * i for i in range(length)]
        # Pick a position to hide (not first or last)
        hide_idx = random.randint(1, length - 2)
        answer = seq[hide_idx]
        display_seq = seq[:]
        display_seq[hide_idx] = "?"
    elif difficulty <= 3:
        # +3 or +5
        step = random.choice([3, 5])
        start = random.randint(lo, max(lo, hi - step * 5))
        length = random.randint(5, 6)
        seq = [start + step * i for i in range(length)]
        hide_idx = random.randint(1, length - 2)
        answer = seq[hide_idx]
        display_seq = seq[:]
        display_seq[hide_idx] = "?"
    else:
        # x2 or alternating +1/+2
        if random.random() < 0.5:
            # x2 sequence
            x2_lo = max(1, min(lo, 3))
            x2_hi = max(x2_lo, min(3, hi))
            start = random.randint(x2_lo, x2_hi)
            seq = []
            val = start
            for _ in range(5):
                seq.append(val)
                val = val * 2
                if val > 100:
                    break
            if len(seq) < 4:
                seq = [start + i for i in range(5)]
        else:
            # Alternating +1/+2
            start = random.randint(lo, max(lo, hi - 10))
            seq = [start]
            for i in range(5):
                step = 1 if i % 2 == 0 else 2
                seq.append(seq[-1] + step)

        hide_idx = random.randint(1, len(seq) - 2)
        answer = seq[hide_idx]
        display_seq = seq[:]
        display_seq[hide_idx] = "?"

    wrongs = make_wrong_options(answer, n_opts - 1, max(0, answer - 10), answer + 10)
    options = wrongs + [answer]
    random.shuffle(options)

    return {
        "text": "What number is missing in the sequence?",
        "visual_objects": [],
        "options": options,
        "correct_answer": answer,
        "sequence": display_seq,
    }


def gen_sudoku(world_cfg, difficulty):
    # Base valid 4x4 sudoku solution
    base = [
        [1, 2, 3, 4],
        [3, 4, 1, 2],
        [2, 1, 4, 3],
        [4, 3, 2, 1],
    ]

    # Randomly permute rows within each band (rows 0-1, rows 2-3)
    if random.random() < 0.5:
        base[0], base[1] = base[1], base[0]
    if random.random() < 0.5:
        base[2], base[3] = base[3], base[2]

    # Randomly permute columns within each stack (cols 0-1, cols 2-3)
    if random.random() < 0.5:
        for row in base:
            row[0], row[1] = row[1], row[0]
    if random.random() < 0.5:
        for row in base:
            row[2], row[3] = row[3], row[2]

    # Swap number labels randomly
    perm = list(range(1, 5))
    random.shuffle(perm)
    label_map = {i + 1: perm[i] for i in range(4)}
    solution = [[label_map[cell] for cell in row] for row in base]

    # Create puzzle by removing cells
    if difficulty <= 2:
        remove_count = random.randint(3, 4)
    elif difficulty <= 3:
        remove_count = random.randint(5, 6)
    else:
        remove_count = random.randint(7, 8)

    puzzle = [row[:] for row in solution]
    all_positions = [(r, c) for r in range(4) for c in range(4)]
    random.shuffle(all_positions)
    for r, c in all_positions[:remove_count]:
        puzzle[r][c] = 0

    return {
        "text": "Fill in the missing numbers! Each row, column, and box must have 1, 2, 3, 4.",
        "visual_objects": [],
        "options": [1, 2, 3, 4],
        "correct_answer": 0,
        "grid": puzzle,
        "sudoku_solution": solution,
    }


def gen_mirror_symmetry(world_cfg, difficulty):
    if difficulty <= 3:
        # Horizontal flip, 3x3 grid
        size = 3
        grid = [[random.randint(0, 1) for _ in range(size)] for _ in range(size)]
        # Correct mirror: flip left-right (reverse each row)
        correct_mirror = [row[::-1] for row in grid]
    else:
        # Vertical flip, 4x4 grid
        size = 4
        grid = [[random.randint(0, 1) for _ in range(size)] for _ in range(size)]
        # Correct mirror: flip top-bottom (reverse row order)
        correct_mirror = grid[::-1]

    # Generate wrong candidates by flipping 1-2 random cells
    wrong_candidates = []
    for _ in range(3):
        candidate = [row[:] for row in correct_mirror]
        flips = random.randint(1, 2)
        for _ in range(flips):
            r = random.randint(0, size - 1)
            c = random.randint(0, size - 1)
            candidate[r][c] = 1 - candidate[r][c]
        # Make sure it's actually different from correct
        if candidate != correct_mirror:
            wrong_candidates.append(candidate)

    # Ensure we have at least 2 wrong candidates
    while len(wrong_candidates) < 2:
        candidate = [row[:] for row in correct_mirror]
        r = random.randint(0, size - 1)
        c = random.randint(0, size - 1)
        candidate[r][c] = 1 - candidate[r][c]
        if candidate != correct_mirror and candidate not in wrong_candidates:
            wrong_candidates.append(candidate)

    # Pick 2-3 wrong ones
    n_wrong = min(3, len(wrong_candidates))
    selected_wrong = random.sample(wrong_candidates, n_wrong)

    # Build mirror_options with correct answer at a random position
    mirror_options = selected_wrong[:]
    correct_idx = random.randint(0, len(mirror_options))
    mirror_options.insert(correct_idx, correct_mirror)

    flip_type = "horizontal" if difficulty <= 3 else "vertical"

    return {
        "text": f"Which is the correct {flip_type} mirror of this pattern?",
        "visual_objects": [],
        "options": list(range(len(mirror_options))),
        "correct_answer": correct_idx,
        "grid": grid,
        "mirror_options": mirror_options,
        "flip_type": flip_type,
    }


def gen_general_knowledge(world_cfg, difficulty):
    q_data = random.choice(GK_QUESTIONS)
    opts = q_data["opts"][:]
    random.shuffle(opts)

    return {
        "text": q_data["q"],
        "visual_objects": [],
        "options": opts,
        "correct_answer": q_data["a"],
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
    "sight_words": gen_sight_words,
    "phonics": gen_phonics,
    "make_ten": gen_make_ten,
    "number_sequence": gen_number_sequence,
    "sudoku": gen_sudoku,
    "mirror_symmetry": gen_mirror_symmetry,
    "general_knowledge": gen_general_knowledge,
}

CHARACTERS = ["wukong", "pigsy", "sandy", "tripitaka"]
REWARD_DIALOGUES = [
    "Great job!", "Amazing!", "You're so smart!",
    "Wonderful!", "Keep going!", "The mountain is so pretty!",
    "Brilliant work!", "Wukong is proud of you!",
    "You did it!", "Fantastic!",
]

HINT_BANK = {
    "counting": ["Count each one carefully!", "Point at each one as you count."],
    "addition": ["Try counting all of them together!", "Add the two groups."],
    "subtraction": ["Start with the big number and count down.", "Take away means subtract."],
    "comparison": ["Count each group and compare!", "Which group looks bigger?"],
    "ordering": ["Find the smallest one first.", "Look for the biggest number."],
    "pattern": ["Look at what repeats!", "Say the pattern out loud."],
    "shape_pattern": ["Look at the colors and shapes.", "What comes next in the pattern?"],
    "clock_reading": ["Look at where the hands point.", "The short hand shows the hour."],
    "memory": ["Try to remember the positions!", "Flip two cards at a time."],
    "find_difference": ["Look carefully at both pictures!", "Compare them side by side."],
    "classification": ["Think about what goes together.", "Sort them into groups!"],
    "maze": ["Try going one step at a time.", "Look for open paths!"],
    "sight_words": ["Look at the picture for a clue!", "Sound out the word slowly."],
    "phonics": ["Say the word out loud!", "What sound do you hear first?"],
    "make_ten": ["Think about how many more to get to 10.", "Use your fingers to help!"],
    "number_sequence": ["Look at how the numbers change.", "What is the rule?"],
    "sudoku": ["Each number can only appear once in each row.", "Check each column too!"],
    "mirror_symmetry": ["Imagine flipping the picture.", "A mirror shows the reverse!"],
    "general_knowledge": ["Think carefully about what you know!", "Take your time!"],
}


def generate_all_levels():
    all_levels = []

    for world_cfg in WORLDS:
        diff_lo, diff_hi = world_cfg["diff_range"]
        game_types = world_cfg["game_types"]

        # Shuffle game types to mix them within the world
        shuffled_types = game_types[:]
        random.shuffle(shuffled_types)

        for i in range(world_cfg["count"]):
            level_num = i + 1
            level_id = f"{world_cfg['prefix']}_{level_num:02d}"

            # Difficulty ramps within world
            frac = i / max(1, world_cfg["count"] - 1)
            difficulty = round(diff_lo + frac * (diff_hi - diff_lo))
            difficulty = max(diff_lo, min(diff_hi, difficulty))

            game_type = shuffled_types[i] if i < len(shuffled_types) else random.choice(shuffled_types)

            # Generate question
            gen_func = GENERATORS[game_type]
            question = gen_func(world_cfg, difficulty)

            # Remove None values from question
            question = {k: v for k, v in question.items() if v is not None}

            obj = random.choice(world_cfg["objects"])

            level = {
                "id": level_id,
                "world": world_cfg["id"],
                "level_number": level_num,
                "name": pick_name(game_type, obj),
                "story_intro": pick_story(game_type, obj),
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
                "hints": HINT_BANK.get(game_type, ["Take your time!", "Look carefully!"]),
                "tags": [game_type, f"world_{world_cfg['prefix']}"],
            }

            all_levels.append(level)

    return all_levels


def print_stats(levels):
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

    # Pattern + shape proportion
    total_pattern = sum(1 for l in levels if l["game_type"] in ("pattern", "shape_pattern"))
    print(f"\nPattern + Shape Pattern: {total_pattern}/{len(levels)} ({total_pattern / len(levels) * 100:.0f}%)")

    # English types proportion
    english_types = {"sight_words", "phonics"}
    total_english = sum(1 for l in levels if l["game_type"] in english_types)
    print(f"English (sight_words + phonics): {total_english}/{len(levels)} ({total_english / len(levels) * 100:.0f}%)")

    # New type counts
    new_types = {"sight_words", "phonics", "make_ten", "number_sequence", "mirror_symmetry", "sudoku", "general_knowledge"}
    new_counts = Counter(l["game_type"] for l in levels if l["game_type"] in new_types)
    print(f"\nNew game type counts:")
    for t, c in sorted(new_counts.items()):
        print(f"  {t}: {c}")

    # Clock reading count
    total_clock = sum(1 for l in levels if l["game_type"] == "clock_reading")
    print(f"\nClock Reading: {total_clock}/{len(levels)} ({total_clock / len(levels) * 100:.0f}%)")


if __name__ == "__main__":
    levels = generate_all_levels()
    print_stats(levels)

    # Write to backend/data
    backend_path = Path(__file__).parent.parent / "data" / "levels.json"
    backend_path.parent.mkdir(parents=True, exist_ok=True)
    with open(backend_path, "w", encoding="utf-8") as f:
        json.dump(levels, f, indent=2, ensure_ascii=False)
    print(f"\nWritten to {backend_path}")

    # Copy to frontend/src/data
    frontend_path = Path(__file__).parent.parent.parent / "frontend" / "src" / "data" / "levels.json"
    frontend_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(backend_path, frontend_path)
    print(f"Copied to {frontend_path}")
