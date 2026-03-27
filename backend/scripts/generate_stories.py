"""Generate 81 Journey to the West story adventures with story-relevant questions."""

import json
import random
import shutil
from pathlib import Path

random.seed(99)  # reproducible

# ---------------------------------------------------------------------------
# Reuse generators from regenerate_levels.py
# ---------------------------------------------------------------------------
import sys
sys.path.insert(0, str(Path(__file__).parent))
from regenerate_levels import (
    GENERATORS, SIGHT_WORDS_TIER1, PHONICS_LETTER_BANK, PHONICS_CONSONANTS,
    GK_QUESTIONS, HINT_BANK, make_wrong_options,
)

# ---------------------------------------------------------------------------
# 81 Tribulations with story-relevant question seeds
# ---------------------------------------------------------------------------
# Each scene has a "q" dict defining the question tied to the narration.
# Supported q types:
#   counting:    {"t":"counting", "text":..., "count":N, "obj":"emoji_key"}
#   addition:    {"t":"addition", "text":..., "a":N, "b":N, "obj_a":"...", "obj_b":"..."}
#   subtraction: {"t":"subtraction", "text":..., "a":N, "b":N, "obj":"..."}
#   comparison:  {"t":"comparison", "text":..., "left":[...], "right":[...]}
#   sight_words: {"t":"sight_words", "word":"...", "text":...}
#   phonics:     {"t":"phonics", "word":"...", "letter":"X"}
#   general_knowledge: {"t":"general_knowledge", "text":..., "options":[...], "correct_answer":...}
#   pattern:     {"t":"pattern"} — uses generator
#   make_ten:    {"t":"make_ten", "text":..., "a":N}
#   number_sequence: {"t":"number_sequence"} — uses generator
#   ordering:    {"t":"ordering", "text":..., "items":[...], "correct_order":[...]}
#   shape_pattern: {"t":"shape_pattern"} — uses generator
#   clock_reading: {"t":"clock_reading"} — uses generator
#   memory:      {"t":"memory"} — uses generator
#   maze:        {"t":"maze"} — uses generator
#   sudoku:      {"t":"sudoku"} — uses generator
#   mirror_symmetry: {"t":"mirror_symmetry"} — uses generator
#   classification: {"t":"classification", "text":..., "groups":{"A":[...], "B":[...]}}
#   find_difference: {"t":"find_difference"} — uses generator

TRIBULATIONS = [
    # =====================================================================
    # Tier 1: Flower Fruit Mountain (stories 1-14, difficulty 1)
    # =====================================================================
    {"num": 1, "title": "The Stone Monkey is Born", "title_cn": "石猴出世",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "Long ago, on top of a beautiful mountain, there was a magical stone. One day, the stone cracked open and a baby monkey jumped out!",
          "setting": "mountain peak with a glowing cracked stone, golden light, cherry blossoms",
          "q": {"t": "counting", "text": "How many monkeys jumped out of the stone?", "count": 1, "obj": "monkey"}},
         {"narration": "The baby monkey opened his eyes and looked around. He saw 2 trees and 3 flowers everywhere!",
          "setting": "lush mountain forest with waterfalls and colorful flowers",
          "q": {"t": "addition", "text": "The monkey saw 2 trees and 3 flowers. How many things did he see?", "a": 2, "b": 3, "obj_a": "tree", "obj_b": "flower"}},
         {"narration": "Other monkeys came running to see him. 5 monkeys gathered around the baby!",
          "setting": "group of monkeys gathered around baby monkey on mountain",
          "q": {"t": "counting", "text": "How many monkeys came to see the baby?", "count": 5, "obj": "monkey"}},
         {"narration": "The monkeys cheered and danced. They had a new friend! The stone monkey smiled and played with them.",
          "setting": "monkeys celebrating and dancing on a mountain meadow",
          "q": {"t": "sight_words", "word": "play", "text": "Which word means to have fun together?"}},
     ]},
    {"num": 2, "title": "King of the Monkeys", "title_cn": "美猴王",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "The monkeys found a beautiful waterfall. Behind it, there must be a cave! But who would dare jump through?",
          "setting": "monkeys standing before a massive waterfall on a mountain",
          "q": {"t": "phonics", "word": "jump", "letter": "j"}},
         {"narration": "The stone monkey bravely jumped through the waterfall! Splash! He found a wonderful cave inside.",
          "setting": "monkey jumping through a waterfall into a sparkling cave",
          "q": {"t": "general_knowledge", "text": "What did the monkey find behind the waterfall?", "options": ["A cave", "A tree", "A fish", "A cloud"], "correct_answer": "A cave"}},
         {"narration": "The cave had 3 stone chairs, 2 stone beds, and 1 stone table! It was a perfect home.",
          "setting": "inside a beautiful stone cave with natural furniture",
          "q": {"t": "addition", "text": "The cave had 3 chairs, 2 beds, and 1 table. How many stone things?", "a": 5, "b": 1, "obj_a": "chair", "obj_b": "table"}},
         {"narration": "The monkeys made him their king! From now on, he was called the Handsome Monkey King.",
          "setting": "monkey sitting on a stone throne with a crown, other monkeys bowing",
          "q": {"t": "sight_words", "word": "king", "text": "What word means the ruler of a kingdom?"}},
     ]},
    {"num": 3, "title": "Seeking Immortality", "title_cn": "拜师学艺",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "The Monkey King was worried. He didn't want to grow old. He decided to find a teacher who could teach him magic!",
          "setting": "monkey king looking thoughtful at sunset on mountain",
          "q": {"t": "general_knowledge", "text": "What did the Monkey King want to learn?", "options": ["Magic", "Cooking", "Swimming", "Painting"], "correct_answer": "Magic"}},
         {"narration": "He built a raft and sailed across the wide ocean. The waves were big, but he was brave!",
          "setting": "monkey on a small raft sailing across a vast ocean",
          "q": {"t": "phonics", "word": "raft", "letter": "r"}},
         {"narration": "After a long journey, he found Master Subhuti on a mountain. The master agreed to teach him!",
          "setting": "monkey kneeling before an old wise master in a temple",
          "q": {"t": "counting", "text": "How many teachers did the monkey find?", "count": 1, "obj": "star"}},
     ]},
    {"num": 4, "title": "Learning 72 Transformations", "title_cn": "学会七十二变",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "Master Subhuti taught Wukong many magical spells. Wukong studied hard every day!",
          "setting": "monkey studying scrolls in a temple classroom",
          "q": {"t": "sight_words", "word": "read", "text": "Which word means to look at and understand writing?"}},
         {"narration": "Wukong learned to transform into different things! He could become a bird, a fish, or even a tree!",
          "setting": "monkey surrounded by magical transformation clouds, showing bird and fish forms",
          "q": {"t": "counting", "text": "How many things can Wukong transform into? A bird, a fish, and a tree.", "count": 3, "obj": "star"}},
         {"narration": "He also learned to ride on clouds! One jump could take him very far!",
          "setting": "monkey joyfully flying on a golden cloud high in the sky",
          "q": {"t": "phonics", "word": "cloud", "letter": "c"}},
     ]},
    {"num": 5, "title": "Return to Flower Fruit Mountain", "title_cn": "重返花果山",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "Wukong flew back to Flower Fruit Mountain on his cloud. His monkey friends were so happy to see him!",
          "setting": "monkey flying on cloud towards a beautiful mountain",
          "q": {"t": "sight_words", "word": "home", "text": "Which word means the place where you live?"}},
         {"narration": "But a monster had taken over their cave! The monkeys were scared and hiding.",
          "setting": "monkeys hiding behind rocks, looking scared",
          "q": {"t": "general_knowledge", "text": "Why were the monkeys scared?", "options": ["A monster took their cave", "It was raining", "They were hungry", "It was dark"], "correct_answer": "A monster took their cave"}},
         {"narration": "Wukong was angry! He chased 4 small monsters and 1 big monster away!",
          "setting": "monkey king fighting a demon with magical golden light",
          "q": {"t": "addition", "text": "Wukong chased away 4 small monsters and 1 big monster. How many monsters?", "a": 4, "b": 1, "obj_a": "monster", "obj_b": "monster"}},
         {"narration": "The monkeys celebrated! Their king was back and stronger than ever!",
          "setting": "monkeys celebrating with fireworks on the mountain",
          "q": {"t": "phonics", "word": "strong", "letter": "s"}},
     ]},
    {"num": 6, "title": "The Magic Weapon", "title_cn": "寻找兵器",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "Wukong needed a weapon. He was strong, but he needed something special to fight monsters!",
          "setting": "monkey king practicing martial arts moves on a mountain",
          "q": {"t": "general_knowledge", "text": "What did Wukong need to fight monsters?", "options": ["A weapon", "A hat", "A boat", "A book"], "correct_answer": "A weapon"}},
         {"narration": "His monkey friends told him about the Dragon King who lived under the ocean. He had many magic weapons!",
          "setting": "monkeys pointing towards the ocean, with underwater palace visible",
          "q": {"t": "phonics", "word": "ocean", "letter": "o"}},
         {"narration": "Wukong dove into the ocean! He swam past 3 fish and 2 turtles to reach the Dragon Palace.",
          "setting": "monkey swimming down through clear blue ocean water",
          "q": {"t": "addition", "text": "Wukong swam past 3 fish and 2 turtles. How many sea animals?", "a": 3, "b": 2, "obj_a": "fish", "obj_b": "turtle"}},
     ]},
    {"num": 7, "title": "The Golden Staff", "title_cn": "如意金箍棒",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "In the Dragon Palace, Wukong tried many weapons. He tried 2 swords, 1 spear, and 1 axe — none felt right!",
          "setting": "monkey testing various weapons in an underwater armory",
          "q": {"t": "addition", "text": "Wukong tried 2 swords, 1 spear, and 1 axe. How many weapons did he try?", "a": 3, "b": 1, "obj_a": "sword", "obj_b": "axe"}},
         {"narration": "Then he saw a glowing pillar in the corner. It was the Ruyi Jingu Bang — a magical iron staff!",
          "setting": "glowing golden staff/pillar in an underwater palace, radiating light",
          "q": {"t": "sight_words", "word": "gold", "text": "Which word describes the color of the staff?"}},
         {"narration": "The staff could grow big or shrink small! Wukong shrunk it to the size of a needle and put it behind his ear.",
          "setting": "monkey holding a golden staff that glows, looking happy",
          "q": {"t": "general_knowledge", "text": "Where did Wukong put the tiny staff?", "options": ["Behind his ear", "In his pocket", "On his head", "In his shoe"], "correct_answer": "Behind his ear"}},
         {"narration": "The Dragon King was not happy, but Wukong flew away with his new weapon! Now he was ready for anything!",
          "setting": "monkey flying away from underwater palace on a cloud, staff in hand",
          "q": {"t": "phonics", "word": "fly", "letter": "f"}},
     ]},
    {"num": 8, "title": "Erasing Names from Death", "title_cn": "大闹地府",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "One night, 2 scary guards came to take Wukong to the Underworld. They said it was his time!",
          "setting": "two dark ghost guards approaching monkey at night",
          "q": {"t": "counting", "text": "How many guards came for Wukong?", "count": 2, "obj": "ghost"}},
         {"narration": "Wukong was not afraid! He followed them to the Underworld and found the Book of Life and Death.",
          "setting": "monkey in a dark palace looking at a large ancient book",
          "q": {"t": "sight_words", "word": "book", "text": "What did Wukong find in the Underworld?"}},
         {"narration": "He crossed out his name and all the monkeys' names from the book! Now they would live forever!",
          "setting": "monkey crossing out names in a glowing book with a brush",
          "q": {"t": "general_knowledge", "text": "What did Wukong cross out from the book?", "options": ["His name", "A picture", "A number", "A story"], "correct_answer": "His name"}},
     ]},
    {"num": 9, "title": "The Jade Emperor's Invitation", "title_cn": "天庭招安",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "The Jade Emperor in Heaven heard about Wukong. He was worried about this powerful monkey!",
          "setting": "jade emperor on golden throne in heavenly palace, looking concerned",
          "q": {"t": "general_knowledge", "text": "Where does the Jade Emperor live?", "options": ["In Heaven", "Under the sea", "In a cave", "On a cloud"], "correct_answer": "In Heaven"}},
         {"narration": "He sent 1 messenger to invite Wukong to Heaven. Maybe they could give him a job to keep him happy!",
          "setting": "heavenly messenger flying down to the mountain on a cloud",
          "q": {"t": "counting", "text": "How many messengers did the Emperor send?", "count": 1, "obj": "star"}},
         {"narration": "Wukong was excited! He flew up to Heaven on his cloud to see the beautiful palace.",
          "setting": "monkey flying through clouds towards a magnificent golden palace",
          "q": {"t": "phonics", "word": "heaven", "letter": "h"}},
     ]},
    {"num": 10, "title": "The Horse Keeper", "title_cn": "弼马温",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "The Jade Emperor gave Wukong a job — taking care of 5 heavenly horses!",
          "setting": "monkey in stable surrounded by beautiful white heavenly horses",
          "q": {"t": "counting", "text": "How many horses did Wukong take care of?", "count": 5, "obj": "horse"}},
         {"narration": "When Wukong found out it was a tiny, unimportant job, he was furious!",
          "setting": "angry monkey with flames around him in the heavenly stable",
          "q": {"t": "sight_words", "word": "angry", "text": "Which word means very mad?"}},
         {"narration": "He quit the job and flew back home. He called himself the Great Sage Equal to Heaven!",
          "setting": "monkey planting a flag on mountain that reads Great Sage Equal to Heaven",
          "q": {"t": "general_knowledge", "text": "What did Wukong call himself?", "options": ["Great Sage Equal to Heaven", "Horse King", "Dragon Master", "Star Prince"], "correct_answer": "Great Sage Equal to Heaven"}},
     ]},
    {"num": 11, "title": "Battle in Heaven", "title_cn": "大闹天宫",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "The Jade Emperor sent an army to capture Wukong! Many heavenly soldiers came down to the mountain.",
          "setting": "army of heavenly soldiers descending from clouds towards mountain",
          "q": {"t": "comparison", "text": "Who had more soldiers? The Emperor had 5, Wukong had 1.", "left": ["soldier", "soldier", "soldier", "soldier", "soldier"], "right": ["monkey"]}},
         {"narration": "But Wukong was too strong! He fought off all the soldiers with his golden staff.",
          "setting": "monkey king fighting soldiers in mid-air with golden staff, clouds everywhere",
          "q": {"t": "sight_words", "word": "fight", "text": "Which word means to battle someone?"}},
         {"narration": "No one in Heaven could defeat him! The Jade Emperor didn't know what to do.",
          "setting": "jade emperor worried on throne with defeated soldiers returning",
          "q": {"t": "phonics", "word": "staff", "letter": "s"}},
     ]},
    {"num": 12, "title": "Peach Garden Feast", "title_cn": "偷吃蟠桃",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "To keep Wukong happy, they gave him a new job: guarding the Peach Garden. There were 5 magical peach trees!",
          "setting": "beautiful garden full of giant glowing peach trees",
          "q": {"t": "counting", "text": "How many peach trees were in the garden?", "count": 5, "obj": "peach"}},
         {"narration": "But Wukong couldn't resist! He ate 3 magical peaches. Each one made him even more powerful!",
          "setting": "monkey happily eating glowing peaches in a magical garden",
          "q": {"t": "subtraction", "text": "There were 5 peaches. Wukong ate 3. How many are left?", "a": 5, "b": 3, "obj": "peach"}},
         {"narration": "When the fairies came to pick peaches for the party, they found most were gone! Wukong was in big trouble!",
          "setting": "fairies looking at empty peach trees in shock",
          "q": {"t": "sight_words", "word": "eat", "text": "Which word means to put food in your mouth?"}},
     ]},
    {"num": 13, "title": "Laozi's Furnace", "title_cn": "炼丹炉",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "They finally caught Wukong and put him in Laozi's magical furnace. The fire burned for 49 days!",
          "setting": "monkey trapped inside a giant bronze furnace with flames",
          "q": {"t": "general_knowledge", "text": "How long was Wukong in the furnace?", "options": ["49 days", "7 days", "1 day", "100 days"], "correct_answer": "49 days"}},
         {"narration": "But instead of being destroyed, Wukong became even stronger! He got special golden eyes that could see through any disguise!",
          "setting": "monkey emerging from furnace with glowing golden eyes, surrounded by smoke",
          "q": {"t": "phonics", "word": "fire", "letter": "f"}},
         {"narration": "He broke free and caused even more chaos in Heaven! Nobody could stop him!",
          "setting": "monkey breaking through palace walls with incredible power",
          "q": {"t": "sight_words", "word": "break", "text": "Which word means to crack something apart?"}},
     ]},
    {"num": 14, "title": "Buddha's Palm", "title_cn": "如来佛祖",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "Finally, the Buddha himself came. He made a bet with Wukong: jump out of my palm, and you win!",
          "setting": "giant buddha hand with tiny monkey standing on it",
          "q": {"t": "general_knowledge", "text": "What did the Buddha ask Wukong to do?", "options": ["Jump out of his palm", "Climb a mountain", "Cross a river", "Find a star"], "correct_answer": "Jump out of his palm"}},
         {"narration": "Wukong jumped as far as he could! He saw 5 huge pillars and thought he reached the edge of the world.",
          "setting": "monkey standing between five giant pillars in misty landscape",
          "q": {"t": "counting", "text": "How many pillars did Wukong see?", "count": 5, "obj": "pillar"}},
         {"narration": "But the 5 pillars were actually Buddha's fingers! Wukong could not escape.",
          "setting": "buddha smiling with his hand closing, monkey looking surprised",
          "q": {"t": "general_knowledge", "text": "What were the 5 pillars really?", "options": ["Buddha's fingers", "Mountains", "Trees", "Towers"], "correct_answer": "Buddha's fingers"}},
         {"narration": "Buddha placed a mountain on top of Wukong. He would stay there for 500 years until he learned his lesson.",
          "setting": "monkey trapped under a large mountain with a golden seal on top",
          "q": {"t": "sight_words", "word": "wait", "text": "Which word means to stay until something happens?"}},
     ]},

    # =====================================================================
    # Tier 2: Dragon Palace (stories 15-27, difficulty 2)
    # =====================================================================
    {"num": 15, "title": "500 Years Under the Mountain", "title_cn": "五百年",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "500 years passed. Wukong was still trapped under the mountain. Rain, snow, sun — he endured it all.",
          "setting": "mountain with seasons changing around it, monkey peeking out",
          "q": {"t": "general_knowledge", "text": "How many years was Wukong trapped?", "options": ["500 years", "100 years", "50 years", "1000 years"], "correct_answer": "500 years"}},
         {"narration": "One day, a kind monk named Tang Sanzang walked by. He was on a journey to fetch holy scriptures.",
          "setting": "monk in orange robes walking along a path near a mountain",
          "q": {"t": "phonics", "word": "monk", "letter": "m"}},
         {"narration": "He heard Wukong calling for help! The monk removed the golden seal and freed Wukong.",
          "setting": "monk removing a glowing seal from mountain, monkey emerging",
          "q": {"t": "sight_words", "word": "help", "text": "Which word means to give someone assistance?"}},
         {"narration": "Wukong promised to protect the monk on his journey. He became his first disciple!",
          "setting": "monkey bowing to monk on a sunny road, beginning their journey",
          "q": {"t": "counting", "text": "Wukong was the first disciple. How many disciples so far?", "count": 1, "obj": "monkey"}},
     ]},
    {"num": 16, "title": "The Golden Headband", "title_cn": "紧箍咒",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "Wukong was wild and hard to control. The Goddess of Mercy gave Tang Sanzang a magical golden headband.",
          "setting": "goddess in white giving a golden headband to monk",
          "q": {"t": "general_knowledge", "text": "Who gave the headband to the monk?", "options": ["Goddess of Mercy", "The Dragon King", "The Jade Emperor", "Buddha"], "correct_answer": "Goddess of Mercy"}},
         {"narration": "When Wukong put it on, it couldn't come off! If he misbehaved, Tang Sanzang could chant a spell to make it tighten.",
          "setting": "monkey with golden headband on head, looking uncomfortable",
          "q": {"t": "phonics", "word": "spell", "letter": "s"}},
         {"narration": "Wukong was angry at first, but he learned to listen and be patient. The headband taught him discipline.",
          "setting": "monkey and monk walking together peacefully on a mountain path",
          "q": {"t": "sight_words", "word": "listen", "text": "Which word means to pay attention to sounds?"}},
     ]},
    {"num": 17, "title": "Pigsy Joins the Team", "title_cn": "收服猪八戒",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "On their journey, they met a pig monster living in a village. He had been causing trouble!",
          "setting": "pig monster in a village, villagers looking scared",
          "q": {"t": "general_knowledge", "text": "What kind of monster did they meet?", "options": ["A pig", "A tiger", "A dragon", "A snake"], "correct_answer": "A pig"}},
         {"narration": "Wukong fought the pig monster! After a fierce battle, the pig surrendered.",
          "setting": "monkey and pig monster fighting in a field",
          "q": {"t": "sight_words", "word": "brave", "text": "Which word means not afraid?"}},
         {"narration": "The pig's name was Zhu Bajie, also called Pigsy. He used to be a heavenly general! He joined their team.",
          "setting": "pig character bowing to monk, monkey standing nearby",
          "q": {"t": "counting", "text": "Now with Pigsy, how many disciples does the monk have?", "count": 2, "obj": "star"}},
         {"narration": "Pigsy was funny and always hungry, but he was strong and had a good heart.",
          "setting": "pig character eating rice, monkey and monk watching and laughing",
          "q": {"t": "phonics", "word": "hungry", "letter": "h"}},
     ]},
    {"num": 18, "title": "Sandy from the River", "title_cn": "收服沙僧",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "They came to a wide, dangerous river. A monster lived in the water and wouldn't let them cross!",
          "setting": "wide misty river with dark waters, travelers on the shore",
          "q": {"t": "phonics", "word": "river", "letter": "r"}},
         {"narration": "Wukong and the river monster fought! The monster was strong in water but Wukong was clever.",
          "setting": "monkey fighting a blue river monster in splashing water",
          "q": {"t": "sight_words", "word": "water", "text": "Which word means the liquid in rivers and oceans?"}},
         {"narration": "The monster was actually Sandy, another fallen heavenly general. He agreed to join them! Now they had 3 disciples.",
          "setting": "sandy character with a necklace, joining the group on the riverbank",
          "q": {"t": "counting", "text": "With Sandy, how many disciples does the monk have now?", "count": 3, "obj": "star"}},
     ]},
    {"num": 19, "title": "The White Dragon Horse", "title_cn": "白龙马",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "Tang Sanzang's horse was eaten by a dragon! Oh no! How would he travel now?",
          "setting": "dragon emerging from a lake, monk looking shocked",
          "q": {"t": "general_knowledge", "text": "What happened to the monk's horse?", "options": ["A dragon ate it", "It ran away", "It got sick", "It was sleeping"], "correct_answer": "A dragon ate it"}},
         {"narration": "But the dragon was actually a prince who had made a mistake. The Goddess of Mercy transformed him into a white horse.",
          "setting": "dragon transforming into a beautiful white horse in golden light",
          "q": {"t": "phonics", "word": "horse", "letter": "h"}},
         {"narration": "Now Tang Sanzang had a magical dragon horse to ride! The team of 5 was complete.",
          "setting": "monk riding white horse, with monkey, pig, and sandy walking alongside",
          "q": {"t": "counting", "text": "Count the team: monk, Wukong, Pigsy, Sandy, and the horse. How many?", "count": 5, "obj": "star"}},
     ]},
    {"num": 20, "title": "The First Demon Village", "title_cn": "降妖除魔",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "They arrived at a small village. The people looked scared and sad. A demon was stealing their food!",
          "setting": "sad villagers in a small Chinese village",
          "q": {"t": "sight_words", "word": "scared", "text": "Which word means afraid?"}},
         {"narration": "Wukong turned into a butterfly to spy on the demon. He found the demon's cave in the mountains.",
          "setting": "butterfly flying near a dark cave entrance in mountains",
          "q": {"t": "general_knowledge", "text": "What did Wukong turn into to spy?", "options": ["A butterfly", "A bird", "A fish", "A rock"], "correct_answer": "A butterfly"}},
         {"narration": "Wukong fought the demon and won! The villagers cheered and gave them a big feast with 6 dishes.",
          "setting": "villagers celebrating, giving food to the travelers",
          "q": {"t": "counting", "text": "How many dishes did the villagers prepare for the feast?", "count": 6, "obj": "apple"}},
     ]},
    {"num": 21, "title": "The Yellow Wind Demon", "title_cn": "黄风怪",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "A powerful demon who controlled the wind attacked them! Sand and wind blew everywhere!",
          "setting": "massive sandstorm with a demon figure in the center",
          "q": {"t": "phonics", "word": "wind", "letter": "w"}},
         {"narration": "The wind was so strong that Wukong's 2 eyes hurt. He needed help!",
          "setting": "monkey shielding eyes from powerful wind, staff in hand",
          "q": {"t": "counting", "text": "How many eyes does Wukong have?", "count": 2, "obj": "eye"}},
         {"narration": "Wukong found a special medicine for his eyes. Then he defeated the Wind Demon!",
          "setting": "monkey with glowing eyes defeating the wind demon, wind calming",
          "q": {"t": "sight_words", "word": "strong", "text": "Which word means having great power?"}},
         {"narration": "With the wind gone, the path was clear again. They continued their journey west.",
          "setting": "peaceful road stretching west with clear blue skies",
          "q": {"t": "general_knowledge", "text": "Which direction were they traveling?", "options": ["West", "East", "North", "South"], "correct_answer": "West"}},
     ]},
    {"num": 22, "title": "The River of Flowing Sand", "title_cn": "流沙河",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "They came to a river full of quicksand. Nothing could float on it — not even a feather!",
          "setting": "mysterious river of flowing sand, dark and swirling",
          "q": {"t": "general_knowledge", "text": "What was special about this river?", "options": ["Nothing could float on it", "It was frozen", "It was very deep", "It had fish"], "correct_answer": "Nothing could float on it"}},
         {"narration": "Sandy knew this river well — it was where he used to live! He helped build a magic raft.",
          "setting": "sandy building a raft with magical powers on the riverbank",
          "q": {"t": "phonics", "word": "build", "letter": "b"}},
         {"narration": "They crossed the river safely! Sandy was proud to help his new friends.",
          "setting": "group crossing the sandy river on a glowing raft",
          "q": {"t": "sight_words", "word": "safe", "text": "Which word means out of danger?"}},
     ]},
    {"num": 23, "title": "Test of the Four Saints", "title_cn": "四圣试禅心",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "4 beautiful women invited them to stay in their mansion. They offered food and riches!",
          "setting": "beautiful mansion with four elegant women welcoming travelers",
          "q": {"t": "counting", "text": "How many women invited them to stay?", "count": 4, "obj": "flower"}},
         {"narration": "Pigsy was excited! He wanted to stay. But it was actually a test from 4 heavenly saints!",
          "setting": "pig character looking happy, being tempted by luxury",
          "q": {"t": "general_knowledge", "text": "Who were the 4 women really?", "options": ["Heavenly saints", "Demons", "Queens", "Fairies"], "correct_answer": "Heavenly saints"}},
         {"narration": "Pigsy failed the test and got tied up in the forest! The others helped free him.",
          "setting": "pig tied to a tree, monkey laughing, monk looking disapproving",
          "q": {"t": "sight_words", "word": "friend", "text": "Which word means someone you care about?"}},
     ]},
    {"num": 24, "title": "The Ginseng Fruit Tree", "title_cn": "人参果",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "They visited a magical temple with a tree that grew Ginseng Fruits — shaped like tiny babies!",
          "setting": "ancient temple with a magical tree bearing baby-shaped fruits",
          "q": {"t": "general_knowledge", "text": "What shape were the Ginseng Fruits?", "options": ["Like babies", "Like stars", "Like apples", "Like fish"], "correct_answer": "Like babies"}},
         {"narration": "Wukong secretly picked 4 fruits for everyone to share!",
          "setting": "close-up of glowing baby-shaped fruits on a tree",
          "q": {"t": "counting", "text": "How many Ginseng Fruits did Wukong pick?", "count": 4, "obj": "peach"}},
         {"narration": "But the temple master found out and was furious! 8 fruits were missing from the tree.",
          "setting": "angry old master confronting monkey near the fruit tree",
          "q": {"t": "subtraction", "text": "The tree had 8 fruits but now 4 are missing. How many are left?", "a": 8, "b": 4, "obj": "peach"}},
         {"narration": "Wukong accidentally knocked down the tree. The Goddess of Mercy fixed it with her magic water!",
          "setting": "goddess pouring magical water on a fallen tree, it starts growing again",
          "q": {"t": "phonics", "word": "tree", "letter": "t"}},
     ]},
    {"num": 25, "title": "The Silver Horn King", "title_cn": "银角大王",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "2 demon brothers with magic gourds blocked the path. If you answered when they called your name, you'd be sucked inside!",
          "setting": "two demon kings holding magical gourds on a mountain pass",
          "q": {"t": "counting", "text": "How many demon brothers were there?", "count": 2, "obj": "monster"}},
         {"narration": "They tricked Wukong and sucked him into the gourd! It was dark and scary inside.",
          "setting": "monkey being pulled into a glowing purple gourd",
          "q": {"t": "sight_words", "word": "dark", "text": "Which word means without light?"}},
         {"narration": "But Wukong was clever! He turned into a bug and escaped. Then he stole their 2 gourds!",
          "setting": "monkey transformed as tiny bug escaping from gourd",
          "q": {"t": "general_knowledge", "text": "What did Wukong turn into to escape?", "options": ["A bug", "A bird", "A fish", "A mouse"], "correct_answer": "A bug"}},
         {"narration": "With their own weapons, Wukong defeated the demon brothers! The path was safe again.",
          "setting": "monkey holding magic gourds triumphantly, defeated demons on ground",
          "q": {"t": "subtraction", "text": "There were 2 demon brothers. Wukong defeated both. How many demons are left?", "a": 2, "b": 2, "obj": "monster"}},
     ]},
    {"num": 26, "title": "The Golden Horn King", "title_cn": "金角大王",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "The Golden Horn King was even stronger than his brother! He had a magic rope that could tie up anyone.",
          "setting": "powerful golden-horned demon with a magical golden rope",
          "q": {"t": "general_knowledge", "text": "What magic item did the Golden Horn King have?", "options": ["A magic rope", "A magic sword", "A magic mirror", "A magic hat"], "correct_answer": "A magic rope"}},
         {"narration": "Wukong and the demon fought for 3 days! Mountains shook and rivers trembled.",
          "setting": "epic battle between monkey and golden demon, landscape shaking",
          "q": {"t": "counting", "text": "How many days did Wukong fight the demon?", "count": 3, "obj": "sun"}},
         {"narration": "The Goddess of Mercy revealed that the demons were actually her servants who had escaped. She took them back to Heaven.",
          "setting": "goddess taking the two demons back to heaven on a cloud",
          "q": {"t": "addition", "text": "The Silver Horn and Golden Horn are 2 brothers. The Goddess took them both. How many went to Heaven?", "a": 1, "b": 1, "obj_a": "monster", "obj_b": "monster"}},
     ]},
    {"num": 27, "title": "The Kingdom of Wuji", "title_cn": "乌鸡国",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "They arrived at the Kingdom of Wuji. The king's ghost appeared to Tang Sanzang in a dream!",
          "setting": "ghost of a king appearing in monk's dream, misty and ethereal",
          "q": {"t": "phonics", "word": "dream", "letter": "d"}},
         {"narration": "A demon had pushed the real king into a well and taken his place! Nobody knew!",
          "setting": "demon disguised as king sitting on throne in palace",
          "q": {"t": "general_knowledge", "text": "Where did the demon push the real king?", "options": ["Into a well", "Into a river", "Into a cave", "Into a forest"], "correct_answer": "Into a well"}},
         {"narration": "Wukong pulled the real king from the well and used a magic pill to bring him back to life!",
          "setting": "monkey pulling a king out of a well, golden light around them",
          "q": {"t": "sight_words", "word": "alive", "text": "Which word means living and breathing?"}},
         {"narration": "Then Wukong exposed the fake king and defeated the demon! The real king got his throne back.",
          "setting": "real king back on throne, people celebrating, demon defeated",
          "q": {"t": "comparison", "text": "Who had more power? The real king had 5 guards, the fake king had 2.", "left": ["soldier", "soldier", "soldier", "soldier", "soldier"], "right": ["soldier", "soldier"]}},
     ]},

    # =====================================================================
    # Tier 3: Heaven Palace (stories 28-41, difficulty 3)
    # =====================================================================
    {"num": 28, "title": "The White Bone Demon", "title_cn": "三打白骨精",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "A clever demon called the White Bone Spirit could change into different people! First, she became a young girl.",
          "setting": "beautiful young girl on a mountain path, with hidden skeleton shadow",
          "q": {"t": "counting", "text": "How many disguises has the demon used so far?", "count": 1, "obj": "mask"}},
         {"narration": "Wukong saw through her disguise with his golden eyes! He struck her with his staff.",
          "setting": "monkey striking girl with staff, skeleton briefly visible",
          "q": {"t": "general_knowledge", "text": "How did Wukong see through the disguise?", "options": ["Golden eyes", "A magic mirror", "He guessed", "Someone told him"], "correct_answer": "Golden eyes"}},
         {"narration": "The demon came back as an old woman, then an old man. That's 3 disguises total! Tang Sanzang thought Wukong was hurting innocent people!",
          "setting": "old woman and old man forms, monk looking angry at monkey",
          "q": {"t": "addition", "text": "The demon disguised as a girl, old woman, and old man. How many disguises? 1+1+1=?", "a": 2, "b": 1, "obj_a": "mask", "obj_b": "mask"}},
         {"narration": "Tang Sanzang sent Wukong away! Poor Wukong cried as he flew back to Flower Fruit Mountain alone.",
          "setting": "sad monkey flying away on cloud, looking back at monk",
          "q": {"t": "sight_words", "word": "cry", "text": "Which word means tears come from your eyes?"}},
         {"narration": "Later, when Tang Sanzang was captured by the real demon, he realized Wukong was right. Wukong came back and saved everyone!",
          "setting": "monkey heroically saving monk from a skeleton demon in a cave",
          "q": {"t": "general_knowledge", "text": "Who saved Tang Sanzang from the demon?", "options": ["Wukong", "Pigsy", "Sandy", "The Dragon King"], "correct_answer": "Wukong"}},
     ]},
    {"num": 29, "title": "The Yellow Robe Demon", "title_cn": "黄袍怪",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "Without Wukong, the team was in trouble! A demon captured Tang Sanzang and turned him into a tiger!",
          "setting": "monk being transformed into a tiger by a demon's spell",
          "q": {"t": "general_knowledge", "text": "What animal was the monk turned into?", "options": ["A tiger", "A lion", "A bear", "A wolf"], "correct_answer": "A tiger"}},
         {"narration": "Pigsy flew to Flower Fruit Mountain to beg Wukong to come back. Wukong pretended he didn't care!",
          "setting": "pig character begging monkey on mountain, monkey turning away",
          "q": {"t": "phonics", "word": "please", "letter": "p"}},
         {"narration": "But Wukong secretly cared a lot. He rushed back and defeated the Yellow Robe Demon!",
          "setting": "monkey flying fast on cloud towards a demon's lair",
          "q": {"t": "sight_words", "word": "fast", "text": "Which word means moving very quickly?"}},
         {"narration": "He changed Tang Sanzang back from a tiger to a human. The team was together again!",
          "setting": "monkey using magic to turn tiger back into monk, everyone relieved",
          "q": {"t": "make_ten", "text": "Wukong has 7 magic points. How many more does he need to reach 10?", "a": 7}},
     ]},
    {"num": 30, "title": "The Red Boy", "title_cn": "红孩儿",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "A demon child called Red Boy could breathe fire! He was the Bull Demon King's son.",
          "setting": "small red demon child breathing flames on a mountain",
          "q": {"t": "general_knowledge", "text": "What could Red Boy breathe?", "options": ["Fire", "Water", "Ice", "Wind"], "correct_answer": "Fire"}},
         {"narration": "Red Boy captured Tang Sanzang with his fire! The flames were too hot even for Wukong!",
          "setting": "ring of fire surrounding monk, monkey unable to get through",
          "q": {"t": "phonics", "word": "flame", "letter": "f"}},
         {"narration": "Wukong asked the Goddess of Mercy for help. She captured Red Boy and made him her servant.",
          "setting": "goddess with Red Boy now calm and reformed, standing beside her",
          "q": {"t": "addition", "text": "The Goddess now has Red Boy and 2 other helpers. How many helpers total?", "a": 2, "b": 1, "obj_a": "star", "obj_b": "star"}},
     ]},
    {"num": 31, "title": "The Black River Demon", "title_cn": "黑水河妖",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "A demon from the Black River pretended to be a boatman. He tricked Tang Sanzang onto his boat!",
          "setting": "demon disguised as boatman on a dark river",
          "q": {"t": "general_knowledge", "text": "What did the demon pretend to be?", "options": ["A boatman", "A fisherman", "A farmer", "A monk"], "correct_answer": "A boatman"}},
         {"narration": "The boat sank and the demon dragged Tang Sanzang underwater! Wukong dove in to save him.",
          "setting": "monkey diving into dark waters after sinking boat",
          "q": {"t": "sight_words", "word": "dive", "text": "Which word means to jump into water?"}},
         {"narration": "With help from a heavenly prince, they defeated the Black River Demon and saved Tang Sanzang.",
          "setting": "monkey and a prince warrior defeating water demon, freeing monk",
          "q": {"t": "counting", "text": "How many heroes fought the demon? Wukong and the prince.", "count": 2, "obj": "star"}},
     ]},
    {"num": 32, "title": "The Cart-Slow Kingdom", "title_cn": "车迟国",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "In this kingdom, 3 fake masters used tricks to pretend they had magic powers!",
          "setting": "three shifty-looking masters performing fake magic in a royal court",
          "q": {"t": "counting", "text": "How many fake masters were there?", "count": 3, "obj": "mask"}},
         {"narration": "Wukong challenged them to a contest! They competed in prayer for rain.",
          "setting": "monkey and fake master both praying, clouds gathering",
          "q": {"t": "phonics", "word": "rain", "letter": "r"}},
         {"narration": "Wukong asked the Dragon King to help him win! Real rain fell from the sky.",
          "setting": "rain falling from clouds, monkey smiling, fake masters looking worried",
          "q": {"t": "sight_words", "word": "real", "text": "Which word means true, not fake?"}},
         {"narration": "The fake masters were exposed! The king freed all the monks they had imprisoned.",
          "setting": "freed monks celebrating, king punishing the fake masters",
          "q": {"t": "subtraction", "text": "There were 3 fake masters. All 3 were exposed. How many fakes are left?", "a": 3, "b": 3, "obj": "mask"}},
     ]},
    {"num": 33, "title": "The Golden Fish Demon", "title_cn": "金鱼精",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "A huge golden fish demon flooded a whole temple! The monks were trapped in the water.",
          "setting": "flooded temple with giant golden fish swimming around",
          "q": {"t": "general_knowledge", "text": "What kind of demon flooded the temple?", "options": ["A golden fish", "A dragon", "A turtle", "A crab"], "correct_answer": "A golden fish"}},
         {"narration": "Wukong fought the fish but it was very slippery! Every time he grabbed it, it escaped.",
          "setting": "monkey trying to catch a giant golden fish in water",
          "q": {"t": "sight_words", "word": "catch", "text": "Which word means to grab and hold something?"}},
         {"narration": "The Goddess of Mercy came with her bamboo basket and caught the fish easily. It was her pet goldfish!",
          "setting": "goddess scooping up golden fish with a basket, smiling",
          "q": {"t": "phonics", "word": "fish", "letter": "f"}},
     ]},
    {"num": 34, "title": "The Scorpion Demon", "title_cn": "蝎子精",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "A scorpion demon stung Wukong! Her poison was so strong that even Wukong was hurt.",
          "setting": "giant scorpion demon attacking monkey with its tail",
          "q": {"t": "general_knowledge", "text": "What kind of creature was the demon?", "options": ["A scorpion", "A spider", "A snake", "A bee"], "correct_answer": "A scorpion"}},
         {"narration": "Wukong had to find the Star of Light, the only one who could defeat the scorpion.",
          "setting": "monkey flying through stars searching for the Star of Light",
          "q": {"t": "sight_words", "word": "light", "text": "Which word means brightness that lets you see?"}},
         {"narration": "The Star of Light turned into a giant rooster! Its crow was the scorpion's weakness. The demon was defeated!",
          "setting": "giant magical rooster crowing at a scorpion demon, golden light",
          "q": {"t": "phonics", "word": "rooster", "letter": "r"}},
     ]},
    {"num": 35, "title": "The Land of Women", "title_cn": "女儿国",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "They arrived at a kingdom where only women lived! The queen wanted Tang Sanzang to be her king.",
          "setting": "beautiful kingdom with palace, all female guards and citizens",
          "q": {"t": "general_knowledge", "text": "Who lived in this kingdom?", "options": ["Only women", "Only men", "Only children", "Only animals"], "correct_answer": "Only women"}},
         {"narration": "Tang Sanzang politely refused. He had to continue his journey to get the holy scriptures!",
          "setting": "monk politely declining queen in throne room",
          "q": {"t": "sight_words", "word": "polite", "text": "Which word means having good manners?"}},
         {"narration": "A scorpion demon tried to capture Tang Sanzang while they were leaving. Wukong saved him just in time!",
          "setting": "monkey fighting off demon while monk escapes the kingdom gates",
          "q": {"t": "make_ten", "text": "Wukong fought 6 enemies today. How many more to reach 10?", "a": 6}},
     ]},
    {"num": 36, "title": "The Real and Fake Monkey", "title_cn": "真假美猴王",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "A monkey that looked exactly like Wukong appeared! Nobody could tell them apart.",
          "setting": "two identical monkeys standing face to face, everyone confused",
          "q": {"t": "counting", "text": "How many monkeys that look like Wukong are there now?", "count": 2, "obj": "monkey"}},
         {"narration": "They both claimed to be the real Wukong! They fought from Earth to Heaven to the Underworld.",
          "setting": "two monkeys fighting across different realms, heaven and underworld",
          "q": {"t": "counting", "text": "They fought in how many places? Earth, Heaven, and the Underworld.", "count": 3, "obj": "star"}},
         {"narration": "Even the Jade Emperor couldn't tell them apart! They went to see the Buddha.",
          "setting": "two monkeys standing before a giant buddha, heavenly beings watching",
          "q": {"t": "sight_words", "word": "same", "text": "Which word means exactly alike?"}},
         {"narration": "The Buddha knew! The fake one was a Six-Eared Monkey. Wukong defeated him and the team was reunited.",
          "setting": "real monkey defeating fake monkey, buddha watching approvingly",
          "q": {"t": "subtraction", "text": "There were 2 monkeys. The fake one was defeated. How many are left?", "a": 2, "b": 1, "obj": "monkey"}},
     ]},
    {"num": 37, "title": "The Banana Fan", "title_cn": "芭蕉扇",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "A mountain of fire blocked their path! The flames stretched for hundreds of miles!",
          "setting": "massive flaming mountain blocking a road, intense red and orange fire",
          "q": {"t": "general_knowledge", "text": "What blocked their path?", "options": ["A mountain of fire", "A wide river", "A tall wall", "A deep hole"], "correct_answer": "A mountain of fire"}},
         {"narration": "Only the Iron Fan Princess had a magic banana fan that could blow out the fire.",
          "setting": "woman holding a giant green banana leaf fan, looking fierce",
          "q": {"t": "phonics", "word": "fan", "letter": "f"}},
         {"narration": "But she was Red Boy's mother! She was angry at Wukong and wouldn't help.",
          "setting": "angry woman refusing to help monkey, turning away",
          "q": {"t": "sight_words", "word": "angry", "text": "Which word means very upset?"}},
     ]},
    {"num": 38, "title": "Borrowing the Fan", "title_cn": "三借芭蕉扇",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "Wukong turned into a tiny bug and flew into the Iron Fan Princess's belly! She had to give him the fan.",
          "setting": "tiny bug flying into woman's tea cup, she's unaware",
          "q": {"t": "general_knowledge", "text": "What did Wukong turn into to trick the princess?", "options": ["A tiny bug", "A bird", "A mouse", "A cat"], "correct_answer": "A tiny bug"}},
         {"narration": "But it was a fake fan! When Wukong used it, the fire grew even bigger!",
          "setting": "monkey waving fan at fire, fire growing larger, monkey looking shocked",
          "q": {"t": "comparison", "text": "After the fake fan, did the fire get bigger or smaller?", "left": ["flame", "flame", "flame", "flame", "flame"], "right": ["flame", "flame"]}},
         {"narration": "The Bull Demon King, her husband, fought Wukong for the real fan. It was an epic battle!",
          "setting": "monkey fighting a bull demon in the sky, both powerful",
          "q": {"t": "phonics", "word": "battle", "letter": "b"}},
         {"narration": "With help from heavenly soldiers, Wukong finally got the real fan and put out the fire!",
          "setting": "monkey waving magical fan, fire being extinguished, cool breeze",
          "q": {"t": "make_ten", "text": "Wukong tried 3 times to get the fan. How many more tries to reach 10?", "a": 3}},
     ]},
    {"num": 39, "title": "The Bull Demon King", "title_cn": "牛魔王",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "The Bull Demon King was furious! He transformed into a giant white bull to fight Wukong.",
          "setting": "enormous white bull charging at monkey, dust and rocks flying",
          "q": {"t": "general_knowledge", "text": "What did the Bull Demon King transform into?", "options": ["A giant white bull", "A dragon", "A tiger", "An eagle"], "correct_answer": "A giant white bull"}},
         {"narration": "Wukong transformed too! He became a giant to match the bull. They fought across mountains!",
          "setting": "giant monkey and giant bull fighting, mountains crumbling",
          "q": {"t": "sight_words", "word": "giant", "text": "Which word means something very, very big?"}},
         {"narration": "The heavenly prince Nezha came to help! Together they defeated the Bull Demon King.",
          "setting": "boy warrior on fire wheels helping monkey defeat bull demon",
          "q": {"t": "addition", "text": "Wukong and Nezha teamed up. That's 1+1 heroes! How many?", "a": 1, "b": 1, "obj_a": "monkey", "obj_b": "star"}},
     ]},
    {"num": 40, "title": "Crossing the Flaming Mountain", "title_cn": "过火焰山",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "With the real banana fan, Wukong waved it 3 times. Whoooosh! The fire went out!",
          "setting": "monkey waving fan, powerful wind extinguishing mountain fire",
          "q": {"t": "counting", "text": "How many times did Wukong wave the fan?", "count": 3, "obj": "fan"}},
         {"narration": "Rain fell on the mountain for the first time in years! Plants started growing again.",
          "setting": "rain falling on formerly burning mountain, green sprouts appearing",
          "q": {"t": "phonics", "word": "green", "letter": "g"}},
         {"narration": "The people who lived nearby were so happy! They could finally cross the mountain safely.",
          "setting": "happy villagers crossing a now-green mountain, travelers continuing journey",
          "q": {"t": "sight_words", "word": "happy", "text": "Which word means feeling good and joyful?"}},
     ]},
    {"num": 41, "title": "The Kingdom of Sacrifice", "title_cn": "祭赛国",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "In this kingdom, the king had lost his magical golden pagoda to demons! The kingdom was cursed with endless rain.",
          "setting": "rainy kingdom with sad people, empty pagoda tower",
          "q": {"t": "general_knowledge", "text": "What was stolen from the kingdom?", "options": ["A golden pagoda", "A magic sword", "A holy book", "A golden crown"], "correct_answer": "A golden pagoda"}},
         {"narration": "Wukong flew up through the clouds and found the demons who stole the pagoda.",
          "setting": "monkey flying through storm clouds towards a hidden demon lair",
          "q": {"t": "sight_words", "word": "search", "text": "Which word means to look for something carefully?"}},
         {"narration": "He defeated the demons, returned the golden pagoda, and the rain finally stopped! The sun came out again.",
          "setting": "monkey returning golden pagoda to king, sun breaking through clouds",
          "q": {"t": "subtraction", "text": "There were 5 rainy days. After Wukong helped, 5 days of sun returned. How many rainy days left?", "a": 5, "b": 5, "obj": "cloud"}},
     ]},

    # =====================================================================
    # Tier 4: White Bone Cave (stories 42-54, difficulty 4)
    # =====================================================================
    {"num": 42, "title": "The Spider Demons", "title_cn": "蜘蛛精",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "7 spider demons disguised as beautiful women lived near a hot spring. They trapped Tang Sanzang!",
          "setting": "seven beautiful women at a misty hot spring, webs hidden",
          "q": {"t": "counting", "text": "How many spider demons were there?", "count": 7, "obj": "spider"}},
         {"narration": "When their disguise was revealed, they turned into giant spiders and spun webs everywhere!",
          "setting": "seven giant colorful spiders spinning webs, monk trapped",
          "q": {"t": "phonics", "word": "spider", "letter": "s"}},
         {"narration": "Wukong fought through the sticky webs and freed Tang Sanzang. The spiders ran away!",
          "setting": "monkey cutting through webs with staff, freeing monk",
          "q": {"t": "subtraction", "text": "There were 7 spiders. Wukong scared away 5. How many are left?", "a": 7, "b": 5, "obj": "spider"}},
     ]},
    {"num": 43, "title": "The Centipede Demon", "title_cn": "蜈蚣精",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "The spider demons ran to their big brother — a giant centipede demon with a thousand golden lights!",
          "setting": "enormous centipede demon glowing with golden light in a cave",
          "q": {"t": "general_knowledge", "text": "What kind of creature was the big brother demon?", "options": ["A centipede", "A scorpion", "A spider", "A snake"], "correct_answer": "A centipede"}},
         {"narration": "The golden lights blinded Wukong! He couldn't fight what he couldn't see.",
          "setting": "monkey shielding his eyes from blinding golden beams",
          "q": {"t": "sight_words", "word": "blind", "text": "Which word means unable to see?"}},
         {"narration": "A heavenly rooster came to help again! The centipede was afraid of roosters and was defeated.",
          "setting": "magical rooster facing down centipede demon, golden light fading",
          "q": {"t": "general_knowledge", "text": "What animal scared the centipede?", "options": ["A rooster", "A dog", "A cat", "A horse"], "correct_answer": "A rooster"}},
     ]},
    {"num": 44, "title": "The Green Lion", "title_cn": "青狮精",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "A powerful green lion demon had swallowed an entire kingdom! Everyone was inside his belly.",
          "setting": "massive green lion demon outside a city, mouth wide open",
          "q": {"t": "general_knowledge", "text": "What did the green lion swallow?", "options": ["An entire kingdom", "A mountain", "A river", "A cloud"], "correct_answer": "An entire kingdom"}},
         {"narration": "Wukong let the lion swallow him too! Then he kicked and punched from inside the lion's belly.",
          "setting": "monkey inside a lion's belly, punching and kicking, lion in pain",
          "q": {"t": "sight_words", "word": "inside", "text": "Which word means in the middle of something?"}},
         {"narration": "The lion couldn't take it anymore! He spit everyone out, and Wukong defeated him.",
          "setting": "lion spitting out people and monkey, looking defeated",
          "q": {"t": "phonics", "word": "lion", "letter": "l"}},
         {"narration": "The kingdom was saved! Everyone cheered for Wukong and his friends.",
          "setting": "grateful kingdom people celebrating with the travel team",
          "q": {"t": "make_ten", "text": "The kingdom gave 4 gifts to Wukong. How many more to make 10?", "a": 4}},
     ]},
    {"num": 45, "title": "The White Elephant Demon", "title_cn": "白象精",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "A giant white elephant demon used his long trunk to grab Tang Sanzang! He was incredibly strong.",
          "setting": "massive white elephant grabbing monk with trunk, others fighting",
          "q": {"t": "general_knowledge", "text": "What body part did the elephant use to grab the monk?", "options": ["His trunk", "His tail", "His foot", "His ear"], "correct_answer": "His trunk"}},
         {"narration": "Wukong and Pigsy fought the elephant together, but his skin was too thick!",
          "setting": "monkey and pig fighting elephant, weapons bouncing off",
          "q": {"t": "addition", "text": "Wukong hit the elephant 6 times and Pigsy hit 4 times. How many hits total?", "a": 6, "b": 4, "obj_a": "star", "obj_b": "star"}},
         {"narration": "The elephant was actually a celestial creature who had escaped from Heaven. He was taken back.",
          "setting": "elephant being led back to heaven by celestial beings",
          "q": {"t": "sight_words", "word": "escape", "text": "Which word means to run away from a place?"}},
     ]},
    {"num": 46, "title": "The Golden Winged Peng", "title_cn": "大鹏金翅鸟",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "The most dangerous demon yet — a giant golden bird called the Peng! It could fly faster than Wukong!",
          "setting": "enormous golden eagle-like bird swooping through clouds",
          "q": {"t": "general_knowledge", "text": "What kind of creature was the Peng?", "options": ["A giant golden bird", "A dragon", "A bat", "A butterfly"], "correct_answer": "A giant golden bird"}},
         {"narration": "The Peng grabbed Tang Sanzang and flew to a mountain top. Even Wukong's cloud couldn't catch up!",
          "setting": "giant bird carrying monk, monkey chasing on cloud but falling behind",
          "q": {"t": "comparison", "text": "Who was faster? The Peng flew 8 miles, Wukong flew 5 miles.", "left": ["star", "star", "star", "star", "star", "star", "star", "star"], "right": ["star", "star", "star", "star", "star"]}},
         {"narration": "Wukong went to ask the Buddha for help. The Buddha revealed that the Peng was his own relative!",
          "setting": "buddha speaking to monkey, golden bird perched nearby",
          "q": {"t": "phonics", "word": "buddha", "letter": "b"}},
         {"narration": "The Buddha tamed the Peng. The golden bird would now serve and protect, not attack.",
          "setting": "golden bird now peaceful, perched near buddha, monk freed",
          "q": {"t": "sight_words", "word": "peace", "text": "Which word means calm and no fighting?"}},
     ]},
    {"num": 47, "title": "The Kingdom of Bhikku", "title_cn": "比丘国",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "In this kingdom, the evil minister was actually a deer demon! He was tricking the old king.",
          "setting": "sneaky deer demon disguised as a minister, whispering to old king",
          "q": {"t": "general_knowledge", "text": "What animal was the disguised minister?", "options": ["A deer", "A fox", "A wolf", "A snake"], "correct_answer": "A deer"}},
         {"narration": "Wukong saw through the disguise with his golden eyes! He exposed the deer demon.",
          "setting": "monkey pointing at minister, demon form becoming visible",
          "q": {"t": "subtraction", "text": "The demon had 9 hiding spots. Wukong found 6. How many are left to find?", "a": 9, "b": 6, "obj": "star"}},
         {"narration": "The demon tried to run but Wukong was too fast! The kingdom was saved from the trickster.",
          "setting": "monkey chasing deer demon, catching it easily",
          "q": {"t": "make_ten", "text": "Wukong caught 8 demons this week. How many more to reach 10?", "a": 8}},
     ]},
    {"num": 48, "title": "The Three Demon Kings", "title_cn": "青毛狮子怪",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "3 powerful demon kings joined forces! A lion, an elephant, and a giant bird — together they were terrifying!",
          "setting": "three powerful demons standing together on a mountain, looking menacing",
          "q": {"t": "counting", "text": "How many demon kings joined forces?", "count": 3, "obj": "monster"}},
         {"narration": "They captured Tang Sanzang and put him in a cage. They wanted to eat him to become immortal!",
          "setting": "monk in cage, three demons preparing a feast",
          "q": {"t": "sight_words", "word": "trapped", "text": "Which word means stuck and can't get out?"}},
         {"narration": "Wukong had to fight all 3 at once! It was the hardest battle yet.",
          "setting": "monkey fighting three demons simultaneously in an epic battle",
          "q": {"t": "subtraction", "text": "Wukong faced 3 demon kings. He defeated 1. How many are left?", "a": 3, "b": 1, "obj": "monster"}},
         {"narration": "With help from heavenly beings, all 3 demons were captured and taken back to where they belonged.",
          "setting": "three demons being taken away by celestial guards, team reunited",
          "q": {"t": "addition", "text": "The heavenly guards sent 5 warriors and 3 more came later. How many warriors total?", "a": 5, "b": 3, "obj_a": "soldier", "obj_b": "soldier"}},
     ]},
    {"num": 49, "title": "The Rhinoceros Demons", "title_cn": "犀牛精",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "3 rhinoceros demons pretended to be Buddhas! They stole all the holy oil from a temple.",
          "setting": "three rhino demons wearing fake Buddhist robes near a temple",
          "q": {"t": "counting", "text": "How many rhino demons pretended to be Buddhas?", "count": 3, "obj": "monster"}},
         {"narration": "Wukong chased them through mountains and rivers. They were fast runners!",
          "setting": "monkey chasing three rhinos across landscape, dust flying",
          "q": {"t": "phonics", "word": "chase", "letter": "c"}},
         {"narration": "4 heavenly star warriors came to help. Together they cornered the fake Buddhas and captured them!",
          "setting": "four star warriors and monkey surrounding three rhino demons",
          "q": {"t": "addition", "text": "Wukong plus 4 star warriors. How many heroes total?", "a": 1, "b": 4, "obj_a": "monkey", "obj_b": "star"}},
     ]},
    {"num": 50, "title": "The Jade Rabbit", "title_cn": "玉兔精",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "The moon's jade rabbit escaped to Earth! She disguised herself as a princess.",
          "setting": "white rabbit transforming into a princess under moonlight",
          "q": {"t": "general_knowledge", "text": "Where did the jade rabbit come from?", "options": ["The moon", "The sun", "A mountain", "The ocean"], "correct_answer": "The moon"}},
         {"narration": "She wanted to marry Tang Sanzang! She set up a fake contest to win his hand.",
          "setting": "princess on a tower throwing a ball, monk below looking confused",
          "q": {"t": "sight_words", "word": "trick", "text": "Which word means to fool someone?"}},
         {"narration": "Wukong saw through the disguise. But the rabbit was quick and kept hopping away!",
          "setting": "monkey chasing a white rabbit that's jumping super fast",
          "q": {"t": "phonics", "word": "rabbit", "letter": "r"}},
         {"narration": "The Moon Goddess came down from the moon to take her rabbit back. The real princess was found safe.",
          "setting": "beautiful moon goddess descending on moonbeams, taking rabbit home",
          "q": {"t": "subtraction", "text": "There were 2 princesses (real and fake). The fake one left. How many remain?", "a": 2, "b": 1, "obj": "star"}},
     ]},
    {"num": 51, "title": "The Fire and Ice Demons", "title_cn": "火焰山再遇",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "They passed through a land where everything was frozen! A demon had stolen all the warmth.",
          "setting": "frozen icy landscape, travelers shivering",
          "q": {"t": "general_knowledge", "text": "Why was everything frozen?", "options": ["A demon stole the warmth", "It was winter", "It was raining", "A spell was cast"], "correct_answer": "A demon stole the warmth"}},
         {"narration": "The Ice Demon and Fire Demon were fighting each other! Their battle caused chaos everywhere.",
          "setting": "ice demon and fire demon clashing, ice and fire everywhere",
          "q": {"t": "counting", "text": "How many demons were fighting each other?", "count": 2, "obj": "monster"}},
         {"narration": "Wukong brought balance! He helped the 2 demons make peace. The land returned to normal.",
          "setting": "monkey mediating between ice and fire, landscape becoming green",
          "q": {"t": "sight_words", "word": "peace", "text": "Which word means no more fighting?"}},
     ]},
    {"num": 52, "title": "The Underground River", "title_cn": "地下河",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "An underground river blocked their path. Strange glowing fish swam in the dark water.",
          "setting": "underground cave with glowing river, bioluminescent fish",
          "q": {"t": "phonics", "word": "glow", "letter": "g"}},
         {"narration": "A turtle demon offered to carry them across, but it was a trap!",
          "setting": "giant turtle in underground river, travelers about to step on",
          "q": {"t": "general_knowledge", "text": "What did the turtle demon offer to do?", "options": ["Carry them across", "Give them food", "Show them a map", "Tell them a story"], "correct_answer": "Carry them across"}},
         {"narration": "Wukong saw through the trick! He caught the turtle and made it carry them safely across for real.",
          "setting": "monkey riding turtle safely across glowing river with teammates",
          "q": {"t": "addition", "text": "The turtle carried 4 travelers and 1 horse. How many total?", "a": 4, "b": 1, "obj_a": "star", "obj_b": "horse"}},
     ]},
    {"num": 53, "title": "The Magic Garden", "title_cn": "仙人花园",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "They discovered a beautiful garden with fruits that could cure any illness!",
          "setting": "magical garden with glowing colorful fruits on trees",
          "q": {"t": "general_knowledge", "text": "What was special about the garden fruits?", "options": ["They cure illness", "They give wings", "They make you big", "They are golden"], "correct_answer": "They cure illness"}},
         {"narration": "But the garden was guarded by a fierce flower demon! Its petals were sharp as swords.",
          "setting": "beautiful but dangerous flower demon, petals like blades",
          "q": {"t": "phonics", "word": "flower", "letter": "f"}},
         {"narration": "Pigsy accidentally ate a sleeping fruit and fell into a deep sleep! They had to find the cure.",
          "setting": "pig character sleeping on the ground, flowers around",
          "q": {"t": "sight_words", "word": "sleep", "text": "Which word means to close your eyes and rest?"}},
         {"narration": "Wukong found a dew drop that woke Pigsy up. They carefully picked 6 healing fruits and continued on.",
          "setting": "monkey dropping dew on pig to wake him, team leaving garden",
          "q": {"t": "counting", "text": "How many healing fruits did they pick?", "count": 6, "obj": "peach"}},
     ]},
    {"num": 54, "title": "The Mountain Spirits", "title_cn": "山神考验",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "The mountain spirits blocked the path with riddles! They would only let smart travelers pass.",
          "setting": "ghostly mountain spirits floating near a mountain pass, riddle stones",
          "q": {"t": "general_knowledge", "text": "What did the mountain spirits use to test travelers?", "options": ["Riddles", "Swords", "Magic", "Races"], "correct_answer": "Riddles"}},
         {"narration": "Wukong answered the first riddle easily. Pigsy got the second one wrong and had to try again!",
          "setting": "monkey answering confidently, pig scratching head",
          "q": {"t": "subtraction", "text": "There were 3 riddles. Wukong solved 1 and Pigsy solved 1. How many are left?", "a": 3, "b": 2, "obj": "scroll"}},
         {"narration": "Sandy solved the final riddle! The spirits were impressed and let them through.",
          "setting": "sandy answering wisely, spirits nodding and opening the path",
          "q": {"t": "make_ten", "text": "Sandy has solved 5 riddles on the journey. How many more to reach 10?", "a": 5}},
     ]},

    # =====================================================================
    # Tier 5: Flaming Mountain (stories 55-68, difficulty 5)
    # =====================================================================
    {"num": 55, "title": "The Bottomless Cave", "title_cn": "无底洞",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "A demon woman captured Tang Sanzang and took him to a cave so deep nobody could find the bottom!",
          "setting": "dark endless cave going deep underground, dim light",
          "q": {"t": "general_knowledge", "text": "What was special about the cave?", "options": ["It had no bottom", "It was full of gold", "It was underwater", "It was on fire"], "correct_answer": "It had no bottom"}},
         {"narration": "Wukong followed the demon's trail deep into the earth. The cave was full of traps!",
          "setting": "monkey navigating traps in a deep cave, avoiding sharp rocks",
          "q": {"t": "subtraction", "text": "Wukong avoided 12 traps but hit 3. How many did he dodge?", "a": 12, "b": 3, "obj": "star"}},
         {"narration": "He found Tang Sanzang and fought the demon. It turned out she was a mouse spirit who had once stolen lamp oil from the Buddha!",
          "setting": "mouse demon being defeated, transforming back to mouse form",
          "q": {"t": "general_knowledge", "text": "What kind of spirit was the demon really?", "options": ["A mouse", "A cat", "A snake", "A bat"], "correct_answer": "A mouse"}},
         {"narration": "The heavenly cat warriors came and captured the mouse spirit. Tang Sanzang was saved!",
          "setting": "celestial cat warriors catching mouse demon, monk freed",
          "q": {"t": "phonics", "word": "mouse", "letter": "m"}},
     ]},
    {"num": 56, "title": "The Python Demon", "title_cn": "蟒蛇精",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "A python demon as big as a mountain blocked the road! Its body stretched across the entire valley.",
          "setting": "enormous python coiled across a valley, blocking the path",
          "q": {"t": "general_knowledge", "text": "How big was the python demon?", "options": ["As big as a mountain", "As big as a house", "As big as a dog", "As big as a tree"], "correct_answer": "As big as a mountain"}},
         {"narration": "It opened its mouth and a powerful wind pulled everything inside! Even trees were uprooted.",
          "setting": "giant python mouth creating suction, trees and rocks flying in",
          "q": {"t": "subtraction", "text": "The python pulled in 10 trees. 4 were saved by Wukong. How many were swallowed?", "a": 10, "b": 4, "obj": "tree"}},
         {"narration": "Wukong turned himself into a needle and poked the python from inside! It had to open its mouth and let everyone go.",
          "setting": "monkey using staff to poke python from inside, it opens mouth",
          "q": {"t": "sight_words", "word": "escape", "text": "Which word means to get free from a dangerous place?"}},
     ]},
    {"num": 57, "title": "The Cloud Stepping Kingdom", "title_cn": "天竺国",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "They arrived at a beautiful kingdom high in the clouds. The people lived in houses among the clouds!",
          "setting": "kingdom built on clouds, beautiful floating buildings",
          "q": {"t": "phonics", "word": "cloud", "letter": "c"}},
         {"narration": "But the princess had been replaced by a demon! The real princess was locked in a tower.",
          "setting": "demon disguised as princess in throne room, real princess in tower",
          "q": {"t": "general_knowledge", "text": "Where was the real princess?", "options": ["Locked in a tower", "In the garden", "Under the bridge", "In the kitchen"], "correct_answer": "Locked in a tower"}},
         {"narration": "Wukong discovered the truth and rescued the real princess. The demon was a crane spirit from Heaven.",
          "setting": "monkey freeing princess from tower, crane demon flying away",
          "q": {"t": "sight_words", "word": "rescue", "text": "Which word means to save someone from danger?"}},
         {"narration": "The king was so grateful! He gave them 8 bags of supplies and pointed the way west.",
          "setting": "grateful king giving supplies to travelers at kingdom gates",
          "q": {"t": "counting", "text": "How many bags of supplies did the king give them?", "count": 8, "obj": "bag"}},
     ]},
    {"num": 58, "title": "The Nine-Headed Bug", "title_cn": "九头虫",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "A terrifying monster with 9 heads attacked from the sky! Each head could breathe a different element.",
          "setting": "nine-headed dragon/bug in the sky, each head different color",
          "q": {"t": "counting", "text": "How many heads did the monster have?", "count": 9, "obj": "monster"}},
         {"narration": "One head breathed fire, another breathed ice, another shot lightning! Wukong had to dodge them all.",
          "setting": "monkey dodging multiple elemental attacks from the nine heads",
          "q": {"t": "counting", "text": "The monster breathed fire, ice, and lightning. How many elements is that?", "count": 3, "obj": "star"}},
         {"narration": "Wukong called for help from a heavenly warrior who chopped off 1 head. The bug fled in fear!",
          "setting": "warrior chopping off one head, bug flying away in pain",
          "q": {"t": "subtraction", "text": "The bug had 9 heads. 1 was chopped off. How many heads are left?", "a": 9, "b": 1, "obj": "star"}},
     ]},
    {"num": 59, "title": "The Thorn Forest", "title_cn": "荆棘岭",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "A dense forest of thorny trees blocked their way! Every branch had sharp thorns.",
          "setting": "dense dark forest with impossibly thorny trees everywhere",
          "q": {"t": "sight_words", "word": "sharp", "text": "Which word means pointy and able to cut?"}},
         {"narration": "Tree spirits came alive at night! They wanted Tang Sanzang to write poems with them.",
          "setting": "tree spirits shaped like old men, holding scrolls and brushes",
          "q": {"t": "phonics", "word": "write", "letter": "w"}},
         {"narration": "While Tang Sanzang was busy with poems, other tree demons tried to eat the horse! Wukong burned 5 of them down.",
          "setting": "monkey using fire to burn evil tree demons, protecting white horse",
          "q": {"t": "subtraction", "text": "There were 8 tree demons. Wukong burned 5. How many are left?", "a": 8, "b": 5, "obj": "tree"}},
     ]},
    {"num": 60, "title": "The Little Thunder Temple", "title_cn": "小雷音寺",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "They found what looked like the Thunder Temple! Tang Sanzang was excited — were they at the end of their journey?",
          "setting": "beautiful golden temple that looks like the final destination",
          "q": {"t": "general_knowledge", "text": "Why was Tang Sanzang excited?", "options": ["He thought the journey was over", "He found treasure", "He met a friend", "He was hungry"], "correct_answer": "He thought the journey was over"}},
         {"narration": "But it was a fake temple built by a yellow-browed demon! He trapped everyone in a golden cymbal.",
          "setting": "demon laughing, golden cymbal trapping the travelers",
          "q": {"t": "sight_words", "word": "trap", "text": "Which word means to catch and hold someone?"}},
         {"narration": "Wukong had to travel far to find a celestial dragon to crack the cymbal open. It was a long battle!",
          "setting": "monkey riding to find help, dragon breaking golden cymbal",
          "q": {"t": "phonics", "word": "dragon", "letter": "d"}},
         {"narration": "The fake temple crumbled. They learned to be more careful and not trust everything they see.",
          "setting": "fake temple collapsing into dust, team looking wiser",
          "q": {"t": "make_ten", "text": "They've visited 7 kingdoms so far. How many more to reach 10?", "a": 7}},
     ]},
    {"num": 61, "title": "The Seven Spider Sisters Return", "title_cn": "蜘蛛精再现",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "The spider sisters found a powerful ally — a centipede demon with poison! They attacked again.",
          "setting": "spiders and centipede demon combining forces in a dark forest",
          "q": {"t": "addition", "text": "7 spider sisters plus 1 centipede demon. How many enemies total?", "a": 7, "b": 1, "obj_a": "spider", "obj_b": "bug"}},
         {"narration": "The poison made Wukong feel weak! He had to find the antidote before it was too late.",
          "setting": "monkey looking weak, searching through a garden for herbs",
          "q": {"t": "sight_words", "word": "medicine", "text": "Which word means something that makes you feel better when sick?"}},
         {"narration": "Sandy found the healing herb just in time! Wukong recovered and defeated all the demons.",
          "setting": "sandy bringing herb to monkey, monkey recovering and fighting",
          "q": {"t": "subtraction", "text": "8 demons attacked. Wukong defeated all 8. How many are left?", "a": 8, "b": 8, "obj": "monster"}},
     ]},
    {"num": 62, "title": "The Leopard Demon", "title_cn": "豹子精",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "A fast leopard demon attacked at night! He was almost as fast as Wukong.",
          "setting": "spotted leopard demon running at incredible speed in moonlight",
          "q": {"t": "general_knowledge", "text": "When did the leopard attack?", "options": ["At night", "At morning", "At noon", "At sunset"], "correct_answer": "At night"}},
         {"narration": "They chased each other across 6 mountains and 3 valleys. The leopard was tricky and kept hiding!",
          "setting": "monkey chasing leopard through various landscapes",
          "q": {"t": "addition", "text": "They crossed 6 mountains and 3 valleys. How many places total?", "a": 6, "b": 3, "obj_a": "mountain", "obj_b": "valley"}},
         {"narration": "Pigsy set a clever trap! The leopard ran right into it. Even fast demons can be outsmarted.",
          "setting": "pig character's trap catching the leopard demon",
          "q": {"t": "sight_words", "word": "clever", "text": "Which word means smart and quick-thinking?"}},
     ]},
    {"num": 63, "title": "The Golden Light Cave", "title_cn": "金光洞",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "A cave full of golden light appeared! Inside, a demon hoarded stolen treasures from villages.",
          "setting": "cave filled with golden light and piles of treasures",
          "q": {"t": "general_knowledge", "text": "What was the demon hoarding?", "options": ["Stolen treasures", "Stolen food", "Stolen horses", "Stolen books"], "correct_answer": "Stolen treasures"}},
         {"narration": "The demon could turn invisible! Wukong couldn't hit what he couldn't see.",
          "setting": "monkey swinging at air, invisible demon laughing",
          "q": {"t": "phonics", "word": "invisible", "letter": "i"}},
         {"narration": "Wukong used magic dust to reveal the invisible demon. Now he could see and defeat him!",
          "setting": "monkey throwing magical dust, demon becoming visible, getting hit",
          "q": {"t": "sight_words", "word": "reveal", "text": "Which word means to make something hidden become visible?"}},
         {"narration": "They returned all 15 stolen treasures to the villages. But 3 were broken. How many good ones were returned?",
          "setting": "villagers receiving their treasures back, thanking the travelers",
          "q": {"t": "subtraction", "text": "They found 15 treasures but 3 were broken. How many good ones?", "a": 15, "b": 3, "obj": "gem"}},
     ]},
    {"num": 64, "title": "The Ice Demon", "title_cn": "冰封妖",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "Everything was frozen solid! An Ice Demon had frozen a whole kingdom, including the king and his people.",
          "setting": "frozen kingdom, people frozen like ice statues",
          "q": {"t": "general_knowledge", "text": "What did the Ice Demon do to the kingdom?", "options": ["Froze everything", "Flooded it", "Burned it", "Made it disappear"], "correct_answer": "Froze everything"}},
         {"narration": "The Ice Demon shot 12 freezing beams! Even Wukong's staff got covered in ice.",
          "setting": "blue demon shooting ice beams, everything freezing",
          "q": {"t": "counting", "text": "How many freezing beams did the Ice Demon shoot?", "count": 12, "obj": "snowflake"}},
         {"narration": "Wukong remembered the Iron Fan Princess's fan! He borrowed it and blew warm wind to melt the ice.",
          "setting": "monkey using fan to blow warm wind, ice melting everywhere",
          "q": {"t": "phonics", "word": "melt", "letter": "m"}},
         {"narration": "The kingdom thawed and everyone came back to life! The Ice Demon melted away in the warmth.",
          "setting": "kingdom coming back to life, people moving again, sun shining",
          "q": {"t": "sight_words", "word": "warm", "text": "Which word means a nice hot feeling?"}},
     ]},
    {"num": 65, "title": "The Flame Phoenix", "title_cn": "火凤凰",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "A magnificent fire phoenix guarded the only bridge they needed to cross. It would burn anyone who came near!",
          "setting": "beautiful fire phoenix on a stone bridge, flames everywhere",
          "q": {"t": "general_knowledge", "text": "What did the fire phoenix guard?", "options": ["A bridge", "A cave", "A temple", "A river"], "correct_answer": "A bridge"}},
         {"narration": "Wukong tried to fight it, but every time it was hurt, it was reborn from the flames!",
          "setting": "phoenix rising from flames again and again, monkey frustrated",
          "q": {"t": "addition", "text": "The phoenix was reborn 5 times, then 3 more times. How many times total?", "a": 5, "b": 3, "obj_a": "flame", "obj_b": "flame"}},
         {"narration": "Tang Sanzang played a calming song on a flute. The phoenix became peaceful and let them cross!",
          "setting": "monk playing flute, phoenix becoming gentle, lowering its wings",
          "q": {"t": "phonics", "word": "flute", "letter": "f"}},
     ]},
    {"num": 66, "title": "The Sand Demon", "title_cn": "沙漠魔",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "They crossed a vast desert. The sand shifted and moved on its own — a sand demon controlled it!",
          "setting": "vast desert with sand swirling and forming shapes",
          "q": {"t": "sight_words", "word": "desert", "text": "Which word means a dry place with lots of sand?"}},
         {"narration": "The sand tried to bury them! Sandy used his water powers to turn the sand to mud.",
          "setting": "sandy using water magic, turning attacking sand into mud",
          "q": {"t": "general_knowledge", "text": "What did Sandy use to fight the sand?", "options": ["Water powers", "Fire powers", "Wind powers", "Lightning"], "correct_answer": "Water powers"}},
         {"narration": "The Sand Demon rose from the desert as a giant sand creature! Wukong smashed it with his staff.",
          "setting": "giant sand monster rising, monkey leaping to strike with staff",
          "q": {"t": "subtraction", "text": "The sand creature was 15 feet tall. Wukong smashed 8 feet off. How tall is it now?", "a": 15, "b": 8, "obj": "block"}},
     ]},
    {"num": 67, "title": "The Stone Kingdom", "title_cn": "石头国",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "A curse turned everyone in this kingdom to stone! Only children were left, scared and alone.",
          "setting": "stone statues of adults everywhere, scared children hiding",
          "q": {"t": "general_knowledge", "text": "Who was NOT turned to stone?", "options": ["The children", "The king", "The soldiers", "The monks"], "correct_answer": "The children"}},
         {"narration": "The curse was cast by a stone demon who lived in the mountain. Wukong went to confront him.",
          "setting": "monkey climbing a mountain towards a stone demon's lair",
          "q": {"t": "phonics", "word": "stone", "letter": "s"}},
         {"narration": "Wukong remembered — he was born from stone too! He used his stone magic to break the curse.",
          "setting": "monkey glowing with stone energy, statues turning back to people",
          "q": {"t": "sight_words", "word": "magic", "text": "Which word means supernatural power?"}},
         {"narration": "Families were reunited! 10 children hugged their parents again. Wukong was their hero.",
          "setting": "families reuniting, children hugging now-unfrozen parents",
          "q": {"t": "counting", "text": "How many children were reunited with their parents?", "count": 10, "obj": "child"}},
     ]},
    {"num": 68, "title": "The Thunder Giant", "title_cn": "雷公巨人",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "A giant made of thunder and lightning stood as tall as the mountains! Each step shook the earth.",
          "setting": "enormous glowing giant made of lightning standing between mountains",
          "q": {"t": "general_knowledge", "text": "What was the giant made of?", "options": ["Thunder and lightning", "Fire and smoke", "Ice and snow", "Rock and earth"], "correct_answer": "Thunder and lightning"}},
         {"narration": "Its lightning bolts destroyed 6 trees and 5 rocks nearby! Even Wukong's cloud couldn't get close.",
          "setting": "lightning bolts striking everywhere, monkey dodging on cloud",
          "q": {"t": "addition", "text": "The lightning destroyed 6 trees and 5 rocks. How many things were destroyed?", "a": 6, "b": 5, "obj_a": "tree", "obj_b": "rock"}},
         {"narration": "Pigsy had an idea! He threw mud at the giant. The mud blocked the lightning! Wukong struck the final blow.",
          "setting": "pig throwing mud, monkey striking mud-covered giant with staff",
          "q": {"t": "sight_words", "word": "idea", "text": "Which word means a thought or plan in your mind?"}},
     ]},

    # =====================================================================
    # Tier 6: Journey Road (stories 69-81, difficulty 5-6)
    # =====================================================================
    {"num": 69, "title": "The River of No Return", "title_cn": "无归河",
     "world": "journey_road", "difficulty": 5,
     "scenes": [
         {"narration": "A river that flows backwards! Anyone who falls in floats back to where they started their journey.",
          "setting": "strange river flowing backwards, swirling with time magic",
          "q": {"t": "general_knowledge", "text": "What happens if you fall in this river?", "options": ["Float back to the start", "Turn invisible", "Fall asleep", "Grow wings"], "correct_answer": "Float back to the start"}},
         {"narration": "Pigsy fell in and appeared back at the village where they found him! Oh no!",
          "setting": "pig character appearing in a distant village, confused",
          "q": {"t": "sight_words", "word": "return", "text": "Which word means to go back to where you came from?"}},
         {"narration": "Wukong flew to get Pigsy and bring him back. They found 10 stepping stones to cross safely.",
          "setting": "team carefully crossing river on magical stepping stones",
          "q": {"t": "counting", "text": "How many stepping stones did they use to cross?", "count": 10, "obj": "rock"}},
     ]},
    {"num": 70, "title": "The Dream Demon", "title_cn": "梦魔",
     "world": "journey_road", "difficulty": 5,
     "scenes": [
         {"narration": "Everyone fell asleep and couldn't wake up! A Dream Demon was trapping them in pleasant dreams.",
          "setting": "team sleeping in a field, dreamy mist around them",
          "q": {"t": "general_knowledge", "text": "What was the Dream Demon doing?", "options": ["Trapping people in dreams", "Stealing gold", "Breaking bridges", "Making storms"], "correct_answer": "Trapping people in dreams"}},
         {"narration": "In their dreams, each person saw what they wanted most. Pigsy dreamed of food, Sandy dreamed of peace.",
          "setting": "dream bubbles above sleeping characters showing their desires",
          "q": {"t": "general_knowledge", "text": "What did Pigsy dream about?", "options": ["Food", "Power", "Gold", "Adventure"], "correct_answer": "Food"}},
         {"narration": "But Wukong's golden eyes saw through the dream! He woke up and defeated the Dream Demon.",
          "setting": "monkey waking up with glowing eyes, dispelling dream mist",
          "q": {"t": "phonics", "word": "dream", "letter": "d"}},
         {"narration": "Everyone woke up and continued on. They learned that sometimes the easiest path is a trap.",
          "setting": "team getting up, shaking off sleep, continuing journey",
          "q": {"t": "sight_words", "word": "awake", "text": "Which word means no longer sleeping?"}},
     ]},
    {"num": 71, "title": "The Shadow Monster", "title_cn": "影子怪",
     "world": "journey_road", "difficulty": 5,
     "scenes": [
         {"narration": "A monster that lived in shadows attacked! When there was no light, it was invisible and powerful.",
          "setting": "dark shadows moving and attacking, glowing red eyes visible",
          "q": {"t": "general_knowledge", "text": "Where did the shadow monster live?", "options": ["In shadows", "In water", "In fire", "In trees"], "correct_answer": "In shadows"}},
         {"narration": "It grabbed Sandy and pulled him into the darkness! They needed light to fight it.",
          "setting": "sandy being dragged into shadows, others reaching for him",
          "q": {"t": "sight_words", "word": "shadow", "text": "Which word means the dark shape made when light is blocked?"}},
         {"narration": "Wukong called upon the sun! Bright light filled the area and the shadow monster shrank and disappeared.",
          "setting": "brilliant sunlight flooding the area, shadow creature dissolving",
          "q": {"t": "subtraction", "text": "The shadow made 14 copies of itself. The sunlight destroyed 14. How many are left?", "a": 14, "b": 14, "obj": "shadow"}},
     ]},
    {"num": 72, "title": "The Cloud Sea", "title_cn": "云海",
     "world": "journey_road", "difficulty": 5,
     "scenes": [
         {"narration": "They had to cross a sea made entirely of clouds! One wrong step and you'd fall through.",
          "setting": "vast sea of puffy white clouds, barely visible path",
          "q": {"t": "general_knowledge", "text": "What was the sea made of?", "options": ["Clouds", "Water", "Sand", "Ice"], "correct_answer": "Clouds"}},
         {"narration": "Wukong tested each cloud to find the solid ones. He found 8 solid clouds out of 13!",
          "setting": "monkey carefully stepping between clouds, testing each one",
          "q": {"t": "subtraction", "text": "Out of 13 clouds, 8 were solid. How many would you fall through?", "a": 13, "b": 8, "obj": "cloud"}},
         {"narration": "They all held hands and carefully walked across the cloud sea. Teamwork made it possible!",
          "setting": "team walking hand in hand across cloud path, beautiful sky around",
          "q": {"t": "sight_words", "word": "together", "text": "Which word means with each other, as a group?"}},
     ]},
    {"num": 73, "title": "The Mirror Lake", "title_cn": "镜湖",
     "world": "journey_road", "difficulty": 6,
     "scenes": [
         {"narration": "A lake that reflected everything perfectly. But the reflections could come to life!",
          "setting": "perfectly still mirror lake reflecting landscape and sky",
          "q": {"t": "general_knowledge", "text": "What was special about the lake?", "options": ["Reflections came to life", "It was made of gold", "It could talk", "It was on fire"], "correct_answer": "Reflections came to life"}},
         {"narration": "Evil copies of Wukong, Pigsy, and Sandy emerged from the lake! They had to fight themselves!",
          "setting": "dark copies of the heroes emerging from lake water",
          "q": {"t": "counting", "text": "How many evil copies emerged from the lake?", "count": 3, "obj": "monster"}},
         {"narration": "They won by working together! The copies couldn't cooperate like the real team could.",
          "setting": "real team fighting in formation, defeating disorganized copies",
          "q": {"t": "subtraction", "text": "3 copies attacked. The real team defeated all 3. How many copies remain?", "a": 3, "b": 3, "obj": "monster"}},
     ]},
    {"num": 74, "title": "The Crystal Cave", "title_cn": "水晶洞",
     "world": "journey_road", "difficulty": 6,
     "scenes": [
         {"narration": "A cave made entirely of crystal! Beautiful but dangerous — the crystals could trap you inside.",
          "setting": "stunning cave made of colorful crystals, beautiful but eerie",
          "q": {"t": "general_knowledge", "text": "What was the cave made of?", "options": ["Crystal", "Gold", "Ice", "Diamond"], "correct_answer": "Crystal"}},
         {"narration": "Tang Sanzang touched a crystal and his hand got stuck! The cave was alive and hungry.",
          "setting": "monk's hand stuck to crystal, cave walls slowly closing in",
          "q": {"t": "sight_words", "word": "stuck", "text": "Which word means unable to move from a place?"}},
         {"narration": "Wukong used his staff to shatter the magic crystal at the cave's heart. All the crystals crumbled!",
          "setting": "monkey striking a central crystal, entire cave breaking apart",
          "q": {"t": "phonics", "word": "crystal", "letter": "c"}},
         {"narration": "They escaped just in time! The cave collapsed behind them as they ran.",
          "setting": "team running out of collapsing cave, light ahead",
          "q": {"t": "subtraction", "text": "They had 18 seconds to escape. They used 11 seconds. How many seconds to spare?", "a": 18, "b": 11, "obj": "star"}},
     ]},
    {"num": 75, "title": "The Maze Mountains", "title_cn": "迷宫山",
     "world": "journey_road", "difficulty": 6,
     "scenes": [
         {"narration": "The mountains ahead formed a natural maze! Every path looked the same and they kept going in circles.",
          "setting": "confusing mountain paths that look identical, team lost",
          "q": {"t": "general_knowledge", "text": "What did the mountains form?", "options": ["A maze", "A bridge", "A lake", "A wall"], "correct_answer": "A maze"}},
         {"narration": "Wukong flew up high to see the whole maze from above. He counted 12 paths but only 1 was correct!",
          "setting": "monkey high in sky looking down at mountain maze pattern",
          "q": {"t": "subtraction", "text": "There were 12 paths but only 1 was correct. How many wrong paths?", "a": 12, "b": 1, "obj": "path"}},
         {"narration": "He guided the team through the twisting paths. Left, right, straight, left — they made it through!",
          "setting": "team following monkey's directions through mountain maze, exit visible",
          "q": {"t": "counting", "text": "Wukong gave directions: left, right, straight, left. How many directions?", "count": 4, "obj": "arrow"}},
     ]},
    {"num": 76, "title": "The Wind Valley", "title_cn": "风之谷",
     "world": "journey_road", "difficulty": 6,
     "scenes": [
         {"narration": "A valley where the wind never stopped blowing! It was so strong that nobody could walk through.",
          "setting": "valley with incredibly powerful wind, trees bent sideways",
          "q": {"t": "sight_words", "word": "wind", "text": "Which word means moving air?"}},
         {"narration": "The wind demon laughed as they tried to push through. Even Wukong was blown backwards!",
          "setting": "wind demon in sky laughing, monkey being blown back",
          "q": {"t": "phonics", "word": "blow", "letter": "b"}},
         {"narration": "Sandy found 6 heavy rocks and they tied themselves together. Step by step, they pushed through the wind!",
          "setting": "team tied together with ropes, pushing against wind with rocks",
          "q": {"t": "counting", "text": "How many heavy rocks did Sandy find?", "count": 6, "obj": "rock"}},
     ]},
    {"num": 77, "title": "The Five Finger Mountain Return", "title_cn": "再回五指山",
     "world": "journey_road", "difficulty": 6,
     "scenes": [
         {"narration": "They passed by the mountain where Wukong was trapped for 500 years. He felt sad and grateful.",
          "setting": "monkey looking at a familiar mountain with mixed emotions",
          "q": {"t": "general_knowledge", "text": "How long was Wukong trapped under the mountain?", "options": ["500 years", "100 years", "50 years", "1000 years"], "correct_answer": "500 years"}},
         {"narration": "Wukong thought about how much he had changed. He used to be wild and selfish, but now he cared about his friends.",
          "setting": "monkey meditating near the mountain, memories floating around him",
          "q": {"t": "sight_words", "word": "change", "text": "Which word means to become different?"}},
         {"narration": "He placed a peach at the base of the mountain as thanks. Without those 500 years, he wouldn't be who he is today.",
          "setting": "monkey placing a peach at mountain base, warm golden light",
          "q": {"t": "counting", "text": "How many peaches did Wukong place at the mountain?", "count": 1, "obj": "peach"}},
     ]},
    {"num": 78, "title": "The Gate of Thunder", "title_cn": "雷音门",
     "world": "journey_road", "difficulty": 6,
     "scenes": [
         {"narration": "They finally saw it in the distance — the Holy Mountain where the scriptures were kept!",
          "setting": "majestic holy mountain visible in distance, golden light",
          "q": {"t": "sight_words", "word": "mountain", "text": "Which word means a very tall piece of land?"}},
         {"narration": "But one final test remained: the Gate of Thunder! Only those with pure hearts could pass through.",
          "setting": "massive gate crackling with energy, bright and intimidating",
          "q": {"t": "general_knowledge", "text": "What kind of heart did you need to pass the gate?", "options": ["A pure heart", "A strong heart", "A fast heart", "A brave heart"], "correct_answer": "A pure heart"}},
         {"narration": "Tang Sanzang walked through bravely. Wukong, Pigsy, and Sandy followed. Their hearts were true!",
          "setting": "team walking through glowing gate together, light washing over them",
          "q": {"t": "counting", "text": "How many team members walked through the gate? Tang Sanzang, Wukong, Pigsy, and Sandy.", "count": 4, "obj": "star"}},
     ]},
    {"num": 79, "title": "Crossing the Final River", "title_cn": "渡过通天河",
     "world": "journey_road", "difficulty": 6,
     "scenes": [
         {"narration": "One last river to cross! A holy turtle appeared and offered to carry them across.",
          "setting": "giant ancient turtle in a wide holy river, golden mist",
          "q": {"t": "general_knowledge", "text": "What offered to carry them across the river?", "options": ["A holy turtle", "A dragon", "A boat", "A fish"], "correct_answer": "A holy turtle"}},
         {"narration": "As they crossed, the turtle asked if Tang Sanzang remembered to ask Buddha a question for him.",
          "setting": "turtle carrying travelers across river, asking a question",
          "q": {"t": "phonics", "word": "turtle", "letter": "t"}},
         {"narration": "Tang Sanzang forgot! The turtle was upset and dumped them in the water. All the scriptures got wet!",
          "setting": "travelers falling into water, scrolls getting wet",
          "q": {"t": "sight_words", "word": "forgot", "text": "Which word means you didn't remember?"}},
         {"narration": "They dried the scriptures in the sun. A few pages were lost, but most were saved. Almost there!",
          "setting": "team drying scrolls on rocks in sunshine, relieved",
          "q": {"t": "subtraction", "text": "They had 20 scrolls. 3 were damaged. How many good scrolls remain?", "a": 20, "b": 3, "obj": "scroll"}},
     ]},
    {"num": 80, "title": "The Holy Mountain", "title_cn": "灵山",
     "world": "journey_road", "difficulty": 6,
     "scenes": [
         {"narration": "They climbed the Holy Mountain! Clouds parted to reveal a magnificent golden temple at the top.",
          "setting": "travelers climbing mountain stairs through clouds towards golden temple",
          "q": {"t": "sight_words", "word": "climb", "text": "Which word means to go up something high?"}},
         {"narration": "The Buddha himself welcomed them! After 14 years of travel, they finally arrived.",
          "setting": "buddha welcoming the travelers in a grand golden hall",
          "q": {"t": "general_knowledge", "text": "How many years did the journey take?", "options": ["14 years", "7 years", "3 years", "100 years"], "correct_answer": "14 years"}},
         {"narration": "The Buddha gave them the holy scriptures — thousands of pages of wisdom and kindness!",
          "setting": "monk receiving glowing scrolls from buddha, tears of joy",
          "q": {"t": "phonics", "word": "wisdom", "letter": "w"}},
         {"narration": "But wait — the first set of scriptures were blank! They had to go back and get the real ones.",
          "setting": "monk opening scroll to find blank pages, looking confused",
          "q": {"t": "general_knowledge", "text": "What was wrong with the first scriptures?", "options": ["They were blank", "They were torn", "They were wet", "They were lost"], "correct_answer": "They were blank"}},
     ]},
    {"num": 81, "title": "Journey Complete", "title_cn": "功德圆满",
     "world": "journey_road", "difficulty": 6,
     "scenes": [
         {"narration": "With the real scriptures in hand, they began the long journey home. But this time, they flew on a cloud!",
          "setting": "team flying on a golden cloud over beautiful landscape, carrying scrolls",
          "q": {"t": "general_knowledge", "text": "How did they travel home?", "options": ["On a cloud", "On a horse", "On foot", "On a boat"], "correct_answer": "On a cloud"}},
         {"narration": "They brought the scriptures back to China! The Emperor and all the people celebrated.",
          "setting": "grand celebration in ancient Chinese palace, scrolls on display",
          "q": {"t": "sight_words", "word": "celebrate", "text": "Which word means to have a party because something good happened?"}},
         {"narration": "As a reward for their devotion, the Buddha made each of them a heavenly being. Wukong became the Victorious Fighting Buddha!",
          "setting": "wukong ascending to heaven in golden light, becoming a buddha",
          "q": {"t": "general_knowledge", "text": "What did Wukong become?", "options": ["The Victorious Fighting Buddha", "The Monkey King", "The Jade Emperor", "A dragon"], "correct_answer": "The Victorious Fighting Buddha"}},
         {"narration": "Tang Sanzang, Wukong, Pigsy, Sandy, and the dragon horse — they all found peace. The journey of 81 tribulations was complete!",
          "setting": "five characters standing together in heaven, peaceful and happy, golden light",
          "q": {"t": "counting", "text": "How many heroes completed the journey? Tang Sanzang, Wukong, Pigsy, Sandy, and the dragon horse.", "count": 5, "obj": "star"}},
         {"narration": "And so, the greatest adventure ever told came to an end. But the wisdom they found will last forever!",
          "setting": "scroll closing with the words The End, surrounded by clouds and stars",
          "q": {"t": "addition", "text": "They faced 81 tribulations and won them all! If 40 were easy and 41 were hard, how many total?", "a": 40, "b": 41, "obj_a": "star", "obj_b": "star"}},
     ]},
]

# ---------------------------------------------------------------------------
# World config for number ranges and objects
# ---------------------------------------------------------------------------

WORLD_CONFIGS = {
    "flower_fruit_mountain": {"num_range": (1, 5), "options": 3, "objects": ["peach", "monkey", "banana", "flower", "coconut"], "diff_range": (1, 2)},
    "dragon_palace":         {"num_range": (1, 8), "options": 3, "objects": ["fish", "shell", "pearl", "gem", "coral"], "diff_range": (1, 2)},
    "heaven_palace":         {"num_range": (1, 10), "options": 4, "objects": ["star", "cloud", "gem", "moon", "lantern"], "diff_range": (2, 3)},
    "white_bone_cave":       {"num_range": (5, 15), "options": 4, "objects": ["bone", "mask", "mirror", "candle", "scroll"], "diff_range": (2, 4)},
    "flaming_mountain":      {"num_range": (5, 18), "options": 4, "objects": ["flame", "fan", "rock", "ember", "spark"], "diff_range": (3, 4)},
    "journey_road":          {"num_range": (10, 20), "options": 4, "objects": ["scroll", "staff", "hat", "gem", "star"], "diff_range": (3, 5)},
}

# ---------------------------------------------------------------------------
# Image prompt generation — improved with character descriptions and art style
# ---------------------------------------------------------------------------

CHARACTER_DESCRIPTIONS = {
    "wukong": "Sun Wukong the Monkey King — golden-furred monkey wearing golden armor and a golden headband, carrying a golden iron staff",
    "tang_sanzang": "Tang Sanzang the monk — kind bald monk in flowing orange Buddhist robes, riding a white horse",
    "pigsy": "Zhu Bajie (Pigsy) — a large jolly pig-man in dark robes carrying a nine-tooth rake",
    "sandy": "Sha Wujing (Sandy) — a tall blue-skinned warrior monk with a necklace of skulls, carrying a monk's spade",
    "dragon_horse": "a beautiful white horse with a flowing silver mane (actually a dragon prince)",
}

WORLD_SETTINGS = {
    "flower_fruit_mountain": "lush tropical mountain with waterfalls, peach trees, and cherry blossoms, misty peaks",
    "dragon_palace": "magnificent underwater crystal palace with colorful coral reefs, glowing jellyfish, and schools of fish",
    "heaven_palace": "majestic heavenly palace above golden clouds with towering jade pillars and celestial bridges",
    "white_bone_cave": "dark mysterious cavern with glowing purple crystals, ancient bones, and flickering torchlight",
    "flaming_mountain": "fiery volcanic mountain with rivers of lava, red sky, and dramatic rock formations",
    "journey_road": "ancient Silk Road winding through dramatic mountain passes towards a distant golden temple",
}

IMAGE_STYLE = (
    "Studio Ghibli inspired, child-friendly watercolor illustration, soft warm lighting, "
    "vibrant saturated colors, gentle brush strokes, magical atmosphere, "
    "Chinese mythology Journey to the West theme, 16:9 aspect ratio, "
    "no text, no watermark, no realistic photos, safe for children"
)


def generate_image_prompt(scene_setting, world_id, narration=""):
    """Generate a detailed image prompt for a scene."""
    world_bg = WORLD_SETTINGS.get(world_id, "ancient Chinese landscape")

    # Extract likely characters from narration
    chars = []
    narr_lower = narration.lower()
    if "wukong" in narr_lower or "monkey" in narr_lower:
        chars.append(CHARACTER_DESCRIPTIONS["wukong"])
    if "tang" in narr_lower or " monk " in narr_lower or "the monk" in narr_lower or "sanzang" in narr_lower:
        chars.append(CHARACTER_DESCRIPTIONS["tang_sanzang"])
    if "pigsy" in narr_lower or "pig" in narr_lower or "bajie" in narr_lower:
        chars.append(CHARACTER_DESCRIPTIONS["pigsy"])
    if "sandy" in narr_lower or "sha" in narr_lower:
        chars.append(CHARACTER_DESCRIPTIONS["sandy"])

    char_str = "; ".join(chars) if chars else "fantasy characters"

    return f"{scene_setting}. Characters: {char_str}. Background: {world_bg}. Style: {IMAGE_STYLE}"


# ---------------------------------------------------------------------------
# Question generation from seed
# ---------------------------------------------------------------------------

SIGHT_WORDS_OPTIONS = {
    "play": ["play", "stop", "sleep", "sit"],
    "king": ["king", "fish", "tree", "rock"],
    "book": ["book", "door", "rock", "fish"],
    "home": ["home", "rock", "fish", "moon"],
    "read": ["read", "jump", "swim", "fly"],
    "gold": ["gold", "blue", "red", "dark"],
    "angry": ["angry", "happy", "sleepy", "cold"],
    "fight": ["fight", "sleep", "cook", "sing"],
    "eat": ["eat", "run", "fly", "sit"],
    "break": ["break", "build", "sleep", "sing"],
    "wait": ["wait", "run", "eat", "fly"],
    "help": ["help", "hide", "sleep", "eat"],
    "brave": ["brave", "tired", "cold", "slow"],
    "scared": ["scared", "happy", "hungry", "tall"],
    "dark": ["dark", "light", "fast", "tall"],
    "water": ["water", "fire", "wind", "earth"],
    "safe": ["safe", "lost", "cold", "dark"],
    "friend": ["friend", "rock", "cloud", "tree"],
    "real": ["real", "fake", "old", "new"],
    "dive": ["dive", "fly", "run", "sit"],
    "catch": ["catch", "throw", "drop", "hide"],
    "light": ["light", "dark", "cold", "slow"],
    "happy": ["happy", "sad", "angry", "cold"],
    "search": ["search", "sleep", "sit", "eat"],
    "fast": ["fast", "slow", "tall", "old"],
    "cry": ["cry", "laugh", "run", "eat"],
    "same": ["same", "big", "old", "fast"],
    "giant": ["giant", "tiny", "fast", "old"],
    "polite": ["polite", "rude", "fast", "old"],
    "blind": ["blind", "deaf", "tall", "fast"],
    "inside": ["inside", "outside", "above", "below"],
    "escape": ["escape", "arrive", "sleep", "eat"],
    "peace": ["peace", "war", "fire", "dark"],
    "trick": ["trick", "help", "sing", "cook"],
    "sleep": ["sleep", "run", "eat", "fly"],
    "trapped": ["trapped", "free", "fast", "old"],
    "stuck": ["stuck", "free", "fast", "old"],
    "sharp": ["sharp", "smooth", "soft", "round"],
    "warm": ["warm", "cold", "fast", "old"],
    "magic": ["magic", "boring", "cold", "slow"],
    "desert": ["desert", "forest", "ocean", "sky"],
    "clever": ["clever", "silly", "slow", "old"],
    "idea": ["idea", "rock", "fish", "tree"],
    "rescue": ["rescue", "leave", "hide", "sleep"],
    "reveal": ["reveal", "hide", "sleep", "run"],
    "shadow": ["shadow", "light", "fire", "water"],
    "together": ["together", "alone", "fast", "old"],
    "return": ["return", "leave", "sleep", "fly"],
    "awake": ["awake", "asleep", "cold", "fast"],
    "wind": ["wind", "fire", "rock", "water"],
    "change": ["change", "stay", "sleep", "sit"],
    "mountain": ["mountain", "river", "tree", "rock"],
    "climb": ["climb", "fall", "sit", "sleep"],
    "celebrate": ["celebrate", "cry", "sleep", "hide"],
    "forgot": ["forgot", "recalled", "slept", "ran"],
    "listen": ["listen", "talk", "run", "eat"],
    "medicine": ["medicine", "poison", "food", "water"],
    "alive": ["alive", "asleep", "angry", "alone"],
}

PHONICS_MAP = {
    "j": ("j", "/j/"), "r": ("r", "/r/"), "c": ("c", "/k/"), "s": ("s", "/s/"),
    "o": ("o", "/o/"), "f": ("f", "/f/"), "h": ("h", "/h/"), "m": ("m", "/m/"),
    "b": ("b", "/b/"), "w": ("w", "/w/"), "d": ("d", "/d/"), "p": ("p", "/p/"),
    "g": ("g", "/g/"), "l": ("l", "/l/"), "t": ("t", "/t/"), "i": ("i", "/i/"),
    "n": ("n", "/n/"),
}


def generate_question_from_seed(seed, difficulty, world_id):
    """Generate a LevelQuestion from a scene's question seed."""
    t = seed["t"]
    world_cfg = WORLD_CONFIGS.get(world_id, WORLD_CONFIGS["flower_fruit_mountain"])
    num_options = world_cfg["options"]

    if t == "counting":
        count = seed["count"]
        obj = seed.get("obj", "star")
        text = seed["text"]
        wrongs = make_wrong_options(count, num_options - 1, max(0, count - 3), count + 4)
        options = [count] + wrongs
        random.shuffle(options)
        return t, {
            "text": text,
            "visual_objects": [obj] * count,
            "options": options,
            "correct_answer": count,
        }

    elif t == "addition":
        a, b = seed["a"], seed["b"]
        answer = a + b
        text = seed["text"]
        obj_a = seed.get("obj_a", "star")
        obj_b = seed.get("obj_b", "star")
        wrongs = make_wrong_options(answer, num_options - 1, max(0, answer - 4), answer + 5)
        options = [answer] + wrongs
        random.shuffle(options)
        vis = [obj_a] * a + ["|"] + [obj_b] * b
        return t, {
            "text": text,
            "visual_objects": vis,
            "options": options,
            "correct_answer": answer,
        }

    elif t == "subtraction":
        a, b = seed["a"], seed["b"]
        answer = a - b
        text = seed["text"]
        obj = seed.get("obj", "star")
        wrongs = make_wrong_options(answer, num_options - 1, max(0, answer - 3), answer + 5)
        options = [answer] + wrongs
        random.shuffle(options)
        vis = [obj] * a
        return t, {
            "text": text,
            "visual_objects": vis,
            "options": options,
            "correct_answer": answer,
        }

    elif t == "comparison":
        text = seed["text"]
        left = seed["left"]
        right = seed["right"]
        correct = len(left) if len(left) >= len(right) else len(right)
        vis = left + ["|"] + right
        wrongs = make_wrong_options(correct, num_options - 1, max(1, correct - 3), correct + 4)
        options = [correct] + wrongs
        random.shuffle(options)
        return t, {
            "text": text,
            "visual_objects": vis,
            "options": options,
            "correct_answer": correct,
        }

    elif t == "sight_words":
        word = seed["word"]
        text = seed.get("text", f"Which word is '{word}'?")
        opts = SIGHT_WORDS_OPTIONS.get(word, [word, "cat", "dog", "run"])
        random.shuffle(opts)
        return t, {
            "text": text,
            "visual_objects": [],
            "options": opts,
            "correct_answer": word,
        }

    elif t == "phonics":
        word = seed["word"]
        letter = seed["letter"]
        letter_name, sound = PHONICS_MAP.get(letter, (letter, f"/{letter}/"))
        text = f"What sound does '{word}' start with?"
        # Build wrong options from other letters
        all_letters = [l for l in PHONICS_MAP if l != letter]
        random.shuffle(all_letters)
        wrong_sounds = [PHONICS_MAP[l][1] for l in all_letters[:num_options - 1]]
        opts = [sound] + wrong_sounds
        random.shuffle(opts)
        return t, {
            "text": text,
            "visual_objects": [],
            "options": opts,
            "correct_answer": sound,
        }

    elif t == "general_knowledge":
        text = seed["text"]
        opts = seed["options"]
        correct = seed["correct_answer"]
        random.shuffle(opts)
        return t, {
            "text": text,
            "visual_objects": [],
            "options": opts,
            "correct_answer": correct,
        }

    elif t == "make_ten":
        a = seed["a"]
        answer = 10 - a
        text = seed.get("text", f"Wukong has {a}. How many more to make 10?")
        wrongs = make_wrong_options(answer, num_options - 1, max(0, answer - 3), answer + 4)
        options = [answer] + wrongs
        random.shuffle(options)
        return t, {
            "text": text,
            "visual_objects": ["star"] * a,
            "options": options,
            "correct_answer": answer,
        }

    else:
        # Fallback: use existing generators for complex types
        d = max(world_cfg["diff_range"][0], min(world_cfg["diff_range"][1], difficulty))
        gen_func = GENERATORS.get(t, GENERATORS["counting"])
        question = gen_func(world_cfg, d)
        question = {k: v for k, v in question.items() if v is not None}
        return t, question


# ---------------------------------------------------------------------------
# Hint bank
# ---------------------------------------------------------------------------

STORY_HINTS = {
    "counting": ["Count each one carefully!", "Point to each one as you count!"],
    "addition": ["Add the two groups together!", "Count all of them!"],
    "subtraction": ["Take away the second number!", "How many are left?"],
    "comparison": ["Which side has more?", "Count both groups!"],
    "sight_words": ["Sound out the word!", "Which word matches?"],
    "phonics": ["Listen to the first sound!", "What letter makes that sound?"],
    "general_knowledge": ["Think about the story!", "Remember what happened!"],
    "make_ten": ["What number plus this equals 10?", "Count up from the number to 10!"],
}

CHARACTERS = ["wukong", "pigsy", "sandy", "tripitaka"]
REWARD_DIALOGUES = [
    "Great job!", "Amazing!", "You're so smart!",
    "Wonderful!", "Keep going!", "Brilliant work!",
    "Wukong is proud of you!", "You did it!", "Fantastic!",
    "One step closer to the scriptures!",
]


# ---------------------------------------------------------------------------
# Main generation
# ---------------------------------------------------------------------------

def generate_all_stories():
    stories = []

    for trib in TRIBULATIONS:
        story_num = trib["num"]
        story_id = f"story_{story_num:02d}"
        difficulty = trib["difficulty"]
        world_id = trib["world"]

        scenes = []
        for s_idx, scene_data in enumerate(trib["scenes"]):
            scene_id = f"{story_id}_s{s_idx + 1}"

            seed = scene_data["q"]
            game_type, question = generate_question_from_seed(seed, difficulty, world_id)

            hints = STORY_HINTS.get(game_type, HINT_BANK.get(game_type, ["Take your time!", "Look carefully!"]))

            image_prompt = generate_image_prompt(
                scene_data["setting"], world_id, scene_data["narration"]
            )

            scenes.append({
                "scene_id": scene_id,
                "narration": scene_data["narration"],
                "background_image": f"images/stories/{scene_id}.png",
                "image_prompt": image_prompt,
                "game_type": game_type,
                "question": question,
                "hints": hints,
            })

        peach_reward = min(5, 2 + difficulty // 2)

        stories.append({
            "id": story_id,
            "title": trib["title"],
            "title_cn": trib["title_cn"],
            "tribulation_number": story_num,
            "difficulty": difficulty,
            "world": world_id,
            "scenes": scenes,
            "reward": {
                "peaches": peach_reward,
                "animation": "celebrate",
                "dialogue": random.choice(REWARD_DIALOGUES),
                "character": random.choice(CHARACTERS),
            },
        })

    return stories


def print_stats(stories):
    print(f"\nTotal stories: {len(stories)}")
    total_scenes = sum(len(s["scenes"]) for s in stories)
    print(f"Total scenes: {total_scenes}")
    print(f"Average scenes per story: {total_scenes / len(stories):.1f}")

    from collections import Counter
    worlds = Counter(s["world"] for s in stories)
    print("\nStories by world:")
    for w, c in worlds.most_common():
        print(f"  {w}: {c}")

    diffs = Counter(s["difficulty"] for s in stories)
    print("\nStories by difficulty:")
    for d in sorted(diffs):
        print(f"  Difficulty {d}: {diffs[d]}")

    game_types = Counter()
    for s in stories:
        for sc in s["scenes"]:
            game_types[sc["game_type"]] += 1
    print(f"\nGame type distribution ({total_scenes} scenes):")
    for gt, c in game_types.most_common():
        print(f"  {gt}: {c} ({c / total_scenes * 100:.0f}%)")


def export_image_prompts(stories):
    """Export all image prompts to a text file for batch image generation."""
    prompts = []
    for story in stories:
        prompts.append(f"\n{'='*60}")
        prompts.append(f"Story {story['tribulation_number']}: {story['title']} ({story['title_cn']})")
        prompts.append(f"World: {story['world']} | Difficulty: {story['difficulty']}")
        prompts.append(f"{'='*60}")
        for scene in story["scenes"]:
            prompts.append(f"\n[{scene['scene_id']}]")
            prompts.append(f"File: {scene['background_image']}")
            prompts.append(f"Narration: {scene['narration'][:80]}...")
            prompts.append(f"Prompt: {scene['image_prompt']}")

    output_path = Path(__file__).parent.parent / "data" / "image_prompts.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(prompts))
    print(f"\nImage prompts written to {output_path}")
    return output_path


if __name__ == "__main__":
    stories = generate_all_stories()
    print_stats(stories)

    # Write to backend/data
    backend_path = Path(__file__).parent.parent / "data" / "stories.json"
    backend_path.parent.mkdir(parents=True, exist_ok=True)
    with open(backend_path, "w", encoding="utf-8") as f:
        json.dump(stories, f, indent=2, ensure_ascii=False)
    print(f"\nWritten to {backend_path}")

    # Copy to frontend/src/data
    frontend_path = Path(__file__).parent.parent.parent / "frontend" / "src" / "data" / "stories.json"
    frontend_path.parent.mkdir(parents=True, exist_ok=True)
    import shutil
    shutil.copy2(backend_path, frontend_path)
    print(f"Copied to {frontend_path}")

    # Export image prompts
    export_image_prompts(stories)
