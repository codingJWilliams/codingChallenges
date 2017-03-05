import random
from time import gmtime, strftime
def randomNameGen():
    part1 = ["Voltar", "Vultrax", "Frizban", "Rasputin", "Rostor", "Simonexto", "Guurglex"]
    part2 = ["bald", "ban", "buck", "tor", "van", "gax", "trandor", "thuri", "ben", "baldar", "may", "lam", "mor", "dard", "burg", "whit"]
    part3 = ["Ard", "Alf", "Fiz", "Risa", "Warran", "Kel", "Wren", "Kan", "Can", "Gy", "Dero", "Ak", "Dall", "Dell", "Mil", "Ward"]
    return random.choice(part1) + random.choice(part2) + "-" + random.choice(part3)
def bar(stat, maximum, label):
    templateForLabel = list("            :")
    for key, letter in enumerate(label): templateForLabel[key] = letter
    templateForBar = "["
    for i in range(1, maximum+1): templateForBar += " "
    templateForBar += "]"
    templateForBar = list(templateForBar)
    for key in range(stat): templateForBar[key + 1] = "~"
    final = ''.join(templateForLabel) + " " + ''.join(templateForBar)
    return final
random.seed(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
possibilities = {
    "rpgClass": ["Elf", "Dwarf", "Human", "Zombie", "Spirit"],
    "gender": ['Agender', 'Androgyne', 'Androgynous', 'Bigender', 'Cis', 'Cisgender', 'Cis Female', 'Cis Male', 'Cis Man', 'Cis Woman', 'Cisgender Female', 'Cisgender Male', 'Cisgender Man', 'Cisgender Woman', 'Female to Male', 'FTM', 'Gender Fluid', 'Gender Nonconforming', 'Gender Questioning', 'Gender Variant', 'Genderqueer', 'Intersex', 'Male to Female', 'MTF', 'Neither', 'Neutrois', 'Non-binary', 'Other', 'Pangender', 'Trans', 'Trans*', 'Trans Female', 'Trans* Female', 'Trans Male', 'Trans* Male', 'Trans Man', 'Trans* Man', 'Trans Person', 'Trans* Person', 'Trans Woman', 'Trans* Woman', 'Transfeminine', 'Transgender', 'Transgender Female', 'Transgender Male', 'Transgender Man', 'Transgender Person', 'Transgender Woman', 'Transmasculine', 'Transsexual', 'Transsexual Female', 'Transsexual Male', 'Transsexual Man', 'Transsexual Person', 'Transsexual Woman', 'Two-Spirit', 'Male', 'Female'],# Equality Lol
    "strength": {"Elf": list(range(3,8)), "Dwarf": list(range(6,10)), "Human": list(range(0,5)), "Zombie": list(range(7,10)), "Spirit": list(range(0,2))},
    "magic": {"Elf": list(range(5,8)), "Dwarf": list(range(3,5)), "Human": list(range(0,2)), "Zombie": list(range(9,10)), "Spirit": list(range(5,10))},
    "dexterity": {"Elf": list(range(5,8)), "Dwarf": list(range(3,5)), "Human": list(range(0,2)), "Zombie": list(range(9,10)), "Spirit": list(range(5,10))},
    "possibleExtras": [["diorreah", -5], ["super eyesight", 5], ["super speed", 6], ["psycic powers", 10], ["a headache", -3], ["dyspraxia", -4]] # In format [Name, Change to overall power]
}
class Character:
    def __init__(self, rpgName = randomNameGen()):
        assert characterClass in possibilities["rpgClass"]
        assert characterGender in possibilities["gender"]
        self.rpgClass = random.choice(possibilities["rpgClass"]
        self.gender = random.choice(possibilities["gender"])
        self.strength = random.choice(possibilities["strength"][self.rpgClass])
        self.magic = random.choice(possibilities["magic"][self.rpgClass])
        self.dexterity = random.choice(possibilities["dexterity"][self.rpgClass])
        self.extra = random.choice(possibilities["possibleExtras"])
        self.name = rpgName
        if self.calculateOverallPoints() <= 4: self.level = "Junior"
        elif self.calculateOverallPoints() <= 12: self.level = "1"
        elif self.calculateOverallPoints() <= 20: self.level = "2"
        elif self.calculateOverallPoints() <= 30: self.level = "3"
        else: self.level = "4"
    def calculateOverallPoints(self):
        return self.strength + self.magic + self.dexterity + self.extra[1]
    def outputJson(self):
        # Model: {"name":"gender": "Male", "class": "Elf", "stats": {"magic": 6 etc}, "extra": ["super eyesight", 5], "overallPoints": 20}
        jsonBuild = {
            "name": self.name,
            "gender": self.gender,
            "class": self.rpgClass,
            "stats": {
                "magic": self.magic,
                "strength": self.strength,
                "dexterity": self.dexterity
                },
            "extra": self.extra,
            "overallPoints": self.calculateOverallPoints()}
        return jsonBuild
    def save(self, fileName):
        with open(fileName, "w") as f:
            f.write(self.outputJson())
    def prettyPrint(self):
        finalOutput = """
~~~ RPG Character Generator V1 ~~~

Your character is called {}, and has {}.
They identify as a(n) {} {}.
Their overall power is {}.
Their stats are:
{}
{}
{}
""".format(self.name, self.extra[0], self.rpgClass, self.gender, self.calculateOverallPoints(), bar(self.magic, 10, "Magic"), bar(self.dexterity, 10, "Dexterity"), bar(self.strength, 10, "Strength"))
        return finalOutput
