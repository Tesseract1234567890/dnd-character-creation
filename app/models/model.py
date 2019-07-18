bold = "\033"
reset = "\033"

class Race:
    def __init__(self, strMod, dexMod, conMod, intMod, wisMod, chaMod, size, speed, languages, raceTraits):
        self.strMod = strMod
        self.dexMod = dexMod
        self.conMod = conMod
        self.intMod = intMod
        self.wisMod = wisMod
        self.chaMod = chaMod
        self.size = size
        self.speed = speed
        self.languages = languages
        self.raceTraits = raceTraits

class Job:
    def __init__(self, hitDice, armorProf, weaponProf, toolProf, savingThrows, skillProf, equipment, classTraits):
        self.hitDice = hitDice
        self.armorProf = armorProf
        self.weaponProf = weaponProf
        self.toolProf = toolProf
        self.savingThrows = savingThrows
        self.skillProf = skillProf
        self.equipment = equipment
        self.classTraits = classTraits

class barbTableEntry:
    def __init__(self, profBonus, features, rages, rageDamage):
        self.profBonus = profBonus
        self.features = features
        self.rages = rages
        self.rageDamage = rageDamage

class bardTableEntry:
    def __init__(self, profBonus, features, cantripsKnown, spellsKnown, levelOneSlots, levelTwoSlots, levelThreeSlots, levelFourSlots, levelFiveSlots, levelSixSlots, levelSevenSlots, levelEightSlots, levelNineSlots):
        self.profBonus = profBonus
        self.features = features
        self.cantripsKnown = cantripsKnown
        self.spellsKnown = spellsKnown
        self.levelOneSlots = levelOneSlots
        self.levelTwoSlots = levelTwoSlots
        self.levelThreeSlots = levelThreeSlots
        self.levelFourSlots = levelFourSlots
        self.levelFiveSlots = levelFiveSlots
        self.levelSixSlots = levelSixSlots
        self.levelSevenSlots = levelSevenSlots
        self.levelEightSlots = levelEightSlots
        self.levelNineSlots = levelNineSlots

class draconicAncestry:
    def __init__(self, damageType, breathWeapon):
        self.damageType = damageType
        self.breathWeapon = breathWeapon

class Background:
    def __init__(self, skillProf, languages, equipment, feature, featureDesc):
        self.skillProf = skillProf
        self.languages = languages
        self.equipment = equipment
        self.feature = feature
        self.featureDesc = featureDesc

races = {
    "Hill Dwarf": Race(0, 0, 2, 0, 1, 0, "Medium", 25, ["Common", "Dwarvish"], [["Darkvision", "Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."], ["Dwarven Resilience", "You have advantage on saving throws against poison, and you have resistance against poison damage."], ["Dwarven Combat Training", "You have proficiency with the battleaxe, handaxe, light hammer, and warhammer."], ["Tool Proficiency", "You gain proficiency with the artisan's tools of your choice: smith's tools, brewer's supplies, or mason's tools."], ["Stonecunning", "Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus."], ["Dwarven Toughness", "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."]]),
    "Dragonborn": Race(2, 0, 0, 0, 0, 1, "Medium", 30, ["Common", "Draconic"], [["Draconic Ancestry", "You have draconic ancestry. Choose one type of dragon from the Draconic Ancestry table. Your breath weapon and damage resistance are determined by the dragon type, as shown in the table."], ["Breath Weapon", "You can use your action to exhale destructive energy. Your draconic ancestry determines the size, shape, and damage type of the exhalation. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw, the type of which is determined by your draconic ancestry. The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increases to 3d6 at 6th level, 4d6 at 11th level, and 5d6 at 16th level. After you use your breath weapon, you can't use it again until you complete a short or long rest."], ["Damage Resistance", "You have resistance to the damage type associated with your draconic ancestry."]]),
    "High Elf": Race(0, 2, 0, 1, 0, 0, "Medium", 30, ["Common, Elvish"], [["Darkvision", "Accustomed to twilight forests and the night sky, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."], ["Keen Sense","You have proficiency in the Perception skill."], ["Fey Ancestry", "You have advantage on saving throws against being charmed, and magic can't put you to sleep."], ["Trance", "Elves don't need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. (The Common word for such meditation is a trance.) While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep."], ["Elf Weapon Training", "You have proficiency with the longsword, shortsword, shortbow, and longbow."], ["Cantrip", "You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it."], ["Extra Language", "You can speak, read, and write one extra language of your choice."]]),
    "Wood Elf": Race(0, 2, 0, 0, 1, 0, "Medium", 30, ["Common, Elvish"], [["Darkvision", "Accustomed to twilight forests and the night sky, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."], ["Keen Sense","You have proficiency in the Perception skill."], ["Fey Ancestry", "You have advantage on saving throws against being charmed, and magic can't put you to sleep."], ["Trance", "Elves don't need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. (The Common word for such meditation is a trance.) While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep."], ["Elf Weapon Training", "You have proficiency with the longsword, shortsword, shortbow, and longbow."], ["Mask of the Wild", "You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."]]),
    "Deep Gnome": Race(0, 1, 0, 2, 0, 0, "Small", 25, ["Common, Gnomish, Undercommon"], [["Gnome Cunning", "You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic."], ["Superior Darkvision", "Your darkvision has a radius of 120 feet."], ["Stone Camouflage", "You have advantage on Dexterity (stealth) checks to hide in rocky terrain."]]),
    "Tiefling": Race(0, 0, 0, 1, 0, 2, "Medium", 30, ["Common, Infernal"], [["Darkvision", "Thanks to your infernal heritage, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."], ["Hellish Resistance", "You have resistance to fire damage."], ["Infernal Legacy", "You know the thaumaturgy cantrip. When you reach 3rd level, you can cast the hellish rebuke spell as a 2nd-level spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the darkness spell once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."]]),
    "Half-Orc( Mark of Finding)": Race(3, 0, 1, 0, 1, 0, "Medium", 30, ["Common, Orc"], [["Darkvision", "Thanks to your orc blood, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray"], ["Menacing", "You gain proficiency in the Intimidation skill."], ["Relentless Endurance", "When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can't use this feature again until you finish a long rest."], ["Savage Attacks", "When you score a critical hit with a melee weapon attack, you can roll one of the weapon's damage dice one additional time and add it to the extra damage of the critical hit."], ["Hunter's Intuition", "Your mark sharpens your senses and helps you find your prey. When you make a Wisdom (Perception) or Wisdom (Survival) check, you can roll one Intuition die, a d4, and add the number rolled to the ability check."], ["Imprint Prey", "As a bonus action, choose one creature you can see within 30 feet of you. The target is imprinted in your mind until it dies or you use this trait again. Alternatively, you can imprint a creature as your quarry whenever you succeed on a Wisdom (Survival) check to track it. When you are tracking your quarry, double the result of your Intuition die. When your quarry is within 60 feet of you, you have a general sense of its location. Your attacks against it ignore half cover. If you can't see the target when you attack it, your inability to see it doesn't impose disadvantage on the attack roll. Likewise, your quarry doesn't gain advantage on attack rolls against you due to being hidden or invisible. Once you use this trait, you cannot use it again until you finish a short or long rest."], ["Nature's Voice", "When you reach 3rd level you gain the ability to cast locate animals or plants (Describe or name a specific kind of beast or plant. Concentrating on the voice of nature in your surroundings, you learn the direction and distance to the closest creature or plant of that kind within 5 miles, if any are present.), but only as a ritual."]]),

  

    
}

# [["Trait Name", "Trait Description"], ["Trait Name 2", "Trait Description 2"]]

classes = {
    "Barbarian": Job("d12", "light armor, medium armor, shields", "simple weapons, martial weapons", "none", "Strength, Constitution", "Choose two from Animal Handling, Athletics, Intimidation, Nature, Perception, and Survival", ["a greataxe or any martial melee weapon", "two handaxes or any simple weapon", "an explorer's pack", "4 javelins"], [["Rage", "In battle, you fight with primal ferocity. <p>On your turn, you can enter a rage as a bonus action. While raging, you gain the following benefits if you aren't wearing heavy armor: <p><li>You have advantage on Strength checks and Strength saving throws. <li>When you make a melee weapon attack using Strength, you gain a bonus to the damage roll that increases as you gain levels as a barbarian, as shown in the Rage Damage column of the Barbarian table. <li>You have resistance to bludgeoning, piercing, and slashing damage. </li><p>If you are able to cast spells, you can't cast them or concentrate on them while raging. Your rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends and you haven't attacked a hostile creature since your last turn or taken damage since then. You can also end your rage on your turn as a bonus action. <p>Once you have raged the number of times shown for your barbarian level in the Rages column of the Barbarian table, you must finish a long rest before you can rage again."], ["Unarmored Defense", "While you are not wearing any armor, your Armor Class equals 10 + your Dexterity modifier + your Constitution modifier. You can use a shield and still gain this benefit."], ["Danger Sense", "At 2nd level, you gain an uncanny sense of when things nearby aren't as they should be, giving you an edge when you dodge away from danger. <p>You have advantage on Dexterity saving throws against effects that you can see, such as traps and spells. To gain this benefit, you can't be blinded, deafened, or incapacitated."], ["Reckless Attack", "While you are not wearing any armor, your Armor Class equals 10 + your Dexterity modifier + your Constitution modifier. You can use a shield and still gain this benefit."], ["Primal Path", "At 3rd level, you choose a path that shapes the nature of your rage, such as the Path of the Berserker. Your choice grants you features at 3rd level and again at 6th, 10th, and 14th levels."], ["Ability Score Improvement", "When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature."], ["Extra Attack", "Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn."], ["Fast Movement", "Starting at 5th level, your speed increases by 10 feet while you aren't wearing heavy armor."], ["Feral Instinct", "By 7th level, your instincts are so honed that you have advantage on initiative rolls. <p>Additionally, if you are surprised at the beginning of combat and aren't incapacitated, you can act normally on your first turn, but only if you enter your rage before doing anything else on that turn."], ["Brutal Critical", "Beginning at 9th level, you can roll one additional weapon damage die when determining the extra damage for a critical hit with a melee attack. <p>This increases to two additional dice at 13th level and three additional dice at 17th level."], ["Relentless Rage", "Starting at 11th level, your rage can keep you fighting despite grievous wounds. If you drop to 0 hit points while you're raging and don't die outright, you can make a DC 10 Constitution saving throw. If you succeed, you drop to 1 hit point instead. <p>Each time you use this feature after the first, the DC increases by 5. When you finish a short or long rest, the DC resets to 10."], ["Persistent Rage", "Beginning at 15th level, your rage is so fierce that it ends early only if you fall unconscious or if you choose to end it."], ["Indomitable Might", "Beginning at 18th level, if your total for a Strength check is less than your Strength score, you can use that score in place of the total."], ["Primal Champion", "At 20th level, you embody the power of the wilds. Your Strength and Constitution scores increase by 4. Your maximum for those scores is now 24."]]),
    "Bard": Job("d8", ["light armor"], ["simple weapons", "hand crossbows", "longswords", "rapiers", "shortswords"], ["three musical instruments of your choice"], ["Dexterity", "Charisma"], ["choose any three"], ["a rapier, a longsword, or any simple weapon", "a diplomat's pack or an entertainer's pack", "any musical instrument", "leather armor", "dagger"], [["Spellcasting", "You have learned to untangle and reshape the fabric of reality in harmony with your wishes and music. Your spells are part of your vast repertoire, magic that you can tune to different situations. <p>You know two cantrips of your choice from the bard spell list. You learn additional bard cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Bard table.<p><br>The Bard table shows how many spell slots you have to cast your bard spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.<p>For example, if you know the 1st-level spell cure wounds and have a 1st-level and a 2nd-level spell slot available, you can cast cure wounds using either slot."]])
}



backgrounds = {
    "Acolyte": Background("Insight, Religion", "Two of your choice", ["A holy symbol (a gift to you when you entered the priesthood)", "a prayer book or prayer wheel", "5 sticks of incense", "vestments", "a set of common clothes", "a pouch containing 15 gp"], "Shelter of the Faithful", "As an acolyte, you command the respect of those who share your faith, and you can perform the religious ceremonies of your deity. You and your adventuring companions can expect to receive free healing and care at a temple, shrine, or other established presence of your faith, though you must provide any material components needed for spells. Those who share your religion will support you (but only you) at a modest lifestyle. You might also have ties to a specific temple dedicated to your chosen deity or pantheon, and you have a residence there. This could be the temple where you used to serve, if you remain on good terms with it, or a temple where you have found a new home. While near your temple, you can call upon the priests for assistance, provided the assistance you ask for is not hazardous and you remain in good standing with your temple.")
}

barbTable = {
    1: barbTableEntry(2, ["Rage", "Unarmored Defense"], 2, 2),
    2: barbTableEntry(2, ["Reckless Attack", "Danger Sense"], 2, 2),
    3: barbTableEntry(2, ["Primal Path"], 3, 2),
    4: barbTableEntry(2, ["Ability Score Improvement"], 3, 2),
    5: barbTableEntry(3, ["Extra Attack", "Fast Movement"], 3, 2),
    6: barbTableEntry(3, ["Path Feature"], 4, 2),
    7: barbTableEntry(3, ["Feral Instinct"], 4, 2),
    8: barbTableEntry(3, ["Ability Score Improvement"], 4, 2),
    9: barbTableEntry(4, ["Brutal Critical (1 die)"], 4, 3),
    10: barbTableEntry(4, ["Path Feature"], 4, 3),
    11: barbTableEntry(4, ["Relentless Rage"], 4, 3),
    12: barbTableEntry(4, ["Ability Score Improvement"], 5, 3),
    13: barbTableEntry(5, ["Brutal Critical (2 dice)"], 5, 3),
    14: barbTableEntry(5, ["Path Feature"], 5, 3),
    15: barbTableEntry(5, ["Persistent Rage"], 5, 3),
    16: barbTableEntry(5, ["Ability Score Improvement"], 5, 4),
    17: barbTableEntry(6, ["Brutal Critical (3 dice)"], 6, 4),
    18: barbTableEntry(6, ["Indomitable Might"], 6, 4),
    19: barbTableEntry(6, ["Ability Score Improvement"], 6, 4),
    20: barbTableEntry(6, ["Primal Champion"], 'Unlimited', 4),
    
}

bardTable = {
    1: bardTableEntry(2, ["Spellcasting", "Bardic Inspiration (d6)"], 2, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0),
    2: bardTableEntry(2, ["Jack of All Trades", "Song of Rest (d6)"], 2, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0),
    3: bardTableEntry(2, ["Bard College", "Expertise"], 2, 6, 4, 2, 0, 0, 0, 0, 0, 0, 0),
    4: bardTableEntry(2, ["Ability Score Improvement"], 3, 7, 4, 3, 0, 0, 0, 0, 0, 0, 0),
    5: bardTableEntry(3, ["Font of Inspiration", "Bardic Inspiration (d8)"], 3, 8, 4, 3, 2, 0, 0, 0, 0, 0, 0),
    6: bardTableEntry(3, ["Countercharm", "Bard College Feature"], 3, 9, 4, 3, 3, 0, 0, 0, 0, 0, 0),
    7: bardTableEntry(3, [], 3, 10, 4, 3, 3, 1, 0, 0, 0, 0, 0),
    8: bardTableEntry(3, ["Ability Score Improvement"], 3, 11, 4, 3, 3, 2, 0, 0, 0, 0, 0),
    9: bardTableEntry(4, ["Song of Rest (d8)"], 3, 12, 4, 3, 3, 3, 1, 0, 0, 0, 0),
    10: bardTableEntry(4, ["Bardic Inspiration (d10)", "Expertise", "Magical Secrets"], 4, 14, 4, 3, 3, 3, 2, 0, 0, 0, 0),
    11: bardTableEntry(4, [], 4, 14, 4, 3, 3, 3, 2, 0, 0, 0, 0),
    12: bardTableEntry(4, ["Ability Score Improvement"], 4, 15, 4, 3, 3, 3, 2, 1, 0, 0, 0),
    13: bardTableEntry(5, ["Song of Rest (d10)"], 4, 16, 4, 3, 3, 3, 2, 1, 1, 0, 0),
    14: bardTableEntry(5, ["Magical Secrets"], 4, 18, 4, 3, 3, 3, 2, 1, 1, 0, 0),
    15: bardTableEntry(5, ["Bardic Inspiration (d12)"], 4, 19, 4, 3, 3, 3, 2, 1, 1, 1, 0)
}

draconicAncestries = {
    "Black": draconicAncestry("Acid", "5 by 30 ft. line (Dex. Save)"),
    "Blue": draconicAncestry("Lightning", "5 by 30 ft. line (Dex. Save)"),
    "Brass": draconicAncestry("Fire", "5 by 30 ft. line (Dex. Save)"),
    "Bronze": draconicAncestry("Lightning", "5 by 30 ft. line (Dex. Save)"),
    "Copper": draconicAncestry("Acid", "5 by 30 ft. line (Dex. Save)"),
    "Gold": draconicAncestry("Fire", "15 ft. cone (Dex. save)"),
    "Green": draconicAncestry("Poison", "15 ft. cone (Con. save)"),
    "Red": draconicAncestry("Fire", "15 ft. cone (Dex. save)"),
    "Silver": draconicAncestry("Cold", "15 ft. cone (Con. save)"),
    "White": draconicAncestry("Cold", "15 ft. cone (Con. save)")
    
}