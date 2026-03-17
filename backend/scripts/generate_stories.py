"""Generate 81 Journey to the West story adventures with embedded game questions."""

import json
import random
import shutil
from pathlib import Path

random.seed(99)  # reproducible, different seed from levels

# ---------------------------------------------------------------------------
# Reuse generators from regenerate_levels.py
# ---------------------------------------------------------------------------
# We import the generator functions and data banks
import sys
sys.path.insert(0, str(Path(__file__).parent))
from regenerate_levels import (
    GENERATORS, SIGHT_WORDS_TIER1, PHONICS_LETTER_BANK, PHONICS_CONSONANTS,
    GK_QUESTIONS, HINT_BANK, make_wrong_options,
)

# ---------------------------------------------------------------------------
# 81 Tribulations of Journey to the West
# ---------------------------------------------------------------------------

TRIBULATIONS = [
    # Tier 1: Flower Fruit Mountain (stories 1-14, difficulty 1)
    {"num": 1, "title": "The Stone Monkey is Born", "title_cn": "石猴出世",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "Long ago, on top of a beautiful mountain, there was a magical stone. One day, the stone cracked open and a baby monkey jumped out!", "setting": "mountain peak with a glowing cracked stone, golden light, cherry blossoms"},
         {"narration": "The baby monkey opened his eyes and looked around. He saw trees, flowers, and waterfalls everywhere!", "setting": "lush mountain forest with waterfalls and colorful flowers"},
         {"narration": "Other monkeys came running to see him. They were amazed! The stone monkey could already jump and climb!", "setting": "group of monkeys gathered around baby monkey on mountain"},
         {"narration": "The monkeys cheered and danced. They had a new friend! The stone monkey smiled and played with them.", "setting": "monkeys celebrating and dancing on a mountain meadow"},
     ]},
    {"num": 2, "title": "King of the Monkeys", "title_cn": "美猴王",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "The monkeys found a beautiful waterfall. Behind it, there must be a cave! But who would dare jump through?", "setting": "monkeys standing before a massive waterfall on a mountain"},
         {"narration": "The stone monkey bravely jumped through the waterfall! Splash! He found a wonderful cave inside.", "setting": "monkey jumping through a waterfall into a sparkling cave"},
         {"narration": "The cave was full of stone chairs, stone beds, and even stone cups! It was a perfect home.", "setting": "inside a beautiful stone cave with natural furniture"},
         {"narration": "The monkeys made him their king! From now on, he was called the Handsome Monkey King.", "setting": "monkey sitting on a stone throne with a crown, other monkeys bowing"},
     ]},
    {"num": 3, "title": "Seeking Immortality", "title_cn": "拜师学艺",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "The Monkey King was worried. He didn't want to grow old. He decided to find a teacher who could teach him magic!", "setting": "monkey king looking thoughtful at sunset on mountain"},
         {"narration": "He built a raft and sailed across the wide ocean. The waves were big, but he was brave!", "setting": "monkey on a small raft sailing across a vast ocean"},
         {"narration": "After a long journey, he found Master Subhuti on a mountain. The master agreed to teach him!", "setting": "monkey kneeling before an old wise master in a temple"},
     ]},
    {"num": 4, "title": "Learning 72 Transformations", "title_cn": "学会七十二变",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "Master Subhuti taught Wukong many magical spells. Wukong studied hard every day!", "setting": "monkey studying scrolls in a temple classroom"},
         {"narration": "Wukong learned to transform into 72 different things! He could become a bird, a fish, or even a tree!", "setting": "monkey surrounded by magical transformation clouds, showing bird and fish forms"},
         {"narration": "He also learned to ride on clouds! He called it the Cloud Somersault. One jump could take him 108,000 miles!", "setting": "monkey joyfully flying on a golden cloud high in the sky"},
     ]},
    {"num": 5, "title": "Return to Flower Fruit Mountain", "title_cn": "重返花果山",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "Wukong flew back to Flower Fruit Mountain on his cloud. His monkey friends were so happy to see him!", "setting": "monkey flying on cloud towards a beautiful mountain"},
         {"narration": "But a monster had taken over their cave! The monkeys were scared and hiding.", "setting": "monkeys hiding behind rocks, looking scared"},
         {"narration": "Wukong was angry! He used his magic to chase the monster away. The cave was theirs again!", "setting": "monkey king fighting a demon with magical golden light"},
         {"narration": "The monkeys celebrated! Their king was back and stronger than ever!", "setting": "monkeys celebrating with fireworks on the mountain"},
     ]},
    {"num": 6, "title": "The Magic Weapon", "title_cn": "寻找兵器",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "Wukong needed a weapon. He was strong, but he needed something special to fight monsters!", "setting": "monkey king practicing martial arts moves on a mountain"},
         {"narration": "His monkey friends told him about the Dragon King who lived under the ocean. He had many magic weapons!", "setting": "monkeys pointing towards the ocean, with underwater palace visible"},
         {"narration": "Wukong dove into the ocean! He swam deeper and deeper until he reached the Dragon Palace.", "setting": "monkey swimming down through clear blue ocean water"},
     ]},
    {"num": 7, "title": "The Golden Staff", "title_cn": "如意金箍棒",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "In the Dragon Palace, Wukong tried many weapons. Swords, spears, and axes — none felt right!", "setting": "monkey testing various weapons in an underwater armory"},
         {"narration": "Then he saw a glowing pillar in the corner. It was the Ruyi Jingu Bang — a magical iron staff!", "setting": "glowing golden staff/pillar in an underwater palace, radiating light"},
         {"narration": "The staff could grow big or shrink small! Wukong shrunk it to the size of a needle and put it behind his ear.", "setting": "monkey holding a golden staff that glows, looking happy"},
         {"narration": "The Dragon King was not happy, but Wukong flew away with his new weapon! Now he was ready for anything!", "setting": "monkey flying away from underwater palace on a cloud, staff in hand"},
     ]},
    {"num": 8, "title": "Erasing Names from Death", "title_cn": "大闹地府",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "One night, two scary guards came to take Wukong to the Underworld. They said it was his time!", "setting": "two dark ghost guards approaching monkey at night"},
         {"narration": "Wukong was not afraid! He followed them to the Underworld and found the Book of Life and Death.", "setting": "monkey in a dark palace looking at a large ancient book"},
         {"narration": "He crossed out his name and all the monkeys' names from the book! Now they would live forever!", "setting": "monkey crossing out names in a glowing book with a brush"},
     ]},
    {"num": 9, "title": "The Jade Emperor's Invitation", "title_cn": "天庭招安",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "The Jade Emperor in Heaven heard about Wukong. He was worried about this powerful monkey!", "setting": "jade emperor on golden throne in heavenly palace, looking concerned"},
         {"narration": "He sent a messenger to invite Wukong to Heaven. Maybe they could give him a job to keep him happy!", "setting": "heavenly messenger flying down to the mountain on a cloud"},
         {"narration": "Wukong was excited! He flew up to Heaven on his cloud to see the beautiful palace.", "setting": "monkey flying through clouds towards a magnificent golden palace"},
     ]},
    {"num": 10, "title": "The Horse Keeper", "title_cn": "弼马温",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "The Jade Emperor gave Wukong a job — taking care of the heavenly horses! But it was the lowest job in Heaven.", "setting": "monkey in stable surrounded by beautiful white heavenly horses"},
         {"narration": "When Wukong found out it was a tiny, unimportant job, he was furious!", "setting": "angry monkey with flames around him in the heavenly stable"},
         {"narration": "He quit the job and flew back home. He called himself the Great Sage Equal to Heaven!", "setting": "monkey planting a flag on mountain that reads Great Sage Equal to Heaven"},
     ]},
    {"num": 11, "title": "Battle in Heaven", "title_cn": "大闹天宫",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "The Jade Emperor sent an army to capture Wukong! Many heavenly soldiers came down to the mountain.", "setting": "army of heavenly soldiers descending from clouds towards mountain"},
         {"narration": "But Wukong was too strong! He fought off all the soldiers with his golden staff.", "setting": "monkey king fighting soldiers in mid-air with golden staff, clouds everywhere"},
         {"narration": "No one in Heaven could defeat him! The Jade Emperor didn't know what to do.", "setting": "jade emperor worried on throne with defeated soldiers returning"},
     ]},
    {"num": 12, "title": "Peach Garden Feast", "title_cn": "偷吃蟠桃",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "To keep Wukong happy, they gave him a new job: guarding the Peach Garden. These were magical peaches!", "setting": "beautiful garden full of giant glowing peach trees"},
         {"narration": "But Wukong couldn't resist! He ate many magical peaches. Each one made him even more powerful!", "setting": "monkey happily eating glowing peaches in a magical garden"},
         {"narration": "When the fairies came to pick peaches for the party, they found most were gone! Wukong was in big trouble!", "setting": "fairies looking at empty peach trees in shock"},
     ]},
    {"num": 13, "title": "Laozi's Furnace", "title_cn": "炼丹炉",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "They finally caught Wukong and put him in Laozi's magical furnace. The fire burned for 49 days!", "setting": "monkey trapped inside a giant bronze furnace with flames"},
         {"narration": "But instead of being destroyed, Wukong became even stronger! He got special golden eyes that could see through any disguise!", "setting": "monkey emerging from furnace with glowing golden eyes, surrounded by smoke"},
         {"narration": "He broke free and caused even more chaos in Heaven! Nobody could stop him!", "setting": "monkey breaking through palace walls with incredible power"},
     ]},
    {"num": 14, "title": "Buddha's Palm", "title_cn": "如来佛祖",
     "world": "flower_fruit_mountain", "difficulty": 1,
     "scenes": [
         {"narration": "Finally, the Buddha himself came. He made a bet with Wukong: jump out of my palm, and you win!", "setting": "giant buddha hand with tiny monkey standing on it"},
         {"narration": "Wukong jumped as far as he could! He saw five huge pillars and thought he reached the edge of the world.", "setting": "monkey standing between five giant pillars in misty landscape"},
         {"narration": "But the five pillars were actually Buddha's fingers! Wukong could not escape.", "setting": "buddha smiling with his hand closing, monkey looking surprised"},
         {"narration": "Buddha placed a mountain on top of Wukong. He would stay there for 500 years until he learned his lesson.", "setting": "monkey trapped under a large mountain with a golden seal on top"},
     ]},

    # Tier 2: Dragon Palace (stories 15-27, difficulty 2)
    {"num": 15, "title": "500 Years Under the Mountain", "title_cn": "五百年",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "500 years passed. Wukong was still trapped under the mountain. Rain, snow, sun — he endured it all.", "setting": "mountain with seasons changing around it, monkey peeking out"},
         {"narration": "One day, a kind monk named Tang Sanzang walked by. He was on a journey to fetch holy scriptures.", "setting": "monk in orange robes walking along a path near a mountain"},
         {"narration": "He heard Wukong calling for help! The monk removed the golden seal and freed Wukong.", "setting": "monk removing a glowing seal from mountain, monkey emerging"},
         {"narration": "Wukong promised to protect the monk on his journey. He became his first disciple!", "setting": "monkey bowing to monk on a sunny road, beginning their journey"},
     ]},
    {"num": 16, "title": "The Golden Headband", "title_cn": "紧箍咒",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "Wukong was wild and hard to control. The Goddess of Mercy gave Tang Sanzang a magical golden headband.", "setting": "goddess in white giving a golden headband to monk"},
         {"narration": "When Wukong put it on, it couldn't come off! If he misbehaved, Tang Sanzang could chant a spell to make it tighten.", "setting": "monkey with golden headband on head, looking uncomfortable"},
         {"narration": "Wukong was angry at first, but he learned to listen and be patient. The headband taught him discipline.", "setting": "monkey and monk walking together peacefully on a mountain path"},
     ]},
    {"num": 17, "title": "Pigsy Joins the Team", "title_cn": "收服猪八戒",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "On their journey, they met a pig monster living in a village. He had been causing trouble!", "setting": "pig monster in a village, villagers looking scared"},
         {"narration": "Wukong fought the pig monster! After a fierce battle, the pig surrendered.", "setting": "monkey and pig monster fighting in a field"},
         {"narration": "The pig's name was Zhu Bajie, also called Pigsy. He used to be a heavenly general! He joined their team.", "setting": "pig character bowing to monk, monkey standing nearby"},
         {"narration": "Pigsy was funny and always hungry, but he was strong and had a good heart.", "setting": "pig character eating rice, monkey and monk watching and laughing"},
     ]},
    {"num": 18, "title": "Sandy from the River", "title_cn": "收服沙僧",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "They came to a wide, dangerous river. A monster lived in the water and wouldn't let them cross!", "setting": "wide misty river with dark waters, travelers on the shore"},
         {"narration": "Wukong and the river monster fought! The monster was strong in water but Wukong was clever.", "setting": "monkey fighting a blue river monster in splashing water"},
         {"narration": "The monster was actually Sandy, another fallen heavenly general. He agreed to join them and carry their luggage!", "setting": "sandy character with a necklace of skulls, joining the group on the riverbank"},
     ]},
    {"num": 19, "title": "The White Dragon Horse", "title_cn": "白龙马",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "Tang Sanzang's horse was eaten by a dragon! Oh no! How would he travel now?", "setting": "dragon emerging from a lake, eating a horse, monk looking shocked"},
         {"narration": "But the dragon was actually a prince who had made a mistake. The Goddess of Mercy transformed him into a white horse.", "setting": "dragon transforming into a beautiful white horse in golden light"},
         {"narration": "Now Tang Sanzang had a magical dragon horse to ride! The team was complete.", "setting": "monk riding white horse, with monkey, pig, and sandy walking alongside"},
     ]},
    {"num": 20, "title": "The First Demon Village", "title_cn": "降妖除魔",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "They arrived at a small village. The people looked scared and sad. A demon was stealing their food!", "setting": "sad villagers in a small Chinese village"},
         {"narration": "Wukong turned into a butterfly to spy on the demon. He found the demon's cave in the mountains.", "setting": "butterfly flying near a dark cave entrance in mountains"},
         {"narration": "Wukong fought the demon and won! The villagers cheered and gave them a big feast.", "setting": "villagers celebrating, giving food to the travelers"},
     ]},
    {"num": 21, "title": "The Yellow Wind Demon", "title_cn": "黄风怪",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "A powerful demon who controlled the wind attacked them! Sand and wind blew everywhere!", "setting": "massive sandstorm with a demon figure in the center"},
         {"narration": "The wind was so strong that Wukong's eyes hurt. He needed help!", "setting": "monkey shielding eyes from powerful wind, staff in hand"},
         {"narration": "Wukong found a special medicine for his eyes. Then he defeated the Wind Demon!", "setting": "monkey with glowing eyes defeating the wind demon, wind calming"},
         {"narration": "With the wind gone, the path was clear again. They continued their journey west.", "setting": "peaceful road stretching west with clear blue skies"},
     ]},
    {"num": 22, "title": "The River of Flowing Sand", "title_cn": "流沙河",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "They came to a river full of quicksand. Nothing could float on it — not even a feather!", "setting": "mysterious river of flowing sand, dark and swirling"},
         {"narration": "Sandy knew this river well — it was where he used to live! He helped them build a magic raft.", "setting": "sandy building a raft with magical powers on the riverbank"},
         {"narration": "They crossed the river safely! Sandy was proud to help his new friends.", "setting": "group crossing the sandy river on a glowing raft"},
     ]},
    {"num": 23, "title": "Test of the Four Saints", "title_cn": "四圣试禅心",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "Four beautiful women invited them to stay in their mansion. They offered food and riches!", "setting": "beautiful mansion with four elegant women welcoming travelers"},
         {"narration": "Pigsy was excited! He wanted to stay. But it was actually a test from four heavenly saints!", "setting": "pig character looking happy, being tempted by luxury"},
         {"narration": "Pigsy failed the test and got tied up in the forest! The others helped free him and continued the journey.", "setting": "pig tied to a tree, monkey laughing, monk looking disapproving"},
     ]},
    {"num": 24, "title": "The Ginseng Fruit Tree", "title_cn": "人参果",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "They visited a magical temple with a tree that grew Ginseng Fruits — shaped like tiny babies!", "setting": "ancient temple with a magical tree bearing baby-shaped fruits"},
         {"narration": "The fruits were so magical that eating one could give you 10,000 years of life!", "setting": "close-up of glowing baby-shaped fruits on a tree"},
         {"narration": "Wukong secretly picked some for everyone, but when the temple master found out, he was furious!", "setting": "angry old master confronting monkey near the fruit tree"},
         {"narration": "Wukong accidentally knocked down the tree. He had to ask the Goddess of Mercy to fix it with her magic water!", "setting": "goddess pouring magical water on a fallen tree, it starts growing again"},
     ]},
    {"num": 25, "title": "The Silver Horn King", "title_cn": "银角大王",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "Two demon brothers with magic gourds blocked the path. If you answered when they called your name, you'd be sucked inside!", "setting": "two demon kings holding magical gourds on a mountain pass"},
         {"narration": "They tricked Wukong and sucked him into the gourd! It was dark and scary inside.", "setting": "monkey being pulled into a glowing purple gourd"},
         {"narration": "But Wukong was clever! He turned into a bug and escaped. Then he stole their gourds!", "setting": "monkey transformed as tiny bug escaping from gourd"},
         {"narration": "With their own weapons, Wukong defeated the demon brothers! The path was safe again.", "setting": "monkey holding magic gourds triumphantly, defeated demons on ground"},
     ]},
    {"num": 26, "title": "The Golden Horn King", "title_cn": "金角大王",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "The Golden Horn King was even stronger than his brother! He had a magic rope that could tie up anyone.", "setting": "powerful golden-horned demon with a magical golden rope"},
         {"narration": "Wukong and the demon fought for three days! Mountains shook and rivers trembled.", "setting": "epic battle between monkey and golden demon, landscape shaking"},
         {"narration": "In the end, the Goddess of Mercy revealed that the demons were actually her servants who had escaped. She took them back to Heaven.", "setting": "goddess taking the two demons back to heaven on a cloud"},
     ]},
    {"num": 27, "title": "The Kingdom of Wuji", "title_cn": "乌鸡国",
     "world": "dragon_palace", "difficulty": 2,
     "scenes": [
         {"narration": "They arrived at the Kingdom of Wuji. The king's ghost appeared to Tang Sanzang in a dream!", "setting": "ghost of a king appearing in monk's dream, misty and ethereal"},
         {"narration": "A demon had pushed the real king into a well and taken his place! Nobody knew!", "setting": "demon disguised as king sitting on throne in palace"},
         {"narration": "Wukong pulled the real king from the well and used a magic pill to bring him back to life!", "setting": "monkey pulling a king out of a well, golden light around them"},
         {"narration": "Then Wukong exposed the fake king and defeated the demon! The real king got his throne back.", "setting": "real king back on throne, people celebrating, demon defeated"},
     ]},

    # Tier 3: Heaven Palace (stories 28-41, difficulty 3)
    {"num": 28, "title": "The White Bone Demon", "title_cn": "三打白骨精",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "A clever demon called the White Bone Spirit could change into different people! First, she became a young girl.", "setting": "beautiful young girl on a mountain path, with hidden skeleton shadow"},
         {"narration": "Wukong saw through her disguise with his golden eyes! He struck her with his staff.", "setting": "monkey striking girl with staff, skeleton briefly visible"},
         {"narration": "The demon came back as an old woman, then an old man. Each time Wukong defeated her, but Tang Sanzang thought he was hurting innocent people!", "setting": "old woman and old man forms, monk looking angry at monkey"},
         {"narration": "Tang Sanzang sent Wukong away! Poor Wukong cried as he flew back to Flower Fruit Mountain alone.", "setting": "sad monkey flying away on cloud, looking back at monk"},
         {"narration": "Later, when Tang Sanzang was captured by the real demon, he realized Wukong was right. Wukong came back and saved everyone!", "setting": "monkey heroically saving monk from a skeleton demon in a cave"},
     ]},
    {"num": 29, "title": "The Yellow Robe Demon", "title_cn": "黄袍怪",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "Without Wukong, the team was in trouble! A demon captured Tang Sanzang and turned him into a tiger!", "setting": "monk being transformed into a tiger by a demon's spell"},
         {"narration": "Pigsy flew to Flower Fruit Mountain to beg Wukong to come back. Wukong pretended he didn't care!", "setting": "pig character begging monkey on mountain, monkey turning away"},
         {"narration": "But Wukong secretly cared a lot. He rushed back and defeated the Yellow Robe Demon!", "setting": "monkey flying fast on cloud towards a demon's lair"},
         {"narration": "He changed Tang Sanzang back from a tiger to a human. The team was together again!", "setting": "monkey using magic to turn tiger back into monk, everyone relieved"},
     ]},
    {"num": 30, "title": "The Red Boy", "title_cn": "红孩儿",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "A demon child called Red Boy could breathe fire! He was the Bull Demon King's son.", "setting": "small red demon child breathing flames on a mountain"},
         {"narration": "Red Boy captured Tang Sanzang with his fire! The flames were too hot even for Wukong!", "setting": "ring of fire surrounding monk, monkey unable to get through"},
         {"narration": "Wukong asked the Goddess of Mercy for help. She captured Red Boy and made him her servant.", "setting": "goddess with Red Boy now calm and reformed, standing beside her"},
     ]},
    {"num": 31, "title": "The Black River Demon", "title_cn": "黑水河妖",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "A demon from the Black River pretended to be a boatman. He tricked Tang Sanzang onto his boat!", "setting": "demon disguised as boatman on a dark river"},
         {"narration": "The boat sank and the demon dragged Tang Sanzang underwater! Wukong dove in to save him.", "setting": "monkey diving into dark waters after sinking boat"},
         {"narration": "With help from a heavenly prince, they defeated the Black River Demon and saved Tang Sanzang.", "setting": "monkey and a prince warrior defeating water demon, freeing monk"},
     ]},
    {"num": 32, "title": "The Cart-Slow Kingdom", "title_cn": "车迟国",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "In this kingdom, three fake masters used tricks to pretend they had magic powers!", "setting": "three shifty-looking masters performing fake magic in a royal court"},
         {"narration": "Wukong challenged them to a contest! They competed in prayer for rain.", "setting": "monkey and fake master both praying, clouds gathering"},
         {"narration": "Wukong asked the Dragon King to help him win! Real rain fell from the sky.", "setting": "rain falling from clouds, monkey smiling, fake masters looking worried"},
         {"narration": "The fake masters were exposed! The king freed all the monks they had imprisoned.", "setting": "freed monks celebrating, king punishing the fake masters"},
     ]},
    {"num": 33, "title": "The Golden Fish Demon", "title_cn": "金鱼精",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "A huge golden fish demon flooded a whole temple! The monks were trapped in the water.", "setting": "flooded temple with giant golden fish swimming around"},
         {"narration": "Wukong fought the fish but it was very slippery! Every time he grabbed it, it escaped.", "setting": "monkey trying to catch a giant golden fish in water"},
         {"narration": "The Goddess of Mercy came with her bamboo basket and caught the fish easily. It was her pet goldfish!", "setting": "goddess scooping up golden fish with a basket, smiling"},
     ]},
    {"num": 34, "title": "The Scorpion Demon", "title_cn": "蝎子精",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "A scorpion demon stung Wukong! Her poison was so strong that even Wukong was hurt.", "setting": "giant scorpion demon attacking monkey with its tail"},
         {"narration": "Wukong had to find the Star of Light, the only one who could defeat the scorpion.", "setting": "monkey flying through stars searching for the Star of Light"},
         {"narration": "The Star of Light turned into a giant rooster! Its crow was the scorpion's weakness. The demon was defeated!", "setting": "giant magical rooster crowing at a scorpion demon, golden light"},
     ]},
    {"num": 35, "title": "The Land of Women", "title_cn": "女儿国",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "They arrived at a kingdom where only women lived! The queen wanted Tang Sanzang to be her king.", "setting": "beautiful kingdom with palace, all female guards and citizens"},
         {"narration": "Tang Sanzang politely refused. He had to continue his journey to get the holy scriptures!", "setting": "monk politely declining queen in throne room"},
         {"narration": "A scorpion demon tried to capture Tang Sanzang while they were leaving. Wukong saved him just in time!", "setting": "monkey fighting off demon while monk escapes the kingdom gates"},
     ]},
    {"num": 36, "title": "The Real and Fake Monkey", "title_cn": "真假美猴王",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "A monkey that looked exactly like Wukong appeared! Nobody could tell them apart.", "setting": "two identical monkeys standing face to face, everyone confused"},
         {"narration": "They both claimed to be the real Wukong! They fought from Earth to Heaven to the Underworld.", "setting": "two monkeys fighting across different realms, heaven and underworld"},
         {"narration": "Even the Jade Emperor couldn't tell them apart! They went to see the Buddha.", "setting": "two monkeys standing before a giant buddha, heavenly beings watching"},
         {"narration": "The Buddha knew! The fake one was a Six-Eared Monkey. Wukong defeated him and the team was reunited.", "setting": "real monkey defeating fake monkey, buddha watching approvingly"},
     ]},
    {"num": 37, "title": "The Banana Fan", "title_cn": "芭蕉扇",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "A mountain of fire blocked their path! The flames stretched for hundreds of miles!", "setting": "massive flaming mountain blocking a road, intense red and orange fire"},
         {"narration": "Only the Iron Fan Princess had a magic banana fan that could blow out the fire.", "setting": "woman holding a giant green banana leaf fan, looking fierce"},
         {"narration": "But she was Red Boy's mother! She was angry at Wukong and wouldn't help.", "setting": "angry woman refusing to help monkey, turning away"},
     ]},
    {"num": 38, "title": "Borrowing the Fan", "title_cn": "三借芭蕉扇",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "Wukong turned into a tiny bug and flew into the Iron Fan Princess's belly! She had to give him the fan.", "setting": "tiny bug flying into woman's tea cup, she's unaware"},
         {"narration": "But it was a fake fan! When Wukong used it, the fire grew even bigger!", "setting": "monkey waving fan at fire, fire growing larger, monkey looking shocked"},
         {"narration": "The Bull Demon King, her husband, fought Wukong for the real fan. It was an epic battle!", "setting": "monkey fighting a bull demon in the sky, both powerful"},
         {"narration": "With help from heavenly soldiers, Wukong finally got the real fan and put out the fire!", "setting": "monkey waving magical fan, fire being extinguished, cool breeze"},
     ]},
    {"num": 39, "title": "The Bull Demon King", "title_cn": "牛魔王",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "The Bull Demon King was furious! He transformed into a giant white bull to fight Wukong.", "setting": "enormous white bull charging at monkey, dust and rocks flying"},
         {"narration": "Wukong transformed too! He became a giant to match the bull. They fought across mountains!", "setting": "giant monkey and giant bull fighting, mountains crumbling"},
         {"narration": "The heavenly prince Nezha came to help! Together they defeated the Bull Demon King.", "setting": "boy warrior on fire wheels helping monkey defeat bull demon"},
     ]},
    {"num": 40, "title": "Crossing the Flaming Mountain", "title_cn": "过火焰山",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "With the real banana fan, Wukong waved it three times. Whoooosh! The fire went out!", "setting": "monkey waving fan, powerful wind extinguishing mountain fire"},
         {"narration": "Rain fell on the mountain for the first time in years! Plants started growing again.", "setting": "rain falling on formerly burning mountain, green sprouts appearing"},
         {"narration": "The people who lived nearby were so happy! They could finally cross the mountain safely.", "setting": "happy villagers crossing a now-green mountain, travelers continuing journey"},
     ]},
    {"num": 41, "title": "The Kingdom of Sacrifice", "title_cn": "祭赛国",
     "world": "heaven_palace", "difficulty": 3,
     "scenes": [
         {"narration": "In this kingdom, the king had lost his magical golden pagoda to demons! The kingdom was cursed with endless rain.", "setting": "rainy kingdom with sad people, empty pagoda tower"},
         {"narration": "Wukong flew up through the clouds and found the demons who stole the pagoda.", "setting": "monkey flying through storm clouds towards a hidden demon lair"},
         {"narration": "He defeated the demons, returned the golden pagoda, and the rain finally stopped! The sun came out again.", "setting": "monkey returning golden pagoda to king, sun breaking through clouds"},
     ]},

    # Tier 4: White Bone Cave (stories 42-54, difficulty 4)
    {"num": 42, "title": "The Spider Demons", "title_cn": "蜘蛛精",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "Seven spider demons disguised as beautiful women lived near a hot spring. They trapped Tang Sanzang!", "setting": "seven beautiful women at a misty hot spring, webs hidden"},
         {"narration": "When their disguise was revealed, they turned into giant spiders and spun webs everywhere!", "setting": "seven giant colorful spiders spinning webs, monk trapped"},
         {"narration": "Wukong fought through the sticky webs and freed Tang Sanzang. The spiders ran away!", "setting": "monkey cutting through webs with staff, freeing monk"},
     ]},
    {"num": 43, "title": "The Centipede Demon", "title_cn": "蜈蚣精",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "The spider demons ran to their big brother — a giant centipede demon with a thousand golden lights!", "setting": "enormous centipede demon glowing with golden light in a cave"},
         {"narration": "The golden lights blinded Wukong! He couldn't fight what he couldn't see.", "setting": "monkey shielding his eyes from blinding golden beams"},
         {"narration": "A heavenly rooster came to help again! The centipede was afraid of roosters and was defeated.", "setting": "magical rooster facing down centipede demon, golden light fading"},
     ]},
    {"num": 44, "title": "The Green Lion", "title_cn": "青狮精",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "A powerful green lion demon had swallowed an entire kingdom! Everyone was inside his belly.", "setting": "massive green lion demon outside a city, mouth wide open"},
         {"narration": "Wukong let the lion swallow him too! Then he kicked and punched from inside the lion's belly.", "setting": "monkey inside a lion's belly, punching and kicking, lion in pain"},
         {"narration": "The lion couldn't take it anymore! He spit everyone out, and Wukong defeated him.", "setting": "lion spitting out people and monkey, looking defeated"},
         {"narration": "The kingdom was saved! Everyone cheered for Wukong and his friends.", "setting": "grateful kingdom people celebrating with the travel team"},
     ]},
    {"num": 45, "title": "The White Elephant Demon", "title_cn": "白象精",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "A giant white elephant demon used his long trunk to grab Tang Sanzang! He was incredibly strong.", "setting": "massive white elephant grabbing monk with trunk, others fighting"},
         {"narration": "Wukong and Pigsy fought the elephant together, but his skin was too thick!", "setting": "monkey and pig fighting elephant, weapons bouncing off"},
         {"narration": "The elephant was actually a celestial creature who had escaped from Heaven. He was taken back.", "setting": "elephant being led back to heaven by celestial beings"},
     ]},
    {"num": 46, "title": "The Golden Winged Peng", "title_cn": "大鹏金翅鸟",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "The most dangerous demon yet — a giant golden bird called the Peng! It could fly faster than Wukong!", "setting": "enormous golden eagle-like bird swooping through clouds"},
         {"narration": "The Peng grabbed Tang Sanzang and flew to a mountain top. Even Wukong's cloud couldn't catch up!", "setting": "giant bird carrying monk, monkey chasing on cloud but falling behind"},
         {"narration": "Wukong went to ask the Buddha for help. The Buddha revealed that the Peng was his own relative!", "setting": "buddha speaking to monkey, golden bird perched nearby"},
         {"narration": "The Buddha tamed the Peng. The golden bird would now serve and protect, not attack.", "setting": "golden bird now peaceful, perched near buddha, monk freed"},
     ]},
    {"num": 47, "title": "The Kingdom of Bhikku", "title_cn": "比丘国",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "In this kingdom, the evil minister was actually a deer demon! He was tricking the old king.", "setting": "sneaky deer demon disguised as a minister, whispering to old king"},
         {"narration": "Wukong saw through the disguise with his golden eyes! He exposed the deer demon.", "setting": "monkey pointing at minister, demon form becoming visible"},
         {"narration": "The demon tried to run but Wukong was too fast! The kingdom was saved from the trickster.", "setting": "monkey chasing deer demon, catching it easily"},
     ]},
    {"num": 48, "title": "The Green Haired Lion", "title_cn": "青毛狮子怪",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "Three powerful demon kings joined forces! A lion, an elephant, and a giant bird — together they were terrifying!", "setting": "three powerful demons standing together on a mountain, looking menacing"},
         {"narration": "They captured Tang Sanzang and put him in a cage. They wanted to eat him to become immortal!", "setting": "monk in cage, three demons preparing a feast"},
         {"narration": "Wukong had to fight all three at once! It was the hardest battle yet.", "setting": "monkey fighting three demons simultaneously in an epic battle"},
         {"narration": "With help from heavenly beings, all three demons were captured and taken back to where they belonged.", "setting": "three demons being taken away by celestial guards, team reunited"},
     ]},
    {"num": 49, "title": "The Rhinoceros Demons", "title_cn": "犀牛精",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "Three rhinoceros demons pretended to be Buddhas! They stole all the holy oil from a temple.", "setting": "three rhino demons wearing fake Buddhist robes near a temple"},
         {"narration": "Wukong chased them through mountains and rivers. They were fast runners!", "setting": "monkey chasing three rhinos across landscape, dust flying"},
         {"narration": "Four heavenly star warriors came to help. Together they cornered the fake Buddhas and captured them!", "setting": "four star warriors and monkey surrounding three rhino demons"},
     ]},
    {"num": 50, "title": "The Jade Rabbit", "title_cn": "玉兔精",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "The moon's jade rabbit escaped to Earth! She disguised herself as a princess.", "setting": "white rabbit transforming into a princess under moonlight"},
         {"narration": "She wanted to marry Tang Sanzang! She set up a fake contest to win his hand.", "setting": "princess on a tower throwing a ball, monk below looking confused"},
         {"narration": "Wukong saw through the disguise. But the rabbit was quick and kept hopping away!", "setting": "monkey chasing a white rabbit that's jumping super fast"},
         {"narration": "The Moon Goddess came down from the moon to take her rabbit back. The real princess was found safe.", "setting": "beautiful moon goddess descending on moonbeams, taking rabbit home"},
     ]},
    {"num": 51, "title": "The Fire Demon", "title_cn": "火焰山再遇",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "They passed through a land where everything was frozen! A demon had stolen all the warmth.", "setting": "frozen icy landscape, travelers shivering"},
         {"narration": "The Ice Demon and Fire Demon were fighting each other! Their battle caused chaos everywhere.", "setting": "ice demon and fire demon clashing, ice and fire everywhere"},
         {"narration": "Wukong brought balance! He helped the two demons make peace. The land returned to normal.", "setting": "monkey mediating between ice and fire, landscape becoming green"},
     ]},
    {"num": 52, "title": "The Underground River", "title_cn": "地下河",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "An underground river blocked their path. Strange glowing fish swam in the dark water.", "setting": "underground cave with glowing river, bioluminescent fish"},
         {"narration": "A turtle demon offered to carry them across, but it was a trap!", "setting": "giant turtle in underground river, travelers about to step on"},
         {"narration": "Wukong saw through the trick! He caught the turtle and made it carry them safely across for real.", "setting": "monkey riding turtle safely across glowing river with teammates"},
     ]},
    {"num": 53, "title": "The Magic Garden", "title_cn": "仙人花园",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "They discovered a beautiful garden with fruits that could cure any illness!", "setting": "magical garden with glowing colorful fruits on trees"},
         {"narration": "But the garden was guarded by a fierce flower demon! Its petals were sharp as swords.", "setting": "beautiful but dangerous flower demon, petals like blades"},
         {"narration": "Pigsy accidentally ate a sleeping fruit and fell into a deep sleep! They had to find the cure.", "setting": "pig character sleeping on the ground, flowers around"},
         {"narration": "Wukong found a dew drop that woke Pigsy up. They carefully picked healing fruits and continued on.", "setting": "monkey dropping dew on pig to wake him, team leaving garden"},
     ]},
    {"num": 54, "title": "The Mountain Spirits", "title_cn": "山神考验",
     "world": "white_bone_cave", "difficulty": 4,
     "scenes": [
         {"narration": "The mountain spirits blocked the path with riddles! They would only let smart travelers pass.", "setting": "ghostly mountain spirits floating near a mountain pass, riddle stones"},
         {"narration": "Wukong answered the first riddle easily. Pigsy got the second one wrong and had to try again!", "setting": "monkey answering confidently, pig scratching head"},
         {"narration": "Sandy solved the final riddle! The spirits were impressed and let them through.", "setting": "sandy answering wisely, spirits nodding and opening the path"},
     ]},

    # Tier 5: Flaming Mountain (stories 55-68, difficulty 5)
    {"num": 55, "title": "The Bottomless Cave", "title_cn": "无底洞",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "A demon woman captured Tang Sanzang and took him to a cave so deep nobody could find the bottom!", "setting": "dark endless cave going deep underground, dim light"},
         {"narration": "Wukong followed the demon's trail deep into the earth. The cave was full of traps!", "setting": "monkey navigating traps in a deep cave, avoiding sharp rocks"},
         {"narration": "He found Tang Sanzang and fought the demon. It turned out she was a mouse spirit who had once stolen lamp oil from the Buddha!", "setting": "mouse demon being defeated, transforming back to mouse form"},
         {"narration": "The heavenly cat warriors came and captured the mouse spirit. Tang Sanzang was saved!", "setting": "celestial cat warriors catching mouse demon, monk freed"},
     ]},
    {"num": 56, "title": "The Python Demon", "title_cn": "蟒蛇精",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "A python demon as big as a mountain blocked the road! Its body stretched across the entire valley.", "setting": "enormous python coiled across a valley, blocking the path"},
         {"narration": "It opened its mouth and a powerful wind pulled everything inside! Even trees were uprooted.", "setting": "giant python mouth creating suction, trees and rocks flying in"},
         {"narration": "Wukong turned himself into a needle and poked the python from inside! It had to open its mouth and let everyone go.", "setting": "monkey using staff to poke python from inside, it opens mouth"},
     ]},
    {"num": 57, "title": "The Cloud Stepping Kingdom", "title_cn": "天竺国",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "They arrived at a beautiful kingdom high in the clouds. The people lived in houses among the clouds!", "setting": "kingdom built on clouds, beautiful floating buildings"},
         {"narration": "But the princess had been replaced by a demon! The real princess was locked in a tower.", "setting": "demon disguised as princess in throne room, real princess in tower"},
         {"narration": "Wukong discovered the truth and rescued the real princess. The demon was a crane spirit from Heaven.", "setting": "monkey freeing princess from tower, crane demon flying away"},
         {"narration": "The king was so grateful! He gave them supplies and pointed the way west.", "setting": "grateful king giving supplies to travelers at kingdom gates"},
     ]},
    {"num": 58, "title": "The Nine-Headed Bug", "title_cn": "九头虫",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "A terrifying monster with nine heads attacked from the sky! Each head could breathe a different element.", "setting": "nine-headed dragon/bug in the sky, each head different color"},
         {"narration": "One head breathed fire, another breathed ice, another shot lightning! Wukong had to dodge them all.", "setting": "monkey dodging multiple elemental attacks from the nine heads"},
         {"narration": "Wukong called for help from a heavenly warrior who chopped off one head. The bug fled in fear!", "setting": "warrior chopping off one head, bug flying away in pain"},
     ]},
    {"num": 59, "title": "The Thorn Forest", "title_cn": "荆棘岭",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "A dense forest of thorny trees blocked their way! Every branch had sharp thorns.", "setting": "dense dark forest with impossibly thorny trees everywhere"},
         {"narration": "Tree spirits came alive at night! They wanted Tang Sanzang to write poems with them.", "setting": "tree spirits shaped like old men, holding scrolls and brushes"},
         {"narration": "While Tang Sanzang was busy with poems, other tree demons tried to eat the horse! Wukong burned them down.", "setting": "monkey using fire to burn evil tree demons, protecting white horse"},
     ]},
    {"num": 60, "title": "The Little Thunder Temple", "title_cn": "小雷音寺",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "They found what looked like the Thunder Temple! Tang Sanzang was excited — were they at the end of their journey?", "setting": "beautiful golden temple that looks like the final destination"},
         {"narration": "But it was a fake temple built by a yellow-browed demon! He trapped everyone in a golden cymbal.", "setting": "demon laughing, golden cymbal trapping the travelers"},
         {"narration": "Wukong had to travel far to find a celestial dragon to crack the cymbal open. It was a long battle!", "setting": "monkey riding to find help, dragon breaking golden cymbal"},
         {"narration": "The fake temple crumbled. They learned to be more careful and not trust everything they see.", "setting": "fake temple collapsing into dust, team looking wiser"},
     ]},
    {"num": 61, "title": "The Seven Spider Sisters Return", "title_cn": "蜘蛛精再现",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "The spider sisters found a powerful ally — a centipede demon with poison! They attacked again.", "setting": "spiders and centipede demon combining forces in a dark forest"},
         {"narration": "The poison made Wukong feel weak! He had to find the antidote before it was too late.", "setting": "monkey looking weak, searching through a garden for herbs"},
         {"narration": "Sandy found the healing herb just in time! Wukong recovered and defeated all the demons.", "setting": "sandy bringing herb to monkey, monkey recovering and fighting"},
     ]},
    {"num": 62, "title": "The Leopard Demon", "title_cn": "豹子精",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "A fast leopard demon attacked at night! He was almost as fast as Wukong.", "setting": "spotted leopard demon running at incredible speed in moonlight"},
         {"narration": "They chased each other across mountains and valleys. The leopard was tricky and kept hiding!", "setting": "monkey chasing leopard through various landscapes"},
         {"narration": "Pigsy set a clever trap! The leopard ran right into it. Even fast demons can be outsmarted.", "setting": "pig character's trap catching the leopard demon"},
     ]},
    {"num": 63, "title": "The Golden Light Cave", "title_cn": "金光洞",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "A cave full of golden light appeared! Inside, a demon hoarded stolen treasures from villages.", "setting": "cave filled with golden light and piles of treasures"},
         {"narration": "The demon could turn invisible! Wukong couldn't hit what he couldn't see.", "setting": "monkey swinging at air, invisible demon laughing"},
         {"narration": "Wukong used magic dust to reveal the invisible demon. Now he could see and defeat him!", "setting": "monkey throwing magical dust, demon becoming visible, getting hit"},
         {"narration": "They returned all the stolen treasures to the villages. The people were so happy!", "setting": "villagers receiving their treasures back, thanking the travelers"},
     ]},
    {"num": 64, "title": "The Ice Demon", "title_cn": "冰封妖",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "Everything was frozen solid! An Ice Demon had frozen a whole kingdom, including the king and his people.", "setting": "frozen kingdom, people frozen like ice statues"},
         {"narration": "The Ice Demon shot freezing beams! Even Wukong's staff got covered in ice.", "setting": "blue demon shooting ice beams, everything freezing"},
         {"narration": "Wukong remembered the Iron Fan Princess's fan! He borrowed it and blew warm wind to melt the ice.", "setting": "monkey using fan to blow warm wind, ice melting everywhere"},
         {"narration": "The kingdom thawed and everyone came back to life! The Ice Demon melted away in the warmth.", "setting": "kingdom coming back to life, people moving again, sun shining"},
     ]},
    {"num": 65, "title": "The Flame Phoenix", "title_cn": "火凤凰",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "A magnificent fire phoenix guarded the only bridge they needed to cross. It would burn anyone who came near!", "setting": "beautiful fire phoenix on a stone bridge, flames everywhere"},
         {"narration": "Wukong tried to fight it, but every time it was hurt, it was reborn from the flames!", "setting": "phoenix rising from flames again and again, monkey frustrated"},
         {"narration": "Tang Sanzang played a calming song on a flute. The phoenix became peaceful and let them cross!", "setting": "monk playing flute, phoenix becoming gentle, lowering its wings"},
     ]},
    {"num": 66, "title": "The Sand Demon", "title_cn": "沙漠魔",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "They crossed a vast desert. The sand shifted and moved on its own — a sand demon controlled it!", "setting": "vast desert with sand swirling and forming shapes"},
         {"narration": "The sand tried to bury them! Sandy used his water powers to turn the sand to mud.", "setting": "sandy using water magic, turning attacking sand into mud"},
         {"narration": "The Sand Demon rose from the desert as a giant sand creature! Wukong smashed it with his staff.", "setting": "giant sand monster rising, monkey leaping to strike with staff"},
     ]},
    {"num": 67, "title": "The Stone Kingdom", "title_cn": "石头国",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "A curse turned everyone in this kingdom to stone! Only children were left, scared and alone.", "setting": "stone statues of adults everywhere, scared children hiding"},
         {"narration": "The curse was cast by a stone demon who lived in the mountain. Wukong went to confront him.", "setting": "monkey climbing a mountain towards a stone demon's lair"},
         {"narration": "Wukong remembered — he was born from stone too! He used his stone magic to break the curse.", "setting": "monkey glowing with stone energy, statues turning back to people"},
         {"narration": "Families were reunited! Children hugged their parents again. Wukong was their hero.", "setting": "families reuniting, children hugging now-unfrozen parents"},
     ]},
    {"num": 68, "title": "The Thunder Giant", "title_cn": "雷公巨人",
     "world": "flaming_mountain", "difficulty": 5,
     "scenes": [
         {"narration": "A giant made of thunder and lightning stood as tall as the mountains! Each step shook the earth.", "setting": "enormous glowing giant made of lightning standing between mountains"},
         {"narration": "Its lightning bolts destroyed everything nearby! Even Wukong's cloud couldn't get close.", "setting": "lightning bolts striking everywhere, monkey dodging on cloud"},
         {"narration": "Pigsy had an idea! He threw mud at the giant. The mud blocked the lightning! Wukong struck the final blow.", "setting": "pig throwing mud, monkey striking mud-covered giant with staff"},
     ]},

    # Tier 6: Journey Road (stories 69-81, difficulty 5-6)
    {"num": 69, "title": "The River of No Return", "title_cn": "无归河",
     "world": "journey_road", "difficulty": 5,
     "scenes": [
         {"narration": "A river that flows backwards! Anyone who falls in floats back to where they started their journey.", "setting": "strange river flowing backwards, swirling with time magic"},
         {"narration": "Pigsy fell in and appeared back at the village where they found him! Oh no!", "setting": "pig character appearing in a distant village, confused"},
         {"narration": "Wukong flew to get Pigsy and bring him back. They found a way to cross using stepping stones.", "setting": "team carefully crossing river on magical stepping stones"},
     ]},
    {"num": 70, "title": "The Dream Demon", "title_cn": "梦魔",
     "world": "journey_road", "difficulty": 5,
     "scenes": [
         {"narration": "Everyone fell asleep and couldn't wake up! A Dream Demon was trapping them in pleasant dreams.", "setting": "team sleeping in a field, dreamy mist around them"},
         {"narration": "In their dreams, each person saw what they wanted most. Pigsy dreamed of food, Sandy dreamed of peace.", "setting": "dream bubbles above sleeping characters showing their desires"},
         {"narration": "But Wukong's golden eyes saw through the dream! He woke up and defeated the Dream Demon.", "setting": "monkey waking up with glowing eyes, dispelling dream mist"},
         {"narration": "Everyone woke up and continued on. They learned that sometimes the easiest path is a trap.", "setting": "team getting up, shaking off sleep, continuing journey"},
     ]},
    {"num": 71, "title": "The Shadow Monster", "title_cn": "影子怪",
     "world": "journey_road", "difficulty": 5,
     "scenes": [
         {"narration": "A monster that lived in shadows attacked! When there was no light, it was invisible and powerful.", "setting": "dark shadows moving and attacking, glowing red eyes visible"},
         {"narration": "It grabbed Sandy and pulled him into the darkness! They needed light to fight it.", "setting": "sandy being dragged into shadows, others reaching for him"},
         {"narration": "Wukong called upon the sun! Bright light filled the area and the shadow monster shrank and disappeared.", "setting": "brilliant sunlight flooding the area, shadow creature dissolving"},
     ]},
    {"num": 72, "title": "The Cloud Sea", "title_cn": "云海",
     "world": "journey_road", "difficulty": 5,
     "scenes": [
         {"narration": "They had to cross a sea made entirely of clouds! One wrong step and you'd fall through.", "setting": "vast sea of puffy white clouds, barely visible path"},
         {"narration": "Wukong tested each cloud to find the solid ones. It was like a huge puzzle!", "setting": "monkey carefully stepping between clouds, testing each one"},
         {"narration": "They all held hands and carefully walked across the cloud sea. Teamwork made it possible!", "setting": "team walking hand in hand across cloud path, beautiful sky around"},
     ]},
    {"num": 73, "title": "The Mirror Lake", "title_cn": "镜湖",
     "world": "journey_road", "difficulty": 6,
     "scenes": [
         {"narration": "A lake that reflected everything perfectly. But the reflections could come to life!", "setting": "perfectly still mirror lake reflecting landscape and sky"},
         {"narration": "Evil copies of Wukong, Pigsy, and Sandy emerged from the lake! They had to fight themselves!", "setting": "dark copies of the heroes emerging from lake water"},
         {"narration": "They won by working together! The copies couldn't cooperate like the real team could.", "setting": "real team fighting in formation, defeating disorganized copies"},
     ]},
    {"num": 74, "title": "The Crystal Cave", "title_cn": "水晶洞",
     "world": "journey_road", "difficulty": 6,
     "scenes": [
         {"narration": "A cave made entirely of crystal! Beautiful but dangerous — the crystals could trap you inside.", "setting": "stunning cave made of colorful crystals, beautiful but eerie"},
         {"narration": "Tang Sanzang touched a crystal and his hand got stuck! The cave was alive and hungry.", "setting": "monk's hand stuck to crystal, cave walls slowly closing in"},
         {"narration": "Wukong used his staff to shatter the magic crystal at the cave's heart. All the crystals crumbled!", "setting": "monkey striking a central crystal, entire cave breaking apart"},
         {"narration": "They escaped just in time! The cave collapsed behind them as they ran.", "setting": "team running out of collapsing cave, light ahead"},
     ]},
    {"num": 75, "title": "The Maze Mountains", "title_cn": "迷宫山",
     "world": "journey_road", "difficulty": 6,
     "scenes": [
         {"narration": "The mountains ahead formed a natural maze! Every path looked the same and they kept going in circles.", "setting": "confusing mountain paths that look identical, team lost"},
         {"narration": "Wukong flew up high to see the whole maze from above. He mapped out the correct path!", "setting": "monkey high in sky looking down at mountain maze pattern"},
         {"narration": "He guided the team through the twisting paths. Left, right, straight, left — they made it through!", "setting": "team following monkey's directions through mountain maze, exit visible"},
     ]},
    {"num": 76, "title": "The Wind Valley", "title_cn": "风之谷",
     "world": "journey_road", "difficulty": 6,
     "scenes": [
         {"narration": "A valley where the wind never stopped blowing! It was so strong that nobody could walk through.", "setting": "valley with incredibly powerful wind, trees bent sideways"},
         {"narration": "The wind demon laughed as they tried to push through. Even Wukong was blown backwards!", "setting": "wind demon in sky laughing, monkey being blown back"},
         {"narration": "Sandy found heavy rocks and they tied themselves together. Step by step, they pushed through the wind!", "setting": "team tied together with ropes, pushing against wind with rocks"},
     ]},
    {"num": 77, "title": "The Five Finger Mountain Return", "title_cn": "再回五指山",
     "world": "journey_road", "difficulty": 6,
     "scenes": [
         {"narration": "They passed by the mountain where Wukong was trapped for 500 years. He felt sad and grateful.", "setting": "monkey looking at a familiar mountain with mixed emotions"},
         {"narration": "Wukong thought about how much he had changed. He used to be wild and selfish, but now he cared about his friends.", "setting": "monkey meditating near the mountain, memories floating around him"},
         {"narration": "He placed a peach at the base of the mountain as thanks. Without those 500 years, he wouldn't be who he is today.", "setting": "monkey placing a peach at mountain base, warm golden light"},
     ]},
    {"num": 78, "title": "The Gate of Thunder", "title_cn": "雷音门",
     "world": "journey_road", "difficulty": 6,
     "scenes": [
         {"narration": "They finally saw it in the distance — the Holy Mountain where the scriptures were kept!", "setting": "majestic holy mountain visible in distance, golden light"},
         {"narration": "But one final test remained: the Gate of Thunder! Only those with pure hearts could pass through.", "setting": "massive gate crackling with energy, bright and intimidating"},
         {"narration": "Tang Sanzang walked through bravely. Wukong, Pigsy, and Sandy followed. Their hearts were true!", "setting": "team walking through glowing gate together, light washing over them"},
     ]},
    {"num": 79, "title": "Crossing the Final River", "title_cn": "渡过通天河",
     "world": "journey_road", "difficulty": 6,
     "scenes": [
         {"narration": "One last river to cross! A holy turtle appeared and offered to carry them across.", "setting": "giant ancient turtle in a wide holy river, golden mist"},
         {"narration": "As they crossed, the turtle asked if Tang Sanzang remembered to ask Buddha a question for him.", "setting": "turtle carrying travelers across river, asking a question"},
         {"narration": "Tang Sanzang forgot! The turtle was upset and dumped them in the water. All the scriptures got wet!", "setting": "travelers falling into water, scrolls getting wet"},
         {"narration": "They dried the scriptures in the sun. A few pages were lost, but most were saved. Almost there!", "setting": "team drying scrolls on rocks in sunshine, relieved"},
     ]},
    {"num": 80, "title": "The Holy Mountain", "title_cn": "灵山",
     "world": "journey_road", "difficulty": 6,
     "scenes": [
         {"narration": "They climbed the Holy Mountain! Clouds parted to reveal a magnificent golden temple at the top.", "setting": "travelers climbing mountain stairs through clouds towards golden temple"},
         {"narration": "The Buddha himself welcomed them! After 14 years of travel, they finally arrived.", "setting": "buddha welcoming the travelers in a grand golden hall"},
         {"narration": "The Buddha gave them the holy scriptures — thousands of pages of wisdom and kindness!", "setting": "monk receiving glowing scrolls from buddha, tears of joy"},
         {"narration": "But wait — the first set of scriptures were blank! They had to go back and get the real ones.", "setting": "monk opening scroll to find blank pages, looking confused"},
     ]},
    {"num": 81, "title": "Journey Complete", "title_cn": "功德圆满",
     "world": "journey_road", "difficulty": 6,
     "scenes": [
         {"narration": "With the real scriptures in hand, they began the long journey home. But this time, they flew on a cloud!", "setting": "team flying on a golden cloud over beautiful landscape, carrying scrolls"},
         {"narration": "They brought the scriptures back to China! The Emperor and all the people celebrated.", "setting": "grand celebration in ancient Chinese palace, scrolls on display"},
         {"narration": "As a reward for their devotion, the Buddha made each of them a heavenly being. Wukong became the Victorious Fighting Buddha!", "setting": "wukong ascending to heaven in golden light, becoming a buddha"},
         {"narration": "Tang Sanzang, Wukong, Pigsy, Sandy, and the dragon horse — they all found peace. The journey of 81 tribulations was complete!", "setting": "five characters standing together in heaven, peaceful and happy, golden light"},
         {"narration": "And so, the greatest adventure ever told came to an end. But the wisdom they found will last forever!", "setting": "scroll closing with the words The End, surrounded by clouds and stars"},
     ]},
]

# ---------------------------------------------------------------------------
# Game type pools per difficulty tier
# ---------------------------------------------------------------------------

TIER_GAME_POOLS = {
    1: ["counting"] * 4 + ["addition"] * 3 + ["sight_words"] * 3 + ["phonics"] * 3 +
       ["pattern"] * 3 + ["make_ten"] * 3 + ["comparison"] * 2 + ["general_knowledge"] * 2,
    2: ["counting"] * 2 + ["addition"] * 3 + ["subtraction"] * 2 + ["sight_words"] * 3 +
       ["phonics"] * 2 + ["pattern"] * 3 + ["shape_pattern"] * 2 + ["make_ten"] * 2 +
       ["number_sequence"] * 2 + ["general_knowledge"] * 3 + ["memory"] * 2 + ["comparison"] * 2,
    3: ["addition"] * 3 + ["subtraction"] * 3 + ["pattern"] * 2 + ["shape_pattern"] * 3 +
       ["number_sequence"] * 3 + ["clock_reading"] * 2 + ["sudoku"] * 2 +
       ["mirror_symmetry"] * 2 + ["general_knowledge"] * 3 + ["sight_words"] * 2 +
       ["make_ten"] * 2 + ["maze"] * 2,
    4: ["addition"] * 2 + ["subtraction"] * 3 + ["shape_pattern"] * 3 +
       ["number_sequence"] * 3 + ["clock_reading"] * 3 + ["sudoku"] * 3 +
       ["mirror_symmetry"] * 3 + ["general_knowledge"] * 3 + ["maze"] * 2 +
       ["ordering"] * 2 + ["make_ten"] * 2,
    5: ["subtraction"] * 3 + ["addition"] * 2 + ["number_sequence"] * 3 +
       ["clock_reading"] * 3 + ["sudoku"] * 3 + ["mirror_symmetry"] * 3 +
       ["shape_pattern"] * 2 + ["maze"] * 3 + ["general_knowledge"] * 2 +
       ["ordering"] * 2 + ["comparison"] * 2,
    6: ["subtraction"] * 3 + ["addition"] * 3 + ["number_sequence"] * 3 +
       ["sudoku"] * 4 + ["mirror_symmetry"] * 3 + ["maze"] * 3 +
       ["clock_reading"] * 3 + ["shape_pattern"] * 3 + ["ordering"] * 2 +
       ["general_knowledge"] * 2,
}

# World config lookup for generators
WORLD_CONFIGS = {
    "flower_fruit_mountain": {
        "num_range": (1, 5), "options": 3,
        "objects": ["peach", "monkey", "banana", "flower", "coconut"],
        "diff_range": (1, 2),
    },
    "dragon_palace": {
        "num_range": (1, 8), "options": 3,
        "objects": ["fish", "shell", "pearl", "gem", "coral"],
        "diff_range": (1, 2),
    },
    "heaven_palace": {
        "num_range": (1, 10), "options": 4,
        "objects": ["star", "cloud", "gem", "moon", "lantern"],
        "diff_range": (2, 3),
    },
    "white_bone_cave": {
        "num_range": (5, 15), "options": 4,
        "objects": ["bone", "mask", "mirror", "candle", "scroll"],
        "diff_range": (2, 4),
    },
    "flaming_mountain": {
        "num_range": (5, 18), "options": 4,
        "objects": ["flame", "fan", "rock", "ember", "spark"],
        "diff_range": (3, 4),
    },
    "journey_road": {
        "num_range": (10, 20), "options": 4,
        "objects": ["scroll", "staff", "hat", "gem", "star"],
        "diff_range": (3, 5),
    },
}

# Image prompt settings
SETTING_BY_WORLD = {
    "flower_fruit_mountain": "lush green mountain with waterfalls, peach trees, and tropical flowers",
    "dragon_palace": "underwater crystal palace with coral reefs, fish, and glowing pearls",
    "heaven_palace": "majestic heavenly palace above the clouds with golden pillars",
    "white_bone_cave": "dark mysterious cave with glowing crystals and ancient bones",
    "flaming_mountain": "fiery volcanic mountain with lava rivers and red sky",
    "journey_road": "ancient Chinese road winding through mountains towards a golden temple",
}

IMAGE_STYLE = "Chinese mythology, Journey to the West, child-friendly cartoon illustration, vibrant colors, soft lighting, no text, 16:9 aspect ratio"

CHARACTERS = ["wukong", "pigsy", "sandy", "tripitaka"]
REWARD_DIALOGUES = [
    "Great job!", "Amazing!", "You're so smart!",
    "Wonderful!", "Keep going!", "Brilliant work!",
    "Wukong is proud of you!", "You did it!", "Fantastic!",
    "One step closer to the scriptures!",
]


def generate_question_for_scene(difficulty, world_id):
    """Generate a random game question matching the difficulty."""
    pool = TIER_GAME_POOLS.get(difficulty, TIER_GAME_POOLS[1])
    game_type = random.choice(pool)

    world_cfg = WORLD_CONFIGS.get(world_id, WORLD_CONFIGS["flower_fruit_mountain"])
    # Set difficulty within world range
    d = max(world_cfg["diff_range"][0], min(world_cfg["diff_range"][1], difficulty))

    gen_func = GENERATORS.get(game_type)
    if gen_func is None:
        # Fallback to counting
        game_type = "counting"
        gen_func = GENERATORS["counting"]

    question = gen_func(world_cfg, d)
    question = {k: v for k, v in question.items() if v is not None}

    hints = HINT_BANK.get(game_type, ["Take your time!", "Look carefully!"])

    return game_type, question, hints


def generate_image_prompt(scene_setting, world_id):
    """Generate an image prompt for a scene."""
    world_setting = SETTING_BY_WORLD.get(world_id, "ancient Chinese landscape")
    return f"{scene_setting}, {world_setting}, {IMAGE_STYLE}"


def generate_all_stories():
    stories = []

    for trib in TRIBULATIONS:
        story_num = trib["num"]
        story_id = f"story_{story_num:02d}"
        difficulty = trib["difficulty"]
        world_id = trib["world"]

        # Track game types used in this story to avoid repeats
        used_types = set()

        scenes = []
        for s_idx, scene_data in enumerate(trib["scenes"]):
            scene_id = f"{story_id}_s{s_idx + 1}"

            # Generate question, trying to avoid repeat game types within a story
            attempts = 0
            while attempts < 10:
                game_type, question, hints = generate_question_for_scene(difficulty, world_id)
                if game_type not in used_types or attempts >= 8:
                    used_types.add(game_type)
                    break
                attempts += 1

            image_prompt = generate_image_prompt(scene_data["setting"], world_id)

            scenes.append({
                "scene_id": scene_id,
                "narration": scene_data["narration"],
                "background_image": f"images/stories/{scene_id}.png",
                "image_prompt": image_prompt,
                "game_type": game_type,
                "question": question,
                "hints": hints,
            })

        # Reward scales with difficulty
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

    # By world
    from collections import Counter
    worlds = Counter(s["world"] for s in stories)
    print("\nStories by world:")
    for w, c in worlds.most_common():
        print(f"  {w}: {c}")

    # By difficulty
    diffs = Counter(s["difficulty"] for s in stories)
    print("\nStories by difficulty:")
    for d in sorted(diffs):
        print(f"  Difficulty {d}: {diffs[d]}")

    # Game type distribution across all scenes
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
        prompts.append(f"\n=== {story['title']} ({story['title_cn']}) ===")
        for scene in story["scenes"]:
            prompts.append(f"\n[{scene['scene_id']}]")
            prompts.append(f"File: {scene['background_image']}")
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
    shutil.copy2(backend_path, frontend_path)
    print(f"Copied to {frontend_path}")

    # Export image prompts
    export_image_prompts(stories)
