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

class Background:
    def __init__(self, skillProf, languages, equipment, feature, featureDesc):
        self.skillProf = skillProf
        self.languages = languages
        self.equipment = equipment
        self.feature = feature
        self.featureDesc = featureDesc

races = {
    "Hill Dwarf": Race(0, 0, 2, 0, 1, 0, "Medium", 25, ["Common", "Dwarvish"], [["Darkvision", "Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."], ["Dwarven Resilience", "You have advantage on saving throws against poison, and you have resistance against poison damage."], ["Dwarven Combat Training", "You have proficiency with the battleaxe, handaxe, light hammer, and warhammer."], ["Tool Proficiency", "You gain proficiency with the artisan's tools of your choice: smith's tools, brewer's supplies, or mason's tools."], ["Stonecunning", "Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus."], ["Dwarven Toughness", "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."]]),
    "Dragonborn": Race(2, 0, 0, 0, 0, 1, "Medium", 30, ["Common", "Draconic"], [["Draconic Ancestry"],   ["Breath Weapon, Damage Resistance"]]),
    "High Elf": Race(0, 2, 0, 1, 0, 0, "Medium", 30, "Common, Elvish", "Darkvision, Keen Senses, Fey Ancestry, Trance, Elf Weapon Training, Cantrip, Extra Language")
    
}

# [["Trait Name", "Trait Description"], ["Trait Name 2", "Trait Description 2"]]

classes = {
    "Barbarian": Job("d12", "light armor, medium armor, shields", "simple weapons, martial weapons", "none", "Strength, Constitution", "Choose two from Animal Handling, Athletics, Intimidation, Nature, Perception, and Survival", "e", "e")
}

backgrounds = {
    "Acolyte": Background("Insight, Religion", "Two of your choice", "A holy symbol (a gift to you when you entered the priesthood), a prayer book or prayer wheel, 5 sticks of incense, vestments, a set of common clothes, and a pouch containing 15 gp", "Shelter of the Faithful", "As an acolyte, you command the respect of those who share your faith, and you can perform the religious ceremonies of your deity. You and your adventuring companions can expect to receive free healing and care at a temple, shrine, or other established presence of your faith, though you must provide any material components needed for spells. Those who share your religion will support you (but only you) at a modest lifestyle. You might also have ties to a specific temple dedicated to your chosen deity or pantheon, and you have a residence there. This could be the temple where you used to serve, if you remain on good terms with it, or a temple where you have found a new home. While near your temple, you can call upon the priests for assistance, provided the assistance you ask for is not hazardous and you remain in good standing with your temple.")
}